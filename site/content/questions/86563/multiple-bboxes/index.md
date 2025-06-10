+++
type = "question"
title = "Multiple BBoxes"
description = '''I want to make 1 query which would look over multiple BBoxes. How would I achieve this? My current code is: [out:json];  way[highway][highway~&quot;(primary|secondary|tertiary|unclassified)&quot;](50.89377370152463,-2.5791936347428144,50.93869042414434,-2.488528471457792);node(w);  out center; '''
date = "2023-01-24T20:07:00Z"
lastmod = "2023-01-27T10:11:00Z"
weight = 86563
keywords = [ "overpass", "bbox" ]
aliases = [ "/questions/86563" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Multiple BBoxes](/questions/86563/multiple-bboxes)

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
<span id="post-86563-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86563-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86563-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to make 1 query which would look over multiple BBoxes. How would I achieve this?</p>
<p>My current code is:</p>
<pre><code>[out:json];
&#10;way[highway][highway~&quot;(primary|secondary|tertiary|unclassified)&quot;](50.89377370152463,-2.5791936347428144,50.93869042414434,-2.488528471457792);node(w);
&#10;out center;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-bbox" rel="tag" title="see questions tagged &#39;bbox&#39;">bbox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jan '23, 20:07</strong></p>
<img src="https://secure.gravatar.com/avatar/f5e1c09b7a9ffbc384f9d586c90f89a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ogisha&#39;s gravatar image" />
<p><span>Ogisha</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ogisha has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jan '23, 07:23</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-86563" class="comments-container">
&#10;</div>
<div id="comment-tools-86563" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86563-form-container" class="comment-form-container">
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

<span id="86573"></span>

<div id="answer-container-86573" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86573-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86573-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86573-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello.</p>
<p>The union operator <code>()</code> will help.</p>
<p>This is an <a href="https://overpass-turbo.eu/s/1qEg">example</a> with two bounding boxes.</p>
<p>Side note, if you want the ways as well as the nodes, you need to nest unions, like <a href="https://overpass-turbo.eu/s/1qEh">here</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jan '23, 10:11</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-86573" class="comments-container">
&#10;</div>
<div id="comment-tools-86573" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86573-form-container" class="comment-form-container">
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

