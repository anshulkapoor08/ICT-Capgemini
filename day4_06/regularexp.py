import re
text = "This is a test"
pattern = "test"
wordmatch = re.search(pattern, text)
print(wordmatch)

# ^: This expression matches the start of a string
# $: This expression matches the end of a string
# .: This expression matches any character except a new line
# ?: The preceding character is optional
# +: The preceding character appears one or more times
# *: The preceding character appears zero or more times
# ,: The preceding character appears zero or more times
# []: A set of characters
# \: Escapes special characters