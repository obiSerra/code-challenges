const helpers = require("../helpers/helpers.js");

const isValidSeq = seq => {
  seq.sort((a, b) => a - b);

  for (let i = 0; i < seq.length; i++) {
    if (i > 0 && seq[i] - seq[i - 1] > 3) return false;
  }
  return true;
};

// const findArrangemnt = (adapters, startVoltage, outVoltage, memo = {}) => {
//   if (!isValidSeq([startVoltage, ...adapters, outVoltage])) return 0;
//   const key = adapters.join(",");
//   if (memo[key]) return 0;
//   memo[key] = true;
//   console.log(Object.keys(memo).length, adapters.length);
//   let ways = 1;
//   for (let i = 0; i < adapters.length; i++) {
//     ways += findArrangemnt([...adapters.slice(0, i), ...adapters.slice(i + 1)], startVoltage, outVoltage, memo);
//   }

//   return ways;
// };
const findArrangemnt = (adapters, startVoltage, outVoltage, memo = {}) => {
  adapters.sort((a, b) => a - b);
  if (!isValidSeq([startVoltage, ...adapters, outVoltage])) return 0;
  const key = adapters.join(",");
  if (memo[key]) return 0;
  memo[key] = true;
  let last = startVoltage;
  let ways = 1;
  for (let i = 0; i < [...adapters, outVoltage].length - 1; i++) {
    const element = adapters[i];
    if (adapters[i + 1] - last <= 3) {
      ways += findArrangemnt([...adapters.slice(0, i), ...adapters.slice(i + 1)], startVoltage, outVoltage, memo);
    }
    last = element;
  }

  console.log(Object.keys(memo).length);
  return ways;
};

const solution = input => {
  const outVoltage = Math.max(...input) + 3;
  //input.push(outVoltage);

  //console.log(input);
  input.sort((a, b) => a - b);
  const res = findArrangemnt(input, 0, outVoltage);
  console.log(res);

  return false;
};

(async () => {
  let input = await helpers.readInput(10);
  input = input.split("\n");
  //let input = ["16", "10", "15", "5", "1", "11", "7", "19", "6", "12", "4"];
  //   let input = [
  //     "28",
  //     "33",
  //     "18",
  //     "42",
  //     "31",
  //     "14",
  //     "46",
  //     "20",
  //     "48",
  //     "47",
  //     "24",
  //     "23",
  //     "49",
  //     "45",
  //     "19",
  //     "38",
  //     "39",
  //     "11",
  //     "1",
  //     "32",
  //     "25",
  //     "35",
  //     "8",
  //     "17",
  //     "7",
  //     "9",
  //     "4",
  //     "2",
  //     "34",
  //     "10",
  //     "3",
  //   ];

  input = input.map(i => parseInt(i, 10)).filter(n => !isNaN(n));
  if (require.main === module) {
    console.log(solution(input));
  }
})();
