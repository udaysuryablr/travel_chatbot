import streamlit as st

# Define a list of predefined travel destinations with their attributes
DESTINATIONS = {
    "Paris": {
        "attraction": "Cultural",
        "budget": "Moderate",
        "weather": "Mild",
        "description": "Paris is the capital city of France, known for its iconic landmarks such as the Eiffel Tower and Louvre Museum.",
        "image_url": "https://media.istockphoto.com/id/1345426734/photo/eiffel-tower-paris-river-seine-sunset-twilight-france.jpg?s=612x612&w=0&k=20&c=I5rAH5d_-Yyag8F0CKzk9vzMr_1rgkAASGTE11YMh9A="
    },
    "Tokyo": {
        "attraction": "Entertainment",
        "budget": "Moderate",
        "weather": "Mild",
        "description": "Tokyo is the capital city of Japan, famous for its vibrant neighborhoods, delicious cuisine, and rich culture.",
        "image_url": "https://cdn.britannica.com/09/193909-050-5804497B/photo-Tokyo-distance-right-Sky-Tree-image.jpg"
    },
    "New York": {
        "attraction": "Entertainment",
        "budget": "High",
        "weather": "Mild",
        "description": "New York City is the most populous city in the United States, known for its iconic landmarks, Broadway theaters, and diverse culture.",
        "image_url": "https://t3.ftcdn.net/jpg/02/09/70/56/360_F_209705645_b78HGJI1i1mxqLwMYA7z1m3VvCxgxJFO.jpg"
    },
    "Rome": {
        "attraction": "Historical",
        "budget": "Moderate",
        "weather": "Mild",
        "description": "Rome is the capital city of Italy, famous for its ancient ruins such as the Colosseum and the Roman Forum.",
        "image_url": "https://thumbs.dreamstime.com/b/rome-italy-colosseum-coliseum-sunrise-144201572.jpg"
    },
    "Barcelona": {
        "attraction": "Cultural",
        "budget": "Moderate",
        "weather": "Mild",
        "description": "Barcelona is the capital city of the Catalonia region in Spain, known for its unique architecture, vibrant street life, and beautiful beaches.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/dd/Barcelona_skyline.jpg"
    },
    "London": {
        "attraction": "Cultural",
        "budget": "Moderate",
        "weather": "Mild",
        "description": "London is the capital city of England, known for its rich history, iconic landmarks such as the Big Ben and Buckingham Palace, and cultural diversity.",
        "image_url": "https://images.pexels.com/photos/427679/pexels-photo-427679.jpeg?cs=srgb&dl=pexels-chris-schippers-139261-427679.jpg&fm=jpg"
    },
    "Sydney": {
        "attraction": "Natural",
        "budget": "High",
        "weather": "Sunny",
        "description": "Sydney is the largest city in Australia, famous for its Sydney Opera House, Harbour Bridge, and beautiful beaches.",
        "image_url": "data:image/jpeg;base64,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"
    },
    "Dubai": {
        "attraction": "Entertainment",
        "budget": "High",
        "weather": "Sunny",
        "description": "Dubai is a city in the United Arab Emirates, known for luxury shopping, ultramodern architecture, and a lively nightlife scene.",
        "image_url": "https://cdn.britannica.com/15/189715-050-4310222B/Dubai-United-Arab-Emirates-Burj-Khalifa-top.jpg"
    },
    "Bangkok": {
        "attraction": "Cultural",
        "budget": "Low",
        "weather": "Sunny",
        "description": "Bangkok is the capital city of Thailand, known for its ornate shrines, vibrant street life, and cultural landmarks.",
        "image_url": "https://content.r9cdn.net/rimg/dimg/86/2e/2d3ef5c0-city-26166-153e6c3d8ab.jpg?crop=true&width=1020&height=498"
    },
    "Cape Town": {
        "attraction": "Natural",
        "budget": "Moderate",
        "weather": "Mild",
        "description": "Cape Town is a port city on South Africa’s southwest coast, known for its stunning landscapes, including Table Mountain and beautiful beaches.",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3sWO5iWTvxSkjuFZ0kKxssRZbaXOReJZwAg&s"
    },
    "Rio de Janeiro": {
        "attraction": "Natural",
        "budget": "Moderate",
        "weather": "Sunny",
        "description": "Rio de Janeiro is a huge seaside city in Brazil, famed for its Copacabana and Ipanema beaches, the Christ the Redeemer statue, and Sugarloaf Mountain.",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLVKhtF3WT2iK5JMqzc7788QhUa0Wo8JAH0A&s"
    },
    "Istanbul": {
        "attraction": "Cultural",
        "budget": "Low",
        "weather": "Mild",
        "description": "Istanbul is a major city in Turkey that straddles Europe and Asia across the Bosphorus Strait, known for its historic sites and vibrant culture.",
        "image_url": "https://cdn.britannica.com/58/93158-050-7719EB2B/view-Blue-Mosque-Istanbul-Hagia-Sophia.jpg"
    },
    "Seattle": {
        "attraction": "Natural",
        "budget": "Moderate",
        "weather": "Rainy",
        "description": "Seattle is a major city in the state of Washington, known for its coffee culture, the iconic Space Needle, and its frequent rainy weather.",
        "image_url": "https://uploads.visitseattle.org/2023/01/11122537/Banner_rachael-jones-media_aerial-destination-photos-24_3.jpg"
    },
    "London": {
        "attraction": "Historical",
        "budget": "High",
        "weather": "Rainy",
        "description": "London, the capital of the United Kingdom, is famous for its rich history, the British Museum, Buckingham Palace, and its frequent drizzly weather.",
        "image_url": "https://images.pexels.com/photos/427679/pexels-photo-427679.jpeg?cs=srgb&dl=pexels-chris-schippers-139261-427679.jpg&fm=jpg"
    },
    "Dublin": {
        "attraction": "Cultural",
        "budget": "Moderate",
        "weather": "Rainy",
        "description": "Dublin, the capital of Ireland, is known for its vibrant culture, historic landmarks, and its frequent rainy days.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/42/Samuel_Beckett_Bridge_At_Sunset_Dublin_Ireland_%2897037639%29_%28cropped%29.jpeg"
    },
    "Vancouver": {
        "attraction": "Natural",
        "budget": "High",
        "weather": "Rainy",
        "description": "Vancouver, located in British Columbia, Canada, is known for its beautiful natural landscapes, vibrant city life, and rainy weather.",
        "image_url": "https://res.cloudinary.com/simpleview/image/upload/v1589990523/clients/vancouverbc/Vancouver_Aerial_2017_1__72115131-4a31-42dc-b369-7a5ccec8273f.jpg"
    }
}

    # Add more destinations here...


