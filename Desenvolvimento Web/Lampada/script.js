const lampada = document.getElementById('lampadaDesligada');
pisca = false

function Ligar(){
    lampada.setAttribute("src", "imgs/luzLigada.gif");
}

function Desligar(){
    lampada.setAttribute("src", "imgs/luzDesligada.gif");
}

function Aparecer(){
    lampada.hidden = false;
}

function Sumir(){
    lampada.hidden = true;
}

function Magica(){

}

function Piscar(){
if (pisca == false){
    a = setInterval(Alternar, 800);
}
else {
    clearInterval(a)
}
pisca = !pisca
}

function Alternar(){
    if  ("imgs/luzDesligada.gif" == lampada.getAttribute("src")){
        lampada.setAttribute("src", "imgs/luzLigada.gif");
    }
    
    else { 
        lampada.setAttribute("src", "imgs/luzDesligada.gif");
    }
}
