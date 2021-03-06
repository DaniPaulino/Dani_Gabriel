import cloudpickle
from flask import Flask, render_template, request

with open('model.pkl', 'rb') as file_in:
  model = cloudpickle.load(file_in)

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', nome='Fulano')

@app.route('/predicao', methods=['POST'])
def predicao():
  Genero = int(request.form['Genero'])
  Casado = int(request.form['Casado'])
  Dependentes = int(request.form['Dependentes'])
  MesesComoCliente = int(request.form['MesesComoCliente'])
  ServicoTelefone = int(request.form['ServicoTelefone'])
  ServicoInternet = int(request.form['ServicoInternet'])
  ServicoSegurancaOnline = int(request.form['ServicoSegurancaOnline'])
  ServicoBackupOnline = int(request.form['ServicoBackupOnline'])
  ProtecaoEquipamento = int(request.form['ProtecaoEquipamento'])
  ServicoSuporteTecnico = int(request.form['ServicoSuporteTecnico'])
  ServicoStreamingTV = int(request.form['ServicoStreamingTV'])
  ServicoFilmes = int(request.form['ServicoFilmes'])
  TipoContrato = int(request.form['TipoContrato'])
  FaturaDigital = int(request.form['FaturaDigital'])
  FormaPagamento = int(request.form['FormaPagamento'])
  ValorMensal = float(request.form['ValorMensal'])
 
  predicao = model.predict([[Genero,Casado,Dependentes,MesesComoCliente,ServicoTelefone,ServicoInternet,ServicoSegurancaOnline,ServicoBackupOnline,ProtecaoEquipamento,ServicoSuporteTecnico,ServicoStreamingTV,ServicoFilmes,TipoContrato,FaturaDigital,FormaPagamento,ValorMensal]])
  return render_template('resposta.html', predicao=predicao[0])

app.run(debug=True)

# pip install python app.py-r requirements.txt (instala as bibliotecas)
#  (para executar)
# git add .
# git commit -m "nomenovo"
# git push

#0 - nao houve churn
#1 - sim


