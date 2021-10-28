# with open("binary", 'bw') as bin_file:
#     bin_file.write(bytes(range(17)))
#
# with open("binary", 'br') as binFile:
#     for b in binFile:
#         print(b)



# Write Code
a = 65534       # FF FE
b = 65535       # FF FF
c = 65536       # 00 01 00 00
x = 2998302     # 02 2D C0 1E

with open("binary2", 'bw') as bin_file:
    bin_file.write(a.to_bytes(2, 'big')) # parameter = length aka num of bytes wanted, byte order aka
    bin_file.write(b.to_bytes(2, 'big')) # whether to return BIG indian or LITTLE indian
    bin_file.write(c.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'little'))

# Read Code
with open("binary2", 'br') as bin_file:
    e = int.from_bytes(bin_file.read(2), 'big') # var `a`
    print(e)
    f = int.from_bytes(bin_file.read(2), 'big') # var `b`
    print(f)
    g = int.from_bytes(bin_file.read(4), 'big') # var `c`
    print(g)
    h = int.from_bytes(bin_file.read(4), 'big') # var `x` w/ BIG endian
    print(h)
    i = int.from_bytes(bin_file.read(4), 'big') # var `x` w/ LITTLE endian
    print(i)

# we WANT to read all the files back as BIG endian

