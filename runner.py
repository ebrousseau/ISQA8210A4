# tests/runner.py
import unittest

# import your test modules

import mfs_custadd
import mfs_custedit
import mfs_custdelete


#Prepared by Erik Brousseau

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTest(loader.loadTestsFromModule(mfs_custadd))
suite.addTest(loader.loadTestsFromModule(mfs_custedit))
suite.addTest(loader.loadTestsFromModule(mfs_custdelete))



# initialize a runner, pass it your suite and run it
executor = unittest.TextTestRunner(verbosity=3)
result = executor.run(suite)