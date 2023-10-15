from solutions.CHK import checkout_solution


class TestCHK():
    def test_CHK(self):
        assert checkout_solution.compute("AAAABB") == 225
        assert checkout_solution.compute("AA") == 100
        assert checkout_solution.compute("AF") == -1
