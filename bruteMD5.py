import hashlib

target_hash = "c3fcd3d76192e4007dfb496cca67e13b"

with open('fsocity.dic') as wordlist:
	lines = [line.strip() for line in wordlist.readlines() if line]
	lines = set(lines)
	for line in lines:
		hash_actual = hashlib.md5(line.encode()).hexdigest()
		hash_lower = hashlib.md5(line.lower().encode()).hexdigest()
		hash_upper = hashlib.md5(line.upper().encode()).hexdigest()
		if hash_actual == target_hash:
			print(line)
		if hash_lower == target_hash:
			print(line.lower())
		if hash_upper == target_hash:
			print(line.upper())