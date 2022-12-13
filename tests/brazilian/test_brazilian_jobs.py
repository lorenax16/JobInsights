from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    file = "tests/mocks/brazilians_jobs.csv"
    fun = read_brazilian_file(file)[0].keys()
    assert "salary" in fun
    assert "title" in fun
    assert "type" in fun
