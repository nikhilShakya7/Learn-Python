def pin_extractor(poem):
    secret_code=''
    lines=poem.split("\n")
    for line in lines:
        words=line.split()
    return secret_code

poem="""Stars and the moon
shine in the sky
white and
until the end of the night"""

print(pin_extractor(poem))