+++
type = "question"
title = "Can&#x27;t find province, should I use admin_level in Nominatim Python?"
description = '''Hi! I am using geopy Nominatim in python to retrieve city names, province and regions of some postcodes. I have been able to get accurate city names using coutry_codes, but now I am having problems with provinces. The problem is that I don&#x27;t have the province in my raw[&#x27;address&#x27;] field. I learned th...'''
date = "2020-04-06T08:03:00Z"
lastmod = "2020-04-06T08:03:00Z"
weight = 74021
keywords = [ "python", "boundaries", "nominatim", "city", "admin_level" ]
aliases = [ "/questions/74021" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can't find province, should I use admin_level in Nominatim Python?](/questions/74021/cant-find-province-should-i-use-admin_level-in-nominatim-python)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74021-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74021-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74021-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi!</p>
<p>I am using geopy Nominatim in python to retrieve city names, province and regions of some postcodes. I have been able to get accurate city names using coutry_codes, but now I am having problems with provinces.</p>
<p>The problem is that I don't have the province in my raw['address'] field. I learned that I should use admin_level = 6 to get the province in my output but I don't know how to use it.</p>
<p>This is the code:</p>
<pre><code>from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
geolocator = Nominatim()
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
&#10;Locations = pd.read_csv(&quot;geoloc1.csv&quot;, delimiter = &#39;;&#39;)
for index, row in Locations.iterrows():
time.sleep(1)
country = np.where(countries == row[&#39;NAZIONE&#39;])[0][0] # Finding the index of the corresponding country
country = switch_country(country) # Finding the correct code for the country
#print(nazione)
&#10;if country == &#39;it&#39;:
    loca = geocode(query = row[&#39;CAP&#39;], country_codes = country, addressdetails = True, language = &#39;it,en&#39;)
    try:
        row[&#39;PROVINCIA&#39;] = loca.raw[&#39;address&#39;][&#39;county&#39;]
    except:
        row[&#39;PROVINCIA&#39;] = &#39;_&#39;
    try:
        row[&#39;REGIONE&#39;] = loca.raw[&#39;address&#39;][&#39;state&#39;]
    except:
        row[&#39;REGIONE&#39;] = &#39;_&#39;
loca = geocode(query = row[&#39;CAP&#39;], country_codes = country, addressdetails = True, language = &#39;it,en&#39;)
try:
    row[&#39;LOCATION&#39;] = loca.raw[&#39;address&#39;][&#39;city&#39;]
    Cities.append(loca.raw[&#39;address&#39;])
except:
    try:
        row[&#39;LOCATION&#39;] = loca.raw[&#39;address&#39;][&#39;hamlet&#39;]
        Cities.append(loca.raw[&#39;address&#39;])
    except:
        try:
            row[&#39;LOCATION&#39;] = loca.raw[&#39;address&#39;][&#39;village&#39;]
            Cities.append(loca.raw[&#39;address&#39;])
        except:
            row[&#39;LOCATION&#39;] = &#39;_&#39;
            Cities.append(loca)
&#10;Output = Output.append(row)</code></pre>
<p>How can I use admin_level = 6 to get the province name in my raw['address']?</p>
<p>Thanks, Carlotta.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-admin_level" rel="tag" title="see questions tagged &#39;admin_level&#39;">admin_level</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Apr '20, 08:03</strong></p>
<img src="https://secure.gravatar.com/avatar/dba77ed68b48f13134f0ade205307d59?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Carlotta&#39;s gravatar image" />
<p><span>Carlotta</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Carlotta has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Apr '20, 14:57</strong> </span></p>
</div>
</div>
<div id="comments-container-74021" class="comments-container">
&#10;</div>
<div id="comment-tools-74021" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74021-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

