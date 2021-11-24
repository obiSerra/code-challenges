const helpers = require("../helpers/helpers.js");

const { parseInstruction, exec_program } = require("./silver-star.js");

const solution = input => {
  for (let i in input) {
    const newSeq = [...input];

    let instruction = input[i];

    if (/^nop/.test(instruction)) instruction = instruction.replace("nop", "jmp");
    else if (/^jmp/.test(instruction)) instruction = instruction.replace("jmp", "nop");

    newSeq[i] = instruction;

    const res = exec_program(newSeq);
    if (!res[1]) return res[0];
  }
};

module.exports.parseInstruction = parseInstruction;
(async () => {
  let input = await helpers.readInput(8);
  input = input.split("\n");
  //   const input = ["nop +0", "acc +1", "jmp +4", "acc +3", "jmp -3", "acc -99", "acc +1", "jmp -4", "acc +6"];

  if (require.main === module) {
    console.log(solution(input));
  }
})();
