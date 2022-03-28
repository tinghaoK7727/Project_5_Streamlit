mkdir -p ~/.streamlit/
echo "\
[theme]\n\
base='dark'\n\
primaryColor='#3285a8'\n\
background='#839C9C'\n\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml