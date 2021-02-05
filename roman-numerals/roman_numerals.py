def roman(number):
       number_inv = str(number)[::-1]

       uni = {"0": "",
              "1": "I",
              "2": "II",
              "3": "III",
              "4": "IV",
              "5": "V",
              "6": "VI",
              "7": "VII",
              "8": "VIII",
              "9": "IX"}
       
       dez = {}
       cen = {}
       mil = {}
       for n in uni:
              dez[n] = uni[n].replace("X", "C").replace("I", "X").replace("V", "L")
              cen[n] = uni[n].replace("X", "M").replace("I", "C").replace("V", "D")
              mil[n] = uni[n].replace("I", "M").replace("V", "V-")

       romano = []
       for n, i in enumerate(number_inv):
              if n == 0:
                     romano.append(uni[i])
              elif n == 1:
                     romano.append(dez[i])
              elif n == 2:
                     romano.append(cen[i])
              else:
                     romano.append(mil[i])

       return "".join(reversed(romano))
