import streamlit as st
import random
import time
import matplotlib.pyplot as plt
import numpy as np

# Função para encontrar a posição de partição (com exibição de informações)
def partition_with_display(array, low, high):
    pivot = array[high]
    st.write(f"Pivot escolhido: {pivot}")
    
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    
    st.write(f"Partição realizada no índice {i + 1}, Array: {array}")
    return i + 1

# Função para encontrar a posição de partição (sem exibição de informações)
def partition_no_display(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

# Função para realizar o quicksort (com exibição de informações)
def quickSort_with_display(array, low, high):
    if low < high:
        pi = partition_with_display(array, low, high)
        quickSort_with_display(array, low, pi - 1)
        quickSort_with_display(array, pi + 1, high)

# Função para realizar o quicksort (sem exibição de informações)
def quickSort_no_display(array, low, high):
    if low < high:
        pi = partition_no_display(array, low, high)
        quickSort_no_display(array, low, pi - 1)
        quickSort_no_display(array, pi + 1, high)

# Função para medir o tempo de execução (sem exibição de informações)
def measure_time(array):
    start_time = time.time()
    quickSort_no_display(array, 0, len(array) - 1)
    end_time = time.time()
    return (end_time - start_time) * 1000  # Tempo em milissegundos

# Interface Streamlit
st.title("QuickSort Visualization")

# Entrada do array pelo usuário
array_input = st.text_input("Digite os números do array separados por vírgula", "10, 7, 8, 9, 1, 5")
array = [int(x) for x in array_input.split(',')]

if st.button('Executar QuickSort'):
    st.write("Array inicial:", array)
    quickSort_with_display(array, 0, len(array) - 1)
    st.write("Array ordenado:", array)

# Gráfico de desempenho
st.title("Gráfico de Desempenho do QuickSort")

# Entrada para tamanhos diferentes para os arrays
size_input = st.text_input("Digite tamanhos de array separados por vírgula (ex: 10, 100, 1000)", "10, 100, 1000, 10000, 100000")
sizes = [int(x) for x in size_input.split(',')]

if st.button('Gerar Gráfico de Desempenho'):
    times = []
    for size in sizes:
        array = random.sample(range(size * 10), size)  # Array aleatório
        exec_time = measure_time(array)
        times.append(exec_time)
    
    # Criar o gráfico
    fig, ax = plt.subplots()
    ax.plot(sizes, times, marker='o', color='b')
    
    # Adicionando rótulos e título
    ax.set_xlabel('Tamanho da Entrada')
    ax.set_ylabel('Tempo de Execução (ms)')
    ax.set_title('Relação entre Tempo de Execução e Tamanho da Entrada (QuickSort)')
    ax.grid(True)
    
    # Exibir o gráfico no Streamlit
    st.pyplot(fig)
