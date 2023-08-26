from main import doom_printer, what_are_the_vars

obj = what_are_the_vars(None)
doom_printer(obj)

print("var_0: None\nend")
print("--------------------------")
obj = what_are_the_vars(lambda x: x, function=what_are_the_vars)
doom_printer(obj)

print("function: <function what_are_the_vars at 0x...>\nvar_0: <function <lambda> at 0x...>\nend")
print("--------------------------")

obj = what_are_the_vars(3, var_0=2)
doom_printer(obj)

print("ERROR\nend")

