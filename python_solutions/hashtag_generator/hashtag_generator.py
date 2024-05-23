def generate_hashtag(s):
    result = "#"
    s_split = s.split(" ")
    word_list = list(filter(lambda a: a != '', s_split))
    for word in word_list:
        result += word.capitalize()
    if result == "#" or len(result) > 140:
        return False
    else:
        return result