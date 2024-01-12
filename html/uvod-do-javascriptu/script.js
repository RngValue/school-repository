function bubak() {
  alert("Vyskakovací okno! ooOOooOOooOOoo");
}

var span = document.getElementById("klik");

var a = 0
function byvalo() {
  if (a == 0) {
    span.innerHTML = "Tohle <button onclick=\"byvalo()\">tlačítko</button> je super";
    span.style.color = "cyan";
    a = 1
  } else {
    span.innerHTML = "Klikni <button onclick=\"byvalo()\">sem</button> prosím";
    span.style.color = "orange";
    a = 0
  }
}

var cas = document.getElementById("cas");
function ted() {
  var datum = new Date();
  cas.innerHTML = "<span style=\"color: orange\">Teď je...<br>" + String(datum.getDate()).padStart(2, '0') + "." + String(datum.getMonth() + 1).padStart(2, '0') + "." + datum.getFullYear() + "<br>" + datum.getHours() + ":" + datum.getMinutes() + ":" + datum.getSeconds() + "</span>";
}

function denudify() {
  document.getElementById("text").style.fontFamily = "cursive";
  document.getElementById("trada").innerHTML = "<button onclick=\"alert(\'Zpátky už to nepujde\')\">To je lepší</button>";
  document.getElementById("prekvapko").innerHTML = "jinak, tohle je <span style=\"color: magenta\">rar</span><br><img style=\"width: 70%; max-width: 640px\" src=\"unnamed.jpg\">"
}