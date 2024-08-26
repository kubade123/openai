from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are an expert in data engineer, skilled in big data and able to breakdown complex enterprise data problema into simple steps."},
    {"role": "user", "content": "Make a study case for big data problem in Province Government Level with its breadkown and solution"}
  ]
)

print(completion.choices[0].message)