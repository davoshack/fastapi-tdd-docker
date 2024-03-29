import pytest


def test_create_summary(test_app, monkeypatch):
    pass


def test_create_summaries_invalid_json(test_app):
    pass


def test_read_summary(test_app, monkeypatch):
    pass


def test_read_summary_incorrect_id(test_app, monkeypatch):
    pass


def test_read_all_summaries(test_app, monkeypatch):
    pass


def test_remove_summary(test_app, monkeypatch):
    pass


def test_remove_summary_incorrect_id(test_app, monkeypatch):
    pass


def test_update_summary(test_app, monkeypatch):
    pass


@pytest.mark.parametrize(
    "summary_id, payload, status_code, detail",
    [
        [
            999,
            {"url": "https://foo.bar", "summary": "updated!"},
            404,
            "Summary not found",
        ],
        [
            0,
            {"url": "https://foo.bar", "summary": "updated!"},
            422,
            [
                {
                    "loc": ["path", "id"],
                    "msg": "ensure this value is greater than 0",
                    "type": "value_error.number.not_gt",
                    "ctx": {"limit_value": 0},
                }
            ],
        ],
        [
            1,
            {},
            422,
            [
                {
                    "loc": ["body", "url"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
                {
                    "loc": ["body", "summary"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
            ],
        ],
        [
            1,
            {"url": "https://foo.bar"},
            422,
            [
                {
                    "loc": ["body", "summary"],
                    "msg": "field required",
                    "type": "value_error.missing",
                }
            ],
        ],
    ],
)
def test_update_summary_invalid(
    test_app, monkeypatch, summary_id, payload, status_code, detail
):
    pass


def test_update_summary_invalid_url(test_app):
    pass
