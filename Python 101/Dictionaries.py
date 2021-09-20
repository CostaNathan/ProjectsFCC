## dictionaries are structures that store " key value pairs"
## variable = { key value pairs}
## within the {} -  'key': 'value'
## each key has to be unique
## the keys can be any type of data as long as it is unique

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

## print(monthConversions[key])
print(monthConversions["Mar"])
##print(monthConversions.get("Mar"))
## .get function = specify a default value if the key is not found
## .get(value, default)
print(monthConversions.get("Mar", "Not a valid key"))
