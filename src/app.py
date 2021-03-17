"""https://izziswift.com/flask-calling-python-function-on-button-onclick-event/"""  # noqa
from flask import Flask, render_template, request, redirect, url_for                # noqa
from iSocket import iSocket
import webbrowser
app = Flask(__name__)

data = {'ip1':'192.168.58.114', 'SCPI1':'*IDN?', 'out1':'',
        'ip2':'192.168.58.109', 'SCPI2':'*IDN?\r\n*OPT?', 'out2':''}

@app.route("/")     # noqa
def index():
    return render_template('index.html', data=data)


@app.route("/instr1/", methods=['POST'])
def instr1():
    if request.method == 'POST':
        # (((Get HTML Form Data)))
        data['ip1']   = request.form.get('ipaddr', '')      # form element name
        data['SCPI1'] = request.form.get('scpiArry', '')    # form element name
    else:
        data['ip1']   = request.args.get('ipaddr')
        data['SCPI1'] = request.args.get('scpi')

    # (((Perform actions)))
    instr1 = iSocket().open(data['ip1'], 5025)
    data['out1'] = instr1.send_SCPI_arry(data['SCPI1'].split('\r\n'))
    instr1.close()
    return redirect(url_for('index'))


@app.route("/instr2/", methods=['POST'])
def instr2():
    # (((Get HTML Form Data)))
    data['ip2']   = request.form.get('ipaddr', '')          # form element name
    data['SCPI2'] = request.form.get('scpiArry', '')        # form element name

    # (((Perform actions)))
    instr2 = iSocket().open(data['ip2'], 5025)
    data['out2'] = instr2.send_SCPI_arry(data['SCPI2'].split('\r\n'))
    instr2.close()
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    # app.debug = True
    webbrowser.open('http:////127.0.0.1:5000/')
    app.run()
