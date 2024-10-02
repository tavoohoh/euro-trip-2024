import streamlit as st
import json

appTitle = "Itinerario Europa 2024"

st.set_page_config(
    page_title=appTitle,
    page_icon="https://tavoohoh.com/favicon.ico",
    layout="centered"
)

st.logo(
    "https://tavoohoh.com/favicon.ico",
    icon_image="https://tavoohoh.com/favicon.ico",
)

st.title(appTitle)

with open("itinerary_europe_2024.json", "r") as f:
    itinerary_json = json.load(f)

bg_colors = {
    "Mañana": "#E2B173",
    "Mediodía": "#D07272",
    "Tarde": "#769472",
    "Tardenoche": "#477A70",
    "Noche": "#434C63"
}

card_style = """
    <style>
    .card {
        border-radius: 16px;
        margin-bottom: 20px;
        color: white;
        display: flex;
        flex-direction: column;
        overflow: hidden;
    }
    @media(min-width: 768px) {
        .card {
            flex-direction: row;
        }
    }
    .card h2 {
        font-weight: bold;
        margin-bottom: 10px;
    }
    .card p {
        margin: 5px 0;
    }

    .card h2 {
        margin: 0;
        padding-top: 0;
    }

    .iframe-container {
        width: 100%;
        height: 300px;
    }
    @media(min-width: 768px) {
        .iframe-container {
            width: 50%;
            height: 300px;
        }
    }
    </style>
"""

st.markdown(card_style, unsafe_allow_html=True)

# Crear links con anchorpoints en el sidebar
st.sidebar.write("Días disponibles:")
for day in itinerary_json.keys():
    st.sidebar.markdown(f'<a href="#{day}">{day}</a>', unsafe_allow_html=True)

# Mostrar todas las actividades de todos los días
for day, schedule in itinerary_json.items():
    st.markdown(f'<h2 id="{day}">{day}</h2>', unsafe_allow_html=True)

    # Recorrer los momentos del día (mañana, mediodía, tarde, tardenoche, noche)
    for time_of_day, activities in schedule.items():
        st.subheader(f"{time_of_day.capitalize()}")

        bg_color = bg_colors.get(time_of_day, "#FFFFFF")

        # Mostrar una tarjeta por cada actividad
        for activity in activities:
            card_content = f'<div class="card" style="background-color: {bg_color};">'

            if 'Iframe' in activity and activity['Iframe']:
                card_content += f'<div class="iframe-container">'
                card_content += f'<iframe src="{activity["Iframe"]}" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'
                card_content += f'</div>'

            card_content += f'<div style="padding: 16px;">'
            
            if 'Subtitle' in activity and activity['Subtitle']:
                card_content += f'<b>{activity["Subtitle"]}</b>'

            card_content += f'<h2>{activity["Place"]} - {activity["City"]}</h2>'
            card_content += f'<p><strong>Dirección:</strong> {activity["Address"]}</p>'
            card_content += f'<p><strong>Notas:</strong> {activity["Notes"]}</p>'

            if activity['Link']:
                card_content += f'<p><a href="{activity["Link"]}" style="color:white;">Más información</a></p>'

            card_content += f'</div></div>'

            # Mostrar la tarjeta en la app
            st.markdown(card_content, unsafe_allow_html=True)