from flask import Blueprint, render_template, request, redirect, url_for, flash
from model.personagem import Personagem
from model.classico import Classico
from model.aventureiro import Aventureiro
from model.heroico import Heroico
from model.elfo import Elfo
from model.anao import Anao
from model.humano import Humano
from model.guerreiro import Guerreiro
from model.ladrao import Ladrao
from model.mago import Mago

bp = Blueprint('character', __name__)

RACES = {
    'elfo': Elfo,
    'anao': Anao,
    'humano': Humano
}

CLASSES = {
    'guerreiro': Guerreiro,
    'ladrao': Ladrao,
    'mago': Mago
}


@bp.route('/', methods=['GET'])
def index():
    races = [('elfo', 'Elfo'), ('anao', 'Anão'), ('humano', 'Humano')]
    classes = [('guerreiro', 'Guerreiro'), ('ladrao', 'Ladrão'), ('mago', 'Mago')]
    return render_template('index.html', races=races, classes=classes)


@bp.route('/generate', methods=['POST'])
def generate():
    estilo = request.form.get('estilo')
    raca_key = request.form.get('raca')
    classe_key = request.form.get('classe')

    if not estilo or not raca_key or not classe_key:
        flash('Escolha estilo, raça e classe.')
        return redirect(url_for('character.index'))

    # escolher gerador
    if estilo == 'classico':
        personagem = Classico()
        atributos = personagem.gerar_atributos()
        for nome, valor in zip(Personagem.atributos_nomes, atributos):
            setattr(personagem, nome, valor)

    elif estilo == 'heroico':
        # gerar 6 rolagens 4d6 drop lowest, permitir distribuir
        hero = Heroico()
        rolados = hero.gerar_atributos()
        return render_template('assign.html', rolled=rolados, raca=raca_key, classe=classe_key, estilo=estilo)

    elif estilo == 'aventureiro':
        personagem = Aventureiro()
        rolados = personagem.gerar_atributos()
        return render_template('assign.html', rolled=rolados, raca=raca_key, classe=classe_key, estilo=estilo)

    else:
        flash('Estilo desconhecido')
        return redirect(url_for('character.index'))

    # atribuir raça e classe (para classico)
    personagem.raca = RACES[raca_key]()
    personagem.classe = CLASSES[classe_key]()

    atributos = personagem.to_dict()
    return render_template('result.html', personagem=personagem, atributos=atributos)


@bp.route('/create', methods=['POST'])
def create():
    estilo = request.form.get('estilo')
    raca_key = request.form.get('raca')
    classe_key = request.form.get('classe')

    # aceitar distribuição para aventureiro OU heroico
    if estilo not in ('aventureiro', 'heroico'):
        flash('Rota inválida para este estilo.')
        return redirect(url_for('character.index'))

    # Map selected indices -> rolled values (rolled_index_0, rolled_index_1, ...)
    atribs = {}
    selected_indices = []

    for nome in Personagem.atributos_nomes:
        idx = request.form.get(nome)
        if idx is None or idx == '':
            flash('Todos os atributos devem receber um valor.')
            return redirect(url_for('character.index'))
        try:
            idx_int = int(idx)
        except ValueError:
            flash('Valores inválidos.')
            return redirect(url_for('character.index'))

        rolled_val = request.form.get(f'rolled_index_{idx_int}')
        if rolled_val is None:
            flash('Valor de rolagem inválido (índice não encontrado).')
            return redirect(url_for('character.index'))

        try:
            atribs[nome] = int(rolled_val)
        except ValueError:
            flash('Valor de rolagem inválido (não é inteiro).')
            return redirect(url_for('character.index'))

        selected_indices.append(idx_int)

    # valida unicidade por índice (cada rolagem só pode ser usada uma vez)
    if len(set(selected_indices)) != 6:
        flash('Cada rolagem só pode ser usada uma vez — escolha índices diferentes.')
        return redirect(url_for('character.index'))

    # criar personagem do estilo adequado
    if estilo == 'heroico':
        personagem = Heroico()
    else:
        personagem = Aventureiro()

    for nome, valor in atribs.items():
        setattr(personagem, nome, valor)

    personagem.raca = RACES[raca_key]()
    personagem.classe = CLASSES[classe_key]()

    atributos = personagem.to_dict()
    return render_template('result.html', personagem=personagem, atributos=atributos)
