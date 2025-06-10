+++
type = "question"
title = "Retrieve right city from zip codes"
description = '''Hi everyone! I am trying to retrieve cities from zipcode_state. Here is the code: Locations = pd.read_csv(&quot;geoloc1.csv&quot;, delimiter = &#x27;;&#x27;) Locations = Locations.drop_duplicates() Locations[&#x27;GEOLOC1&#x27;] = Locations[&#x27;GEOLOC1&#x27;].str.rstrip() # Removing spaces at the right ot the nation name Locations[&#x27;CAP ...'''
date = "2020-03-31T17:10:00Z"
lastmod = "2020-04-01T08:13:00Z"
weight = 73890
keywords = [ "python", "geopy", "nominatim", "cities", "zip-code" ]
aliases = [ "/questions/73890" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Retrieve right city from zip codes](/questions/73890/retrieve-right-city-from-zip-codes)

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
<span id="post-73890-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73890-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73890-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone!</p>
<p>I am trying to retrieve cities from zipcode_state. Here is the code:</p>
<pre><code>Locations = pd.read_csv(&quot;geoloc1.csv&quot;, delimiter = &#39;;&#39;)
Locations = Locations.drop_duplicates()
Locations[&#39;GEOLOC1&#39;] = Locations[&#39;GEOLOC1&#39;].str.rstrip() # Removing spaces at the right ot the nation name
Locations[&#39;CAP NAZIONE&#39;] = Locations[&#39;GEOLOC1&#39;].str.split(&#39;-&#39;).str[-1].str.strip() # Remove everything before -
Locations[&#39;CAP NAZIONE&#39;] = Locations[&#39;CAP NAZIONE&#39;].str.replace(&#39;_&#39;,&#39; &#39;) # Substitutes - with space 
Output = pd.DataFrame()
&#10;for index, row in Locations.iterrows():
time.sleep(1)
cap = row[&#39;CAP NAZIONE&#39;].split(&quot; &quot;,1)[0]
nazione = row[&#39;CAP NAZIONE&#39;].split(&quot; &quot;,1)[1]
loca = geocode(query = row[&#39;CAP NAZIONE&#39;], addressdetails = True, language = &#39;it,en&#39;)
try:
    row[&#39;LOCATION&#39;] = loca.raw[&#39;address&#39;][&#39;city&#39;]
except:
    try:
        row[&#39;LOCATION&#39;] = loca.raw[&#39;address&#39;][&#39;hamlet&#39;]
    except:
        try:
            row[&#39;LOCATION&#39;] = loca.raw[&#39;address&#39;][&#39;county&#39;]
        except:
            row[&#39;LOCATION&#39;] = &#39;_&#39;
&#10;if nazione == &#39;ITALIA&#39;:
    try:
        row[&#39;REGIONE&#39;] = loca.raw[&#39;address&#39;][&#39;state&#39;]
    except:
        &#39;_&#39;
Output = Output.append(row)</code></pre>
<p>The problem is that fro certain zipcode_nazione it doesn't return the right city. For example: 23841_ITALIA it returns Avellaneda that is in Buenos Aires not in Italy.</p>
<p>How can I get the correct city? Is there something I am doing wrong or some more accurate method, package, library I can use?</p>
<p>Thanks, Carlotta.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-geopy" rel="tag" title="see questions tagged &#39;geopy&#39;">geopy</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-cities" rel="tag" title="see questions tagged &#39;cities&#39;">cities</span> <span class="post-tag tag-link-zip-code" rel="tag" title="see questions tagged &#39;zip-code&#39;">zip-code</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Mar '20, 17:10</strong></p>
<img src="https://secure.gravatar.com/avatar/dba77ed68b48f13134f0ade205307d59?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Carlotta&#39;s gravatar image" />
<p><span>Carlotta</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Carlotta has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73890" class="comments-container">
&#10;</div>
<div id="comment-tools-73890" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73890-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="73893"></span>

<div id="answer-container-73893" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73893-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73893-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-73893-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Carlotta has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nobody has added an address in Italy with that postcode to the OpenStreetMap data yet.</p>
<p>Right now <a href="https://nominatim.openstreetmap.org/search.php?q=23841+ITALIA">https://nominatim.openstreetmap.org/search.php?q=23841+ITALIA</a> returning a residential road in Argentia.</p>
<p>You already set <code>language = 'it,en'</code>. Try if it supports <code>countrycodes = 'it'</code> as well as filter and remove the "Italia" from the main query if possible. That will return no results, but it's slightly better than having the geocoder search in all countries.</p>
<p>OpenStreetMap has no central reporting tool for missing data. We often rely on people living the area to add data. I hope setting the countrycodes filter will return more results for your other postcodes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Mar '20, 19:53</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-73893" class="comments-container">
<span id="73894"></span>
<div id="comment-73894" class="comment">
<div id="post-73894-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Update: I found the address of a local golf course with the postcode in their website and added it to OpenStreetMap. The Nominatim database updates its postcode database once per night (London time).</p>
</div>
<div id="comment-73894-info" class="comment-info">
<span class="comment-age">(31 Mar '20, 19:57)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="73899"></span>
<div id="comment-73899" class="comment">
<div id="post-73899-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you a lot, I will try with countrycodes and see how it goes.</p>
<p>Thank you for adding this postecode to the OpenStreetMap website. How can I do it if I find other postecodes that are not in the OpenStreetMap data yet?</p>
</div>
<div id="comment-73899-info" class="comment-info">
<span class="comment-age">(01 Apr '20, 08:13)</span> <span class="comment-user userinfo">Carlotta</span>
</div>
</div>
</div>
<div id="comment-tools-73893" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73893-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

