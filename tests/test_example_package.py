from example_package import __file__ as test_file, __version__, home, main


def test_version():
    assert __version__ == '1.0.0'


def test_home():
    assert test_file == f'{home()}/__init__.py'


def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert 'successfully installed' in captured.out
