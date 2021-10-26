const helpers = require("../helpers/helpers.js");

(async () => {
  let input = await helpers.readInput(4);
  input = input.split("\n");

  //   const input = [
  //     "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
  //     "byr:1937 iyr:2017 cid:147 hgt:183cm",
  //     "",
  //     "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
  //     "hcl:#cfa07d byr:1929",
  //     "",
  //     "hcl:#ae17e1 iyr:2013",
  //     "eyr:2024",
  //     "ecl:brn pid:760753108 byr:1931",
  //     "hgt:179cm",
  //     "",
  //     "hcl:#cfa07d eyr:2025 pid:166559648",
  //     "iyr:2011 ecl:brn hgt:59in",
  //   ];

  const hasRequired = entry =>
    entry.match("byr:") &&
    entry.match("iyr:") &&
    entry.match("eyr:") &&
    entry.match("hgt:") &&
    entry.match("hcl") &&
    entry.match("ecl") &&
    entry.match("pid");

  const solution = input => {
    const entries = input.reduce(
      (acc, v) => {
        if (v === "") {
          acc.push("");
        } else {
          acc[acc.length - 1] = acc[acc.length - 1] + " " + v;
        }
        return acc;
      },
      [""]
    );
    return entries.filter(hasRequired).length;
  };

  console.log(solution(input));
})();
