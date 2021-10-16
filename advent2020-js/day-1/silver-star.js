const helpers = require("../helpers/helpers.js");

(async () => {
  let input = await helpers.readInput(1);
  input = input.split("\n");

  const solution = input => {
    const rem = {};
    for (let entry of input) {
      const num = parseInt(entry, 10);
      if (`${entry}` in rem) {
        return num * rem[entry];
      }
      rem[`${2020 - num}`] = num;
    }
  };

  console.log(solution(input));
})();
