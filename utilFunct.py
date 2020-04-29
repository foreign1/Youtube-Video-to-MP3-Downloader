import re
# Function to remove non alphanumeric characters from video title
def titleNormalizer(title):
    title = [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in title.split("\n")]
    # Convert title list to string
    title = listToString(title)
    # Return title
    return title

# Function to convert list to string
def listToString(l):
    # Initialize empty string
    string = ''
    # Iterate over list and add elements to string
    for ele in l:
        string = string + ele
    # Return converted list
    return string