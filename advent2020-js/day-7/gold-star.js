const generateTree = require("./silver-star.js").generateTree;
const helpers = require("../helpers/helpers.js");

(async () => {
  let input = await helpers.readInput(7);
  input = input.split("\n");

  //   const input = [
  //     "light red bags contain 1 bright white bag, 2 muted yellow bags.",
  //     "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
  //     "bright white bags contain 1 shiny gold bag.",
  //     "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
  //     "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
  //     "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
  //     "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
  //     "dotted black bags contain no other bags.",
  //     "faded blue bags contain no other bags.",
  //   ];

  //   const input = [
  //     "shiny gold bags contain 2 dark red bags.",
  //     "dark red bags contain 2 dark orange bags.",
  //     "dark orange bags contain 2 dark yellow bags.",
  //     "dark yellow bags contain 2 dark green bags.",
  //     "dark green bags contain 2 dark blue bags.",
  //     "dark blue bags contain 2 dark violet bags.",
  //     "dark violet bags contain no other bags.",
  //   ];

  const containBags = (tree, root, count = 0, cache = {}) => {
    if (!root) return count;
    if (cache[root]) return cache[root];

    let cnt = count;
    const content = tree[root];
    for (let c of content) {
      cnt = cnt + c.num * containBags(tree, c.name, 1, cache);
    }

    cache[root] = cnt;
    return cnt;
  };

  const solution = input => {
    const tree = generateTree(input);
    return containBags(tree, "shiny gold");
  };

  if (require.main === module) {
    console.log(solution(input));
  }
})();
