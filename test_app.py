import app


def test_header_present():
    layout = str(app.app.layout)
    assert "Soul Foods" in layout


def test_visualisation_present():
    layout = str(app.app.layout)
    assert "sales-graph" in layout


def test_region_picker_present():
    layout = str(app.app.layout)
    assert "region-filter" in layout