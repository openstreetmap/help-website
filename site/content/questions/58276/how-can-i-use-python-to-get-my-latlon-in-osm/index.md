+++
type = "question"
title = "How can I use python to get my lat,lon in OSM?"
description = '''I have try geocode to get my lat and lon , but not current it is get by my ip and conver to lat,lon Can help me osm(openstreetmap) api can get my current lat and lon? import geocoder g = geocoder.ip(&#x27;me&#x27;) print(g.latlng)  and freegeoip = &quot;http://freegeoip.net/json&quot; geo_r = requests.get(freegeoip) ge...'''
date = "2017-08-13T09:50:00Z"
lastmod = "2017-08-14T08:20:00Z"
weight = 58276
keywords = [ "python" ]
aliases = [ "/questions/58276" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I use python to get my lat,lon in OSM?](/questions/58276/how-can-i-use-python-to-get-my-latlon-in-osm)

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
<span id="post-58276-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58276-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-58276-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have try geocode to get my lat and lon , but not current</p>
<p>it is get by my ip and conver to lat,lon</p>
<p>Can help me osm(openstreetmap) api can get my current lat and lon?</p>
<pre><code>import geocoder
g = geocoder.ip(&#39;me&#39;)
print(g.latlng)</code></pre>
<p>and</p>
<pre><code>freegeoip = &quot;http://freegeoip.net/json&quot;
geo_r = requests.get(freegeoip)
geo_json = geo_r.json()
&#10;user_postition = [geo_json[&quot;latitude&quot;], geo_json[&quot;longitude&quot;]]
&#10;print(user_postition)</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Aug '17, 09:50</strong></p>
<img src="https://secure.gravatar.com/avatar/e26390b32f2d9c4469ebcf3ffc1652df?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arvis_Su&#39;s gravatar image" />
<p><span>Arvis_Su</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arvis_Su has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Aug '17, 09:50</strong> </span></p>
</div>
</div>
<div id="comments-container-58276" class="comments-container">
&#10;</div>
<div id="comment-tools-58276" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58276-form-container" class="comment-form-container">
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

<span id="58297"></span>

<div id="answer-container-58297" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58297-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58297-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-58297-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap doesn't offer a geolocation API. However you can find various geolocation services and databases on the Internet. Some of them are mentioned here: <a href="https://opendata.stackexchange.com/questions/2087/ip-geocoding-data-sources-and-or-apis">https://opendata.stackexchange.com/questions/2087/ip-geocoding-data-sources-and-or-apis</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Aug '17, 08:20</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-58297" class="comments-container">
&#10;</div>
<div id="comment-tools-58297" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58297-form-container" class="comment-form-container">
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

