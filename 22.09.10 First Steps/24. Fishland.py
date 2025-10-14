skumriya_price = float(input())
caca_price = float(input())
palamud_quantity = float(input())
safrid_qunatity = float(input())
midi_quantity = int(input())

palamud_price = skumriya_price * 0.6 + skumriya_price
safrid_price = caca_price * 0.8 + caca_price
midi_price = 7.5
total = palamud_price * palamud_quantity + safrid_price * safrid_qunatity + midi_price * midi_quantity

print(f"{total:.2f}")
