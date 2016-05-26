def formate_name(name):
	return name[0].upper() + name[1:].lower()


if __name__ == "__main__":
	print map(formate_name,["adam","LISA","barT"])
