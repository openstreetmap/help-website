+++
type = "question"
title = "How to get OSM history from beginning of times"
description = '''Is it possible to get OSM history from the very first changeset (even better for specific territory)? I checked planet minute diffs and they seems to be starting from 2012 (https://planet.openstreetmap.org/replication/minute/000/000/001.state.txt). I also tried adiff from overpass and it works, but ...'''
date = "2018-08-30T21:12:00Z"
lastmod = "2018-08-31T07:58:00Z"
weight = 65652
keywords = [ "diff", "data", "history" ]
aliases = [ "/questions/65652" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to get OSM history from beginning of times](/questions/65652/how-to-get-osm-history-from-beginning-of-times)

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
<span id="post-65652-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65652-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65652-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible to get OSM history from the very first changeset (even better for specific territory)? I checked planet minute diffs and they seems to be starting from 2012 (<a href="https://planet.openstreetmap.org/replication/minute/000/000/001.state.txt).">https://planet.openstreetmap.org/replication/minute/000/000/001.state.txt).</a></p>
<p>I also tried adiff from overpass and it works, but it usually hangs and cannot effectively process even rather small territory.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-diff" rel="tag" title="see questions tagged &#39;diff&#39;">diff</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-history" rel="tag" title="see questions tagged &#39;history&#39;">history</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Aug '18, 21:12</strong></p>
<img src="https://secure.gravatar.com/avatar/7beec6d85fed7bf5255d6657d7609ad0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sergey%20Karavay&#39;s gravatar image" />
<p><span>Sergey Karavay</span><br />
<span class="score" title="539 reputation points">539</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sergey Karavay has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65652" class="comments-container">
&#10;</div>
<div id="comment-tools-65652" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65652-form-container" class="comment-form-container">
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

<span id="65656"></span>

<div id="answer-container-65656" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65656-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65656-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-65656-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Sergey Karavay has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well if your specific territory is not England then the earth will be void and without form ;)</p>
<p>Your best bet is downloading the "full history" file from planet.openstreetmap.org (also available per-contry on download.geofabrik.de) and decoding that. It will contain historic versions of data.</p>
<p>There's a couple things that you should know:</p>
<ul>
<li>The current API version is 0.6 which was introduced in April of 2009. Before that, OSM did not <em>have</em> changesets. Hence, changesets for earlier edits are made up by automatically grouping edits made by the same user.</li>
<li>API 0.5 was introduced in October 2007. This was when we started using relations, and ways were composed of nodes; before API 0.5, there was another data type called segment (each segment connecting 2 nodes), and ways were built from segments. You will find some nodes older than October 2007 in the history planet but not segments or ways; you can download old planet files that still have segments but processing them is difficult.</li>
<li>In September 2012 we changed the license to ODbL. This meant we had to remove all old contributions that weren't released by their authors under this new license. Since these objects have been "redacted" i.e. removed from the history file, you cannot get an accurate picture of pre-September 2012 data from a current history file; you'd have to go back to the CC-BY-SA files also available on planet.openstreetmap.org - but it is difficult legally to combine CC-BY-SA and ODbL data in one work since this can easily lead to a requirement of publishing the result under CC-BY-SA <em>only</em> and under ODbL <em>only</em>.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Aug '18, 21:59</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Aug '18, 22:13</strong> </span></p>
</div>
</div>
<div id="comments-container-65656" class="comments-container">
<span id="65658"></span>
<div id="comment-65658" class="comment">
<div id="post-65658-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Aha, so this is why Planet OSM diffs starts in 2012? Thanks.</p>
</div>
<div id="comment-65658-info" class="comment-info">
<span class="comment-age">(31 Aug '18, 07:58)</span> <span class="comment-user userinfo">Sergey Karavay</span>
</div>
</div>
</div>
<div id="comment-tools-65656" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65656-form-container" class="comment-form-container">
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

