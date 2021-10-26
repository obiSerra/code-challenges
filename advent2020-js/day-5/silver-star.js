const helpers = require("../helpers/helpers.js");

(async () => {
  let input = await helpers.readInput(5);
  input = input.split("\n");

  const binSearch = (operations, up, down, l) => {
    let cUp = l;
    let cDown = 0;
    const instructions = operations.split("");
    for (let inst of instructions) {
      const middle = Math.floor((cUp - cDown) / 2);
      if (inst === up) {
        cDown = middle + cDown + 1;
      } else if (inst === down) {
        cUp = cDown + middle;
      }
    }

    return cUp;
  };

  const seatId = input => {
    const row = binSearch(input, "B", "F", 127);
    const col = binSearch(input, "R", "L", 7);
    return row * 8 + col;
  };

  const solution = inputs => {
    let max = 0;
    for (let ipt of inputs) {
      const sol = seatId(ipt);
      max = sol > max ? sol : max;
    }

    return max;
  };

  console.log(solution(input));
})();
