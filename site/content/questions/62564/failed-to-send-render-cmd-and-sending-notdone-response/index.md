+++
type = "question"
title = "Failed to send render cmd and Sending NotDone Response."
description = '''Hi all, I am trying to run rendered daemon and when I try to render multiple tiles at a time, it is showing error mentioned in the figure. I am using following configuration to run the Tileserver for whole world Map: Rendering Server: 16GB RAM with 2 CPUs Database Server: 16GB RAM with 2 CPUs I am n...'''
date = "2018-03-08T00:23:00Z"
lastmod = "2018-03-08T10:53:00Z"
weight = 62564
keywords = [ "openstreetmap", "rendering", "renderd", "mod_tile" ]
aliases = [ "/questions/62564" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Failed to send render cmd and Sending NotDone Response.](/questions/62564/failed-to-send-render-cmd-and-sending-notdone-response)

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
<span id="post-62564-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62564-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62564-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all, I am trying to run rendered daemon and when I try to render multiple tiles at a time, it is showing error mentioned in the figure.<img src="https://help.openstreetmap.org/upfiles/NotDone_Error.PNG" alt="alt text" /></p>
<p>I am using following configuration to run the Tileserver for whole world Map: Rendering Server: 16GB RAM with 2 CPUs Database Server: 16GB RAM with 2 CPUs</p>
<p>I am not sure what is this error about. Could somebody help me to figure out the problem? I pre-rendered tiles till zoom level 14. Thats why I thought of using servers with less number of CPUs and moderate memory.</p>
<p>Please let me know if you need any more details regarding the configuration or setup. Thanks in Advance Subin</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Mar '18, 00:23</strong></p>
<img src="https://secure.gravatar.com/avatar/95e9674b7a67d58ada813e0c6bc38d84?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="subinjp7&#39;s gravatar image" />
<p><span>subinjp7</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="subinjp7 has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-62564" class="comments-container">
<span id="62570"></span>
<div id="comment-62570" class="comment">
<div id="post-62570-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you post a bit more of the relevant log somewhere (as text, not just a picture)? Of particular interest would be what messages appear when you start or restart renderd.</p>
<p>Also - you say you have problems with rendering multiple tiles; can you render single tiles OK?</p>
</div>
<div id="comment-62570-info" class="comment-info">
<span class="comment-age">(08 Mar '18, 09:49)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="62571"></span>
<div id="comment-62571" class="comment">
<div id="post-62571-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your reply.</p>
<p>The following log details are the only relevant logs available from Rendering server.</p>
<p>DEBUG: Got Incoming connection, fd 12, number 1</p>
<p>DEBUG: Got incoming request with protocol version 2</p>
<p>DEBUG: Got command RenderLow fd(12) xml(ajt), z(18), x(137843), y(90010), mime(image/png), options()</p>
<p>DEBUG: Sending NotDone response(4)</p>
<p>DEBUG: Sending render cmd(1 ajt 18/137843/90010) with prpotocol version 2 to fd 12</p>
<p>WARNING: Failed to send render cmd on fd 12</p>
<p><strong>In the PostgreSQL server (using AWS RDS instance), I could see following logs</strong>:</p>
<p>LOG: Could not send data to client: connection timed out.</p>
<p>LOG: FATAL: Connection to client lost.</p>
<p>As I mentioned in my question, I am using database server with 16GB of memory with 2 CPUs.</p>
<p>Are those above logs occurred because of SQL query is taking too much time to complete and thus rendering server timedout the particular connection?</p>
<p>Thanks in Advance Subin</p>
</div>
<div id="comment-62571-info" class="comment-info">
<span class="comment-age">(08 Mar '18, 10:32)</span> <span class="comment-user userinfo">subinjp7</span>
</div>
</div>
<span id="62572"></span>
<div id="comment-62572" class="comment">
<div id="post-62572-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you give us a few more clues? I notice "AWS RDS" is mentioned there, but I frankly don't believe that these are the <em>only</em> logs available.</p>
<p>What I'm guessing is happening is that the disk on which the postgres database is stored is far far too slow. This was the answer given at <a href="https://help.openstreetmap.org/questions/62113/not-getting-output-from-tileserver-when-i-reduce-the-aws-rds-memory-size-to-16gb/62132">https://help.openstreetmap.org/questions/62113/not-getting-output-from-tileserver-when-i-reduce-the-aws-rds-memory-size-to-16gb/62132</a> and yet you still seem to be persisting with this configuration.</p>
<p>I'd suggest that you follow the advice that you've already been given ("For a world-wide database you must have your database on SSD, and ideally the database should be local to the rendering machine and not connected to over the network.").</p>
</div>
<div id="comment-62572-info" class="comment-info">
<span class="comment-age">(08 Mar '18, 10:45)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-62564" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62564-form-container" class="comment-form-container">
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

<span id="62577"></span>

<div id="answer-container-62577" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62577-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62577-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62577-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This appears to be essentially a duplicate of <a href="https://help.openstreetmap.org/questions/62113/not-getting-output-from-tileserver-when-i-reduce-the-aws-rds-memory-size-to-16gb">this question</a>. You're trying to use a cloud service for something it's not really designed for.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Mar '18, 10:53</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-62577" class="comments-container">
&#10;</div>
<div id="comment-tools-62577" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62577-form-container" class="comment-form-container">
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

