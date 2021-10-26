const helpers = require("../helpers/helpers.js");

(async () => {
    let input = await helpers.readInput(6);
    input = input.split("\n");

//  const input = ["abc", "", "a", "b", "c", "", "ab", "ac", " ", "a", "a", "a", "a", "", "b"];

  const solution = input => {
    const groups = input.reduce(
      (acc, v) => {
        if (v.match(/^\s*$/)) acc.push(new Set());
        else acc[acc.length - 1] = new Set([...acc[acc.length - 1], ...v.split("")]);
        return acc;
      },
      [new Set()]
    ).reduce((acc, v) => acc + v.size, 0);
      return groups
  };

  console.log(solution(input));
})();
