+++
type = "question"
title = "Missing Nodes after extraction using osmosis."
description = '''I have extracted a small area of Welwyn Garden City using osmosis bounding box. When I analyse the data using my program, (or JOSM) it reports some nodes are missing, about 11,000 out of 250,000. This may/will be over-estimated due to several ways sharing nodes. Are these nodes outside the bounding ...'''
date = "2019-06-13T12:23:00Z"
lastmod = "2019-06-14T07:04:00Z"
weight = 69613
keywords = [ "nodes", "way", "missing" ]
aliases = [ "/questions/69613" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Missing Nodes after extraction using osmosis.](/questions/69613/missing-nodes-after-extraction-using-osmosis)

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
<span id="post-69613-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69613-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69613-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have extracted a small area of Welwyn Garden City using osmosis bounding box. When I analyse the data using my program, (or JOSM) it reports some nodes are missing, about 11,000 out of 250,000. This may/will be over-estimated due to several ways sharing nodes. Are these nodes outside the bounding box? Is this 'ok'. Is it something you have to 'cope with'. Thanks Mike</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jun '19, 12:23</strong></p>
<img src="https://secure.gravatar.com/avatar/ad5de24a5107cfe177b2c9c73b13c29f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20Begesford&#39;s gravatar image" />
<p><span>Mike Begesford</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike Begesford has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69613" class="comments-container">
&#10;</div>
<div id="comment-tools-69613" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69613-form-container" class="comment-form-container">
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

<span id="69618"></span>

<div id="answer-container-69618" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69618-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69618-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69618-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should likely be setting "completeWays" https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.47#Area_Filtering_Tasks when extracting, and perhaps even the equivalent setting for relations.</p>
<p>While editing apps can in general handle referentially incomplete relation data, doing the same with ways, resp. way nodes is not a good idea (maybe JOSM does something reasonable, but I wouldn't count on it)..</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jun '19, 07:04</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-69618" class="comments-container">
&#10;</div>
<div id="comment-tools-69618" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69618-form-container" class="comment-form-container">
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

