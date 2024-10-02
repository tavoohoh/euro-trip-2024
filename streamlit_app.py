import streamlit as st
import json

st.title("Itinerario Europa 2024")

with open("itinerary_europe_2024.json", "r") as f:
    itinerary_json = json.load(f)

selected_day = st.sidebar.selectbox("Selecciona el día", list(itinerary_json.keys()))

if selected_day:
    st.header(f"Actividades del día {selected_day}")

    for time_of_day, activities in itinerary_json[selected_day].items():
        st.subheader(f"{time_of_day.capitalize()}")

        # Mostrar una tarjeta por cada actividad
        for activity in activities:
            st.write(f"### {activity['Lugar a visitar']}")
            st.write(f"**Ciudad:** {activity['Ciudad']}")
            st.write(f"**Dirección:** {activity['Dirección']}")
            st.write(f"**Notas:** {activity['Notas']}")
            if activity['Link']:
                st.write(f"[Más información]({activity['Link']})")
            st.write("---")
