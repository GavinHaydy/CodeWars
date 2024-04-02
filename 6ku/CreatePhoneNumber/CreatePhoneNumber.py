def create_phone_number(n):
    n = "".join([str(i) for i in n])
    return f"({n[0:3]}) {n[3:6]}-{n[6:10]}"

# best
def create_phone_number1(n):
    print(*n)
	# return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
