sample_dict={"Ashutosh":"KIm jeha","madhur":"sashank","Om":"omjali"}
print(type(sample_dict))
print(sample_dict.items())
print(sample_dict["Om"])
sample_dict.update({"sashank":"sonam"})
print(sample_dict)
#sample_dict.pop("madhur")
print(sample_dict)
print(sample_dict.get("madhur"))
print(sample_dict.keys())
print(sample_dict.values())
#print(sample_dict.clear())
sample_dict.popitem()
print(sample_dict)