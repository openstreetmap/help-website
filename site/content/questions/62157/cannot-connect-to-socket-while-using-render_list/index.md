+++
type = "question"
title = "Cannot connect to socket while using render_list"
description = '''Hi all,  I was trying prerender some tiles using the render_list command. But it is showing the following error:  socket connect failed for: /var/run/renderd/renderd.sock &quot;renderd&quot; directory has the right permission to create and connect to the socket. But I am not sure why is not working. Please he...'''
date = "2018-02-16T21:37:00Z"
lastmod = "2018-03-08T10:51:00Z"
weight = 62157
keywords = [ "render_list", "rendering", "renderd", "socket", "mod_tile" ]
aliases = [ "/questions/62157" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot connect to socket while using render_list](/questions/62157/cannot-connect-to-socket-while-using-render_list)

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
<span id="post-62157-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62157-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62157-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all, I was trying prerender some tiles using the render_list command. But it is showing the following error:</p>
<p>socket connect failed for: /var/run/renderd/renderd.sock</p>
<p>"renderd" directory has the right permission to create and connect to the socket. But I am not sure why is not working. Please help me to find out the reason. <img src="/upfiles/render_list.PNG" alt="alt text" /></p>
<p>Thanks SJP</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-render_list" rel="tag" title="see questions tagged &#39;render_list&#39;">render_list</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-socket" rel="tag" title="see questions tagged &#39;socket&#39;">socket</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Feb '18, 21:37</strong></p>
<img src="https://secure.gravatar.com/avatar/95e9674b7a67d58ada813e0c6bc38d84?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="subinjp7&#39;s gravatar image" />
<p><span>subinjp7</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="subinjp7 has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-62157" class="comments-container">
<span id="62161"></span>
<div id="comment-62161" class="comment">
<div id="post-62161-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Silly question - do /var/run/renderd and /var/run/renderd/renderd.sock exist? In <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a> you have to manually create /var/run/renderd the first time around. If you haven't set things up to create it at startup it won't exist.</p>
</div>
<div id="comment-62161-info" class="comment-info">
<span class="comment-age">(16 Feb '18, 22:39)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="62164"></span>
<div id="comment-62164" class="comment">
<div id="post-62164-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have already done that. And renderd folder has right permission also to create socket and connect to it. But I am not sure what is supposed to be inside renderd.sock file. When I open it with vim editor, it shows an empty file with a warning permission denied.</p>
</div>
<div id="comment-62164-info" class="comment-info">
<span class="comment-age">(16 Feb '18, 23:15)</span> <span class="comment-user userinfo">subinjp7</span>
</div>
</div>
</div>
<div id="comment-tools-62157" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62157-form-container" class="comment-form-container">
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

<span id="62575"></span>

<div id="answer-container-62575" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62575-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62575-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62575-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This appears to be essentially a duplicate of <a href="/questions/62113/not-getting-output-from-tileserver-when-i-reduce-the-aws-rds-memory-size-to-16gb">this question</a>. You're trying to use a cloud service for something it's not really designed for.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Mar '18, 10:51</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-62575" class="comments-container">
&#10;</div>
<div id="comment-tools-62575" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62575-form-container" class="comment-form-container">
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

