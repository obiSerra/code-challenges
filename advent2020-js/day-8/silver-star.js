const helpers = require("../helpers/helpers.js");

const parseInstruction = instruction => {
  const instr = instruction.split(" ");

  const num = parseInt(instr[1], 10);
  return [instr[0], num];
};
function exec_program(instructions) {
  let accumulator = 0;
  let instrNum = 0;

  const used = {};

  let nextInstr = instructions[instrNum];

  while (nextInstr) {
    if (instrNum in used) {
      return [accumulator, true];
    }
    used[instrNum] = true;
    const instr = parseInstruction(nextInstr);
    if (instr[0] === "nop") {
      instrNum++;
    } else if (instr[0] === "acc") {
      accumulator += instr[1];
      instrNum++;
    } else if (instr[0] === "jmp") {
      instrNum += instr[1];
    }
    nextInstr = instructions[instrNum];
  }

  return [accumulator, false]
}

module.exports.parseInstruction = parseInstruction;
module.exports.exec_program = exec_program;
(async () => {
  let input = await helpers.readInput(8);
  input = input.split("\n");
  //const input = ["nop +0", "acc +1", "jmp +4", "acc +3", "jmp -3", "acc -99", "acc +1", "jmp -4", "acc +6"];

  if (require.main === module) {
    console.log(exec_program(input)[0]);
  }
})();
