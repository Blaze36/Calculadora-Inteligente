import streamlit as st
import pandas as pd

st.set_page_config(page_title="Calculadora Inteligente")

st.title(" Calculadora de Presupuesto Inteligente ")
st.write("Gestiona tus finanzas académicos")

# Formulario de entrada
with st.form("presupuesto_form"):
    st.subheader("Ingresa tus datos mensuales")
    
    ingresos = st.number_input("Ingresos Totales (Mesas, becas, trabajos):", min_value=0.0, step=10.0)
    alquiler = st.number_input("Gasto en Alquiler/Residencia:", min_value=0.0, step=10.0)
    comida = st.number_input("Gasto en Alimentación:", min_value=0.0, step=10.0)
    transporte = st.number_input("Gasto en Transporte:", min_value=0.0, step=10.0)
    
    submit = st.form_submit_button("Calcular Balance")

if submit:
    # Validación básica (ya controlada por min_value, pero reforzamos)
    if ingresos == 0:
        st.warning(" ingresar un monto de ingresos valido")
    else:
        # Procesamiento de datos con Pandas pd 
        data = {
            "Categoría": ["Alquiler", "Comida", "Transporte"],
            "Monto": [alquiler, comida, transporte]
        }
        df = pd.DataFrame(data)
        total_gastos = df["Monto"].sum()
        saldo_final = ingresos - total_gastos
        
        # Visualizar la tabla de los gastos 
        st.write("### Resumen de Gastos")
        st.dataframe(df, use_container_width=True)
        
        st.metric("Saldo Final", f"${saldo_final:,.2f}")
        
        if saldo_final < 0:
            st.error(f" Estás gastando mas de lo que ingresas ¡Déficit de ${abs(saldo_final):,.2f}!")
        elif saldo_final < (ingresos * 0.1):
            st.warning(" Tu margen de ahorro es muy bajo.")
        else:
            st.success(" Tienes un presupuesto Bueno")