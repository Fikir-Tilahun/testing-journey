import string
def word_count(text):
    if text is None:
        return {}
    
    
    words = text.lower().split()
    word_counts = {}
    
    
    for word in words:
        clean = word.strip(string.punctuation)
        if clean:    
            word_counts[clean] = word_counts.get(clean, 0) + 1
        
    return word_counts