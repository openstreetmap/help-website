+++
type = "question"
title = "Geopy Nominatim: Retrieving city names in Italian"
description = '''I am trying to retrieve some cities names from zip codes using Geopy Nominatim. Here is the code: from geopy.geocoders import Nominatim geolocator = Nominatim()  Locations = pd.read_csv(&quot;cap.csv&quot;, delimiter = &#x27;&#92;t&#x27;) Locations.columns = [&#x27;CAP&#x27;] Locations = Locations.drop_duplicates() Cities = [] for c...'''
date = "2020-03-30T08:17:00Z"
lastmod = "2020-03-30T14:04:00Z"
weight = 73850
keywords = [ "python", "city", "nominatim", "geocoding", "language" ]
aliases = [ "/questions/73850" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Geopy Nominatim: Retrieving city names in Italian](/questions/73850/geopy-nominatim-retrieving-city-names-in-italian)

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
<span id="post-73850-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73850-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73850-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to retrieve some cities names from zip codes using Geopy Nominatim. Here is the code:</p>
<pre><code>from geopy.geocoders import Nominatim
geolocator = Nominatim()
&#10;Locations = pd.read_csv(&quot;cap.csv&quot;, delimiter = &#39;\t&#39;)
Locations.columns = [&#39;CAP&#39;]
Locations = Locations.drop_duplicates()
Cities = []
for cap in Locations[&#39;CAP&#39;]:
  print(cap)
  city = geolocator.geocode(query = cap, addressdetails = True, language = &#39;it&#39;)</code></pre>
<p>The problem is that the results I get are not in Italian, but they are:</p>
<pre><code>arrondissement d&#39;Anfa مقاطعة أنفا
성거읍
Sinak
Galatone
H/E Ward
Δήμος Κερατσινίου - Δραπετσώνας</code></pre>
<p>Do you know how can I get these names in Italian?</p>
<p>I would also like to get a more detailed address output. At the moment this is what I get: Susegana, Treviso, Veneto, 31058, Italia</p>
<p>I would like something that tells me which is the city, so for example city: Susegana, etc.</p>
<p>Thank you, Carlotta.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-language" rel="tag" title="see questions tagged &#39;language&#39;">language</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Mar '20, 08:17</strong></p>
<img src="https://secure.gravatar.com/avatar/dba77ed68b48f13134f0ade205307d59?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Carlotta&#39;s gravatar image" />
<p><span>Carlotta</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Carlotta has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Mar '20, 10:42</strong> </span></p>
</div>
</div>
<div id="comments-container-73850" class="comments-container">
&#10;</div>
<div id="comment-tools-73850" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73850-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="73852"></span>

<div id="answer-container-73852" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73852-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73852-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-73852-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Carlotta has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim can only return Italian names if there are ones in the database (e.g. the name:it hstore tag has a value).</p>
<p>You could try to alter your geolocator.geocode call by setting it's language to 'it,en' to get more results in latin script, as the name:en hstore tag is far more often filled with a value than the name:it one.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Mar '20, 10:29</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-73852" class="comments-container">
<span id="73853"></span>
<div id="comment-73853" class="comment">
<div id="post-73853-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks!</p>
<p>I will try this way and let you know if I solved my problem.</p>
<p>At the moment if I do city.address I get this output: Susegana, Treviso, Veneto, 31058, Italia</p>
<p>I assumed that the city is the first string, but I am not sure. Is there a way to get an output that tells me something like city: Susegana, etc? I tried with addressdetails = True, but it doesn't seem to return what I need.</p>
<p>Thanks, Carlotta.</p>
</div>
<div id="comment-73853-info" class="comment-info">
<span class="comment-age">(30 Mar '20, 10:40)</span> <span class="comment-user userinfo">Carlotta</span>
</div>
</div>
<span id="73854"></span>
<div id="comment-73854" class="comment">
<div id="post-73854-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm not familiar with geopy, but the city name should be in address.city from the addressdetails. Your city.address looks rather like the display_name returned by Nominatim. Can you get the raw output returned by the geocode function and than see if you have a ['address']['city'] in there?</p>
</div>
<div id="comment-73854-info" class="comment-info">
<span class="comment-age">(30 Mar '20, 10:56)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="73855"></span>
<div id="comment-73855" class="comment">
<div id="post-73855-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You are totally right! Under city.raw['address']['town'] I found what I needed.</p>
<p>Thanks, Carlotta.</p>
</div>
<div id="comment-73855-info" class="comment-info">
<span class="comment-age">(30 Mar '20, 11:12)</span> <span class="comment-user userinfo">Carlotta</span>
</div>
</div>
</div>
<div id="comment-tools-73852" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73852-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73856"></span>

<div id="answer-container-73856" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73856-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73856-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73856-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Many countries have 5 digit zip codes. Make sure you add the country name to the query, e.g. '12345, Italy'. It also helps to inspect the result for the country and remove any that are not in Italy.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Mar '20, 11:57</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-73856" class="comments-container">
<span id="73859"></span>
<div id="comment-73859" class="comment">
<div id="post-73859-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I had in plan to add it but thank you for the advice anyway!</p>
</div>
<div id="comment-73859-info" class="comment-info">
<span class="comment-age">(30 Mar '20, 14:04)</span> <span class="comment-user userinfo">Carlotta</span>
</div>
</div>
</div>
<div id="comment-tools-73856" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73856-form-container" class="comment-form-container">
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

