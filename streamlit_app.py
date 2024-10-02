import streamlit as st
import json

# Cargar el archivo JSON con el itinerario
with open("itinerary_europe_2024.json", "r") as f:
    itinerary_json = json.load(f)

# Título de la aplicación
st.title("Itinerario de Viaje - Europa 2024")

# Sidebar para seleccionar el día
selected_day = st.sidebar.selectbox("Selecciona el día", list(itinerary_json.keys()))

# Mostrar las actividades del día seleccionado
if selected_day:
    st.header(f"Actividades del día {selected_day}")

    # Iterar por los momentos del día (mañana, mediodía, tarde, tardenoche, noche)
    for time_of_day, activities in itinerary_json[selected_day].items():
        st.subheader(f"{time_of_day.capitalize()}")

        # Mostrar una tarjeta por cada actividad
        for activity in activities:
            st.write(f"### {activity['Lugar a visitar']}")
            st.write(f"**Ciudad:** {activity['Ciudad']}")
            st.write(f"**Fecha:** {activity['Fecha']}")
            st.write(f"**Dirección:** {activity['Dirección']}")
            st.write(f"**Notas:** {activity['Notas']}")
            if activity['Link']:
                st.write(f"[Más información]({activity['Link']})")
            st.write("---")