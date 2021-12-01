const helpers = require("../helpers/helpers.js");

const makeAdpChain = (adapters, currentVoltage, diffs = [0, 0]) => {
  if (adapters.length === 0) return diffs;

  for (let i = 0; i < adapters.length; i++) {
    const adapter = adapters[i];
    const diff = adapter - currentVoltage;

    if (diff >= 0 && diff <= 3) {
      const remAdapters = [...adapters.slice(0, i), ...adapters.slice(i + 1)];
      let updDiffs = [...diffs];

      if (diff === 1) updDiffs[0] = updDiffs[0] + 1;
      if (diff === 3) updDiffs[1] = updDiffs[1] + 1;
      const changes = makeAdpChain(remAdapters, adapter, updDiffs);
      if (changes) {
        return changes;
      }
    }
  }

  return false;
};

const solution = input => {
  const outAdapter = Math.max(...input) + 3;
  input.push(outAdapter);
  input.sort((a, b) => a - b);
  console.log(input);
  const res = makeAdpChain(input, 0);
  if (res) return res[0] * res[1];

  return false;
};

(async () => {
  let input = await helpers.readInput(10);
  input = input.split("\n");
  //let input = ["16", "10", "15", "5", "1", "11", "7", "19", "6", "12", "4"];
  // let input = [
  //   "28",
  //   "33",
  //   "18",
  //   "42",
  //   "31",
  //   "14",
  //   "46",
  //   "20",
  //   "48",
  //   "47",
  //   "24",
  //   "23",
  //   "49",
  //   "45",
  //   "19",
  //   "38",
  //   "39",
  //   "11",
  //   "1",
  //   "32",
  //   "25",
  //   "35",
  //   "8",
  //   "17",
  //   "7",
  //   "9",
  //   "4",
  //   "2",
  //   "34",
  //   "10",
  //   "3",
  // ];

  input = input.map(i => parseInt(i, 10)).filter(n => !isNaN(n));
  if (require.main === module) {
    console.log(solution(input));
  }
})();
