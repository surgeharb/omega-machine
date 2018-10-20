from config import *
from program import *

# Main Memory containing program instructions
M = code

# Program Counter
PC = 0

# Registers
R = [0, 0, 0]

# OFFSETS
OP_OFFSET = 26
R1_OFFSET = 21
R2_OFFSET = 16
R3_OFFSET = 11

def printRegisters():
  print('==> REGISTERS PRINT START')
  print('REG 1:', R[0])
  print('REG 2:', R[1])
  print('REG 3:', R[2])
  print('<== REGISTERS PRINT END\n')

def _load(destination, address):
  R[destination] = M[address]
  PC = PC + 1

def _store(source, address):
  M[address] = R[source]
  PC = PC + 1

def _add(destination, source1, source2):
  R[destination]= R[source1] + R[source2]
  PC = PC + 1

def _sub(destination, source1, source2):
  R[destination]= R[source1] - R[source2]
  PC = PC + 1

def _beq(source1, source2, address):
  if(R[source2] - R[source1] == 0):
    PC = address
  else:
    PC = PC + 1

def _shl(destination, source1, source2):
  R[destination] = R[source1] << R[source2]
  PC = PC + 1

def _shr(destination, source1, source2):
  R[destination] = R[source1] >> R[source2]
  PC = PC + 1

def _br(address):
  PC = address

def _addc(destination, source, val):
    R[destination] = R[source] + val
    PC = PC + 1

def _subc(destination, source, val):
    R[destination] = R[source] - val
    PC = PC + 1

def _and(destination, source1, source2):
    R[destination] = R[source1] & R[source2]
    PC = PC + 1

def _or(destination,  source1,  source2):
    R[destination] = R[source1] | R[source2]
    PC = PC + 1

def _xor(destination,  source1,  source2):
    R[destination] = R[source1] ^ R[source2]
    PC = PC + 1

def _slt(destination,  source1,  source2):
  if (R[source1] - R[source2] < 0):
    R[destination] = 1
  else:
    R[destination] = 0

  PC = PC + 1

def _seq(destination,  source1,  source2):
  if (R[source1] == R[source2]):
    R[destination] = 1
  else:
    R[destination] = 0

  PC = PC + 1

def binary(string):
  return bin(int(string))[2:]

