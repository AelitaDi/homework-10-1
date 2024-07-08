from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(operation_list_1):
    assert filter_by_state(operation_list_1, "EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert filter_by_state(operation_list_1, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    assert filter_by_state(operation_list_1, "ABC") == []


def test_sort_by_state_base(operation_list_1, expected_sort_false, expected_sort_true):
    assert sort_by_date(operation_list_1) == expected_sort_true
    assert sort_by_date(operation_list_1, False) == expected_sort_false


def test_sort_by_date_incorrect(operation_list_2, operation_list_3, operation_list_4, operation_list_5):
    assert sort_by_date(operation_list_2) == []
    assert sort_by_date(operation_list_3) == []
    assert sort_by_date(operation_list_4) == []
    assert sort_by_date(operation_list_5) == []
