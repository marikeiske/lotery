import streamlit as st
import random

def mega_sena():
    return random.sample(range(1, 61), 6)

def quina():
    return random.sample(range(1, 81), 5)

def lotofacil():
    return random.sample(range(1, 26), 15)

def verificar_acertos(numeros_sorteados, numeros_usuario):
    acertos = len(set(numeros_sorteados).intersection(set(numeros_usuario)))
    return acertos

def jogar_loteria(tipo, numeros_usuario):
    if tipo == 'Mega Sena':
        numeros_sorteados = mega_sena()
    elif tipo == 'Quina':
        numeros_sorteados = quina()
    elif tipo == 'Lotofácil':
        numeros_sorteados = lotofacil()
    else:
        return "Erro: Selecione um tipo de loteria válido"

    try:
        numeros_usuario = [int(num) for num in numeros_usuario.split()]
        if len(numeros_usuario) != len(numeros_sorteados):
            raise ValueError("Quantidade incorreta de números")
        if not all(1 <= num <= (60 if tipo == 'Mega Sena' else 80 if tipo == 'Quina' else 25) for num in numeros_usuario):
            raise ValueError(f"Os números devem estar entre 1 e {60 if tipo == 'Mega Sena' else 80 if tipo == 'Quina' else 25}")
    except ValueError as e:
        return f"Erro: Entrada inválida - {e}"

    acertos = verificar_acertos(numeros_sorteados, numeros_usuario)
    resultado = f"Números sorteados: {numeros_sorteados}\nNúmeros do usuário: {numeros_usuario}\nQuantidade de acertos: {acertos}"
    if acertos == len(numeros_sorteados):
        resultado += "\nParabéns, você acertou todos os números!"
    return resultado

st.title("Simulador de Loteria")
st.markdown("Selecione o tipo de loteria:")
tipo = st.selectbox("", ["Mega Sena", "Quina", "Lotofácil"])

if tipo == 'Mega Sena':
    instrucoes = "Insira 6 números entre 1 e 60:"
elif tipo == 'Quina':
    instrucoes = "Insira 5 números entre 1 e 80:"
elif tipo == 'Lotofácil':
    instrucoes = "Insira 15 números entre 1 e 25:"

st.markdown(instrucoes)
numeros_usuario = st.text_input("Números", type="default")

if st.button("Jogar"):
    resultado = jogar_loteria(tipo, numeros_usuario)
    st.write(resultado)