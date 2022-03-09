def multi_input(request: str) -> "list[str]":
	resp = input(request)
	vals = resp.split(',')
	if len(vals) > 4:
		print("too many values, only using first 4")
		return vals[:4]
	elif len(vals) == 0:
		print("no inputs provided, returning zeroed array")
		return [0,0,0,0]
	elif len(vals) < 4:
		print("not enough values, appending 0s")
		while len(vals) < 4:
			vals.append(0)
		return vals
	else:
		return vals

[x, y, z, b] = multi_input('Insert x1, x2, y1, y2 as comma separated values (ex: 2,1,3,5): ')
print(x)
print(y)
print(z)
print(b)
print([x,y,z,b])
