import logging
from subprocess import Popen, PIPE
from flask import Flask, request, render_template, jsonify


def _setup_log():
  log = logging.getLogger('sosimple')
  log.setLevel(logging.DEBUG)

  sh = logging.StreamHandler()
  sh.setLevel(logging.DEBUG)
  sh.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s'))
  log.addHandler(sh)

  fh = logging.FileHandler('sosimple.log')
  fh.setLevel(logging.INFO)
  fh.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
  log.addHandler(fh)

  return log


log = _setup_log()


def update():
  p = Popen(["git", "pull"], stdout=PIPE, stderr=PIPE)
  return p.communicate()


app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/hookey', methods=['POST'])
def hookey():
  data = dict(request.form)
  log.info('hook %r', data)
  pull, err = update()
  if err:
    log.error('pull %s', err)
  else:
    log.info('pull %r', pull)
  return jsonify(data=data)


if __name__ == '__main__':
  app.run(host='0.0.0.0')
