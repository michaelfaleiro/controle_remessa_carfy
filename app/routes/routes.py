from app import app
from flask import render_template, url_for, jsonify, request
import gspread

gc = gspread.service_account(filename='service_account.json')

sh = gc.open_by_key('1z9OMBvdHQm8LTnDDPLMaNi6B79C9avh-6hm4cDkhOtQ')


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/listar', methods=['GET', 'POST'])
def listar_envios():
    worksheet = sh.worksheet("Teste")
    data = {}

    if request.method == 'POST':
        search = request.form.get('search')
        values = worksheet.findall(search)
        print(values)
        print(worksheet.find(search))
        list = []
        for rows in values:
            list.append(worksheet.row_values(rows.row))

            data = list
    else:
        data = worksheet.get_all_records()
    return render_template('listar_envios.html', values=data)


@app.route('/api/listar')
def api_listar_envios():
    worksheet = sh.worksheet("Teste")
    data = {}
    data['values'] = worksheet.get_all_records()
    return jsonify(data)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/relatorios')
def relatorios():
    return render_template('relatorios.html')


@app.route('/configuracao')
def configuracao():
    return render_template('configuracao.html')
