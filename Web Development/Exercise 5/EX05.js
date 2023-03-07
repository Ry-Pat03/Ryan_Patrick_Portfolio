//JS for EX05a
function jsStyle(){
   document.getElementById("text").style.color = "cyan";
   document.getElementById("text").style.fontSize = "64px";
}

//JS for EX05b
function getFormValues(){
    fname = document.getElementById("fname").value;
    lname = document.getElementById("lname").value;
    //console.log(fname);
    //console.log(lname);
    alert(fname +" "+ lname);
}

//JS for EX05c
function getOptions(){
    options = document.querySelectorAll('option').length;
    console.log(options);
    alert("There are " + options + " options");
}

//JS for EX05d

//Function for onmouseover
function overP(){
    //console.log("Yes")
    document.getElementById("rb").style.color = "red";
}

//Function for onmouseout
function outP(){
    //console.log("Yes");
    document.getElementById("rb").style.color = "black";
}

//JS for EX05e

//divide function
function divide(){
    first = parseInt(document.getElementById("firstoperand").value);
    second = parseInt(document.getElementById("secondoperand").value);
    //console.log(first);
    //console.log(second);
    answer = first / second;
    //console.log(answer)
    document.getElementById("result").innerHTML = answer;
}

//divide function
function multiply(){
    first = parseInt(document.getElementById("firstoperand").value);
    second = parseInt(document.getElementById("secondoperand").value);
    //console.log(first);
    //console.log(second);
    answer = first * second;
    //console.log(answer)
    document.getElementById("result").innerHTML = answer;
}