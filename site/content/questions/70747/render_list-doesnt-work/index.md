+++
type = "question"
title = "render_list doesnt work"
description = '''I&#x27;m running pre-render for ajt style map render_list -all --socket /var/run/renderd/renderd.sock -z 1 -Z 1 -n 15  I can see this in the syslog: renderd[35121]: DEBUG: Got incoming connection, fd 7, number 1 renderd[35121]: DEBUG: Got incoming connection, fd 9, number 2 renderd[35121]: DEBUG: Got inc...'''
date = "2019-09-12T13:06:00Z"
lastmod = "2019-09-12T16:36:00Z"
weight = 70747
keywords = [ "rendering" ]
aliases = [ "/questions/70747" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [render_list doesnt work](/questions/70747/render_list-doesnt-work)

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
<span id="post-70747-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70747-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70747-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm running pre-render for ajt style map</p>
<pre><code>render_list -all --socket /var/run/renderd/renderd.sock -z 1 -Z 1 -n 15</code></pre>
<p>I can see this in the syslog:</p>
<pre><code>renderd[35121]: DEBUG: Got incoming connection, fd 7, number 1
renderd[35121]: DEBUG: Got incoming connection, fd 9, number 2
renderd[35121]: DEBUG: Got incoming connection, fd 10, number 3
renderd[35121]: DEBUG: Got incoming connection, fd 11, number 4
renderd[35121]: DEBUG: Got incoming connection, fd 12, number 5
renderd[35121]: DEBUG: Got incoming connection, fd 13, number 6
renderd[35121]: DEBUG: Got incoming connection, fd 17, number 7
renderd[35121]: DEBUG: Got incoming connection, fd 18, number 8
renderd[35121]: DEBUG: Got incoming connection, fd 19, number 9
renderd[35121]: DEBUG: Got incoming connection, fd 20, number 10
renderd[35121]: DEBUG: Got incoming connection, fd 21, number 11
renderd[35121]: DEBUG: Got incoming connection, fd 22, number 12
renderd[35121]: DEBUG: Got incoming connection, fd 23, number 13
renderd[35121]: DEBUG: Got incoming connection, fd 24, number 14
renderd[35121]: DEBUG: Got incoming connection, fd 25, number 15</code></pre>
<p>But when looking on <code>syslog</code> and <code>htop</code> and even <code>iotop</code> it looks like the machine is doing nothing</p>
<p>What am I missing?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Sep '19, 13:06</strong></p>
<img src="https://secure.gravatar.com/avatar/47110f56c594a7515b757d9975b9a8c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LiorM&#39;s gravatar image" />
<p><span>LiorM</span><br />
<span class="score" title="31 reputation points">31</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LiorM has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Sep '19, 14:02</strong> </span></p>
</div>
</div>
<div id="comments-container-70747" class="comments-container">
&#10;</div>
<div id="comment-tools-70747" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70747-form-container" class="comment-form-container">
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

<span id="70753"></span>

<div id="answer-container-70753" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70753-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70753-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70753-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>it seems that providing the socket fixed it:</p>
<pre><code>render_list -all --socket=/var/run/renderd/renderd.sock -z 1 -Z 1 -n 15</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Sep '19, 16:04</strong></p>
<img src="https://secure.gravatar.com/avatar/47110f56c594a7515b757d9975b9a8c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LiorM&#39;s gravatar image" />
<p><span>LiorM</span><br />
<span class="score" title="31 reputation points">31</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LiorM has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70753" class="comments-container">
<span id="70754"></span>
<div id="comment-70754" class="comment">
<div id="post-70754-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"-s /var/run/renderd/renderd.sock" would also have worked - there are two ways of specifying the options I think.</p>
</div>
<div id="comment-70754-info" class="comment-info">
<span class="comment-age">(12 Sep '19, 16:36)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-70753" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70753-form-container" class="comment-form-container">
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

