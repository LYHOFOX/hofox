from mwclient import Site

user_agent = 'charlesBot/0.0.1(charles@klei.vip)'

wikigg = Site(host='noita.wiki.gg',
              path="/zh/", clients_useragent=user_agent)

bwiki = Site(host='wiki.biligame.com', 
             path="/noita/", clients_useragent=user_agent)

# fandom = Site(host="oxygennotincluded.fandom.com", path="/zh/", clients_useragent=user_agent)
