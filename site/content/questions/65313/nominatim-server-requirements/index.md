+++
type = "question"
title = "Nominatim server requirements ?"
description = '''Hi, I am installing Nominatim in a dedicated server, will it be able to handle calls about 20-30 per second. It will be of only single country having data of about 1gb. server that will be used:- e3 1275v6 Ram - 64GB Hard Disk - 2x480GB Nvme software raid 1 Thanks'''
date = "2018-08-14T02:49:00Z"
lastmod = "2018-08-14T11:48:00Z"
weight = 65313
keywords = [ "nominatim" ]
aliases = [ "/questions/65313" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim server requirements ?](/questions/65313/nominatim-server-requirements)

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
<span id="post-65313-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65313-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65313-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am installing Nominatim in a dedicated server, will it be able to handle calls about 20-30 per second. It will be of only single country having data of about 1gb.</p>
<p>server that will be used:- e3 1275v6 Ram - 64GB Hard Disk - 2x480GB Nvme software raid 1</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Aug '18, 02:49</strong></p>
<img src="https://secure.gravatar.com/avatar/2463811d231d70c616bd07bdc0067395?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arj123&#39;s gravatar image" />
<p><span>arj123</span><br />
<span class="score" title="46 reputation points">46</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arj123 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65313" class="comments-container">
&#10;</div>
<div id="comment-tools-65313" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65313-form-container" class="comment-form-container">
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

<span id="65321"></span>

<div id="answer-container-65321" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65321-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65321-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65321-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, that's plenty.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Aug '18, 10:42</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-65321" class="comments-container">
<span id="65325"></span>
<div id="comment-65325" class="comment">
<div id="post-65325-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the reply, can you say, what will be this servers up limit of concurrent connections for nominatim.</p>
</div>
<div id="comment-65325-info" class="comment-info">
<span class="comment-age">(14 Aug '18, 11:39)</span> <span class="comment-user userinfo">arj123</span>
</div>
</div>
<span id="65326"></span>
<div id="comment-65326" class="comment">
<div id="post-65326-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Impossible to tell. Reverse search is less complex (less table indices to look at) than forward search, long queries (many address components) take a bit longer than single word queries. Depends how much of the database the operating system caches in RAM (in your case it could be all of it), how often the data gets updated (daily, hourly, minutely), if you switch off logging (less database writes).</p>
</div>
<div id="comment-65326-info" class="comment-info">
<span class="comment-age">(14 Aug '18, 11:45)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="65327"></span>
<div id="comment-65327" class="comment">
<div id="post-65327-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The data will be update manually about once a month.</p>
</div>
<div id="comment-65327-info" class="comment-info">
<span class="comment-age">(14 Aug '18, 11:48)</span> <span class="comment-user userinfo">arj123</span>
</div>
</div>
</div>
<div id="comment-tools-65321" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65321-form-container" class="comment-form-container">
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

