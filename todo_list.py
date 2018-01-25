def todo_list(make_list,base_list=['wake up']):
	
	base_list.append(make_list)
	
	return base_list
	
print(todo_list("begin orbital transfer"))
print(todo_list('do masturbate'))
