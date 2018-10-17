from config import *
from program import *

# Main Memory containing program instructions
MAIN_MEMORY = code

# Registers
REG = [0, 0, 0]

def printRegisters():
  print('==> REGISTERS PRINT START')
  print('REG 1:', REG[0])
  print('REG 2:', REG[1])
  print('REG 3:', REG[2])
  print('<== REGISTERS PRINT END\n')

def instructionDecode(instruction):
  print('==> INSTRUCTION FETCH & DECODE START')
  print('instruction:', ''.join(str(x) for x in list(reversed(instruction))))

  opcode = ''.join(str(x) for x in list(reversed(instruction[26:32])))
  reg1 = ''.join(str(x) for x in list(reversed(instruction[21:26])))
  reg2 = ''.join(str(x) for x in list(reversed(instruction[16:21])))
  reg3 = ''.join(str(x) for x in list(reversed(instruction[11:16])))
  unused = ''.join(str(x) for x in list(reversed(instruction[0:11])))

  print('opcode:', opcode)
  print('reg1:', reg1)
  print('reg2:', reg2)
  print('reg3:', reg3)
  print('unused:', unused)
  print('<== INSTRUCTION FETCH & DECODE END\n')

  return {
    'opcode': opcodes[opcode],
    'param1': int(reg1, 2),
    'param2': int(reg2, 2),
    'param3': int(reg3, 2)
  }

def instructionExec(instruction):
  param2 = ''

  if (instruction['opcode'] == 'add'):
    reg_index = instruction['param3'] - 1
    REG[reg_index] = REG[instruction['param1'] - 1] + REG[instruction['param2'] - 1]
    param2 = 'R' + str(instruction['param2'])

  elif (instruction['opcode'] == 'sub'):
    reg_index = instruction['param3'] - 1
    REG[reg_index] = REG[instruction['param1'] - 1] - REG[instruction['param2'] - 1]
    param2 = 'R' + str(instruction['param2'])

  elif (instruction['opcode'] == 'addc'):
    reg_index = instruction['param3'] - 1
    REG[reg_index] = REG[instruction['param1'] - 1] + instruction['param2']
    param2 = instruction['param2']

  elif (instruction['opcode'] == 'subc'):
    reg_index = instruction['param3'] - 1
    REG[reg_index] = REG[instruction['param1'] - 1] - instruction['param2']
    param2 = instruction['param2']

  return print(
    '<== INSTRUCTION EXEC START\n' + instruction['opcode'],
    'R' + str(instruction['param1']) + ',', str(param2) + ',',
    'R' + str(instruction['param3']), '\n<== INSTRUCTION FETCH END\n'
  )

def main():
  print('machine started')

  for instruction in MAIN_MEMORY:
    # for loop applies INSTRUCTION FETCH
    decoded_instruction = instructionDecode(instruction)
    instructionExec(decoded_instruction)
    printRegisters()

  print('bye')

if __name__ == '__main__':
  main()