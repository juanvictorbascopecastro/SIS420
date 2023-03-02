const inicio = [3, 2, 0, 1];
const fin = [0, 1, 2, 3];

const resultados = [];
function combinatoria(arr) {
  // intercambiamos de acuerdo a la posicion
  let result = [arr[1], arr[0], arr[2], arr[3]];
  resultados.push(result);
  console.log(result);
  if (esIgual(resultados[resultados.length - 1], fin)) return true;
  // 2, 3, 0, 1
  result = [arr[0], arr[2], arr[1], arr[3]];
  resultados.push(result);
  console.log(result);
  if (esIgual(resultados[resultados.length - 1], fin)) return true;
  // 3, 0, 2, 1
  result = [arr[0], arr[1], arr[3], arr[2]];
  resultados.push(result);
  console.log(result);
  if (esIgual(resultados[resultados.length - 1], fin)) return true;
  return false;
  // 3, 2, 1, 0;
}
// empezamos haciendo una combinacion base
let existe = combinatoria(inicio);
let contador = 3;
let cont = 0;
while (existe === false) {
  while (cont < contador && existe === false) {
    console.log("======" + cont);
    existe = combinatoria(resultados[cont]);
    cont++;
  }
  contador = contador + inicio.length - 1;
}
console.log(
  "==============ENCONTRADO EN LA ITERACION " +
    resultados.length +
    " ==============="
); // en la iteracion 50
function esIgual(arr1, arr2) {
  let conteo = 0;
  for (let i = 0; i < arr1.length; i++) {
    if (arr1[i] === arr2[i]) conteo++;
  }
  if (conteo === arr1.length) return true;
  else return false;
}
// console.log(resultados);
