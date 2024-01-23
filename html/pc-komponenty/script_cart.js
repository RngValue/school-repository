let produkty = localStorage.length;
document.getElementById("produkticky").innerHTML = produkty;

const leDuck = document.getElementById("grapes");

let celkem_cena = 0;

for (let i = 0; i < produkty; i++) {
  leDuck.innerHTML += "<tr id=\"" + localStorage.key(i) + "\" >\n" + "<td>" + localStorage.key(i) + "</td>\n" + "<td>" + Number(localStorage.getItem(localStorage.key(i))).toLocaleString('de-DE') + " Kč</td>\n" + "<td>" + "<button onclick=\"localStorage.removeItem('" + localStorage.key(i) + "'); document.getElementById('" + localStorage.key(i) + "').remove(); window.alert('" + localStorage.key(i) + " byl odebrán z košíku!');" + "\" >odebrat</button>" + "</td>" + "<tr>";
  celkem_cena += +localStorage.getItem(localStorage.key(i));
}

document.getElementById("celkem").innerHTML = Number(celkem_cena).toLocaleString('de-DE');

function pridej_produkt(produkt, cena) {
  produkty++
  localStorage.setItem(produkt + " (" + produkty + ")", cena)
  document.getElementById("produkticky").innerHTML = produkty - 1;
  window.alert(`${produkt + " (" + produkty + ")"} byl přídán do košíku!`);
}