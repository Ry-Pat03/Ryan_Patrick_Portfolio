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

    //JS for Ex06d
    newColor = colorchanger();
    document.getElementById("rb").style.color = newColor;
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

    //JS for Ex06e
    //Create Text Node
    answerNode = document.createTextNode("The answer: " + answer);
    document.body.appendChild(answerNode);
    //document.getElementById("result").innerHTML = answer;
}

//divide function
function multiply(){
    first = parseInt(document.getElementById("firstoperand").value);
    second = parseInt(document.getElementById("secondoperand").value);
    //console.log(first);
    //console.log(second);
    answer = first * second;
    //console.log(answer)
    
    //JS for Ex06e
    //Create Text Node
    answerNode = document.createTextNode("The answer: " + answer);
    document.body.appendChild(answerNode);
    //document.getElementById("result").innerHTML = answer;
}






//JS for EX06a
function moveText(){
    document.getElementById("text").style.left = parseInt(document.getElementById("text").style.left) + 10 + "px";
}

//JS for EX06b
function howmany(){
    total = 0
    num = document.getElementById("regForm").getElementsByTagName("input");
    for(i=0; i < num.length; i ++){
        total += 1
    }
    console.log("Number of inputs for EX06b: " + total);
}

//JS for EX06c
function colorchanger(){
    colorSelect = document.getElementById("mySelect");
    color = colorSelect.value;
    document.getElementById("colorChange").style.backgroundColor = color;
    return color;
}

