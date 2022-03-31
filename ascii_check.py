# Check if a file contains only ASCII.
def is_ascii(file, buffersize=64*1024**1) -> bool:
  buffer = bytearray(buffersize)
  with open(file, 'rb') as fd:
      n = fd.readinto(buffer)
      if not buffer[:n].isascii():
          return False
  return True
