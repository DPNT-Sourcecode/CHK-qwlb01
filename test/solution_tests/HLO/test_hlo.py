from solutions.HLO import hello_solution


class TestHLO():
    def test_sum(self):
        assert hello_solution.compute("Tom") == "hello Tom"