import copy
import cheese


def test_def_prefs_full():
    cheese.write_default_cheese_preferences()
    expected = cheese._default_prefs
    actual = cheese.read_cheese_preferences()
    assert expected == actual


def test_def_prefs_change_home(monkeypatch, tmpdir):
    monkeypatch.setenv("HOME", tmpdir.mkdir("home"))
    cheese.write_default_cheese_preferences()
    expected = cheese._default_prefs
    actual = cheese.read_cheese_preferences()
    assert expected == actual


def test_def_prefs_change_expanduser(monkeypatch, tmpdir):
    fake_home_dir = tmpdir.mkdir("home")

    monkeypatch.setattr(
        cheese.os.path, "expanduser", (lambda x: x.replace("~", str(fake_home_dir)))
    )

    cheese.write_default_cheese_preferences()
    expected = cheese._default_prefs
    actual = cheese.read_cheese_preferences()
    assert expected == actual


def test_def_prefs_change_defaults(monkeypatch, tmpdir):
    # write the file once
    fake_home_dir = tmpdir.mkdir("home")
    monkeypatch.setattr(
        cheese.os.path, "expanduser", (lambda x: x.replace("~", str(fake_home_dir)))
    )
    cheese.write_default_cheese_preferences()
    defaults_before = copy.deepcopy(cheese._default_prefs)

    # change the defaults
    monkeypatch.setitem(cheese._default_prefs, 'slicing', ['provolone'])
    monkeypatch.setitem(cheese._default_prefs, 'spreadable', ['brie'])
    monkeypatch.setitem(cheese._default_prefs, 'salads', ['pepper jack'])
    defaults_modified = cheese._default_prefs

    # write it again with modified defaults
    cheese.write_default_cheese_preferences()

    # read, and check
    actual = cheese.read_cheese_preferences()
    assert defaults_modified == actual
    assert defaults_modified != defaults_before

