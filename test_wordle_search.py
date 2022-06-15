import wordle_search_engine as wse

def test_read_data():
    assert isinstance(wse.read_data('words.txt'),list) == True
    assert len(wse.read_data('words.txt')) == 2317