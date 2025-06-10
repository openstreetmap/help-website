+++
type = "question"
title = "Nominatim install returning highway instead of house matches"
description = '''Hello again OSM experts, I installed Nomitatim and imported data of one state (Maryland, US). It looks working. But when I query for geocoding, I always (or most of the time)got in returned result class=&quot;highway&quot; and type=&quot;residential&quot;, while same query on openstreetmap website returns class=&quot;place&quot;...'''
date = "2013-07-16T14:54:00Z"
lastmod = "2013-07-17T10:57:00Z"
weight = 24283
keywords = [ "nominatim" ]
aliases = [ "/questions/24283" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim install returning highway instead of house matches](/questions/24283/nominatim-install-returning-highway-instead-of-house-matches)

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
<span id="post-24283-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24283-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24283-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello again OSM experts,</p>
<p>I installed Nomitatim and imported data of one state (Maryland, US). It looks working. But when I query for geocoding, I always (or most of the time)got in returned result class="highway" and type="residential", while same query on openstreetmap website returns class="place", and type="house".</p>
<p>Can someone tell me what I might be missing here? Thanks in advance! TJ</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jul '13, 14:54</strong></p>
<img src="https://secure.gravatar.com/avatar/1586020f0a016a46e7c9a46dbdbd7d66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OSM-TJ2013&#39;s gravatar image" />
<p><span>OSM-TJ2013</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OSM-TJ2013 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jul '13, 15:44</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/bda08a105bb6a4a606d47c1b27187fac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twain&#39;s gravatar image" />
<p><span>twain</span><br />
<span class="score" title="2381 reputation points"><span>2.4k</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span></p>
</div>
</div>
<div id="comments-container-24283" class="comments-container">
&#10;</div>
<div id="comment-tools-24283" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24283-form-container" class="comment-form-container">
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

<span id="24286"></span>

<div id="answer-container-24286" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24286-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24286-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-24286-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In the USA the openstreetmap instance has tiger data loaded in addition to the OSM data. You can find information on how to do this in the response to <a href="https://help.openstreetmap.org/questions/12150/missing-house-numbers-in-local-nominatim-instance">this question</a>. You should be able to just load data for Maryland rather than the whole data set.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jul '13, 15:39</strong></p>
<img src="https://secure.gravatar.com/avatar/bda08a105bb6a4a606d47c1b27187fac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twain&#39;s gravatar image" />
<p><span>twain</span><br />
<span class="score" title="2381 reputation points"><span>2.4k</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twain has 15 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-24286" class="comments-container">
<span id="24287"></span>
<div id="comment-24287" class="comment">
<div id="post-24287-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! That "tiger" link does not work anymore. I found this link: <a href="http://www.census.gov/geo/maps-data/data/tiger.html.">http://www.census.gov/geo/maps-data/data/tiger.html.</a> But there are not EDGES files. Will the Shapefiles work?</p>
<p>Thanks again! TJ</p>
</div>
<div id="comment-24287-info" class="comment-info">
<span class="comment-age">(16 Jul '13, 15:47)</span> <span class="comment-user userinfo">OSM-TJ2013</span>
</div>
</div>
<span id="24288"></span>
<div id="comment-24288" class="comment">
<div id="post-24288-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Never mind, I found it from another old comment. I will try it out and get back here with results.</p>
</div>
<div id="comment-24288-info" class="comment-info">
<span class="comment-age">(16 Jul '13, 15:49)</span> <span class="comment-user userinfo">OSM-TJ2013</span>
</div>
</div>
<span id="24289"></span>
<div id="comment-24289" class="comment">
<div id="post-24289-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You can try <a href="ftp://ftp2.census.gov/geo/tiger/TIGER2012/EDGES/">ftp://ftp2.census.gov/geo/tiger/TIGER2012/EDGES/</a> for a newer version of the data if you wish although I'm not sure this has been tested yet.</p>
</div>
<div id="comment-24289-info" class="comment-info">
<span class="comment-age">(16 Jul '13, 15:53)</span> <span class="comment-user userinfo">twain</span>
</div>
</div>
<span id="24303"></span>
<div id="comment-24303" class="comment">
<div id="post-24303-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>TIGER 2012 works fine. I've updated the original answer.</p>
</div>
<div id="comment-24303-info" class="comment-info">
<span class="comment-age">(17 Jul '13, 10:57)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
</div>
<div id="comment-tools-24286" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24286-form-container" class="comment-form-container">
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

