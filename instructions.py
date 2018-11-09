# REGISTERS
R1 = 0
R2 = 0
R3 = 0

## Index 0 not used
R = [0, 0, 0, 0]

def _load(PC, destination, address):
  # R[destination] = M[address]
  return PC + 1

def _store(PC, source, address):
  # M[address] = R[source]
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

def _jmp(address):
  print('address', address)
  return address

def _addc(PC, destination, source, val):
  R[destination] = R[source] + val
  return PC + 1

def _subc(PC, destination, source, val):
  R[destination] = R[source] - val
  return PC + 1

def _shlc(PC, destination, source, val):
  R[destination] = R[source] << val
  return PC + 1

def _shrc(PC, destination, source, val):
  R[destination] = R[source] >> val
  return PC + 1

def _and(PC, destination, source1, source2):
  R[destination] = R[source1] & R[source2]
  return PC + 1

def _or(PC, destination, source1, source2):
  R[destination] = R[source1] | R[source2]
  return PC + 1

def _xor(PC, destination, source1, source2):
  R[destination] = R[source1] ^ R[source2]
  return PC + 1

def _slt(PC, destination, source1, source2):
  if (R[source1] - R[source2] < 0):
    R[destination] = 1
  else:
    R[destination] = 0

  return PC + 1

def _cmpeq(PC, destination, source1, source2):
  if (R[source1] == R[source2]):
    R[destination] = 1
  else:
    R[destination] = 0

  return PC + 1

def _cmpeqc(PC, destination, source, val):
  if (R[source] == val):
    R[destination] = 1
  else:
    R[destination] = 0

  return PC + 1

dispatch = {
  'OP_LD'     : _load,
  'OP_ST'     : _store,
  'OP_JMP'    : _jmp,
  'OP_BEQ'    : _beq,
  'OP_ADD'    : _add,
  'OP_SUB'    : _sub,
  'OP_CMPEQ'  : _cmpeq,
  'OP_AND'    : _and,
  'OP_OR'     : _or,
  'OP_XOR'    : _xor,
  'OP_SHL'    : _shl,
  'OP_SHR'    : _shr,
  'OP_ADDC'   : _addc,
  'OP_SUBC'   : _subc,
  'OP_CMPEQC' : _cmpeqc,
  'OP_SHLC'   : _shlc,
  'OP_SHRC'   : _shrc
}

def exec_instruction(instr, args):
  return dispatch[instr](args[0], args[1], args[2], args[3])