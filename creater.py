import streamlit as st

def medibot():
    st.title("Creator")
    st.image("myphoto.jpg", width=200)
    st.markdown("<h2 style='text-align: Left;'>Prashansa Pandey</h2>", unsafe_allow_html=True)

    st.write(
        "Hello everyone! I'm Prashansa Pandey, a 2nd-year Computer Science and Engineering student pursuing my "
        "bachelor's degree from IPS College of Technology and Management. My main interest lies in cybersecurity, "
        "but fate somehow led me to the field of AI/ML, where I never thought I'd venture. However, this unexpected "
        "turn brought about my first significant achievement—winning the AWS AI/ML Scholarship! I was ranked among "
        "the top 1000 students globally, receiving a prize of 3000 USD. "
    )

    st.write(
        "I've worked on a few projects that you can check out on my GitHub repository:"
        " [https://github.com/prashansapandey2005](https://github.com/prashansapandey2005). Here are some of them:"
    )
    st.markdown(
        """
        * Pre-trained-Image-Classifier-To-Identify-Dog-Breeds
        * Flower-Detection-Image-Classifier
        * BeautyBill
        """
    )

    st.write(
        "This MediBot AI project was a unique challenge, quite different from my other projects. It certainly "
        "put my skills to the test! But here it is, my one and only creation—MediBot AI, ready to assist you "
        "with medical information. 😊 "
    )

    st.write("You can also connect with me on LinkedIn: [https://www.linkedin.com/in/prashansa-pandey/](https://www.linkedin.com/in/prashansa-pandey/)")