from config import *
from program import *

# Main Memory containing program instructions
M = code

# Registers
## Index 0 not used
R = [0, 0, 0, 0]

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

def _load(PC, destination, address):
  R[destination] = M[address]
  return PC + 1

def _store(PC, source, address):
  M[address] = R[source]
  return PC + 1

def _add(PC, destination, source1, source2):
  R[destination]= R[source1] + R[source2]
  return PC + 1

def _sub(PC, destination, source1, source2):
  R[destination]= R[source1] - R[source2]
  return PC + 1

def _beq(PC, source1, source2, address):
  if(R[source2] - R[source1] == 0):
    return address
  else:
    return PC + 1

def _shl(PC, destination, source1, source2):
  R[destination] = R[source1] << R[source2]
  return PC + 1

def _shr(PC, destination, source1, source2):
  R[destination] = R[source1] >> R[source2]
  return PC + 1

def _br(address):
  return address

def _addc(PC, destination, source, val):
  R[destination] = R[source] + val
  return PC + 1

def _subc(PC, destination, source, val):
  R[destination] = R[source] - val
  return PC + 1

def _and(PC, destination, source1, source2):
  R[destination] = R[source1] & R[source2]
  return PC + 1

def _or(PC, destination,  source1,  source2):
  R[destination] = R[source1] | R[source2]
  return PC + 1

def _xor(PC, destination,  source1,  source2):
  R[destination] = R[source1] ^ R[source2]
  return PC + 1

def _slt(PC, destination,  source1,  source2):
  if (R[source1] - R[source2] < 0):
    R[destination] = 1
  else:
    R[destination] = 0

  return PC + 1

def _seq(PC, destination,  source1,  source2):
  if (R[source1] == R[source2]):
    R[destination] = 1
  else:
    R[destination] = 0

  return PC + 1

def binary(number):
  return bin(number)[2:]

