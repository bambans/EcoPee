try:
    from requests import get, post
except:
    from urequests import get, post
    
try:
    from json import loads
except:
    from ujson import loads

# Show some more information
debug = True

apiToken = '5795451239:AAHPfM2MEqIl0GqupAE2M2a2KF3nC0cqO9s' # EcoPee
# apiToken = '5574509512:AAFqo-1ncnkbgRynTkrG1j5Kiu2wg2LKlKw' # Teste

botAPI_endpoint = f'https://api.telegram.org/bot{apiToken}'

# Get user data from your telegram bot updates, filtering by username
def getUserData(username):
        try:
            print('Getting updates response')

            jsonResponse = loads(get(f'{botAPI_endpoint}/getUpdates').text)

            print('Updates received. Displaying data:')
            print(jsonResponse)

            print('Filtering updates by username and getting chatID...')
            chatID = None

            for result in jsonResponse['result']:
                try:
                    if result['message']['from']['username'] == username:
                        chatID = result['message']['chat']['id']
                        break
                except:
                    pass

            if chatID != None:
                print('Updates received successfully')
            else:
                print('No updates received')

            return chatID
        except Exception as e:
            print(e)

# Send message to telegram user from your bot using chatID (returned by getUserData)
def sendToTelegram(chatID, message):
    try:
        print('Sending message to telegram user')

        # jsonResponse = loads(post(url = f'{botAPI_endpoint}/sendMessage', json = {'chat_id': chatID, 'text': message}, headers = {'Content-Type': 'application/json'}).text)
        jsonResponse = loads(get(f'{botAPI_endpoint}/sendMessage?chat_id={chatID}&text={message}').text)

        print('Tryed. Displaying data:')
        print(jsonResponse)

        return jsonResponse['ok']
    except Exception as e:
        print(e)
        return False
