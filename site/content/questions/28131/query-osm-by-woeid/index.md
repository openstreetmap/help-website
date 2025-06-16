+++
type = "question"
title = "Query OSM by WOEID"
description = '''Is it possible to query open street map locations based on a WOEID? See here: https://wiki.openstreetmap.org/wiki/Key:woeid Update: Also, I have lots of different place names, and I need to translate them into about 10 different locales. Because I know the WOEID for each location, I was thinking that...'''
date = "2013-11-15T12:12:00Z"
lastmod = "2013-11-15T13:21:00Z"
weight = 28131
keywords = [ "geoplanet", "woeid" ]
aliases = [ "/questions/28131" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Query OSM by WOEID](/questions/28131/query-osm-by-woeid)

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
<span id="post-28131-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28131-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-28131-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible to query open street map locations based on a WOEID?</p>
<p>See here: <a href="https://wiki.openstreetmap.org/wiki/Key:woeid">https://wiki.openstreetmap.org/wiki/Key:woeid</a></p>
<p>Update: Also, I have lots of different place names, and I need to translate them into about 10 different locales. Because I know the WOEID for each location, I was thinking that I could just query OSM to achieve this (if the OSM item has WOEID information too). Some of the locales are in the aliases for GeoPlanet, but quite a lot of them aren't as an alias, so I need to find a better way of translating them.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geoplanet" rel="tag" title="see questions tagged &#39;geoplanet&#39;">geoplanet</span> <span class="post-tag tag-link-woeid" rel="tag" title="see questions tagged &#39;woeid&#39;">woeid</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Nov '13, 12:12</strong></p>
<img src="https://secure.gravatar.com/avatar/6f782b51abca2547eb1237981468c9de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Layke&#39;s gravatar image" />
<p><span>Layke</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Layke has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Nov '13, 12:24</strong> </span></p>
</div>
</div>
<div id="comments-container-28131" class="comments-container">
&#10;</div>
<div id="comment-tools-28131" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28131-form-container" class="comment-form-container">
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

<span id="28132"></span>

<div id="answer-container-28132" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28132-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28132-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-28132-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Layke has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No, this is not directly possible. As you can see via <a href="http://taginfo.openstreetmap.org/keys/?key=woeid">taginfo</a> the woeid tag has been used only 73 times so far. Usually we don't keep references between our objects and other databases, with a few exceptions. If you really need this information you can try to create these references automatically for yourself by comparing tags and the rough location. But please don't import this information back into our database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Nov '13, 13:16</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-28132" class="comments-container">
<span id="28135"></span>
<div id="comment-28135" class="comment">
<div id="post-28135-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for the information. :)</p>
</div>
<div id="comment-28135-info" class="comment-info">
<span class="comment-age">(15 Nov '13, 13:21)</span> <span class="comment-user userinfo">Layke</span>
</div>
</div>
</div>
<div id="comment-tools-28132" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28132-form-container" class="comment-form-container">
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