def get_destination_recommendation(preferences):
    # Filter destinations based on user preferences
    filtered_destinations = [destination for destination, attrs in DESTINATIONS.items() if all(attrs[attr] == preferences[attr] for attr in preferences)]

    # If no matching destinations found, return a default destination
    if not filtered_destinations:
        return "default_destination"

    # Return the first matching destination
    return filtered_destinations[0]

def main():
    st.title("Travel Destination Chatbot")

    st.write("Welcome to the Travel Destination Chatbot! Please answer a few questions to get started.")

    # Get user preferences
    attraction = st.radio("What type of attractions do you prefer?", ["Historical", "Natural", "Cultural", "Entertainment"])
    budget = st.slider("What is your budget?", min_value=0, max_value=10000, step=100, value=500)
    weather = st.selectbox("What type of weather do you prefer?", ["Sunny", "Mild", "Cold", "Rainy"])

    preferences = {
        "attraction": attraction,
        "budget": "Moderate" if budget > 3000 else "Low",  # Adjust budget levels based on threshold
        "weather": weather
    }

    # Recommend a destination based on user preferences
    destination = get_destination_recommendation(preferences)

    # Display destination information
    if destination == "default_destination":
        st.write("Sorry, we couldn't find a destination matching your preferences. Please try again.")
    else:
        st.write(f"Based on your preferences, I recommend visiting {destination}.")
        st.image(DESTINATIONS[destination]["image_url"], caption=destination, use_column_width=True)
        st.write(DESTINATIONS[destination]["description"])

if __name__ == "__main__":
    main()


