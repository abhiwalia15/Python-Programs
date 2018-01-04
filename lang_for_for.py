fav_langs={
	'abhi':['python','c','c++'],
	'lovee':['c','ruby','html','r'],
	'mummy':['java','c'],
	}
for name,languages in fav_langs.items():
 print("\nThe favourite language of "+ name.title() + " is ")
 for language in languages:
  print("\t"+language)
