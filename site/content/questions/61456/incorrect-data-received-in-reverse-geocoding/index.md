+++
type = "question"
title = "Incorrect data received in reverse geocoding"
description = '''Hi, Got a location(lat&amp;amp;lon) from a geocode response. Then tried to reverse geocoding with that location(exact lat &amp;amp; lon), But got some other data with different lat &amp;amp; lon in response. For Eg: http://nominatim.openstreetmap.org/search?format=json&amp;amp;polygon_geojson=1&amp;amp;q=vellore,%20tam...'''
date = "2018-01-03T10:27:00Z"
lastmod = "2018-01-03T11:37:00Z"
weight = 61456
keywords = [ "nominatim", "osm", "reversegeocoding", "geocoding", "data" ]
aliases = [ "/questions/61456" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Incorrect data received in reverse geocoding](/questions/61456/incorrect-data-received-in-reverse-geocoding)

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
<span id="post-61456-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61456-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61456-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Got a location(lat&amp;lon) from a geocode response. Then tried to reverse geocoding with that location(exact lat &amp; lon), But got some other data with different lat &amp; lon in response.</p>
<p>For Eg: <a href="http://nominatim.openstreetmap.org/search?format=json&amp;polygon_geojson=1&amp;q=vellore,%20tamilnadu">http://nominatim.openstreetmap.org/search?format=json&amp;polygon_geojson=1&amp;q=vellore,%20tamilnadu</a></p>
<p>Get lat &amp; lon of 1st data(lat=12.9071753&amp;lon=79.1309695).</p>
<p><a href="http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=12.9071753&amp;lon=79.1309695&amp;addressdetails=1">http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=12.9071753&amp;lon=79.1309695&amp;addressdetails=1</a></p>
<p>Check reverse geocoding response, expect the same data(which got in geocoding), but getting different data.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jan '18, 10:27</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffa52ca3632b5a0cf02b51459b7529b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajavelu_M&#39;s gravatar image" />
<p><span>Rajavelu_M</span><br />
<span class="score" title="253 reputation points">253</span><span title="45 badges"><span class="badge1">●</span><span class="badgecount">45</span></span><span title="48 badges"><span class="silver">●</span><span class="badgecount">48</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajavelu_M has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jan '18, 10:58</strong> </span></p>
</div>
</div>
<div id="comments-container-61456" class="comments-container">
<span id="61457"></span>
<div id="comment-61457" class="comment">
<div id="post-61457-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Maybe the reverse geocoding tries to search for the nearest POI. The geocoding query returns the <a href="https://www.openstreetmap.org/node/243713144">city node</a> because that's what you've been searching for. The reverse geocoding query instead returns a <a href="https://www.openstreetmap.org/node/4693434962">school node</a> which I consider to be more relevant than a somewhat arbitrarily placed city node. Could be just a coincidence, though.</p>
</div>
<div id="comment-61457-info" class="comment-info">
<span class="comment-age">(03 Jan '18, 11:21)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-61456" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61456-form-container" class="comment-form-container">
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

<span id="61458"></span>

<div id="answer-container-61458" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61458-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61458-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-61458-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><code>reverse</code> and <code>search</code> are not inverse operations of each other. They use the same database and produce a similar looking output format but that is all. They use completely different algorithms to compute the respective results.</p>
<p>In the particular example <code>search</code> returns the centre coordinates for the town you are looking for and <code>reverse</code> then returns the closest object to that centre. It tries to be as precise as possible, so preferably returns a street or address with house number or a POI like, as in this case, a school building. Your original town is still contained in the response in the address part. So the result is not wrong, just more precise than you expected.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jan '18, 11:37</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-61458" class="comments-container">
&#10;</div>
<div id="comment-tools-61458" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61458-form-container" class="comment-form-container">
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

