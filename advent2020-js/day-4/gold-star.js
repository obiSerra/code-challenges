const helpers = require("../helpers/helpers.js");

(async () => {
  let input = await helpers.readInput(4);
  input = input.split("\n");

  const validateDate = (entry, field, minVal, maxVal) => {
    const matches = entry.match(`${field}:s?([0-9]{4})`);
    if (!matches) return false;
    const value = parseInt(matches[1]);
    return value >= minVal && value <= maxVal;
  };

  const validByr = entry => validateDate(entry, "byr", 1920, 2002);
  const validIyr = entry => validateDate(entry, "iyr", 2010, 2020);
  const validEyr = entry => validateDate(entry, "eyr", 2020, 2030);

  const validHeight = entry => {
    const inMatches = entry.match(`hgt:s?([0-9]*)in`);
    const cmMatches = entry.match(`hgt:s?([0-9]*)cm`);
    if (!inMatches && !cmMatches) return false;
    const value = inMatches ? parseInt(inMatches[1], 10) : parseInt(cmMatches[1], 10);
    if (inMatches) return 59 <= value && value <= 76;
    else if (cmMatches) return 150 <= value && value <= 193;
    else return false;
  };

  const validHcl = entry => entry.match(`hcl:s?#[0-9a-f]{6}`);
  const validEcl = entry => entry.match(`ecl:s?(amb|blu|brn|gry|grn|hzl|oth)`);
  const validPid = entry => entry.match(`pid:s?[0-9]{9}`);

  const hasRequired = entry =>
    validByr(entry) &&
    validIyr(entry) &&
    validEyr(entry) &&
    validHeight(entry) &&
    validHcl(entry) &&
    validEcl(entry) &&
    validPid(entry);

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
    const valids = entries.filter(hasRequired);
    return valids.length;
  };

  console.log(solution(input));
})();
