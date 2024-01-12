const nouns = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "tree", "rock", "table", "stool", "wall", "fire", "bear", "freddy fazzbear", "dream", "obama", "empire", "frontal lobe", "kid"]
const adjectives = ["nice", "the great", "virtue", "wooden", "stone", "awful", "water", "green", "pink", "red", "blue", "rotten", "dead", "undead", "inconvenient", "german", "czech", "swedish", "chinese", "american", "bri\'ish", "strong", "frontal"]
const verbs = ["started", "planned", "went through", "sliced", "placed", "reached", "killed", "frozen", "burnt", "put down", "scared", "ate", "made", "dyed", "blamed", "trimmed", "shortened", "bit"]
const adverbs = ["terribly", "awfully", "truthfully", "evilly", "happilly", "angrilly", "unintentionally", "inconveniently", "probably", "actually", "really", "lazily"]
const particles = ["and", "with"]
function gen_phrase() {
  let nounOne = Math.floor(Math.random() * nouns.length)
  let nounTwo = Math.floor(Math.random() * nouns.length)
  let nounThree = Math.floor(Math.random() * nouns.length)
  let adjeOne = Math.floor(Math.random() * adjectives.length)
  let adjeTwo = Math.floor(Math.random() * adjectives.length)
  let adve = Math.floor(Math.random() * adverbs.length)
  let part = Math.floor(Math.random() * particles.length)
  let verb = Math.floor(Math.random() * verbs.length)

  document.getElementById("phrase").innerHTML = `${adjectives[adjeOne]} ${nouns[nounOne]} ${particles[part]} ${adjectives[adjeTwo]} ${nouns[nounTwo]} ${adverbs[adve]} ${verbs[verb]} a ${nouns[nounThree]}.`
}

const PI = 3.14;
function gen_circle() {
  let radius = parseFloat(document.getElementById("rad").value)
  let plocha = PI * radius ** 2
  document.getElementById("circle").innerHTML = `${plocha}`
}

let lastRNG = [-1, 0];

function xmasinate() {
  let RNG = Math.floor(Math.random() * 5)
  if (lastRNG[lastRNG.length-1] == RNG || lastRNG[lastRNG.length-2] == RNG) {
    xmasinate()
    return
  }
  lastRNG.push(RNG)
  document.body.style.fontFamily = "system-ui, -apple-system"
  document.getElementById("loleffect").style.backgroundImage = ""
  document.getElementById("loleffect").classList.remove("nicedeco")
  console.log(RNG)
  switch (RNG) {
    case 1:
      document.body.style.backgroundImage = "url('https://getwallpapers.com/wallpaper/full/4/f/7/339638.jpg')"
      document.getElementById("loleffect").style.backgroundImage = "url('https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/e5cfcbe3-c4c4-4faa-ad57-3bdea351ab2b/d89z7ri-4b2c6162-b275-4f3d-8024-c9ae64264c34.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwic3ViIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsImF1ZCI6WyJ1cm46c2VydmljZTpmaWxlLmRvd25sb2FkIl0sIm9iaiI6W1t7InBhdGgiOiIvZi9lNWNmY2JlMy1jNGM0LTRmYWEtYWQ1Ny0zYmRlYTM1MWFiMmIvZDg5ejdyaS00YjJjNjE2Mi1iMjc1LTRmM2QtODAyNC1jOWFlNjQyNjRjMzQuZ2lmIn1dXX0.HehwJrU8x6VyLhhycwzjN5IHtGMzMHwgKg5dmWAiGgs')"
      break;
    case 2:
      document.body.style.backgroundImage = "url('https://wallpaperaccess.com/full/883368.jpg')"
      document.body.style.fontFamily = "'Mountains of Christmas', serif";
      break;
    case 3:
      document.getElementById("loleffect").style.backgroundImage = "url('https://freepngimg.com/thumb/christmas/30416-3-christmas-tree-transparent-background.png')"
      document.body.style.backgroundImage = "url('https://wallpapercave.com/wp/wp8145064.jpg')"
      break;
    case 4:
      document.body.style.backgroundImage = "url('https://wallup.net/wp-content/uploads/2015/12/108938-Christmas.jpg')"
      document.getElementById("loleffect").classList.add("nicedeco")
      break;
    default:
      document.body.style.backgroundImage = "url('https://cdn.wallpapersafari.com/67/78/CgY5qz.jpg')"
      break;
  }
}