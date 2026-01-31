from page_loader.naming import generate_filename


def test_generate_filename_simple():
    assert generate_filename("https://example.com/blog/post") == "example-com-blog-post.html"


def test_generate_filename_with_slash():
    assert generate_filename("https://example.com/") == "example-com.html"


def test_generate_filename_with_params():
    assert generate_filename("https://example.com?page=1&utm_source=google") == \
        "example-com-page-1-utm-source-google.html"


def test_generate_filename_with_special_chars():
    assert generate_filename("https://example.com/@author") == "example-com-author.html"
