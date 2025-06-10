+++
type = "question"
title = "Operators in Overpass Turbo"
description = '''I worked with MapInfo Professional and was used to operators such as Contains, Intersects, Not and Within in its SQL. Can these be used in Overpass Turbo Wizard? I do not have the knowledge to construct a query in its own language.'''
date = "2017-10-13T22:22:00Z"
lastmod = "2017-10-14T00:09:00Z"
weight = 60115
keywords = [ "overpass", "query" ]
aliases = [ "/questions/60115" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Operators in Overpass Turbo](/questions/60115/operators-in-overpass-turbo)

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
<span id="post-60115-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60115-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60115-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I worked with MapInfo Professional and was used to operators such as Contains, Intersects, Not and Within in its SQL. Can these be used in Overpass Turbo Wizard? I do not have the knowledge to construct a query in its own language.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Oct '17, 22:22</strong></p>
<img src="https://secure.gravatar.com/avatar/ffcc41f13929627742b4936ec178c6f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="silver%20mapper&#39;s gravatar image" />
<p><span>silver mapper</span><br />
<span class="score" title="256 reputation points">256</span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="27 badges"><span class="silver">●</span><span class="badgecount">27</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="silver mapper has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60115" class="comments-container">
&#10;</div>
<div id="comment-tools-60115" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60115-form-container" class="comment-form-container">
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

<span id="60116"></span>

<div id="answer-container-60116" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60116-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60116-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60116-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Overpass API itself is mostly focused on tags. <code>is_in</code>, <code>around</code> and <code>area</code> filters can be used to do some geometric operations. Around can be used to find intersections, by using a distance of 0.</p>
<p>For the Wizard, the primary operation that is available is something like <code>in Wisconsin</code>, which can be used to restrict the query to within some special areas that Overpass API generates (mostly geographic boundaries, but also some named area features). Use quotes if the name has spaces, like <code>in "Green Bay, Wisconsin"</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Oct '17, 00:09</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-60116" class="comments-container">
&#10;</div>
<div id="comment-tools-60116" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60116-form-container" class="comment-form-container">
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

