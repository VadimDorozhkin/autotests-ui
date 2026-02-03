import pytest


@pytest.mark.xfail(reason="Найден баг в приложении, из-за которого тест падает с ошибкой")
def test_with_bug():
    assert False

@pytest.mark.xfail(reason="Баг уже исправлен, но на тест все еще висит маркировка xfail")
def test_test_without_bug():
    ...


