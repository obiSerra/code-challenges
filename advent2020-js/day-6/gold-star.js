const helpers = require("../helpers/helpers.js");

(async () => {
  let input = await helpers.readInput(6);
  input = input.split("\n");

  //const input = ["abc", "", "a", "b", "c", "", "ab", "ac", " ", "a", "a", "a", "a", "", "b"];

  const solution = input => {
    const groups = input
      .reduce(
        (acc, v) => {
          if (v.match(/^\s*$/)) acc.push(null);
          else if (!acc[acc.length - 1]) {
            const answ = v.split("");
            const res = {};

            for (let a of answ) {
              res[a] = true;
            }
            acc[acc.length - 1] = res;
          } else {
            const answ = new Set([...v.split("")]);
            const current = new Set([...Object.keys(acc[acc.length - 1])]);
            const res = {};
            for (let a of [...new Set([...answ].filter(x => current.has(x)))]) {
              res[a] = true;
            }
            acc[acc.length - 1] = res;
          }
          return acc;
        },
        [null]
      )
      .map(x => (!!x ? Object.keys(x).length : 0))
      .reduce((acc, v) => acc + v, 0);
    return groups;
  };

  console.log(solution(input));
})();
