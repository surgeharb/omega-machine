from program import *
from opcodes import *
from instructions import *

# Main Memory containing program instructions
M = code

# OFFSETS
OP_OFFSET = 26
R1_OFFSET = 21
R2_OFFSET = 16
R3_OFFSET = 11

def printRegisters():
  print('==> REGISTERS PRINT START')
  print('REG 1:', R[1])
  print('REG 2:', R[2])
  print('REG 3:', R[3])
  print('<== REGISTERS PRINT END\n')

def binary(number):
  return bin(number)[2:]

def main():
  print('STARTING')

  # PROGRAM COUNTER #
  PC = 0  # # # # # #
  # # # # # # # # # #

  while (PC < len(M)):
    # # # # # INSTRUCTION FETCH # # # # #
    opcode = binary(int(M[PC], 2) >> OP_OFFSET)
    opcode = ('0' + opcode if (len(opcode) == 5) else opcode)
    opcode = OP_CODES[opcode]

    R1 = int(binary(int(M[PC], 2) >> R1_OFFSET)[-5:], 2)
    R2 = int(binary(int(M[PC], 2) >> R2_OFFSET)[-5:], 2)
    R3 = int(binary(int(M[PC], 2) >> R3_OFFSET)[-5:], 2)

    # # # # # INSTRUCTION EXEC # # # # #
    PC = exec_instruction(opcode, [PC, R1, R2, R3])
  
    printRegisters()
  print('bye')
  return (0)

if __name__ == '__main__':
  main()