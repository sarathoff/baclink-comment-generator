import streamlit as st
import google.generativeai as gen_ai

# Configure Streamlit page settings
st.set_page_config(
    page_title="Backlink Comment Generator",
    page_icon=":link:",  # Favicon emoji
    layout="centered",  # Page layout option
)

# Directly set the API key here (not recommended for production)
GOOGLE_API_KEY = "AIzaSyCO7WIRmXTQUPeiARLTklKLufkZRfjfg4U"

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Streamlit app layout
st.title("Backlink Comment Generator")

# User inputs
blog_title = st.text_input("Enter the title of the blog where the comment will be posted")
blog_url = st.text_input("Enter the URL of the blog")
anchor_text = st.text_input("Enter your anchor text for the backlink")
your_website_url = st.text_input("Enter your website URL")

# Combine user inputs with the prompt for generating a backlink comment
if st.button("Generate Comment"):
    prompt = f"""
    Write a comment praising the blog titled '{blog_title}'. The comment should sound natural and relevant to the blog content. Include a backlink at the end of the comment using the anchor text '{anchor_text}' with the URL '{your_website_url}', encouraging readers to click and read more.
    """

    with st.spinner("Generating comment..."):
        # Generate comment using the Gemini-Pro model
        response = model.generate_content([prompt])
        generated_comment = response.text.strip()

        # Construct the anchor HTML tag
        anchor_html = f'<a href="{your_website_url}" target="_blank">{anchor_text}</a>'
        
        # Ensure the anchor tag is only at the end
        comment_with_backlink = f"{generated_comment} {anchor_html}."

    # Display the generated comment with the anchor tag
    st.subheader("Generated Comment with Backlink")
    st.write(comment_with_backlink)

    # Display HTML version of the comment
    st.subheader("HTML Code")
    st.code(f'<p>{comment_with_backlink}</p>', language='html')
