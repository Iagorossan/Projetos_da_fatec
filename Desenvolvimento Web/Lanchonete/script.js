let adicionais=0;
let entregas =0;

function totalPagar(){
let total=0;
    calcularAdicionais();
    total = adicionais+entregas;
}

function calcularAdicionais(){
    adicionais=0
    let selecionados=document.querySelectorAll("input[name='adicionais']");
    let qtd = selecionados.length;
    for (i=0; i< qtd; i++)
    {
        if (selecionados[i].checked)
        {
            adicionais += Number(selecionados[i].value);
            //adicionais = adicionais + Number([selecionados].value);
        }
    }
    alert(adicionais);
}

function calcularEntrega(){

}