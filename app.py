import bomber
import asyncio

#Set Your inputs
input_keyword = "Marketing Automation"
input_country = "US"

#Set your Open AI API Key
API_KEY = "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"

#run
asyncio.run(bomber.get_keyword_data(input_keyword,input_country,API_KEY))

