let adicionais=0;
let entregas =0;
let valor_lanche = Number(document.getElementById('combos').value)

function totalPagar(){
    let valor_lanche = Number(document.getElementById('combos').value);
    let total=0;
    combos = 0
    
    calcularAdicionais();
    calcularEntrega();
    total = valor_lanche+adicionais+entregas;
    document.getElementById('total_compra').value =  `o total a pagar é ${total},00`
    document.getElementById("descricao_produto").value =  `o total a pagar é ${total},00  ,  ${valor_lanche},00  pelo combo + ${adicionais},00  pelos adicionais + ${entregas},00`
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
    // alert(adicionais);
}

function calcularEntrega(){
    entregas=0
    let entrega=document.querySelectorAll("input[name='entregas']");
    let modo_Entrega=entrega.length;
        for (i=0; i<modo_Entrega; i++)
        {
            if (entrega[i].checked)
            {
                entregas += Number(entrega[i].value);
                break;
            }
        }
    }

function printar(){
    window.print();
}

function relogio(){
    let Hora = new Date()
    //let hora= Hora.getHours()
    //let min = Hora.getMinutes()
    let mensagem = Hora.getHours()+":"+Hora.getMinutes()+":"+Hora.getSeconds()
    document.getElementById("relogio").innerHTML = mensagem
}setInterval(relogio,1000);