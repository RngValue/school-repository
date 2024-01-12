let text;

function funkce(userInput) {
  text = "Nameless... I see...";
  if (/\S/.test(userInput)) {
    text = "Wonderful evening, <span class='myname'>" + userInput + "!</span>";
  }
  
  document.getElementById("text").innerHTML = text;
}