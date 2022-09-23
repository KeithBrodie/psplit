import sys

filename = sys.argv[1]

chunk = 65536
chunks_per_file = int(4e9/chunk)

try:

    f = open(filename,'rb')

except:

    raise ValueError("Cannot open {}".format(filename))

oi = 1
of = open(filename + '.split.{}'.format(oi), 'wb')

chunks = 0

while 1:

    data = f.read(chunk)

    if len(data):
        of.write(data)
        chunks = chunks + 1

    if len(data) < chunk:
         break

    if (chunks % chunks_per_file) == 0:

        of.close()
        oi += 1
        of = open(filename + '.split.{}'.format(oi), 'wb')

of.close()
f.close()

