import streamlit as st
from scripts.json_reader import reader
from streamlit_js_eval import streamlit_js_eval

__all__ = ['LiveRadio']


class Radio:
    __json_file_path = 'resources/radio.json'

    @classmethod
    def get_radio_stations(cls) -> dict:
        """ Returns a dict in radio_name:radio_stream_url format"""
        stations = reader(cls.__json_file_path)
        return stations

    @classmethod
    def get_app_widgets(cls):
        """ Returns Streamlit Widgets """
        page_title = st.title('Online Radio')
        reload_button = st.button('Reload')
        radio_stations = reader(json_filepath='resources/radio.json')
        return page_title, reload_button, radio_stations

    @classmethod
    def refresh_website(cls):
        """ Reloads the browser page (Not the app); Purpose: to update the live-streams """
        streamlit_js_eval(js_expressions="parent.window.location.reload()")

    def __init__(self):
        self.radio_stations = self.get_radio_stations()

    def display_radio_stations(self):
        """ Iterates over the radio stations, displays the name as a text, and inserts the url into audioplayer. """
        tries_count = 0

        for radio_name, radio_url in self.radio_stations.items():
            try:
                st.title(radio_name)
                st.audio(radio_url)
                st.divider()

            except Exception:
                while tries_count < 2:
                    try:
                        st.title(radio_name)
                        st.audio(radio_url)
                        st.divider()
                        # setting the counter to 0 and breaking the loop
                        tries_count = 0
                        break  # Rule1 of while-loops: always use brakes. Especially the redundant ones.
                    except Exception:
                        tries_count += 1

                tries_count = 0


class LiveRadio(Radio):
    def start_radio(self):
        """ main function """
        # initializing the widgets
        page_title, reload_button, radio_stations = self.get_app_widgets()
        st.divider()
        # running the radio stations
        self.display_radio_stations()
        if reload_button:
            # reloading the page
            self.refresh_website()


if __name__ == '__main__':
    radio = LiveRadio()
    radio.start_radio()
