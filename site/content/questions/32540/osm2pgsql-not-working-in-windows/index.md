+++
type = "question"
title = "osm2pgsql not working in windows"
description = '''Hi, I have just downloaded osm2pgsql for Windows and I am trying to execute: osm2pgsql -s -U postgres -d gisdb C:&#92;Users&#92;MyUser&#92;Documents&#92;data.osm  However, I am gettint this error: osm2pgsql SVN version 0.83.0 (64bit id space)  Error: Connection to database failed: could not connect to server: No su...'''
date = "2014-04-22T22:39:00Z"
lastmod = "2014-04-23T12:00:00Z"
weight = 32540
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/32540" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [osm2pgsql not working in windows](/questions/32540/osm2pgsql-not-working-in-windows)

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
<span id="post-32540-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32540-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32540-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I have just downloaded osm2pgsql for Windows and I am trying to execute:</p>
<pre><code>osm2pgsql -s -U postgres -d gisdb C:\Users\MyUser\Documents\data.osm</code></pre>
<p>However, I am gettint this error:</p>
<pre><code>osm2pgsql SVN version 0.83.0 (64bit id space)
&#10;Error: Connection to database failed: could not connect to server: No such file or directory
&#10;  Is the server running locally and accepting connections on Unix domain socket &quot;/tmp/.sPGSQL.5432&quot;?</code></pre>
<p>What is the problem?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Apr '14, 22:39</strong></p>
<img src="https://secure.gravatar.com/avatar/dc4468fcb31a40c6ac8b6aca5a0b33c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AnderOSM&#39;s gravatar image" />
<p><span>AnderOSM</span><br />
<span class="score" title="71 reputation points">71</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AnderOSM has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-32540" class="comments-container">
&#10;</div>
<div id="comment-tools-32540" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32540-form-container" class="comment-form-container">
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

<span id="32543"></span>

<div id="answer-container-32543" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32543-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32543-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-32543-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="AnderOSM has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try the additional options <code>--port 5432</code> and <code>--host localhost</code> to force osm2pgsql to make a TCP connection instead of using the Unix Domain Socket.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Apr '14, 23:38</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-32543" class="comments-container">
<span id="32559"></span>
<div id="comment-32559" class="comment">
<div id="post-32559-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I also needed -W so that the command line asks for my database user's password.</p>
</div>
<div id="comment-32559-info" class="comment-info">
<span class="comment-age">(23 Apr '14, 12:00)</span> <span class="comment-user userinfo">AnderOSM</span>
</div>
</div>
</div>
<div id="comment-tools-32543" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32543-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="32541"></span>

<div id="answer-container-32541" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32541-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32541-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32541-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Are you sure your postgres server is running ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Apr '14, 23:31</strong></p>
<img src="https://secure.gravatar.com/avatar/de5e2187d1e002fc2aa5d8aa59729e1e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="exxos&#39;s gravatar image" />
<p><span>exxos</span><br />
<span class="score" title="81 reputation points">81</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="exxos has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-32541" class="comments-container">
&#10;</div>
<div id="comment-tools-32541" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32541-form-container" class="comment-form-container">
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

