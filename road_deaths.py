import streamlit as st
import streamlit.components.v1 as components
import hydralit_components as hc
from streamlit_lottie import st_lottie
import json

st.set_page_config(layout='wide', initial_sidebar_state='collapsed', page_title='Road Deaths')

#defining lottie function to visualize animated pictures
def load_lottiefile(filepath):
    with open(filepath) as f:
        return json.load(f)

menu_data = [
    {'label': "Road Deaths Dashboard", 'icon': '⚰️'},
    {'label': "Seat Belt Use", 'icon': '⛐'}, 
    {'label': "Helmet Use", 'icon': '⛑️'},
    {'label': "Awareness", 'icon': '💌'}
    ]

over_theme = {'txc_inactive': 'white','menu_background':'rgb(0,0,300)', 'option_active':'white'}

menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    hide_streamlit_markers=False,
    sticky_nav=False, #at the top or not
    sticky_mode='sticky', #jumpy or not-jumpy, but sticky or pinned
)

if menu_id == 'Road Deaths Dashboard':
    
    coll1, coll2, coll3 = st.columns([1,10,1])

    with coll2:
        def main():

            html_temp = """
        <div class='tableauPlaceholder' id='viz1657054690820' style='position: relative'><noscript><a href='#'><img alt='Roads_to_death ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ro&#47;roaddeaths_16570546534920&#47;Roads_to_death&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='roaddeaths_16570546534920&#47;Roads_to_death' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ro&#47;roaddeaths_16570546534920&#47;Roads_to_death&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-GB' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1657054690820');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='800px';vizElement.style.height='627px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        
            st.components.v1.html(html_temp, width=1100, height=800, scrolling = False)
    
        if __name__ == "__main__":
            main()


if menu_id == 'Awareness':

    st.markdown("<h2 style='text-align: center; color: blue;'>Road Death Rates in Lebanon</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: red;'>At Least One Person Dies Per Day</h1>", unsafe_allow_html=True)

    coll1,coll2,coll3 = st.columns(3)
    with coll1:
        
        lottie_acc= load_lottiefile("accidnet.json")
        st_lottie(lottie_acc, width=200)
    
    with coll2:
        lottie_injury= load_lottiefile("injury.json")
        st_lottie(lottie_injury, height=150, width=200)
    
    with coll3:
        lottie_death= load_lottiefile("death.json")
        st_lottie(lottie_death, height=150, width=200)


    col1,col2,col3 = st.columns(3)
    col1.metric("Avg. Number of Accidents", "346")
    col2.metric("Avg. Number of Injuries", "456")
    col3.metric("Avg. Number of Fatalities", "37")

    st.write("""The high numbers of death rates are associated with several factors:
1. Lack of funding for safer strategies
2. Low seat belt wearing rates
3. Not abiding with helmet laws
4. Disregarding the Blood Alcohol Concentration (BAC) limits
5. In-effectiveness of drink-driving penalties""")
    
    st.write("""Average road death rate is 12% higher in countries where penalties
are not applied.
Lebanon's Driving Law 243/2012 imposes two penalties:

1️fines - vary based on the driver's measured BAC

2️penalty points - deducted from a driver's license balance

However, the number of penalties imposed does not affect road death rates.
What's more important is the type of penalties selected by a country.""")

    
if menu_id == 'Seat Belt Use':    
    st.image("screenshot.png")

if menu_id == 'Helmet Use':    
    st.image("screenshot2.png")



