#Grupo OPE
# ALUNO 1: Caio Vinicius da Silva de Souza RA: 1903623
# ALUNO 2: Cristiane de Oliveira RA: 1903794
# ALUNO 3: Guilherme Jacob Mello RA: 1903675
# ALUNO 4: Henrique de Sousa Silva RA: 1903972
# ALUNO 5: João Júnior RA: 1903563
# ALUNO 6: Lucas Silva Teles RA: 1903981

from app import app, db

if __name__ == "__main__":
    # cria Banco
    db.create_all()
    # executa a aplicação
    app.run(debug=True)