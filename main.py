#An Stock trading System developed By Sourav Ghosh
import investpy

# Taking input from user
company_name = input("Enter Company name: ").lower()
enter_countries = input("Enter Countries: ").lower()

# Company info
search_result = investpy.search_quotes(text=company_name, products=['stocks'],
                                       countries=[enter_countries], n_results=1)
print(search_result, "\n")

# information
information = search_result.retrieve_information()
print(information, "\n")

# Currency
default_currency = search_result.retrieve_currency()
print("Currency:",default_currency, "\n")

# technical_indicators
technical_indicators = search_result.retrieve_technical_indicators(interval='daily')
print(technical_indicators)