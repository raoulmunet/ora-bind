from ora_bind import convert_literals

def test_common_literals():
    r=convert_literals("select * from t where id=123 and status='ACTIVE' and d>=DATE '2026-01-01'")
    assert r.sql.count(":b") == 3
    assert [b.kind for b in r.binds] == ["number","string","date"]

def test_comments_unchanged():
    r=convert_literals("select id from t -- id=123\nwhere id=456")
    assert "-- id=123" in r.sql
    assert len(r.binds)==1
