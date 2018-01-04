headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = []
# TODO: set news_ticker to a string that contains no more than 140 characters long.
# HINT: modify the headlines list to verify your loop works with different inputs
print('the lenght of the news is {} chaacters long'.format(len(''.join(headlines))))
for headline in headlines:
   
    if len(''.join(headlines))>=200:
        break
    else:
        print('adding the news "{}"'.format(headline))
        news_ticker.append(headline)
print('\n'+' '.join(news_ticker))
        