+++
type = "question"
title = "POI data from OSM as markers on leaflet"
description = '''Hi guys, I&#x27;ve got a simple question and would be great to have some starting information on how to get this going. I&#x27;m a newbie here with OSM and searched the forums across different platforms, but just can&#x27;T find a simple starting point. So here&#x27;s what I need:  user goes to map on my website and se...'''
date = "2018-12-30T19:07:00Z"
lastmod = "2018-12-31T11:39:00Z"
weight = 67392
keywords = [ "marker", "leaflet", "amenity", "poi" ]
aliases = [ "/questions/67392" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [POI data from OSM as markers on leaflet](/questions/67392/poi-data-from-osm-as-markers-on-leaflet)

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
<span id="post-67392-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67392-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67392-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi guys, I've got a simple question and would be great to have some starting information on how to get this going. I'm a newbie here with OSM and searched the forums across different platforms, but just can'T find a simple starting point. So here's what I need:</p>
<ul>
<li>user goes to map on my website and selects a button f.e. 'clothing shops'</li>
<li>map shows a marker on all clothing shops.</li>
</ul>
<p>And that's it.</p>
<p>I'm using leaflet to get the map on my website and that works, though what I need to figure out is how to get OSM data of the amenities. (preferably through php, java or http request) Then the part of adding markers on the map is easy, and if needed with clustering.</p>
<p>ps: in case anybody knows a better platform for this purpose then leaflet it would be great to know about.</p>
<p>Thanks a bunch!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Dec '18, 19:07</strong></p>
<img src="https://secure.gravatar.com/avatar/89858e1d0e500ae658bf8cf7fc4964c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tijmenheid&#39;s gravatar image" />
<p><span>tijmenheid</span><br />
<span class="score" title="41 reputation points">41</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tijmenheid has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67392" class="comments-container">
&#10;</div>
<div id="comment-tools-67392" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67392-form-container" class="comment-form-container">
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

<span id="67400"></span>

<div id="answer-container-67400" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67400-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67400-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-67400-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tijmenheid has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can query OSM via the <a href="http://overpass-api.de/">Overpass API</a>. A quick search gave me</p>
<ul>
<li>a <a href="https://gist.github.com/tyrasd/45e4a6a44c734497e82ccaae16a9c9ea">minimalistic example</a></li>
<li>a <a href="https://github.com/GuillaumeAmat/leaflet-overpass-layer">Leaflet Overpass layer</a></li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Dec '18, 06:51</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-67400" class="comments-container">
<span id="67402"></span>
<div id="comment-67402" class="comment">
<div id="post-67402-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a bunch mate, the minimalistic sample should have all I need.</p>
<p>Later I hope with some more experience to know where to find these things easier myself too. Habt ne gute rutsch!</p>
</div>
<div id="comment-67402-info" class="comment-info">
<span class="comment-age">(31 Dec '18, 11:39)</span> <span class="comment-user userinfo">tijmenheid</span>
</div>
</div>
</div>
<div id="comment-tools-67400" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67400-form-container" class="comment-form-container">
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

