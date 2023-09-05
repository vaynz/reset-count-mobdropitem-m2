with open('mob_drop_item.txt', 'r', encoding='latin2') as infile, open('output_mob_drop_item.txt', 'w', encoding='latin2') as outfile:
	count = 1
	for line in infile:
		line = line.rstrip()
		parts = line.split('\t')
		
		if '}' in line:
			count = 1
			print("Reset count to 1")
		
		if len(parts) >= 2 and parts[1].isdigit():
			parts[1] = str(count)
			count += 1
			print(f"Modified line: {line.strip()} -> {'    '.join(parts)}")
		
		new_line = '\t'.join(parts) + '\n'
		outfile.write(new_line)
