manifest = [["bananas", 15], ["mattresses", 34], ["dog kennels",2], ["machine that goes ping!", 12], ["tea chests", 10], ["cheeses", 0]]
cargo_hold=[]
cargo_weight=0 
for cargo in manifest:
  print('the current weight is :{}'.format(cargo_weight))
  if cargo_weight>=100:
    break
  else:
    print('adding:{}'.format(cargo[0]))
    print('with weight:{}'.format(cargo[1]))
    cargo_weight+=cargo[1]
    cargo_hold.append(cargo[0])
print(cargo_weight)
print(cargo_hold)