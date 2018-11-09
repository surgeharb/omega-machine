## Index 0 not used (R1, R2, R3)
R = [0, 0, 0, 0]

## Local Memory
MEM = [0, 0, 0, 0, 0, 0, 0, 0]

def _load(args):
  R[args[1]] = MEM[args[2]]
  return args[0] + 1

def _store(args):
  MEM[args[1]] = R[args[2]]
  print('ModifiedMEM', MEM)
  return args[0] + 1

def _add(args):
  R[args[1]] = R[args[2]] + R[args[3]]
  return args[0] + 1

def _sub(args):
  R[args[1]] = R[args[2]] - R[args[3]]
  return args[0] + 1

def _beq(args):
  if(R[args[2]] - R[args[1]] == 0):
    return args[3]
  else:
    return args[0] + 1

def _shl(args):
  R[args[1]] = R[args[2]] << R[args[3]]
  return args[0] + 1

def _shr(args):
  R[args[1]] = R[args[2]] >> R[args[3]]
  return args[0] + 1

def _jmp(args):
  return args[1]

def _addc(args):
  R[args[1]] = R[args[2]] + args[3]
  return args[0] + 1

def _subc(args):
  R[args[1]] = R[args[2]] - args[3]
  return args[0] + 1

def _shlc(args):
  R[args[1]] = R[args[2]] << args[3]
  return args[0] + 1

def _shrc(args):
  R[args[1]] = R[args[2]] >> args[3]
  return args[0] + 1

def _and(args):
  R[args[1]] = R[args[2]] & R[args[3]]
  return args[0] + 1

def _or(args):
  R[args[1]] = R[args[2]] | R[args[3]]
  return args[0] + 1

def _xor(args):
  R[args[1]] = R[args[2]] ^ R[args[3]]
  return args[0] + 1

def _slt(args):
  if (R[args[2]] - R[args[3]] < 0):
    R[args[1]] = 1
  else:
    R[args[1]] = 0

  return args[0] + 1

def _cmpeq(args):
  CF = 0  # COMPARE FLAG
  CF = (R[args[2]] - R[args[3]]) == 0

  if (CF == 0):
    R[args[1]] = 1
  else:
    R[args[1]] = 0

  return args[0] + 1

def _cmpeqc(args):
  CF = 0  # COMPARE FLAG
  CF = (R[args[2]] - args[3]) == 0

  if (CF == 0):
    R[args[1]] = 1
  else:
    R[args[1]] = 0

  return args[0] + 1

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
  return dispatch[instr](args)