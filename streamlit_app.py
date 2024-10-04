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
        color: white;
        display: grid;
        grid-template-rows: auto 1fr auto;
        overflow: hidden;
        max-width: 480px;
        margin: 0 auto 24px;
        padding-bottom: 16px;
    }

    .card * {
        color: #fafafa!important;
    }

    .card-header {
        display: grid;
        grid-template-columns: min-content 1fr;
        gap: 16px;
        padding: 16px;
    }

    .card-content {
        padding: 0 16px;
    }

    .card-emoji {
        font-size: 36px;
    }

    .card h2 {
        font-weight: bold;
        margin: 0;
        padding: 0;
    }

    .card h4 {
        font-weight: bold;
        margin: 0;
        padding: 0;
    }

    .card p {
        margin: 5px 0;
    }

    .iframe-container {
        width: 100%;
        height: 300px;
    }
    </style>
"""

st.markdown(card_style, unsafe_allow_html=True)

st.sidebar.write("Días disponibles:")
for day in itinerary_json.keys():
    st.sidebar.markdown(f'<a href="#{day}">{day}</a>', unsafe_allow_html=True)

for day, schedule in itinerary_json.items():
    st.markdown(f'<h2 id="{day}">{day}</h2>', unsafe_allow_html=True)

    for time_of_day, activities in schedule.items():
        st.subheader(f"{time_of_day.capitalize()}")

        bg_color = bg_colors.get(time_of_day, "#FFFFFF")

        for activity in activities:
            card_content = f'<div class="card" style="background: {bg_color};">'

            if 'Iframe' in activity and activity['Iframe']:
                card_content += f'<div class="iframe-container">'
                card_content += f'<iframe src="{activity["Iframe"]}" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'
                card_content += f'</div>'

            card_content += f'<div class="card-header">'

            if 'Emoji' in activity and activity['Emoji']:
                card_content += f'<div class="card-emoji">{activity["Emoji"]}</div>'


            card_content += f'<div>'

            if 'City' in activity and activity['City']:
                card_content += f'<h4>{activity["City"]}</h4>'
            
            if 'Title' in activity and activity['Title']:
                card_content += f'<h2>{activity["Title"]}</h2>'
            
            if 'Subtitle' in activity and activity['Subtitle']:
                card_content += f'<b>{activity["Subtitle"]}</b>'

            card_content += f'</div>'
            card_content += f'</div>'

            card_content += f'<div class="card-content">'

            if 'Notes' in activity and activity['Notes']:
                card_content += f'<p>{activity["Notes"]}</p>'

            if 'Booking' in activity and activity['Booking']:
                card_content += f'<p><strong>Reserva:</strong> <a href="{activity["Booking"]}" style="color:white;">{activity["Booking_Number"]}</a></p>'

            if 'GoogleMaps' in activity and activity['GoogleMaps']:
                card_content += f'<p><strong>Google Maps:</strong> <a href="{activity["GoogleMaps"]}" style="color:white;">{activity["Address"]}</a></p>'

            if 'Link' in activity and activity['Link']:
                card_content += f'<p><a href="{activity["Link"]}" style="color:white;">Más información</a></p>'

            card_content += f'</div></div>'

            # Mostrar la tarjeta en la app
            st.markdown(card_content, unsafe_allow_html=True)