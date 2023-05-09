#nested dict with list
Benz_dist={
"C_class" : {
	"c180" : ["mercides-c180","mechanical engin","180hp","2022 model","cost 1500000"],
	"c200" : ["mercides-c200","mechanical engin","200hp","2022 model","cost 1500000"]
	},
"G_class" : {
	"g63" : ["mercedes-g63","mechanical engin","270hp","2022 model","cost 3700000"],
	"g65" : ["mercedes-g65","mechanical engin","280hp","2022 model","cost 3900000"]
	},
"S_class" : {
	"s500" : ["mercedes-s500","mechanical engin","300hp","2022 model","cost 2600000"],
	"s600" : ["mercedes-s600","mechanical engin","320hp","2022 model","cost 2350000"]
	}
}
BMW_dist={
"X_series" : {
	"x1" : ["BMW-x1","mechanical engin","200hp","2022 model","cost 3000000"],
	"x6" : ["BMW-x6","hypred engin","450hp","2023 model","cost 5000000"]
	},
"series_7" : {
	"first" : ["BMW7-high line","hypred engin","330hp","2023 model","cost 4800000"],
	"second" : ["BMW7-normal","hypred engin","300hp","2023 model","cost 4300000"]
	},
"series_3" : {
	"first" : ["BMW3-high line","hypred engin","290hp","2023 model","cost 2800000"],
	"second" : ["BMW3-normal","hypred engin","280hp","2023 model","cost 2300000"]
	}
}

brand=input('please enter the Brand name from the list [Benz-BMW] :')
if brand =='Benz':	
	series=input("please enter the series [C_class - G_class - S_class] : ")
	if series =='C_class':
		model=input("please enter the model [c180-c200] :")
		print(Benz_dist[series][model])
	elif series =='G_class':
		model=input("please enter the model [g63-g65] :")
		print(Benz_dist[series][model])
	if series =='S_class':
		model=input("please enter the model [s500-s600] :")
		print(Benz_dist[series][model])
elif brand =='BMW':
	series=input("please enter the series [X_series - series_7 - series_3] : ")
	if series =='X_series':
		model=input("please enter the model [x1-x6] :")
		print(BMW_dist[series][model])
	elif series =='series_7':
		model=input("please enter the model [first-second] :")
		print(BMW_dist[series][model])
	if series =='series_3':
		model=input("please enter the model [first-second] :")
		print(BMW_dist[series][model])
		
'''##test
print(Benz_dist["C_class"]["c200"])
print(Benz_dist["C_class"]["c200"][0])
print(Benz_dist["C_class"]["c200"][:2:1])
'''
