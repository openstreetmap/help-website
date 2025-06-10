+++
type = "question"
title = "How do I find all segments of a motorway?"
description = '''SCENARIO:  i have a segment (of a motorway, for example). is it possible to get all other segments of said motorway using OSM?'''
date = "2013-11-13T18:38:00Z"
lastmod = "2013-11-14T09:39:00Z"
weight = 28059
keywords = [ "osm", "way" ]
aliases = [ "/questions/28059" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I find all segments of a motorway?](/questions/28059/how-do-i-find-all-segments-of-a-motorway)

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
<span id="post-28059-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28059-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-28059-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>SCENARIO:</p>
<p>i have a segment (of a motorway, for example).</p>
<p>is it possible to get all other segments of said motorway using OSM?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Nov '13, 18:38</strong></p>
<img src="https://secure.gravatar.com/avatar/dde3251e03f13e55e9221fc11dd29590?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tonygil&#39;s gravatar image" />
<p><span>tonygil</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tonygil has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-28059" class="comments-container">
<span id="28078"></span>
<div id="comment-28078" class="comment">
<div id="post-28078-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Please be more specific about what should be in the result:</p>
<p>Should the reverse direction of a dual carriageway be included?</p>
<p>Should everything with the same road number be included or the entire motorway grid? What about motorways that are split in multiple non-connected parts?</p>
<p>What parts of exit lanes, intersections and so on should be included?</p>
</div>
<div id="comment-28078-info" class="comment-info">
<span class="comment-age">(14 Nov '13, 07:14)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
<span id="28087"></span>
<div id="comment-28087" class="comment">
<div id="post-28087-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanx roland, wow, you got me there. in an ideal situation, everything that is related as part of the SAME motorway (numbering or name).</p>
</div>
<div id="comment-28087-info" class="comment-info">
<span class="comment-age">(14 Nov '13, 09:37)</span> <span class="comment-user userinfo">tonygil</span>
</div>
</div>
</div>
<div id="comment-tools-28059" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28059-form-container" class="comment-form-container">
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

<span id="28064"></span>

<div id="answer-container-28064" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28064-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28064-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-28064-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is technically possible from the OSM API (making recursive use of the /node/123/ways call to find out which other ways use the first/last node of the given way), but if done frequently it would be considered an abuse of the API.</p>
<p>Often, the motorway will be part of a relation, and then it would be possible to use the /relation/123/full call to download the full relation. This, too, is something that we don't like to see in an automated fashion.</p>
<p>If you want to make such queries regularly, set up your own database and import OSM data into it. Alternatively, check out if <a href="http://wiki.openstreetmap.org/wiki/Overpass_API">Overpasss API</a> offers something that you can use.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Nov '13, 21:28</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-28064" class="comments-container">
<span id="28077"></span>
<div id="comment-28077" class="comment">
<div id="post-28077-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>An algorithm that adds all connected ways is likely to grab the entire street grid (at least of an island, maybe also Eurasia or America).</p>
<p>A similar thing happens when one restricts to motorway and motorway_link with the motorway network.</p>
<p>Thus I would strongly discourage this approach.</p>
</div>
<div id="comment-28077-info" class="comment-info">
<span class="comment-age">(14 Nov '13, 07:10)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
<span id="28088"></span>
<div id="comment-28088" class="comment">
<div id="post-28088-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yes, i understand that, to do so, i would have to be using my own copy of OSM database, so as not to abuse the API. what approach would you suggest?</p>
</div>
<div id="comment-28088-info" class="comment-info">
<span class="comment-age">(14 Nov '13, 09:39)</span> <span class="comment-user userinfo">tonygil</span>
</div>
</div>
</div>
<div id="comment-tools-28064" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28064-form-container" class="comment-form-container">
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

