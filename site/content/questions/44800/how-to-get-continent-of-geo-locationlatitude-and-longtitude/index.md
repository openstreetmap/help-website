+++
type = "question"
title = "How to get continent of geo-location(latitude and longtitude)"
description = '''Hi to all, I need to get continent of a geo-location(lat &amp;amp; lon) or continent of a country. Is there any option available in Nominatim? Any other feasible solutions?'''
date = "2015-08-18T07:33:00Z"
lastmod = "2017-04-25T02:07:00Z"
weight = 44800
keywords = [ "geolocation", "reversegeolocation", "reversegeocoding", "geocoding", "nominatim" ]
aliases = [ "/questions/44800" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get continent of geo-location(latitude and longtitude)](/questions/44800/how-to-get-continent-of-geo-locationlatitude-and-longtitude)

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
<span id="post-44800-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44800-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44800-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi to all,</p>
<p>I need to get continent of a geo-location(lat &amp; lon) or continent of a country.</p>
<p>Is there any option available in Nominatim?</p>
<p>Any other feasible solutions?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geolocation" rel="tag" title="see questions tagged &#39;geolocation&#39;">geolocation</span> <span class="post-tag tag-link-reversegeolocation" rel="tag" title="see questions tagged &#39;reversegeolocation&#39;">reversegeolocation</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Aug '15, 07:33</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffa52ca3632b5a0cf02b51459b7529b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajavelu_M&#39;s gravatar image" />
<p><span>Rajavelu_M</span><br />
<span class="score" title="253 reputation points">253</span><span title="45 badges"><span class="badge1">●</span><span class="badgecount">45</span></span><span title="48 badges"><span class="silver">●</span><span class="badgecount">48</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajavelu_M has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Apr '17, 10:45</strong> </span></p>
</div>
</div>
<div id="comments-container-44800" class="comments-container">
&#10;</div>
<div id="comment-tools-44800" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44800-form-container" class="comment-form-container">
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

<span id="55843"></span>

<div id="answer-container-55843" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55843-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55843-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55843-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM has not defined what the continents are in its tagging structure.</p>
<p>In OSM the top level <a href="http://wiki.openstreetmap.org/wiki/Boundaries">administrative boundaries</a> are for countries, rather than continents. There is a capacity in the administrative tagging structure for defining administrative regions above the level of a country but this has not been done so far. Also, there is more than one view of what constitutes a continent. what you mean by a <a href="http://wiki.openstreetmap.org/wiki/Continents">continent</a> may depend on what geophysical, geopolitical or geo-demographic model of the world you are using. Does your view of the world have 4, 5, 6, 7 (or more) regions that you would call a continent, and if so, do these align with the commonly accepted regions of the world that might be called continents? Opinions differ and there is no definitive standard.</p>
<p>So you will need to create a proxy structure that is probably based on various administrative levels for countries, territories and states. While most countries are likely to be confined to a single continent, some countries, such as the USA, UK, France, and Russia have territorial claims across several continents, including Antarctica, so you may need to determine which part of a country a geo-location is in before determining its continent. You may wish to use <a href="http://en.wikipedia.org/wiki/ISO_3166-1">ISO 3166-1</a> to classify your geo-locations by country code and then group these codes by continent.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Apr '17, 02:07</strong></p>
<img src="https://secure.gravatar.com/avatar/1a623cf4b5df74bee1b91d0c21736921?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Huttite&#39;s gravatar image" />
<p><span>Huttite</span><br />
<span class="score" title="560 reputation points">560</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Huttite has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55843" class="comments-container">
&#10;</div>
<div id="comment-tools-55843" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55843-form-container" class="comment-form-container">
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

