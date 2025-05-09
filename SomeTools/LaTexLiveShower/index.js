function LatexUpdate(event){

    input = document.querySelector('#currentInput').value;
    document.querySelector('#result').innerHTML = `\\\(${input}\\\)`;
    MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
}

function Save(){
    repo = document.querySelector('.SaveSlot');
    const newData = document.createElement('div');

    newData.className = "result";
    input = document.querySelector('#currentInput');
    if(input.value == "") return;
    newData.innerText = `\\\(${input.value}\\\)`;

    repo.appendChild(newData);
    input.value = '';
    LatexUpdate();
}
function Erase(){

    repo = document.querySelector('.SaveSlot');
    repo.lastChild.remove();
}
function Clear(){

    repo = document.querySelector('.SaveSlot');
    while(repo.firstChild)
        repo.firstChild.remove();
}