import logging, logging.config
from subprocess import Popen, PIPE
from flask import Flask, request, render_template, jsonify
import log_config


log = logging.getLogger('sosimple')


def update():
  p = Popen(["git", "pull"], stdout=PIPE, stderr=PIPE)
  return p.communicate()


app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/hookey')
def hookey():
  pull, err = update()
  log.info('pull %r', pull + err)
  return jsonify(data=data)


if __name__ == '__main__':
  logging.config.dictConfig(log_config.config)
  app.run(host='0.0.0.0')
