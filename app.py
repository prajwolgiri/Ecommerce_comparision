import streamlit as st
from PIL import Image

import ecommerce_working_app
import Conversion

headers1 = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}

# st.title('I am a Helper')
st.title('Grab the best :blue[OFFER] :sunglasses:')
st.subheader('Click on :blue[SIDE BAR] :point_left: :wink:')
# st.markdown("<h1 style='text-align : center;'> :blue[Grab The Best Offer]</h>", unsafe_allow_html=True)
# st.markdown("<h1 style='text-align : center;'> <<< </h>", unsafe_allow_html=True)
image = Image.open('dealguru.jpg')
st.text("")

l1 = {}




# amazon_price_app, amazon_url_app, flipkart_price_app, flipkart_url_app = None
with st.sidebar:
    st.markdown("<h1 style='text-align : center;'> Search Fast!!</h>", unsafe_allow_html=True)

    with st.form("Search"):
        keyword = st.text_input("Enter The Item")
        search1 = st.form_submit_button("Search ")
        st.image(image, caption='Get The Best Deal')


if search1:
    if l1:
        l1 = {}
    amazon_price_app, amazon_url_app = ecommerce_working_app.amazon(keyword, headers1)
    l1["amazon_price_app"] = amazon_price_app
    l1["amazon_url_app"] = amazon_url_app

    flipkart_price_app, flipkart_url_app = ecommerce_working_app.flipkart(keyword, headers1)

    l1["flipkart_price_app"] = flipkart_price_app
    l1["flipkart_url_app"] = flipkart_url_app

    # if flipkart_price_app == '0':
    #     b = ("Flipkart: No product found!")
    #     flipkart_price_app = int(flipkart_price_app)
    #
    # else:
    #     print("\nFlipkart Price:", flipkart_price_app)
    #     flipkart_price_app = Conversion.convert(flipkart_price_app)
    # if amazon_price_app == '0':
    #     c = ("Amazon: No product found!")
    #     amazon_price_app = int(amazon_price_app)
    # else:
    #     print("\nAmazon price: ₹", amazon_price_app)
    #     amazon_price_app = Conversion.convert(amazon_price_app)

    col1, col2 = st.columns(2)
    with col1:
        st.header("Price in amazon")
        # st.title(c)
        st.title(amazon_price_app)

    with col2:
        st.header("Price in flipkart")
        # st.title(b)
        st.title(flipkart_price_app)

    min_price = min(amazon_price_app, flipkart_price_app)
    st.header(f"Minimum Price is : {min_price}")

    # st.subheader(min_price)
    st.header("URL")
    if amazon_price_app > flipkart_price_app:
        st.subheader(flipkart_url_app)
    elif flipkart_price_app > amazon_price_app:
        st.subheader(amazon_url_app)
    else:
        st.subheader(':point_left:')



# with st.sidebar:
#     with st.form("Show Links and analysis"):
#         search2 = st.form_submit_button(" Links And Analysis ")

# if search2:
#     print(l1)
#     if not l1:
#         st.subheader("Not available at the moment")
#     else:
#     amazon_price_app, amazon_url_app = ecommerce_working_app.amazon(keyword, headers1)
#     flipkart_price_app, flipkart_url_app = ecommerce_working_app.flipkart(keyword, headers1)
    st.subheader('URLS Of the products:')

    st.subheader("Amazon Link")
    st.subheader(l1["amazon_url_app"])

    st.subheader("Flipkart Link")
    st.subheader(l1["flipkart_url_app"])


# with st.sidebar:
#     with st.form("Email tracker"):
#
#         keyword = st.text_input("Enter Email")
#         search2 = st.form_submit_button(" EmailTracker ")






















