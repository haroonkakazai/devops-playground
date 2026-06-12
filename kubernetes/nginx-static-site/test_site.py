from pathlib import Path

def test_index_exists():
    assert Path("index.html").exists()

def test_css_exists():
    assert Path("style.css").exists()

def test_index_contains_heading():
    content = Path("index.html").read_text()

    assert "<h1>" in content