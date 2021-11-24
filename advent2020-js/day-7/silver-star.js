const helpers = require("../helpers/helpers.js");
const lineTemplate = /([a-z]* [a-z]*) bags contain ([a-z 0-9,]*)./;

const generateTree = input => {
  const bags = {};
  for (const row of input) {
    const groups = row.match(lineTemplate);
    if (!groups) break;
    const [_, name, content] = groups;
    const content_bags = content
      .replace(/bags?/g, "")
      .split(",")
      .map(e => e.trim());
    bags[name] = [];
    for (let c of content_bags) {
      if (c !== "no other") {
        const els = c.match(/([0-9]{1}) ([a-z ]*)/);
        const [_, num, c_name] = els;
        bags[name].push({ num: parseInt(num, 10), name: c_name });
      }
    }
  }
  return bags;
};

exports.generateTree = generateTree;
(async () => {
  let input = await helpers.readInput(7);
  input = input.split("\n");

  // const input = [
  //   "light red bags contain 1 bright white bag, 2 muted yellow bags.",
  //   "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
  //   "bright white bags contain 1 shiny gold bag.",
  //   "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
  //   "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
  //   "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
  //   "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
  //   "dotted black bags contain no other bags.",
  //   "faded blue bags contain no other bags.",
  // ];

  const canContain = (node, tree, toSearch, cache = {}) => {
    const content = tree[node];

    if (node in cache) return cache[node];
    if (content.length === 0) return false;

    let can = false;

    for (let cont of content) {
      if (cont.name === toSearch) can = true;

      can = can || canContain(cont.name, tree, toSearch, cache);
    }

    cache[node] = can;

    return can;
  };

  const solution = input => {
    const tree = generateTree(input);
    const canList = Object.keys(tree).filter(k => canContain(k, tree, "shiny gold"));
    return canList.length;
  };

  if (require.main === module) {
    console.log(solution(input));
  }
})();
