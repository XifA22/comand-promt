import streamlit as st
from streamlit_option_menu import option_menu

# Page configuration
st.set_page_config(page_title="Visualisasi Data", page_icon=":bar_chart:")

# Logo and title
st.sidebar.image("logo.png", use_column_width=True)  # Add your logo image
st.title("Visualisasi Data")

# Navigation buttons
with st.sidebar:
    selection = option_menu(
        menu_title=None,
        options=["Diagram Lingkaran", "Diagram Batang", "Diagram Garis"],
        icons=["pie-chart", "bar-chart", "line-chart"],
        menu_icon="cast",
        default_index=0
    )

# Page selection
if selection == "Diagram Lingkaran":
    import diagram_lingkaran
    diagram_lingkaran.run()
elif selection == "Diagram Batang":
    import diagram_batang
    diagram_batang.run()
elif selection == "Diagram Garis":
    import diagram_garis
    diagram_garis.run()
