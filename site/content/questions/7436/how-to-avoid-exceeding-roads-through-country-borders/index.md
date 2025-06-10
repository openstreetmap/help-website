+++
type = "question"
title = "How to avoid exceeding roads through country borders ?"
description = '''Hi, I&#x27;ve made an extract of whole country using osmosis and *.poly file with border nodes coordinates. Is it possible to avoid exceeding roads which starts in extract country through country borders ?  I want those roads finished exactly at country border. Thanks for any advices..'''
date = "2011-08-30T11:00:00Z"
lastmod = "2011-08-30T11:13:00Z"
weight = 7436
keywords = [ "borders", "extract", "exceeding", "road" ]
aliases = [ "/questions/7436" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to avoid exceeding roads through country borders ?](/questions/7436/how-to-avoid-exceeding-roads-through-country-borders)

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
<span id="post-7436-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7436-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7436-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I've made an extract of whole country using osmosis and *.poly file with border nodes coordinates.</p>
<p>Is it possible to avoid exceeding roads which starts in extract country through country borders ? I want those roads finished exactly at country border.</p>
<p>Thanks for any advices..</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-borders" rel="tag" title="see questions tagged &#39;borders&#39;">borders</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-exceeding" rel="tag" title="see questions tagged &#39;exceeding&#39;">exceeding</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Aug '11, 11:00</strong></p>
<img src="https://secure.gravatar.com/avatar/e8343c2fdfd08fea47ea8a0dc5210607?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MrX1&#39;s gravatar image" />
<p><span>MrX1</span><br />
<span class="score" title="46 reputation points">46</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MrX1 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-7436" class="comments-container">
&#10;</div>
<div id="comment-tools-7436" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7436-form-container" class="comment-form-container">
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

<span id="7437"></span>

<div id="answer-container-7437" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7437-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7437-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7437-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No, this is not possible with Osmosis. It would require the creation of a pseudo node that sits on the intersection of the country border with the road, and Osmosis doesn't do that. I don't know of any program that does it, actually. You can load OSM data into PostgreSQL and then intersect each road with the country border; this will cut the roads in the way you want, but your geometries will then not be strictly based on OSM nodes any more.</p>
<p>If you use --clipIncompleteEntities=true then ways will stop at the last node before the border.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Aug '11, 11:13</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Aug '11, 12:19</strong> </span></p>
</div>
</div>
<div id="comments-container-7437" class="comments-container">
&#10;</div>
<div id="comment-tools-7437" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7437-form-container" class="comment-form-container">
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

