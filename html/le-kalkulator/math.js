function sum(x) { return x.reduce((partialSum, a) => partialSum + a, 0) }
function avg(x) { return sum(x) / x.length }
function cos(x) { return Math.cos(x) }
function sin(x) { return Math.sin(x) }
function sqrt(x) { return Math.sqrt(x) }
function abs(x) { return Math.abs(x) }