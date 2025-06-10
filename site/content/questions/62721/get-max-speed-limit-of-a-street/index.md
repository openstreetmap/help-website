+++
type = "question"
title = "Get max speed limit of a street"
description = '''I want to get max speed limit of a street by Open Street Maps in my ionic application. Please suggest a possible solution.'''
date = "2018-03-19T06:30:00Z"
lastmod = "2018-03-19T09:03:00Z"
weight = 62721
keywords = [ "maxspeed" ]
aliases = [ "/questions/62721" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get max speed limit of a street](/questions/62721/get-max-speed-limit-of-a-street)

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
<span id="post-62721-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62721-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62721-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to get max speed limit of a street by Open Street Maps in my ionic application. Please suggest a possible solution.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-maxspeed" rel="tag" title="see questions tagged &#39;maxspeed&#39;">maxspeed</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Mar '18, 06:30</strong></p>
<img src="https://secure.gravatar.com/avatar/fb2207af7f1c1cacc1d9cb19e520c297?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NextOlive&#39;s gravatar image" />
<p><span>NextOlive</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NextOlive has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Mar '18, 07:30</strong> </span></p>
</div>
</div>
<div id="comments-container-62721" class="comments-container">
&#10;</div>
<div id="comment-tools-62721" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62721-form-container" class="comment-form-container">
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

<span id="62726"></span>

<div id="answer-container-62726" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62726-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62726-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-62726-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi. I don't know what ionic is. In OSM the speed limit is stored in the <a href="https://wiki.openstreetmap.org/wiki/Key:maxspeed"><code>maxspeed</code></a> tag. A word of warning: Data in OSM is patchy, and only ~7% of <code>highway</code>s in OSM have a <code>maxspeed</code> tag. <em>But</em> many (all?) countries have default speed limits based on the road classification, and you can deduce this from the <code>highway</code> tag value (or the <code>ref</code>), so just because the maxspeed tag is missing doesn't mean that you cannot deduce the speed limit. However this requires you to know the speed limits (or road classifications) for the country/ies you're interested in.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Mar '18, 09:03</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-62726" class="comments-container">
&#10;</div>
<div id="comment-tools-62726" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62726-form-container" class="comment-form-container">
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

