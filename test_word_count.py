from word_count import word_count

def test_counts_repeated_words():
    assert word_count("the cat the") == {"the": 2, "cat": 1}
    
    
def test_none_returns_empty_dict():
    assert word_count(None) == {}    


def test_empty_string():
    assert word_count("") == {}
    

def test_extra_spaces():
    assert word_count("a   b") == {"a": 1, "b": 1}    
    
    
def test_capitalization():
    assert word_count("The the") == {"the": 2} 
    
    
def test_punctuation_ignored():
    assert word_count("hello, hello!") == {"hello": 2}
    
    
def test_punctuation_only_is_ignored():
    assert word_count("hello - world") == {"hello": 1, "world": 1}           