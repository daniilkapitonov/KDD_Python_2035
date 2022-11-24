h = "['q', 'w', 'e', 'r', 't', 'y', 'u', 'i']"
print(h, type(h))
h = h.replace("[", "")
h = h.replace("]", "")
h = h.replace("'", "")
h = h.replace(" ", "")
print(h)
print(h.split(","), type(h.split(",")))