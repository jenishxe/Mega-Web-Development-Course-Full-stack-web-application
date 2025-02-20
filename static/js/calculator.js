
var number1="";
var number2="";
var equalSign = document.getElementById("equal");

var isNumber1 = false;

function formNumber(n){
    if (!isNumber1){
        number1+=n;
        document.getElementById("displayNum").textContent = number1;
    }
    else{
        number2+=n;
        document.getElementById("displayNum").textContent = number2;

    }
}


function sum(n1,n2){
    return n1+n2
}

function sub(n1,n2){
    return n1-n2
}

function mul(n1,n2){
    return n1*n2
}

function div(n1,n2){
    return n1/n2
}

function cal(p1,p2,operation){
    p2 = Number(p2);
    result = operation(p1,p2)
    document.getElementById("displayNum").textContent = result;
    
}


function opSum(){
    number1 = Number(number1);
    isNumber1 = true;
    equalSign.setAttribute("onclick", "cal(number1, number2, sum)")
}

function opSub(){
    number1 = Number(number1);
    isNumber1 = true;
    equalSign.setAttribute("onclick", "cal(number1, number2, sub)")
}

function opMul(){
    number1 = Number(number1);
    isNumber1 = true;
    equalSign.setAttribute("onclick", "cal(number1, number2, mul)")
}

function opDiv(){
    number1 = Number(number1);
    isNumber1 = true;
    equalSign.setAttribute("onclick", "cal(number1, number2, div)")
}




// form 

function CreateUser(fname,lname){
    this.fname = fname;
    this.lname = lname;
}

function submitForm(){
    fname = document.getElementById("fname").value
    lname = document.getElementById("lname").value
    var user1 = new CreateUser(fname, lname)
    var text = user1.fname + " " + user1.lname
    document.getElementById("displayUser").textContent= text

}