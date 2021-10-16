const helpers = require("../helpers/helpers.js");

(async () => {
  let input = await helpers.readInput(1);
  input = input.split("\n").map(e => parseInt(e, 10));

  const solution = input => {
    for (let i = 0; i < input.length; i++) {
      for (let j = 0; j < input.length; j++) {
        if (i === j) continue;
        for (let k = 0; k < input.length; k++) {
          if (k === j) continue;

          const numI = input[i];
          const numJ = input[j];
          const numK = input[k];

          if (2020 - numI - numJ - numK === 0) {
            return numI * numJ * numK;
          }
        }
      }
    }
  };

  console.log(solution(input));
})();
