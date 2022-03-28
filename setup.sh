mkdir -p ~/.streamlit/
echo "\
[theme]\n\
primaryColor = '#3285a8'\n\
backgroundColor = '#fafafa'\n\
secondaryBackgroundColor = '#EFEDE8'\n\
textColor= '#424242'\n\
font = 'sans serif'\n\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml