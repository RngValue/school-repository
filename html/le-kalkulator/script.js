const MAX_VISIBLE_DIGITS = -17
const OPERATORS_POINT = "+-*/.,<>"
const MATH_INDICATOR = "_"

const mathOutput = document.getElementById("math")

let mathString = "0"
let mathIndex = 1

update_math()

function update_math() {
  let mathing = [mathString.slice(0, mathIndex), MATH_INDICATOR, mathString.slice(mathIndex)].join('')
  mathOutput.innerHTML = mathing.slice(MAX_VISIBLE_DIGITS)
}

function move_math_right() {
  if (mathIndex < mathString.length) {
    mathIndex++
    update_math()
  }
}

function move_math_left() {
  if (mathIndex > 0) {
    mathIndex--
    update_math()
  }
}

function append_to_math(x) {
  if (mathString == "0" && OPERATORS_POINT.indexOf(x) < 0) {
    mathString = x
  } else {
    mathString = [mathString.slice(0, mathIndex), x, mathString.slice(mathIndex)].join('')
  }
  mathIndex += x.length
  update_math()
}

function clear_math() {
  mathString = "0"
  mathIndex = 1
  update_math()
}

function delete_math() {
  console.log(mathIndex)
  if (mathIndex < mathString.length) {
    mathString = [mathString.slice(0, mathIndex - 1), mathString.slice(mathIndex)].join('')
  } else {
    mathString = mathString.slice(0, -1)
  }

  if (mathString == "") {
    mathString = "0"
  }
  if (mathString != "0") {
    mathIndex--
  }
  update_math()
}

function eval_math() {
  try {
    mathString = String(eval(mathString))
    mathIndex = mathString.length
    update_math()
  } catch (e) {
    mathString = "0"
    mathOutput.innerHTML = "NaN"
    mathIndex = 0
  }
}