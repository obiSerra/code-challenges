const helpers = require("../helpers/helpers.js");

const { getInvalid } = require("./silver-star.js");

const findNums = (nums, target, acc = []) => {
  const sum = acc.reduce((a, v) => a + v, 0);
  if (sum === target) return acc;
  if (nums.length === 0 || sum > target) return false;

  const currentNum = nums.shift();

  return findNums(nums, target, [...acc, currentNum]);
};

const solution = input => {
  const [padd, numList] = input;
  const invalid = getInvalid(padd, numList);
  for (let i in numList) {
    const nums = findNums(numList.slice(i), invalid);

    if (nums) {
      return Math.min(...nums) + Math.max(...nums);
    }
  }
};

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
    console.log(solution(input));
  }
})();
