import telebot, openai


bot = telebot.TeleBot('5947062231:AAEXW6JjFTPnnyayzGpNQxLQJM7oEQLL7h0')

openai.api_key = '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'
model_engine = 'text-davinci-003'

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    prompt = message.text

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5)

    response = completion.choices[0].text

    bot.send_message(message.from_user.id, response)



bot.polling(none_stop=True, interval=0)
