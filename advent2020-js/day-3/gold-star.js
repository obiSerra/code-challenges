const helpers = require("../helpers/helpers.js");
const { basicSolution } = require("./silver-star.js");

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

  const slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
  ]
    .map(dirs => basicSolution(input, dirs[0], dirs[1]))
    .reduce((acc, v) => acc * v);

  console.log(slopes);
})();
