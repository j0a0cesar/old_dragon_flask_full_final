window.addEventListener('DOMContentLoaded', function(){
  const selects = Array.from(document.querySelectorAll('select.assign'));
  function disableUsed(){
    const used = selects.map(s => s.value).filter(v=>v !== "");
    selects.forEach(s => {
      Array.from(s.options).forEach(opt => {
        if(opt.value === "") return;
        opt.disabled = used.includes(opt.value) && s.value !== opt.value;
      });
    });
  }
  selects.forEach(s => s.addEventListener('change', disableUsed));
  disableUsed();
});
