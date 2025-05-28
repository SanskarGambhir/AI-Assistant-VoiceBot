import google.generativeai as genai

genai.configure(api_key="AIzaSyDYIFYLQj1qa91dV3tnCDR0OHAUVyJwyTw")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("How long is burz khalifa")
print(response.text)