def main():
  print('STARTING')

  PC = 0
  R1 = 0
  R2 = 0
  R3 = 0

  while (PC < len(M)):
    # Fetch binary instruction opcode
    opcode = binary(int(M[PC], 2) >> OP_OFFSET)

    if (opcode == OP_LD):
      R1 = int(binary(int(M[PC], 2) >> R1_OFFSET)[-5:], 2)
      R2 = int(binary(int(M[PC], 2) >> R2_OFFSET)[-5:], 2)

      print("ld R" + str(R1) + ", R" + str(R2))
      PC = _load(PC, R1, R2)

    elif (opcode == OP_ST):
      R1 = int(binary(int(M[PC], 2) >> R1_OFFSET)[-5:], 2)
      R2 = int(binary(int(M[PC], 2) >> R2_OFFSET)[-5:], 2)

      print("st R" + str(R1) + ", R" + str(R2))
      PC = _store(PC, R1, R2)

    elif (opcode == OP_ADD):
      R1 = int(binary(int(M[PC], 2) >> R1_OFFSET)[-5:], 2)
      R2 = int(binary(int(M[PC], 2) >> R2_OFFSET)[-5:], 2)
      R3 = int(binary(int(M[PC], 2) >> R3_OFFSET)[-5:], 2)

      print("add R" + str(R1) + ", R" + str(R2) + ", R" + str(R3))
      PC = _add(PC, R1, R2, R3)

    elif (opcode == OP_SUB):
      R1 = int(binary(int(M[PC], 2) >> R1_OFFSET)[-5:], 2)
      R2 = int(binary(int(M[PC], 2) >> R2_OFFSET)[-5:], 2)
      R3 = int(binary(int(M[PC], 2) >> R3_OFFSET)[-5:], 2)

      print("sub R" + str(R1) + ", R" + str(R2) + ", R" + str(R3))
      PC = _sub(PC, R1, R2, R3)

    elif (opcode == OP_BEQ):
      R1 = int(binary(int(M[PC], 2) >> R1_OFFSET)[-5:], 2)
      R2 = int(binary(int(M[PC], 2) >> R2_OFFSET)[-5:], 2)
      R3 = int(binary(int(M[PC], 2) >> R3_OFFSET)[-5:], 2)

      print("beq R" + str(R1) + ", R" + str(R2) + ", R" + str(R3))
      PC = _beq(PC, R1, R2, R3)

    elif (opcode == OP_SHL):
      R1 = int(binary(int(M[PC], 2) >> R1_OFFSET)[-5:], 2)
      R2 = int(binary(int(M[PC], 2) >> R2_OFFSET)[-5:], 2)
      R3 = int(binary(int(M[PC], 2) >> R3_OFFSET)[-5:], 2)

      print("shl R" + str(R1) + ", R" + str(R2) + ", R" + str(R3))
      PC = _shl(PC, R1, R2, R3)

    elif (opcode == OP_SHR):
      R1 = int(binary(int(M[PC], 2) >> R1_OFFSET)[-5:], 2)
      R2 = int(binary(int(M[PC], 2) >> R2_OFFSET)[-5:], 2)
      R3 = int(binary(int(M[PC], 2) >> R3_OFFSET)[-5:], 2)

      print("shr R" + str(R1) + ", R" + str(R2) + ", R" + str(R3))
      PC = _shr(PC, R1, R2, R3)

    # elif (opcode == OP_BR):
    #   R1 = binary(int(M[PC], 2) >> R1_OFFSET)

    #   print("br R" + str(R1))
    #   _br(R1)

    elif (opcode == OP_ADDC):
      R1 = int(binary(int(M[PC], 2) >> R1_OFFSET)[-5:], 2)
      R2 = int(binary(int(M[PC], 2) >> R2_OFFSET)[-5:], 2)
      R3 = int(binary(int(M[PC], 2) >> R3_OFFSET)[-5:], 2)

      print("addc R" + str(R1) + ", R" + str(R2) + ", " + str(R3))
      PC = _addc(PC, R1, R2, R3)

    elif (opcode == OP_SUBC):
      R1 = int(binary(int(M[PC], 2) >> R1_OFFSET)[-5:], 2)
      R2 = int(binary(int(M[PC], 2) >> R2_OFFSET)[-5:], 2)
      R3 = int(binary(int(M[PC], 2) >> R3_OFFSET)[-5:], 2)

      print("addc R" + str(R1) + ", R" + str(R2) + ", " + str(R3))
      PC = _subc(PC, R1, R2, R3)

    elif (opcode == OP_AND):
      R1 = int(binary(int(M[PC], 2) >> R1_OFFSET)[-5:], 2)
      R2 = int(binary(int(M[PC], 2) >> R2_OFFSET)[-5:], 2)
      R3 = int(binary(int(M[PC], 2) >> R3_OFFSET)[-5:], 2)

      print("and R" + str(R1) + ", R" + str(R2) + ", R" + str(R3))
      PC = _and(PC, R1, R2, R3)

    elif (opcode == OP_OR):
      R1 = int(binary(int(M[PC], 2) >> R1_OFFSET)[-5:], 2)
      R2 = int(binary(int(M[PC], 2) >> R2_OFFSET)[-5:], 2)
      R3 = int(binary(int(M[PC], 2) >> R3_OFFSET)[-5:], 2)

      print("or R" + str(R1) + ", R" + str(R2) + ", R" + str(R3))
      PC = _or(PC, R1, R2, R3)

    elif (opcode == OP_XOR):
      R1 = int(binary(int(M[PC], 2) >> R1_OFFSET)[-5:], 2)
      R2 = int(binary(int(M[PC], 2) >> R2_OFFSET)[-5:], 2)
      R3 = int(binary(int(M[PC], 2) >> R3_OFFSET)[-5:], 2)

      print("xor R" + str(R1) + ", R" + str(R2) + ", R" + str(R3))
      PC = _xor(PC, R1, R2, R3)

    # elif (opcode == OP_SLT):
    #   R1 = binary(int(M[PC], 2) >> R1_OFFSET)
    #   R2 = binary(int(M[PC], 2) >> R2_OFFSET)
    #   R3 = binary(int(M[PC], 2) >> R3_OFFSET)

    #   print("slt R" + str(R1) + ", R" + str(R2) + ", R" + str(R3))
    #   _slt(PC, R1, R2, R3)

    # elif (opcode == OP_SEQ):
    #   R1 = binary(int(M[PC], 2) >> R1_OFFSET)
    #   R2 = binary(int(M[PC], 2) >> R2_OFFSET)
    #   R3 = binary(int(M[PC], 2) >> R3_OFFSET)

    #   print("seq R" + str(R1) + ", R" + str(R2) + ", R" + str(R3))
    #   _seq(PC, R1, R2, R3)
  
    printRegisters()
  print('bye')
  return (0)

if __name__ == '__main__':
  main()