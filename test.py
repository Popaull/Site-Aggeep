import difflib
test =["oui" ,"non"]
rem=difflib.get_close_matches("ouii",test).pop()

test.remove(difflib.get_close_matches("ouii",test).pop())
print(test)