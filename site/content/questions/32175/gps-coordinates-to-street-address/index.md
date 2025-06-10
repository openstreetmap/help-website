+++
type = "question"
title = "GPS Coordinates to street address"
description = '''Hi, I&#x27;m very new to OpenStreetMap but I want to build a small java program who converts Latitude and Longitude from GPS to the nearest street address. I know the basics of java so a i know how to create a GUI for input/output, so that&#x27;s not the problem. I just don&#x27;t know how to use OpenStreetMap API...'''
date = "2014-04-07T14:51:00Z"
lastmod = "2014-04-08T09:44:00Z"
weight = 32175
keywords = [ "address", "street", "coordinates", "gps" ]
aliases = [ "/questions/32175" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [GPS Coordinates to street address](/questions/32175/gps-coordinates-to-street-address)

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
<span id="post-32175-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32175-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-32175-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm very new to OpenStreetMap but I want to build a small java program who converts Latitude and Longitude from GPS to the nearest street address. I know the basics of java so a i know how to create a GUI for input/output, so that's not the problem. I just don't know how to use OpenStreetMap API to convert the lat/long to a street address. Could anybody get me on the right track?</p>
<p>Thx Fred</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Apr '14, 14:51</strong></p>
<img src="https://secure.gravatar.com/avatar/8ef31a208d2fdc6b540735e4430b7789?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FredGoe&#39;s gravatar image" />
<p><span>FredGoe</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FredGoe has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-32175" class="comments-container">
&#10;</div>
<div id="comment-tools-32175" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32175-form-container" class="comment-form-container">
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

<span id="32177"></span>

<div id="answer-container-32177" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32177-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32177-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-32177-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The process of converting lat/lon to an address is called "Reverse Geocoding". The OSM API is not suitable for that but the <a href="http://wiki.openstreetmap.org/wiki/Nominatim">Nominatim service</a> does a decent job at reverse geocoding. All that's left for you is send a HTTP request and parse the response. Note that this is subject to usage restrictions (don't bulk geocode tons of addresses).</p>
<p>If you want to implement your own reverse geocoder (not recommended - lots of work to get it right) then you will probably want to import raw OSM data and preprocess it suitably. You could possibly use the Osmosis library for that (also Java).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Apr '14, 16:20</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-32177" class="comments-container">
<span id="32191"></span>
<div id="comment-32191" class="comment">
<div id="post-32191-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thanks for the help! You've set me on the right track :)</p>
</div>
<div id="comment-32191-info" class="comment-info">
<span class="comment-age">(08 Apr '14, 09:44)</span> <span class="comment-user userinfo">FredGoe</span>
</div>
</div>
</div>
<div id="comment-tools-32177" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32177-form-container" class="comment-form-container">
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

