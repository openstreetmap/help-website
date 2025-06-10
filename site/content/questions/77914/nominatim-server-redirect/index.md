+++
type = "question"
title = "Nominatim server redirect"
description = '''We have software which uses OpenStreetMap as a map and Nominatim as reverse geocoding to find exact street address for GPS point. A while ago we noticed that there had been major problem with one Nominatim server (pummelzacken) and it appeared so that our software was not able to connect to address ...'''
date = "2020-12-14T12:04:00Z"
lastmod = "2020-12-17T07:00:00Z"
weight = 77914
keywords = [ "nominatim", "server" ]
aliases = [ "/questions/77914" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim server redirect](/questions/77914/nominatim-server-redirect)

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
<span id="post-77914-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77914-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77914-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We have software which uses OpenStreetMap as a map and Nominatim as reverse geocoding to find exact street address for GPS point. A while ago we noticed that there had been major problem with one Nominatim server (pummelzacken) and it appeared so that our software was not able to connect to address nominatim.openstreetmap.org with proper parameters. The address redirected our query always to pummelzacken and connection attempt failed every time. Is there a reason why the query was redirected to pummelzacken when it was out of service? I see that server dulcy was up and running at same time.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Dec '20, 12:04</strong></p>
<img src="https://secure.gravatar.com/avatar/447324ad179b00811037d3e3766b647f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pocum&#39;s gravatar image" />
<p><span>Pocum</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pocum has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77914" class="comments-container">
<span id="77916"></span>
<div id="comment-77916" class="comment">
<div id="post-77916-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Just in case you haven't seen it: <a href="https://operations.osmfoundation.org/policies/nominatim/">https://operations.osmfoundation.org/policies/nominatim/</a> .</p>
</div>
<div id="comment-77916-info" class="comment-info">
<span class="comment-age">(14 Dec '20, 12:51)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="77964"></span>
<div id="comment-77964" class="comment">
<div id="post-77964-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No replies for a while but I would appreciate if someone can tell me if there has been any reason why the traffic was not redirected to dulcy server while pummelzacken was under maintenance brake (and vice versa). Of course any explanation is appreciated but I just want to know. I think that the problem is not in our end because it seems that the connection string is not cached for later use.</p>
</div>
<div id="comment-77964-info" class="comment-info">
<span class="comment-age">(17 Dec '20, 07:00)</span> <span class="comment-user userinfo">Pocum</span>
</div>
</div>
</div>
<div id="comment-tools-77914" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77914-form-container" class="comment-form-container">
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

<span id="77917"></span>

<div id="answer-container-77917" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77917-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77917-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-77917-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The planet database was reimported on both OSM Nominatim servers during that time, one after the other, which takes about 2 days each, so the redirect was temporary. Full reimports are rare, I think the last one was over 12 months ago. In preparation for Nominatim 3.6 release <a href="https://github.com/osm-search/Nominatim/releases/tag/v3.6.0">https://github.com/osm-search/Nominatim/releases/tag/v3.6.0</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Dec '20, 12:53</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-77917" class="comments-container">
<span id="77926"></span>
<div id="comment-77926" class="comment">
<div id="post-77926-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the explanation. But if I have understood correctly, when server pummelzacken was under maintenance (the import process) other server dulcy should have been accessible in url <a href="https://nominatim.openstreetmap.org">https://nominatim.openstreetmap.org</a>. Am I correct? At least uptime graph shows that dulcy was up between 27th Nov - 1st Dec when pummelzacken was under maintenance. Then I see dulcy was under maintenance between 6th Dec - 8th Dec and pummelzacken was up at that time.</p>
<p>And the redirect. The address was redirected always to pummelzacken when pummelzacken was under maintenance. Do you confirm that?</p>
<p>Do you report about the planet database reimport and other planned maintenance couple of days before the planned maintenance time? And also unplanned as soon as possible? For example in twitter.</p>
</div>
<div id="comment-77926-info" class="comment-info">
<span class="comment-age">(15 Dec '20, 06:53)</span> <span class="comment-user userinfo">Pocum</span>
</div>
</div>
<span id="77932"></span>
<div id="comment-77932" class="comment">
<div id="post-77932-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I can't confirm, I dont' work in the OSM operations group. <a href="https://operations.osmfoundation.org/policies/nominatim/">https://operations.osmfoundation.org/policies/nominatim/</a> has no uptime guarantees.</p>
</div>
<div id="comment-77932-info" class="comment-info">
<span class="comment-age">(15 Dec '20, 12:55)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-77917" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77917-form-container" class="comment-form-container">
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