def main():
  print('machine started')

  R1 = 0
  R2 = 0
  R3 = 0
  
  while(PC < len(M)):
    # Fetch binary instruction opcode
    opcode = binary(M[PC] >> OP_OFFSET)

    if (opcode == OP_LD):
      R1 = binary(M[PC] >> R1_OFFSET)
      R2 = binary(M[PC] >> R2_OFFSET)

      print("ld R" + int(R1, 2) + ", R" + int(R2, 2))
      _load(R1, R2)

    elif (opcode == OP_ST):
      R1 = binary(M[PC] >> R1_OFFSET)
      R2 = binary(M[PC] >> R2_OFFSET)

      print("st R" + int(R1, 2) + ", R" + int(R2, 2))
      _store(R1, R2)

    elif (opcode == OP_ADD):
      R1 = binary(M[PC] >> R1_OFFSET)
      R2 = binary(M[PC] >> R2_OFFSET)
      R3 = binary(M[PC] >> R3_OFFSET)

      print("add R" + int(R1, 2) + ", R" + int(R2, 2) + ", R" + int(R3, 2))
      _add(R1, R2, R3)

    elif (opcode == OP_SUB):
      R1 = binary(M[PC] >> R1_OFFSET)
      R2 = binary(M[PC] >> R2_OFFSET)
      R3 = binary(M[PC] >> R3_OFFSET)

      print("sub R" + int(R1, 2) + ", R" + int(R2, 2) + ", R" + int(R3, 2))
      _sub(R1, R2, R3)

    elif (opcode == OP_BEQ):
      R1 = binary(M[PC] >> R1_OFFSET)
      R2 = binary(M[PC] >> R2_OFFSET)
      R3 = binary(M[PC] >> R3_OFFSET)

      print("beq R" + int(R1, 2) + ", R" + int(R2, 2) + ", R" + int(R3, 2))
      _beq(R1, R2, R3)

    elif (opcode == OP_SHL):
      R1 = binary(M[PC] >> R1_OFFSET)
      R2 = binary(M[PC] >> R2_OFFSET)
      R3 = binary(M[PC] >> R3_OFFSET)

      print("shl R" + int(R1, 2) + ", R" + int(R2, 2) + ", R" + int(R3, 2))
      _shl(R1, R2, R3)

    elif (opcode == OP_SHR):
      R1 = binary(M[PC] >> R1_OFFSET)
      R2 = binary(M[PC] >> R2_OFFSET)
      R3 = binary(M[PC] >> R3_OFFSET)

      print("shr R" + int(R1, 2) + ", R" + int(R2, 2) + ", R" + int(R3, 2))
      _shr(R1, R2, R3)

    elif (opcode == OP_BR):
      R1 = binary(M[PC] >> R1_OFFSET)

      print("br R" + int(R1, 2))
      _br(R1)

    elif (opcode == OP_ADDC):
      R1 = binary(M[PC] >> R1_OFFSET)
      R2 = binary(M[PC] >> R2_OFFSET)
      R3 = binary(M[PC] >> R3_OFFSET)

      print("addc R" + int(R1, 2) + ", R" + int(R2, 2) + ", R" + int(R3, 2))
      _addc(R1, R2, R3)

    elif (opcode == OP_SUBC):
      R1 = binary(M[PC] >> R1_OFFSET)
      R2 = binary(M[PC] >> R2_OFFSET)
      R3 = binary(M[PC] >> R3_OFFSET)

      print("subc R" + int(R1, 2) + ", R" + int(R2, 2) + ", R" + int(R3, 2))
      _subc(R1, R2, R3)

    elif (opcode == OP_AND):
      R1 = binary(M[PC] >> R1_OFFSET)
      R2 = binary(M[PC] >> R2_OFFSET)
      R3 = binary(M[PC] >> R3_OFFSET)

      print("and R" + int(R1, 2) + ", R" + int(R2, 2) + ", R" + int(R3, 2))
      _and(R1, R2, R3)

    elif (opcode == OP_OR):
      R1 = binary(M[PC] >> R1_OFFSET)
      R2 = binary(M[PC] >> R2_OFFSET)
      R3 = binary(M[PC] >> R3_OFFSET)

      print("or R" + int(R1, 2) + ", R" + int(R2, 2) + ", R" + int(R3, 2))
      _or(R1, R2, R3)

    elif (opcode == OP_XOR):
      R1 = binary(M[PC] >> R1_OFFSET)
      R2 = binary(M[PC] >> R2_OFFSET)
      R3 = binary(M[PC] >> R3_OFFSET)

      print("xor R" + int(R1, 2) + ", R" + int(R2, 2) + ", R" + int(R3, 2))
      _xor(R1, R2, R3)

    elif (opcode == OP_SLT):
      R1 = binary(M[PC] >> R1_OFFSET)
      R2 = binary(M[PC] >> R2_OFFSET)
      R3 = binary(M[PC] >> R3_OFFSET)

      print("slt R" + int(R1, 2) + ", R" + int(R2, 2) + ", R" + int(R3, 2))
      _slt(R1, R2, R3)

    elif (opcode == OP_SEQ):
      R1 = binary(M[PC] >> R1_OFFSET)
      R2 = binary(M[PC] >> R2_OFFSET)
      R3 = binary(M[PC] >> R3_OFFSET)

      print("seq R" + int(R1, 2) + ", R" + int(R2, 2) + ", R" + int(R3, 2))
      _seq(R1, R2, R3)
  
  print('bye')
  return (0)

if __name__ == '__main__':
  main()