import unittest
import pypixz_lite as ppxzl

class TestPackagesCase(unittest.TestCase):
    def test_install_requirements(self):
        ppxzl.install_requirements("requirements.txt")

    def test_install_modules(self):
        ppxzl.install_modules("pypixz")

if __name__ == '__main__':
    unittest.main()
