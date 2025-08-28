path = "C:/Users/kumar/OneDrive/Desktop/Python_Works/python_works/file_operation/food_logs.csv"

fr = open(path,"r")

food_logs =[]

for line in fr:

    data = line.rstrip("\n").split(",")

    if len(data)>1:

        dictionary = {"data":data[0],"meal_type":data[1],
                    "name":data[2],
                    "serving_type":data[3]
                    ,"calories":data[4]
                    }
        
    food_logs.append(dictionary)

print(food_logs)


# daily summary


daily_summary = {}

for e in food_logs:
    
    date = e.get("date")

    calories = e.get("calories")

    if date in daily_summary:

        daily_summary[date]+=calories

    else:

        daily_summary [date] = calories

print(daily_summary)
