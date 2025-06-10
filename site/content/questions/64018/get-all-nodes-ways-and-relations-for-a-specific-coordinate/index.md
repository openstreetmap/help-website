+++
type = "question"
title = "Get all nodes, ways and relations for a specific coordinate"
description = '''Hello everybody, I want to get all nodes, ways and relations for a specific coordinate for an example: 49.1259340,9.2101538  [out:json]; node(around:5, 49.1259340,9.2101538); &amp;gt;; way(around:5, 49.1259340,9.2101538); &amp;gt;; relation(around:5, 49.1259340,9.2101538); out;  I tried several approaches b...'''
date = "2018-06-04T12:57:00Z"
lastmod = "2018-06-04T15:13:00Z"
weight = 64018
keywords = [ "overpass", "overpass-turbo" ]
aliases = [ "/questions/64018" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get all nodes, ways and relations for a specific coordinate](/questions/64018/get-all-nodes-ways-and-relations-for-a-specific-coordinate)

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
<span id="post-64018-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64018-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64018-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everybody,</p>
<p>I want to get all nodes, ways and relations for a specific coordinate for an example: 49.1259340,9.2101538</p>
<pre><code>[out:json];
node(around:5, 49.1259340,9.2101538);
&gt;;
way(around:5, 49.1259340,9.2101538);
&gt;;
relation(around:5, 49.1259340,9.2101538);
out;</code></pre>
<p>I tried several approaches but none worked. Help is much appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jun '18, 12:57</strong></p>
<img src="https://secure.gravatar.com/avatar/dbcc94f4176dd0d253bf83871344cbff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gustav9999&#39;s gravatar image" />
<p><span>Gustav9999</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gustav9999 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jun '18, 14:09</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/15d45a99f101e06c9e79916af33f8336?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Privatemajory&#39;s gravatar image" />
<p><span>Privatemajory</span><br />
<span class="score" title="1125 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span></p>
</div>
</div>
<div id="comments-container-64018" class="comments-container">
&#10;</div>
<div id="comment-tools-64018" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64018-form-container" class="comment-form-container">
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

<span id="64020"></span>

<div id="answer-container-64020" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64020-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64020-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64020-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I found myself the solution:</p>
<pre><code>[out:json];
node(around:10,49.1259340,9.2101538);
&lt;;
out geom;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jun '18, 15:13</strong></p>
<img src="https://secure.gravatar.com/avatar/dbcc94f4176dd0d253bf83871344cbff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gustav9999&#39;s gravatar image" />
<p><span>Gustav9999</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gustav9999 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64020" class="comments-container">
&#10;</div>
<div id="comment-tools-64020" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64020-form-container" class="comment-form-container">
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

