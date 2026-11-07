import importlib


def test_package_can_be_imported():
    assert importlib.import_module("test_repo") is not None


def test_cli(capsys):
    from test_repo.__main__ import main

    main()

    assert capsys.readouterr().out == "test-repo\n"
