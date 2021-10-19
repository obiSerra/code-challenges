const helpers = require("../helpers/helpers.js");

const basicSolution = (input, right, down) => {
  let pos = [0, 0];
  const height = input.length;
  const width = input[0].length;
  let trees = 0;

  while (pos[0] < input.length) {
    let [r, c] = pos;
    if (input[r][c] === "#") {
      trees++;
    }
    pos[0] = r + down;
    pos[1] = (c + right) % width;
  }

  return trees;
};

(async () => {
  let input = await helpers.readInput(3);
  input = input.split("\n");

  //   let input = [
  //     "..##.......",
  //     "#...#...#..",
  //     ".#....#..#.",
  //     "..#.#...#.#",
  //     ".#...##..#.",
  //     "..#.##.....",
  //     ".#.#.#....#",
  //     ".#........#",
  //     "#.##...#...",
  //     "#...##....#",
  //     ".#..#...#.#",
  //   ];

  input = input.map(r => r.split(""));

//  console.log(basicSolution(input, 3, 1));
})();

module.exports.basicSolution = basicSolution;
