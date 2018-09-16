def test_{{num}}(selenium):
    selenium.get('http://localhost:8000')
    assert selenium.title == 'Test Page'
