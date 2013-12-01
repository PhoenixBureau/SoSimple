import os, unittest, tempfile
import main


class TestTest(unittest.TestCase):

  def setUp(self):
    self.db_fd, main.app.config['DATABASE'] = tempfile.mkstemp()
    main.app.config['TESTING'] = True
    self.app = main.app.test_client()

  def tearDown(self):
    os.close(self.db_fd)
    os.unlink(main.app.config['DATABASE'])

  def test_hello(self):
    rv = self.app.get('/')
    print 230
    self.assertTrue('Hello World!' in rv.data)


if __name__ == '__main__':
    unittest.main()
