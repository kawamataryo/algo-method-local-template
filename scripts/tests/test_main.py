import io


def test_main(cases, main, capsys, monkeypatch, subtests):
    for i, case in enumerate(cases):
        with subtests.test(msg="case-{}".format(i + 1), case=case):
            monkeypatch.setattr('sys.stdin', io.StringIO(case[0]))
            exec(main)
            captured = capsys.readouterr()
            assert case[1] == captured.out
