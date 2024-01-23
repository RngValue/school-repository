let produkty = localStorage.length;
document.getElementById("produkticky").innerHTML = produkty;

function pridej_produkt(produkt, cena) {
  produkty ++
  localStorage.setItem(produkt + " (" + produkty - 1 + ")", cena)
  document.getElementById("produkticky").innerHTML = produkty - 1;
  window.alert(`${produkt + " (" + produkty + ")"} byl přídán do košíku!`);
}