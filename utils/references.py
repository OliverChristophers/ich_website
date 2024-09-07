import streamlit as st
import bibtexparser
import os

def references():   
    current_dir = os.path.dirname(os.path.abspath(__name__))
    with open(os.path.join(current_dir, 'references.bib'), 'r') as bib_file:
        bib_database = bibtexparser.load(bib_file)
    st.title("Bibliography")

    sorted_entries = sorted(bib_database.entries, key=lambda x: x.get('author', ''))
    for entry in sorted_entries:
        st.subheader(entry.get('title', ''))
        st.write(f"**Author(s):** {entry.get('author', '')}")
        st.write(f"**Journal:** {entry.get('journal', '')}")
        st.write(f"**Volume:** {entry.get('volume', '')}, **Number:** {entry.get('number', '')}, **Pages:** {entry.get('pages', '')}")
        st.write(f"**Year:** {entry.get('year', '')}")
        st.write(f"**Publisher:** {entry.get('publisher', '')}")
        st.write("---")