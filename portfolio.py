import streamlit as st

# Skills and Technologies for AI Engineer
ai_engineer_skills = {
    "🤖Artificial Intelligence": ["Machine Learning", "Deep Learning", "Natural Language Processing", "Computer Vision"],
    "💻Programming Languages": ["Python", "Core Java"],
    "📊Data Analysis": ["Pandas", "NumPy", "Matplotlib", "Seaborn", "Plotly"],
    "🗃️Database": ["MySQL"],
    "☁️Cloud Services": ["Amazon SageMaker", "Google Cloud AI", "Microsoft Azure AI"],
    "🐳Containers": ["Docker"],
    "🔄Version Control": ["Git"],
    "🌐Web Development": ["Streamlit"],
    "📚Frameworks and Libraries": ["TensorFlow", "Keras", "PyTorch", "OpenCV"]
}

# Set page configuration
st.set_page_config(page_title="My Portfolio", page_icon=":rocket:")

# Global variable to keep track of the active page
active_page = "About"

# About page
def about_page():
    st.title("Mangesh Shinde")
    st.write("**🌟 Welcome to my portfolio!**")
    st.write("**🚀 I'm Mangesh Shinde, a passionate AI enthusiast, seeking entry-level opportunities to launch my career in AI and gain experience. Here's a brief summary of who I am and what I do.**")

     #Display profile picture
    st.image("PROFILE IMAGE.jpg", width=200)
    st.header("📝Summary")
    st.write("**I'm a passionate AI Engineer with a strong enthusiasm for artificial intelligence and its potential to drive transformation. As a recent postgraduate, I'm eager to kickstart my AI career, combining my academic foundation and hands-on experience to contribute to groundbreaking projects**.")

    st.header("💡Skills")

    # Displaying Skills and Technologies for AI Engineer
    for category, items in ai_engineer_skills.items():
        st.subheader(category)
        for skill in items:
            st.write("- " + skill)

    st.header("💼Experience")
    st.markdown("**BUSINESS INTELLIGENCE DEVELOPER**  \n"
            "*ineuron.ai*  \n"
            "[12/03/2023 – 17/04/2023]  \n"
            "Location: Bangalore, India  \n"
            "Designing, implementing, and optimizing data models, creating insightful dashboards, and ensuring data accuracy for informed business decision-making as a BI Developer."
            )

    st.header("🎓Education")
    education_section()

