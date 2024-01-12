let produkty = localStorage.length;

document.getElementById("produkticky").innerHTML = produkty;

function pridej_produkt(produkt, cena) {
  localStorage.setItem(produkt, cena);
  produkty += 1;
  document.getElementById("produkticky").innerHTML = produkty;
  window.alert(`${produkt} byl přídán do košíku!`);
}