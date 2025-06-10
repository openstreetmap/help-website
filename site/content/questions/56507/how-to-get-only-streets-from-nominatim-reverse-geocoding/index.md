+++
type = "question"
title = "How to get only streets from Nominatim Reverse Geocoding?"
description = '''Hi, in my application, I get the latitude and longitude of my position. My position is always a road/street because I am in a car. When I have the latitude und longitude, I make a request to Nominatim, e.g.:  http://nominatim.openstreetmap.org/reverse?format=json&amp;amp;lat=LATITUDE&amp;amp;lon=LONGITUDE I...'''
date = "2017-06-08T07:04:00Z"
lastmod = "2017-06-08T20:41:00Z"
weight = 56507
keywords = [ "reversegeocoding", "reversegeolocation", "nominatim", "reverse" ]
aliases = [ "/questions/56507" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to get only streets from Nominatim Reverse Geocoding?](/questions/56507/how-to-get-only-streets-from-nominatim-reverse-geocoding)

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
<span id="post-56507-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56507-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56507-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, in my application, I get the latitude and longitude of my position. My position is always a road/street because I am in a car. When I have the latitude und longitude, I make a request to Nominatim, e.g.:</p>
<p><a href="http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=LATITUDE&amp;lon=LONGITUDE">http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=LATITUDE&amp;lon=LONGITUDE</a></p>
<p>If at my position is only a road, then the request works how I want the request to work: I get the street I am on. But if there is a building in the near of my position, I get the building instead of the street. I can't use the street of the building because it is important for me to get the right section of the road because I need the way id for a further request (e.g. speed limit on the street)</p>
<p>Is it possible to get just streets from Nominatim?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-reversegeolocation" rel="tag" title="see questions tagged &#39;reversegeolocation&#39;">reversegeolocation</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-reverse" rel="tag" title="see questions tagged &#39;reverse&#39;">reverse</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jun '17, 07:04</strong></p>
<img src="https://secure.gravatar.com/avatar/d0c8a30460b2bb4ced62400dcbee2b54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FM_Pete&#39;s gravatar image" />
<p><span>FM_Pete</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FM_Pete has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56507" class="comments-container">
&#10;</div>
<div id="comment-tools-56507" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56507-form-container" class="comment-form-container">
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

<span id="56521"></span>

<div id="answer-container-56521" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56521-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56521-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56521-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="FM_Pete has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can set <code>zoom=16</code> to filter buildings/addresses/POIs.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jun '17, 10:48</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-56521" class="comments-container">
<span id="56525"></span>
<div id="comment-56525" class="comment">
<div id="post-56525-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That does not solve my problem. I am not interested in e.g. buildings, I just need streets.</p>
</div>
<div id="comment-56525-info" class="comment-info">
<span class="comment-age">(08 Jun '17, 11:15)</span> <span class="comment-user userinfo">FM_Pete</span>
</div>
</div>
<span id="56526"></span>
<div id="comment-56526" class="comment">
<div id="post-56526-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Have you tried the parameter? Do you have an example where a building gets returned?</p>
</div>
<div id="comment-56526-info" class="comment-info">
<span class="comment-age">(08 Jun '17, 11:27)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="56528"></span>
<div id="comment-56528" class="comment">
<div id="post-56528-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I tried it with zoom=18, I get the building then. With zoom=16 and zoom=17 I get the street I need. But why? The only thing I found about the zoom parameter is following:</p>
<p>zoom=[0-18]</p>
<p>Level of detail required where 0 is country and 18 is house/building</p>
<p>Where can I see the difference between e.g. 16 and 18 or 16 and 17?</p>
</div>
<div id="comment-56528-info" class="comment-info">
<span class="comment-age">(08 Jun '17, 12:43)</span> <span class="comment-user userinfo">FM_Pete</span>
</div>
</div>
<span id="56536"></span>
<div id="comment-56536" class="comment">
<div id="post-56536-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can test the zoom parameter on <a href="http://nominatim.openstreetmap.org/reverse.php?format=html&amp;lat=35.144792512496686&amp;lon=-90.00751018524171&amp;zoom=16">http://nominatim.openstreetmap.org/reverse.php?format=html&amp;lat=35.144792512496686&amp;lon=-90.00751018524171&amp;zoom=16</a> The red circle is the search point (where you clicked on the map), the blue circle the result that got returned. A zoom=3 will return only the country, zoom=16 the street, zoom=18 the building (address, housenumber, POI) if found.</p>
</div>
<div id="comment-56536-info" class="comment-info">
<span class="comment-age">(08 Jun '17, 15:49)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="56539"></span>
<div id="comment-56539" class="comment">
<div id="post-56539-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your help!</p>
</div>
<div id="comment-56539-info" class="comment-info">
<span class="comment-age">(08 Jun '17, 20:41)</span> <span class="comment-user userinfo">FM_Pete</span>
</div>
</div>
</div>
<div id="comment-tools-56521" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56521-form-container" class="comment-form-container">
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