def education_section():
    st.markdown("- **🎓 PGDAI**  \n"
                "*Centre for Development of Advanced Computing*  \n"
                "[2024]  \n"
                "Location: NOIDA, India  \n"
                )

    st.markdown("- **🎓 MCA**  \n"
                "*ASMA Institute of Management*  \n"
                "[2023]  \n"
                "Location: Pune, India  \n"
                )

    st.markdown("- **🎓 BSC**  \n"
                "*Yashwantrao Chavan Institute of Science,Satara*  \n"
                "[2021]  \n"
                "Location: Satara, India  \n"
                )

    st.markdown("- **🎓 XII**  \n"
                "*Jr.College Of Science, Commerce, Arts And Vocational, Rahimatpur*  \n"
                "[2016]  \n"
                "Location: Rahimatpur, India  \n"
                )

    st.markdown("- **🎓 X**  \n"
                "*Vasantdada Patil Vidyalaya, Rahimatpur*  \n"
                "[2014]  \n"
                "Location: Rahimatpur, India  \n"
                )
    st.header("🗣️ Language Skills")
    st.write("Mother tongue(s): Marathi")
    st.write("Other language(s): English | Hindi")

    st.header("📞Contact Information")
    st.write("You can reach me at [LinkedIn](https://www.linkedin.com/in/mangesh-shinde-667b32136/) 🌐.")
    # Add custom CSS for background color
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #ABF7EA;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Projects page
def projects_page():
    st.title("🛠️Projects")
    st.write("Check out some of my projects below:")

    # Project details
    projects = [
        {
            "name": "Image Background Remover",
            "dates": "[12/01/2024 - 5/02/2024]",
            "description": "The 'Image Background Remover' web app allows users to easily remove backgrounds from images, customize them with colors or other images, and download the edited versions. It offers a user-friendly interface with options to upload images, adjust settings, and personalize edits.",
            "website": "https://bgremover-shinde-2azhnr9agjg6bwrjs7lrnp.streamlit.app/",
            "link": "https://github.com/Mangesh1728/BGremover"   
        },
        {
            "name": "DeepVerify360: Guardian of Truth in Video Realms",
            "dates": "[01/01/2024 – 30/01/2024]",
            "description": "DeepVerify360 employs advanced AI and forensic analysis to authenticate video content, offering real-time monitoring and seamless integration to combat misinformation and uphold truth in digital realms.",
            "website": "https://deepverify360-guardian-of-truth-in-video-realms-fuzkrwrhwkgwgc.streamlit.app/",
            "link": "https://github.com/Mangesh1728/DeepVerify360-Guardian-of-Truth-in-Video-Realms.git"
        },
        {
            "name": "CAR PRICE PREDICTION",
            "dates": "[01/11/2023 – 30/12/2023]",
            "description": "Developed a Streamlit web app for car price prediction using machine learning. The app employs a trained model to forecast accurate car prices based on relevant features, enhancing user decision-making.",
            "website": "https://car-price-prediction-webapp-iznm55nthowaxwgdzvbeqq.streamlit.app/",
            "link": "https://github.com/Mangesh1728/car-price-prediction-app.git"
        },
        {
            "name": "Ten-Year CHD Risk Prediction",
            "description": "This Streamlit web app predicts Ten-Year CHD Risk using a Logistic Regression model, providing personalized risk assessments based on user input.",
            "website": "https://cardiovasculardiseaseprediction-2lv5guavdhj3ggrqeuzygz.streamlit.app/",
            "link": "https://github.com/Mangesh1728/Cardiovascular_Disease_Prediction"
        },
        {
            "name": "heart & diabetes disease prediction system",
            "description": "This Streamlit app predicts diabetes and heart disease using machine learning models, providing instant diagnostic results based on user-provided input. It offers an intuitive interface for easy navigation and data input.",
            "website": "https://heart-diabetes-disease-prediction-system-vlg8ktgrkxtqk8urhsxhx.streamlit.app/",
            "link": "https://github.com/Mangesh1728/Heart-Diabetes-Disease-Prediction-System"
        }
    ]
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #E3F17C;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display project details
    for project in projects:
        st.header(project["name"])
        st.markdown(project["dates"])
        st.write(project["description"])
        if "website" in project:
            st.markdown(f"🌐 [Website]({project['website']})")
        if "link" in project:
            st.markdown(f"🔗 [GitHub]({project['link']})")



# Contact page
def contact_page():
    st.title("📳Contact")
    st.write("**Feel free to reach out to me!**")

    # Contact form with validation

    # Social media links
    st.header("🔗Social Media")
    st.markdown("**[LinkedIn](https://www.linkedin.com/in/mangesh-shinde-667b32136/) 🌐**")
    st.markdown("**[GitHub](https://github.com/Mangesh1728) 🐙**")
    st.markdown("**[Email](mailto:mangeshsshinde2016@gmail.com) 📧**")
    
    # Phone number
    st.header("📞Phone")
    st.write("**+91 8830582812**")
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #F5B7B1;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Main function
def main():
    global active_page

    # Horizontal strip for page links
    col1, col2, col3 = st.columns(3)
    if col1.button("About Me"):
        active_page = "About"
    if col2.button("Projects"):
        active_page = "Projects"
    if col3.button("Contact"):
        active_page = "Contact"

    # Display active page content
    if active_page == "About":
        about_page()
    elif active_page == "Projects":
        projects_page()
    elif active_page == "Contact":
        contact_page()

if __name__ == "__main__":
    main()
