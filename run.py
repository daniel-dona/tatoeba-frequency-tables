#!/usr/bin/env python3

sentences_file = "sentences.csv"

output_path = "output/"

list_size = 10000

skip_lang = ["cmn", "kor", "\\N", "jpn"]

lang_list = []

with open(sentences_file) as sentences:

	for sentence in sentences:
	
		col = sentence.split("\t")
		
		if not col[1] in lang_list and not col[1] in skip_lang:
		
			lang_list.append(col[1])
	
print("Language list:", lang_list)
	
			
for lang in lang_list:
	
	print("Processing language:", lang)
	
	freq_list = {}
	
	with open(sentences_file) as sentences:
		
		with open(output_path+lang+".txt", "w+") as output_file:

			for sentence in sentences:
			
				col = sentence.split("\t")
				
				if col[1] == lang:
					
					words = col[2].replace("\n", "").split(" ")
					
					for word in words:
						
						if word in freq_list:
							
							freq_list[word] += 1
							
						else:
						
							freq_list[word] = 1
							
			ordered_list = { k:v for k, v in sorted(freq_list.items(), key=lambda item: item[1], reverse=True) }
				
			for item in list(ordered_list.keys())[:list_size]:
					
				print(item, ordered_list[item], file=output_file)
				
		
