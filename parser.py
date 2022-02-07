# Parser
# Part of Port. 2.0
# By Port. Prerogative Club
# (c) 2022

# objective: identify all capitalized words in a string of arbitrary length
# Edge case 1: ALL CAPS - for titles, etc. 
# Edge case 2: "We Are Building Something Special"
# Edge case 3: "Alex, Ani, Bill, and Chris went shopping.
# Edge case 4: "People used to work at Alex. Brown & Co."
# Edge case 5: "I like tea by Twinnings. I have also tried Taylors of Harrogate."
# Edge case 6: "athenahealth starts with a lowercase letter."


## take a string
## break it into words - split by " "
## those are your tokens. 
## order the tokens
## for each token in list
## 	if capitalized
## 		brand = token
##		if token + 1 is capitalized:
##			brand = brand + token
## 
## def is_capped(token) --> brand or None
##	for token in list_of_tokens:
##		brand = is_capped(token)
##		for next_token in list of tokens:
##			if is_capped(next_token):
##				brand = brand + next_token			
## def alt_parse(list_of_tokens) --> list_of_brands:
##	brands = []
##	for i in len(list_of_tokens):
##		brand = None		
##		candidate = list_of_tokens[i]
##		j = i + 1
##		next = list_of_tokens[j]
##		if is_valid(candidate):
##			brand = candidate
##			brand = brand + is_valid(next)
##		brands.append(brand)
##	return brands
##
#### won't work? or not very elegant?
#### 

#### a better solution would: pass the remainder, return one brand at a time
####
##   def get_next_brand(list_of_tokens):
##	limit = len(list_of_tokens)
##	brand = ""
##	i = 0
##	while i < limit:
##		candidate = tokens[i]
##		if is_capitalized(candidate):
##			brand = candidate
##			break
##		else:
##			i = i + 1
##			continue
##	return brand
####	will return the first brand or nothing
####

##   def get_next_brand2(list_of_tokens):
##	limit = len(list_of_tokens)
##	brand = ""
##	i = 0
##	while i < limit:
##		candidate = tokens[i]
##		if is_capitalized(candidate):
##			brand = candidate
##			j = 1 + 1
##			remaining_tokens = tokens[1:]
##			next = get_next_brand2(remaining_tokens)
##			## problem is this will look too far ahead. it will skip words
##
##			brand = brand + next
##			break
##		else:
##			i = i + 1
##			continue
##	return brand
####	will return the first brand or nothing
####


## def get_first_brand(tokens):
##	brand = ""
##	while i <= len(tokens):
##		first_token = tokens[i]
##		if not is_brand(first_token):
##			break
##		else:
##			brand = first_token
##			remainder = tokens[1:]
##			addition = get_first_brand(remainder)
##			brand = brand + addition
##			break
##		i = i + 1
##
##	return brand
##

## def one_more_time(tokens):
##	brand = None
##	candidate = tokens[0]
##	if not is_brand(candidate):
##		pass
##	else:
##`		brand = candidate
##		remainder = tokens[1:]
##		addition = one_more_time(remainder)
##		if addition:
##			brand = brand + remainder
##	return brand

## def get_brands(tokens):
##	brands = list()
##	for token in tokens:
##		if is_brand(token):
##			brands.append(token)
##			## does not work
##
##		brand = one_more_time(tokens)
##		brands.append(brand)
##	return brand

## match case?
## if not match case then full text search
## that should be done at the edge? usually is in other clients, but takes time. so may be you push it out ## for background processing. if in watchlist. 
## 

## def append_or_stop(tokens):
##	brand = ""
## 	if not is_brand(tokens[0]):
##		pass
##	else:
##		brand = tokens[0]
##		appendix, remainder = append_or_stop(tokens[1:])
##		brand = brand + appendix
##	return brand, remainder

## def is_brand(word):
##	result = False
##	if word[0].isUpper():
##		result = True
##	return result

##  need to work on position basis too
##

