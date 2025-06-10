+++
type = "question"
title = "append OSM file to existing OSRM"
description = '''I did install and configure OSRM ( Open Street Map Routing Machine ) on my local server with a little osm file. Also i did install rails-port and i&#x27;m be able to change local map and save changes as OSM file with that. Is possible to append little OSM files to OSRM and change existing info?'''
date = "2018-05-28T18:59:00Z"
lastmod = "2018-05-29T08:52:00Z"
weight = 63818
keywords = [ "osrm" ]
aliases = [ "/questions/63818" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [append OSM file to existing OSRM](/questions/63818/append-osm-file-to-existing-osrm)

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
<span id="post-63818-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63818-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63818-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I did install and configure OSRM ( Open Street Map Routing Machine ) on my local server with a little <code>osm</code> file. Also i did install <code>rails-port</code> and i'm be able to change local map and save changes as OSM file with that. Is possible to append little OSM files to <code>OSRM</code> and change existing info?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 May '18, 18:59</strong></p>
<img src="https://secure.gravatar.com/avatar/976e165a9bd4b1aaf035f790545a0776?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cybercoder&#39;s gravatar image" />
<p><span>cybercoder</span><br />
<span class="score" title="36 reputation points">36</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cybercoder has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63818" class="comments-container">
&#10;</div>
<div id="comment-tools-63818" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63818-form-container" class="comment-form-container">
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

<span id="63820"></span>

<div id="answer-container-63820" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63820-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63820-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63820-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cybercoder has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No, OSRM can not update its database. You have to re-create it from scratch after every change.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 May '18, 20:10</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-63820" class="comments-container">
<span id="63833"></span>
<div id="comment-63833" class="comment">
<div id="post-63833-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thus, I need to export my local rails-port database to <code>osm</code> file and then re-extract and e-prepare with <code>osrm</code>. hmmm is it possible to export all rails-port database to a <code>osm</code> file?</p>
</div>
<div id="comment-63833-info" class="comment-info">
<span class="comment-age">(29 May '18, 08:52)</span> <span class="comment-user userinfo">cybercoder</span>
</div>
</div>
</div>
<div id="comment-tools-63820" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63820-form-container" class="comment-form-container">
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

