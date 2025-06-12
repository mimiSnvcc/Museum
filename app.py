import streamlit as st
import requests

def search_artworks(query):
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/search"
    params = {"q": query}
    response = requests.get(url, params=params)
    return response.json().get("objectIDs", [])[:10]  # 상위 10개만

def get_artwork_details(object_id):
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"
    return requests.get(url).json()

st.title("🎨 Explore Artworks with MET Museum API")

query = st.text_input("Search for Artworks:")

if query:
    ids = search_artworks(query)
    if not ids:
        st.write("No artworks found.")
    else:
        for object_id in ids:
            data = get_artwork_details(object_id)
            st.subheader(data.get("title", "Untitled"))
            if data.get("primaryImageSmall"):
                st.image(data.get("primaryImageSmall"), width=300)
            st.write(f"Artist: {data.get('artistDisplayName', 'Unknown')}")
            st.write(f"Year: {data.get('objectDate', 'Unknown')}")
            st.write("---")
