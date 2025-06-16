+++
type = "question"
title = "500 Server Error"
description = '''Is it just me or the api server doesn&#x27;t work? http://api.openstreetmap.org/api/0.6/map?bbox=51.2317,56.4149,51.3997,56.4891 It says 500 Server Error for me.'''
date = "2012-04-03T14:54:00Z"
lastmod = "2012-04-03T19:39:00Z"
weight = 11705
keywords = [ "bug" ]
aliases = [ "/questions/11705" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [500 Server Error](/questions/11705/500-server-error)

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
<span id="post-11705-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11705-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11705-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it just me or the api server doesn't work? <a href="http://api.openstreetmap.org/api/0.6/map?bbox=51.2317,56.4149,51.3997,56.4891">http://api.openstreetmap.org/api/0.6/map?bbox=51.2317,56.4149,51.3997,56.4891</a> It says 500 Server Error for me.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bug" rel="tag" title="see questions tagged &#39;bug&#39;">bug</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Apr '12, 14:54</strong></p>
<img src="https://secure.gravatar.com/avatar/c249eb1d6974d4346d12cfc26e07515b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dogsbollocks&#39;s gravatar image" />
<p><span>dogsbollocks</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dogsbollocks has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11705" class="comments-container">
&#10;</div>
<div id="comment-tools-11705" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11705-form-container" class="comment-form-container">
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

<span id="11709"></span>

<div id="answer-container-11709" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11709-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11709-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-11709-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dogsbollocks has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The database is currently being copyed to a new database server for better performence and to have a database to run the tests for the license change on. During this copying the database can not be altered in any way and is therefore in read-only state.</p>
<p>The map call is creating temperary tables in the database while retreaving the data and have to be turned off during the copy. This is not a big problem because you can not upload any data, so there is little reason to download any data from that call. It is better to let mappers that don't visit the front page discover that something is wrong before working on the data and try to upload it.</p>
<p>If you want data you can download <a href="https://wiki.openstreetmap.org/wiki/Planet.osm">extracts</a> or try a <a href="https://wiki.openstreetmap.org/wiki/Xapi">xapi</a> instance.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Apr '12, 17:19</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-11709" class="comments-container">
&#10;</div>
<div id="comment-tools-11709" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11709-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11708"></span>

<div id="answer-container-11708" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11708-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11708-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-11708-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Currently the database is being upgraded, then there's going to be work done on the data to remove things that don't comply with the new ODbL license. More info: <a href="http://blog.osmfoundation.org/2012/03/27/service-schedule-march-april-2012/">http://blog.osmfoundation.org/2012/03/27/service-schedule-march-april-2012/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Apr '12, 16:09</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-11708" class="comments-container">
<span id="11710"></span>
<div id="comment-11710" class="comment">
<div id="post-11710-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, thank you guys.</p>
</div>
<div id="comment-11710-info" class="comment-info">
<span class="comment-age">(03 Apr '12, 19:39)</span> <span class="comment-user userinfo">dogsbollocks</span>
</div>
</div>
</div>
<div id="comment-tools-11708" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11708-form-container" class="comment-form-container">
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

