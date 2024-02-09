import subprocess

def executar_script(script):
    try:
        subprocess.run(["python", script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o script {script}: {e}")
        raise

# Lista dos scripts em ordem de execução
scripts = ["baixar_resultados.py", "apagar_tabela.py", "gerar_db.py", "popular_db.py"]

# Iterar sobre os scripts e executá-los em sequência
for script in scripts:
    print(f"Executando o script: {script}")
    executar_script(script)

print("Todos os scripts foram executados com sucesso.")
