"""
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
"""

def is_contain(string: str, part: str):
	buff = string[:len(part)]
	if part == buff:
		return True
	else:
		return False

s = [a for a in input().split()]

part = input()

for i in s:
	if is_contain(i, part):
		print(i, end = ' ')
