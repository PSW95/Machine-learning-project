import streamlit as st
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from PIL import Image

# Set page config with a title and a custom icon
st.set_page_config(page_title="Sentiment Analyzer", page_icon="😊", layout="wide")

def main():
    # Load an image (optional: use a nice banner or logo)
    img = Image.open('banners1.jfif')  # Add a custom banner image
    st.image(img, use_column_width=True)

    # Title and subtitle with some color and style
    st.title("💬 Sentiment Analyzer")
    st.markdown("<h3 style='text-align: center; color: #FF6347;'>Analyze Text Emotions Easily</h3>", unsafe_allow_html=True)

    # Sidebar menu with different options
    menu = ['🏠 Home', '📄 About']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == "🏠 Home":
        st.subheader("Welcome! Get started by entering text below.")
        st.markdown("<hr style='border:1px solid #FF6347;'>", unsafe_allow_html=True)  # Add a stylish horizontal line
        
        # Form to input text
        with st.form(key='nlpForm'):
            raw = st.text_area("📝 Enter the text here", height=200, placeholder="Type something meaningful...")
            submit = st.form_submit_button(label='🔍 Analyze')

        # Split page layout into two columns for results and details
        col1, col2 = st.columns(2)

        if submit:
            with col1:
                # Display TextBlob sentiment results
                st.info("Results using TextBlob")
                sentiment = TextBlob(raw).sentiment
                st.write(f"**Polarity:** {sentiment.polarity}")
                st.write(f"**Subjectivity:** {sentiment.subjectivity}")

                # Sentiment results based on polarity score
                if sentiment.polarity > 0.4:
                    st.markdown("### Sentiment: Positive 😊")
                elif sentiment.polarity < -0.05:
                    st.markdown("### Sentiment: Negative 😠")
                else:
                    st.markdown("### Sentiment: Neutral 😐")

            with col2:
                # Optionally, add Vader sentiment analyzer here
                st.info("Token Sentiment (VADER)")
                analyzer = SentimentIntensityAnalyzer()
                sentiment_dict = analyzer.polarity_scores(raw)
                st.write(f"**Compound:** {sentiment_dict['compound']}")
                st.write(f"**Positive:** {sentiment_dict['pos']}")
                st.write(f"**Negative:** {sentiment_dict['neg']}")
                st.write(f"**Neutral:** {sentiment_dict['neu']}")

                # Show Vader sentiment based on compound score
                if sentiment_dict['compound'] >= 0.05:
                    st.markdown("### Sentiment: Positive 😊")
                elif sentiment_dict['compound'] <= -0.05:
                    st.markdown("### Sentiment: Negative 😠")
                else:
                    st.markdown("### Sentiment: Neutral 😐")

    else:
        # About page
        st.subheader("About the Sentiment Analyzer App")
        st.markdown("""
        <p style="text-align: justify;">
        This app uses two popular libraries, <b>TextBlob</b> and <b>VADER</b>, to analyze the sentiment of any text you provide.
        Whether you want to check if your content is positive, neutral, or negative, this tool can help you in real-time.
        <br><br>
        Made with 💙 by Pranav.
        </p>
        """, unsafe_allow_html=True)

# Footer section (optional)
def footer():
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("""
    <p style='text-align: center; color: grey;'>Built with Streamlit | © 2024</p>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
    footer()
