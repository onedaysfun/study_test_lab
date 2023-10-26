import pytest
import request

class Testcase:
    @classmethod
    def setup_class(cls):
        pass

    def test_01(self):
        a = 0
        assert a == 3


if __name__ == '__main__':
    pytest.main(['-vs'])