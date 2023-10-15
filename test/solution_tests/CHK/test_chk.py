from solutions.CHK import checkout_solution


class TestCHK():
    def test_CHK(self):
        assert checkout_solution.compute("AAA") == 145
