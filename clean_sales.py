import csv
import json

USD_TO_INR=91.6

input_file="sales.csv"
output_file="clean_sales.json"

clean_data=[]
seen=set()

with open(input_file,"r") as file:
    reader=csv.reader(file)

    for row in reader:
        order_id=row[0].strip()
        product=row[1].replace('"','').strip()
        price=row[2].replace('$','').strip()
        country=row[3].strip()

        price_usd=float(price)

        key=(product,price_usd)

        if key in seen:
            continue
        seen.add(key)

        price_inr=round(price_usd*USD_TO_INR,2)

        record={
            "order_id":order_id,
            "product":product,
            "price_usd":price_usd,
            "price_inr":price_inr,
            "country":country
        }
        clean_data.append(record)
with open(output_file,"w") as json_file:
    json.dump(clean_data,json_file,indent=4)

print("Data cleaned and saved to clean_sales.json")            