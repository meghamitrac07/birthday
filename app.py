import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Happy Birthday ❤️",
    layout="centered"
)

st.markdown(
    """
    <style>

    .stApp {
        background-color: #ffe6ee;
    }

    h1 {
        color: #d63384 !important;
        text-align: center;
        font-size: 60px !important;
        font-weight: bold;
    }

    h2, h3 {
        color: #c2185b !important;
        text-align: center;
    }

    p {
        color: #444444;
        font-size: 20px;
        text-align: center;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.title("Happy Birthday My Love ❤️")

st.markdown("""
<div style='text-align:center; font-size:24px; color:#555;'>
This is for you ❤️
</div>
""", unsafe_allow_html=True)
from PIL import Image
import streamlit as st
    
audio_file = open("songs/amar_mote.mp3", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mp3")
st.markdown("""
<div style='text-align:center; color:#666; font-size:18px;'>
This song will always remind me of you ❤️
</div>
""", unsafe_allow_html=True)
st.write("")
st.divider()

# FUNCTION TO RESIZE ALL IMAGES SAME SIZE
def resize_image(image_path):
    img = Image.open(image_path)
    img = img.resize((300, 400))
    return img


# FIRST ROW
col1, col2 = st.columns(2)

with col1:
    img1 = resize_image("him/littlekorak3.jpeg")
    st.image(img1)
    st.caption("Tui choto theke super Cute ❤️")

with col2:
    img2 = resize_image("him/littlekorak2.jpeg")
    st.image(img2)
    st.caption("Toke choto teh pele chotke kheye feltam ❤️")


st.write("")


# SECOND ROW
col3, col4 = st.columns(2)

with col3:
    img3 = resize_image("him/angrykorak.jpeg")
    st.image(img3)
    st.caption("Raag korle o toke super cute lage ❤️")

with col4:
    img4 = resize_image("him/sleepningkorak.jpeg")
    st.image(img4)
    st.caption("Remember this pic I clicked in 1st year hehe ❤️")


st.write("")


# THIRD ROW
col5, col6 = st.columns(2)

with col5:
    img5 = resize_image("him/myfavpickorak.jpeg")
    st.image(img5)
    st.caption("This is my Fav Pic ❤️")

with col6:
    img6 = resize_image("him/thisismyfav.jpeg")
    st.image(img6)
    st.caption("This new look is so good ❤️")


st.write("")


# FOURTH ROW
col7, col8 = st.columns(2)

with col7:
    img7 = resize_image("him/handsomekorak.jpeg")
    st.image(img7)
    st.caption("You look like a Hero ❤️")

with col8:
    img8 = resize_image("him/cutekorak.jpeg")
    st.image(img8)
    st.caption("This is always my fav cutie pic ❤️")


# LAST PHOTO CENTERED

left, center, right = st.columns([1,2,1])

with center:
    img9 = resize_image("him/superhandsome.jpeg")

    st.image(img9, width=350)

    st.markdown(
        """
        <div style='text-align:center; font-size:18px; color:#666;'>
        I get dreams about this photo ❤️
        </div>
        """,
        unsafe_allow_html=True
    )
st.write("")
st.divider()
st.write("")
st.header("Something I Need To Tell You ❤️")
st.markdown(
    """
    <div style='
        font-size:22px;
        color:#444;
        line-height:2;
        text-align:center;
        padding:20px;
    '>

    Happy Birthday Baby.Ik amader onek jhogra hoye shob problems hoye but i laways want the best things for you.Tui jeno life e onek boro hosh
    and shob achieve korish.May this 21st Birthday get you everything you ever wished for.Tor sathe its been 3 years since i have known you,
    tao everyday i learn something new about you. I love you very much.I will spend my life trying to be better and taking care of you.

    I love us ❤️

    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style='
        text-align:center;
        font-size:20px;
        color:#d63384;
        margin-top:20px;
        margin-bottom:30px;
    '>

    And now… our favorite memories ❤️

    </div>
    """,
    unsafe_allow_html=True
)
st.header("Our Memories Together ❤️")
col1, col2 = st.columns(2)

with col1:
    us1 = resize_image("us/firstpic.jpeg")
    st.image(us1)
    st.caption("Our first pic together ❤️")

with col2:
    us2 = resize_image("us/cuties.jpeg")
    st.image(us2)
    st.caption("Every moment with you feels special ❤️")
st.write("")

col3, col4 = st.columns(2)

with col3:
    us3 = resize_image("us/holdmelikethis.jpeg")
    st.image(us3)
    st.caption("Us against the world ❤️")

with col4:
    us4 = resize_image("us/ethnic.jpeg")
    st.image(us4)
    st.caption("I wish time stopped here ❤️")
col5, col6 = st.columns(2)

with col5:
    us3 = resize_image("us/Varansi.jpeg")
    st.image(us3)
    st.caption("Koto shundor time spend korechilam")

with col6:
    us4 = resize_image("us/drajeeling.jpeg")
    st.image(us4)
    st.caption("Together in Daejeeling as well")
col7, col8 = st.columns(2)

with col7:
    us3 = resize_image("us/ssexy.jpeg")
    st.image(us3)
    st.caption("So Sexyyy")

with col8:
    us4 = resize_image("us/hot.jpeg")
    st.image(us4)
    st.caption("We are soo Hot")
col9, col10 = st.columns(2)

with col9:
    us3 = resize_image("us/kissme.jpeg")
    st.image(us3)
    st.caption("Love when you kiss me")

with col10:
    us4 = resize_image("us/kissyou.jpeg")
    st.image(us4)
    st.caption("I love kissing you")




st.header("Little Things I Want To Tell You ❤️")
if st.button("Click Me ❤️"):
    st.success("You are my favorite person in the world.")
if st.button("One Secret 🤭"):
    st.write("I love making out with you and you give me the best experiences")
if st.button("Press This"):
    st.balloons()
    st.write("Happy Birthday Baby ❤️")
st.write("")
st.header("Something From My Heart ❤️")
if st.button("Open This Only If You Love Me ❤️"):
    st.markdown("""
    <div style='
        font-size:22px;
        color:#444;
        line-height:2;
        text-align:center;
        padding:20px;
    '>

    I know I make mistakes sometimes.

    I know I can be difficult.

    But loving you has always been the easiest thing for me.

    Thank you for staying,
    understanding me,
    and choosing me every day.

    I am really sorry for every time I hurt you.

    I love you endlessly ❤️

    </div>
    """, unsafe_allow_html=True)
st.write("")
st.divider()
st.header("One Last Thing ❤️")
st.markdown("""
<div style='
    text-align:center;
    font-size:24px;
    color:#444;
    line-height:2.2;
    padding:30px;
'>

No matter where life takes us,
I will always be with you.

Thank you for being my person.

Happy Birthday My Love ❤️

</div>
""", unsafe_allow_html=True)
    