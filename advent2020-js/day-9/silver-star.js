const helpers = require("../helpers/helpers.js");

const isValid = (num, prevs) => {
  let rems = {};
  for (let pr of prevs) {
    const rem = num - pr;
    if (`${pr}` in rems && rems[pr] !== pr) return true;
    rems[rem] = pr;
  }
  return false;
};

const getInvalid = (preamble, input) => {
  const usable = input.slice(0, preamble);
  for (let n of input.slice(preamble)) {
    if (!isValid(n, usable)) {
      return n;
    }
    usable.shift();
    usable.push(n);
  }
};

module.exports.isValid = isValid;
module.exports.getInvalid = getInvalid;


(async () => {
  let input = await helpers.readInput(9);
  input = input.split("\n");
  input = [25, input];
  //   let input = [
  //     5,
  //     [
  //       "35",
  //       "20",
  //       "15",
  //       "25",
  //       "47",
  //       "40",
  //       "62",
  //       "55",
  //       "65",
  //       "95",
  //       "102",
  //       "117",
  //       "150",
  //       "182",
  //       "127",
  //       "219",
  //       "299",
  //       "277",
  //       "309",
  //       "576",
  //     ],
  //   ];

  input[1] = input[1].map(i => parseInt(i, 10));
  
  if (require.main === module) {
    console.log(solution(...input));
  }
})();
