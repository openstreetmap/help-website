+++
type = "question"
title = "Tagging a conditionally oneway road"
description = '''How would I tag a road that&#x27;s conditionally one-way? It&#x27;s the exit road for a parking lot that doubles as a residential street. If you live along that street, or are making a delivery to a residence there, it&#x27;s a two-way road. For everyone else, it&#x27;s one-way. I&#x27;ve found how to tag one-wayness based ...'''
date = "2016-05-09T08:29:00Z"
lastmod = "2016-05-09T12:13:00Z"
weight = 49629
keywords = [ "tagging", "oneway" ]
aliases = [ "/questions/49629" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Tagging a conditionally oneway road](/questions/49629/tagging-a-conditionally-oneway-road)

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
<span id="post-49629-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49629-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-49629-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How would I tag a road that's conditionally one-way? It's the exit road for a parking lot that doubles as a residential street. If you live along that street, or are making a delivery to a residence there, it's a two-way road. For everyone else, it's one-way.</p>
<p>I've found how to tag one-wayness based on what sort of vehicle is involved (eg. two-way for bicycles, but one-way for motor vehicles), but not how to tag it for what you're doing.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-oneway" rel="tag" title="see questions tagged &#39;oneway&#39;">oneway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 May '16, 08:29</strong></p>
<img src="https://secure.gravatar.com/avatar/313c7f1fb7839c95ba6bb396791f56f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Carnildo&#39;s gravatar image" />
<p><span>Carnildo</span><br />
<span class="score" title="831 reputation points">831</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Carnildo has 2 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-49629" class="comments-container">
&#10;</div>
<div id="comment-tools-49629" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49629-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="49632"></span>

<div id="answer-container-49632" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49632-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49632-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-49632-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Carnildo has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would add the common case with "oneway=yes" and the special case using <a href="https://wiki.openstreetmap.org/wiki/Conditional_restrictions">conditional restrictions</a> with "oneway:conditional=no @ destination". As of today, "oneway:conditional=no @ destination" has already been <a href="https://taginfo.openstreetmap.org/tags/oneway%3Aconditional=no%20%40%20destination">used 44 times</a>.</p>
<p>It also covers the <em>delivery</em> case in my opinion.</p>
<p><del>Not sure how to specify multiple conditions. I would expect "oneway:conditional=no @ (destination OR delivery)" but conditional restrictions only specify operator AND but not operator OR.</del></p>
<p>For specifying multiple conditions, the conditional restrictions page allows to use a semicolon (;). So tagging the special case using "oneway:conditional=no @ destination; no @ delivery" is also an option. But as stated before, <em>destination</em> also includes <em>delivery</em> in my opinion.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 May '16, 12:13</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 May '16, 12:28</strong> </span></p>
</div>
</div>
<div id="comments-container-49632" class="comments-container">
&#10;</div>
<div id="comment-tools-49632" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49632-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="49630"></span>

<div id="answer-container-49630" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49630-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49630-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49630-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Carnildo, just tag it as a one way street and make explicit tags for the group that allowed going reversed or the opposite direction, see these pages like <a href="https://wiki.openstreetmap.org/wiki/Key:access">https://wiki.openstreetmap.org/wiki/Key:access</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 May '16, 10:02</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-49630" class="comments-container">
&#10;</div>
<div id="comment-tools-49630" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49630-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="49631"></span>

<div id="answer-container-49631" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49631-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49631-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49631-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Perhaps you need the <code>:forward</code> and <code>:backward</code> suffixes for the <a href="https://wiki.openstreetmap.org/wiki/Key:access#One-way_restrictions">access tag</a>? How about <code>access:forward=yes</code> <code>access:backwards=destination</code> to say "You can drive forwards along this way, but you can go backwards only if this is your destination". Change <code>:forward</code>/<code>:backwards</code> as appropriate. However, rather than the generic <code>access</code> tag, you should use something more accurate, like <code>vehicle:forwards=yes vehicle:backwards=destination</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 May '16, 10:10</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 May '16, 10:12</strong> </span></p>
</div>
</div>
<div id="comments-container-49631" class="comments-container">
&#10;</div>
<div id="comment-tools-49631" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49631-form-container" class="comment-form-container">
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

