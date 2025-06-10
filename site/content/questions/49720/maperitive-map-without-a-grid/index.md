+++
type = "question"
title = "Maperitive: map without a grid"
description = '''Exporting from Maperitive by export-svg or export-bitmap makes a picture WITH the grid which is difficult to delete. For example, the svg file contains the grid not as a separate layer, but it is drawn as a border of every tile. How can I generate a map WITHOUT the grid? I want to draw the grid by m...'''
date = "2016-05-17T21:52:00Z"
lastmod = "2017-04-12T08:11:00Z"
weight = 49720
keywords = [ "grid", "export", "maperitive" ]
aliases = [ "/questions/49720" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Maperitive: map without a grid](/questions/49720/maperitive-map-without-a-grid)

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
<span id="post-49720-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49720-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-49720-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Exporting from Maperitive by <code>export-svg</code> or <code>export-bitmap</code> makes a picture WITH the grid which is difficult to delete.</p>
<p>For example, the <code>svg</code> file contains the grid not as a separate layer, but it is drawn as a border of every tile.</p>
<p>How can I generate a map WITHOUT the grid? I want to draw the grid by myself later.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-grid" rel="tag" title="see questions tagged &#39;grid&#39;">grid</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-maperitive" rel="tag" title="see questions tagged &#39;maperitive&#39;">maperitive</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 May '16, 21:52</strong></p>
<img src="https://secure.gravatar.com/avatar/6cf5f23ff9e96e3379c1b0b2634e99da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pantlmn&#39;s gravatar image" />
<p><span>Pantlmn</span><br />
<span class="score" title="91 reputation points">91</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pantlmn has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49720" class="comments-container">
&#10;</div>
<div id="comment-tools-49720" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49720-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="49721"></span>

<div id="answer-container-49721" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49721-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49721-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-49721-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sorry, I found it out by myself.</p>
<p>Tiny script</p>
<pre><code>from maperipy import Map
Map.grid_visible=0</code></pre>
<p>Save it as <code>no-grid.py</code></p>
<p>Run in Maperitive:</p>
<pre><code>run-script [[your-path-here]]\no-grid.py</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 May '16, 23:23</strong></p>
<img src="https://secure.gravatar.com/avatar/6cf5f23ff9e96e3379c1b0b2634e99da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pantlmn&#39;s gravatar image" />
<p><span>Pantlmn</span><br />
<span class="score" title="91 reputation points">91</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pantlmn has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49721" class="comments-container">
&#10;</div>
<div id="comment-tools-49721" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49721-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55576"></span>

<div id="answer-container-55576" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55576-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55576-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55576-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>set-setting name=map.decoration.grid value=false eingeben oder ins Maperitive Script eintragen!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '17, 08:11</strong></p>
<img src="https://secure.gravatar.com/avatar/b315e73dee231d557adcada6fb5b8821?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="steyregg&#39;s gravatar image" />
<p><span>steyregg</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="steyregg has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55576" class="comments-container">
&#10;</div>
<div id="comment-tools-55576" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55576-form-container" class="comment-form-container">
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

