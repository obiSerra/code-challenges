const helpers = require("../helpers/helpers.js");

(async () => {
    let input = await helpers.readInput(2);
    input = input.split("\n");

  //const input = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"];
  const parseEntry = entry => {
    if (!entry) return false
    const elements = entry.split(" ");
    const range = elements[0].split("-").map(e => parseInt(e, 10));
    const letter = elements[1].replace(":", "");
    let cnt = 0;
    for (let l of elements[2].split("")) {
      if (l === letter) cnt++;
    }
    return range[0] <= cnt && cnt <= range[1];
  };

  const solution = input => {
    let cnt = 0;

    for (let pwd of input) {
      if (parseEntry(pwd)) cnt++;
    }
    return cnt;
  };

  console.log(solution(input));
})();
