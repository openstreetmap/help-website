+++
type = "question"
title = "Key:prow_ref - how to manage preset values?"
description = '''I am tagging Public Rights of Way in Essex using iD Editor, using the key:prow_ref When I start to type in an associated value, I type in a few letters and am prompted with the name of a Parish. Sometimes, the Parish name I am typing is recognised, and I don&#x27;t habe to type in the remaining letters. ...'''
date = "2019-07-31T22:08:00Z"
lastmod = "2019-08-02T17:28:00Z"
weight = 70265
keywords = [ "tags" ]
aliases = [ "/questions/70265" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Key:prow_ref - how to manage preset values?](/questions/70265/keyprow_ref-how-to-manage-preset-values)

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
<span id="post-70265-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70265-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70265-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am tagging Public Rights of Way in Essex using iD Editor, using the key:prow_ref</p>
<p>When I start to type in an associated value, I type in a few letters and am prompted with the name of a Parish.</p>
<p>Sometimes, the Parish name I am typing is recognised, and I don't habe to type in the remaining letters.</p>
<p>Sometimes it isn't, which means I have to type in the entire Parish name.</p>
<p>So my question is, what controls the names of the Parishes offered to me?</p>
<p>Or to put the question another way, how can I add Beaumont Cum Moze FP 3 to the prompt list?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Jul '19, 22:08</strong></p>
<img src="https://secure.gravatar.com/avatar/469bf85c2e48ad6395d931ff7e805b4c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="IanG&#39;s gravatar image" />
<p><span>IanG</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="IanG has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70265" class="comments-container">
&#10;</div>
<div id="comment-tools-70265" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70265-form-container" class="comment-form-container">
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

<span id="70300"></span>

<div id="answer-container-70300" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70300-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70300-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70300-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The discussion on <a href="https://github.com/openstreetmap/iD/issues/6441">this</a> issue on the iD gitub repository indicates that autocomplete for the general tag editor uses taginfo to provide tags already in use.</p>
<p>The values tab for the <a href="https://taginfo.openstreetmap.org/keys/prow_ref#values"><code>prow_ref</code></a> key gives this list when filtered for 'Beaumont':</p>
<ul>
<li><code>Beaumont␣Cum␣Moze␣FP␣8</code></li>
<li><code>Beaumont␣Cum␣Moze␣FP␣15</code></li>
<li><code>Beaumont␣Cum␣Moze␣FP␣26</code></li>
<li><code>Beaumont␣Cum␣Moze␣FP␣10</code></li>
<li><code>Beaumont␣Cum␣Moze␣FP␣19</code></li>
</ul>
<p><em>If</em> they are using the main taginfo instance the suggestion for your parish should appear in the next daily update after your first example is saved to OSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Aug '19, 17:28</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-70300" class="comments-container">
&#10;</div>
<div id="comment-tools-70300" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70300-form-container" class="comment-form-container">
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

