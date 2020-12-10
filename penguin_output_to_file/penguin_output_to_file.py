in_file = open('penguins_amount.txt', 'r')
amount = int(in_file.read())

out_file = open('penguins_picture.txt', 'w')
out_file.write( "   _~_   " * amount + '\n' +
                "  (o o)  " * amount + '\n' +
                " /  V  \\ " * amount + '\n' +
                "/(  _  )\\" * amount + '\n' +
                "  ^^ ^^  " * amount)
out_file.close()
