from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from datetime import datetime
import re

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

def text_to_query(text: str) -> dict:
    prompt = f"Convert this to a MongoDB query: {text}"
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=128)
    raw = tokenizer.decode(outputs[0], skip_special_tokens=True)

    try:
        query = eval(raw)  # not recommended for production
    except:
        query = {}

    # ✅ Post-processing: map words to trip_status
    if "closed" in text.lower():
        query["trip_status"] = 0
    elif "close" in text.lower():
        query["trip_status"] = 0    
    elif "running" in text.lower():
        query["trip_status"] = 1
    elif "cancel" in text.lower():
        query["trip_status"] = 2     


    # ✅ Post-processing: map words to trip_status
    if "district" in text.lower():
        query["district_name"] = "Sitapur"
    elif "district name" in text.lower():
        query["district_name"] = "Gorakhpur"
            

    # ✅ Post-process date ranges (rough example)
    date_match = re.search(r"from (\d{1,2}) to (\d{1,2}) (\w+)", text.lower())
    if date_match:
        start_day, end_day, month = date_match.groups()
        month = month.capitalize()
        start_date = f"2025-{month_to_num(month)}-{int(start_day):02d} 00:00:00"
        end_date = f"2025-{month_to_num(month)}-{int(end_day):02d} 23:59:59"
        query["run_date"] = {
            "$gte": start_date,
            "$lte": end_date
        }

    return query

def month_to_num(month: str) -> str:
    months = {
        "January": "01", "February": "02", "March": "03", "April": "04",
        "May": "05", "June": "06", "July": "07", "August": "08",
        "September": "09", "October": "10", "November": "11", "December": "12"
    }
    return months.get(month, "01")
