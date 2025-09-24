Old Dragon - Criador de Personagens (Flask)

Como rodar (local)

1. Baixe e extraia o zip.

```
python -m venv venv
# Windows (PowerShell)
venv\Scripts\Activate.ps1
# Linux/Mac
# source venv/bin/activate
```

2. Instale dependências:

```
pip install -r requirements.txt
```

3. Rode a aplicação:

```
python app.py
```

4. Abra `http://127.0.0.1:5000/` no navegador.

Estrutura importante:
- controllers/character_controller.py (controllers)
- model/ (models: Personagem, estilos, raças, classes)
- templates/ (views)
- static/ (CSS, JS)
