+++
type = "question"
title = "how to solve socket connect failed for: /tmp/osm-renderd"
description = '''Hi buds ! I&#x27;m getting this error while trying to pre-render tiles ... I fetched Corsica to give it a try, i could import ... ... The problem i when i&#x27;m running render_list Here is the log: osm@osm-server:~$ sudo render_list -a -f –z 18 -Z 18 x 8.5 X 9.8 y 43.03 Y 41.34 - socket=/var/run/renderd/rend...'''
date = "2014-04-30T10:11:00Z"
lastmod = "2014-05-03T00:58:00Z"
weight = 32757
keywords = [ "pre-built", "render" ]
aliases = [ "/questions/32757" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to solve socket connect failed for: /tmp/osm-renderd](/questions/32757/how-to-solve-socket-connect-failed-for-tmposm-renderd)

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
<span id="post-32757-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32757-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32757-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi buds !</p>
<p>I'm getting this error while trying to pre-render tiles ... I fetched Corsica to give it a try, i could import ... ... The problem i when i'm running render_list</p>
<p>Here is the log:</p>
<pre><code>osm@osm-server:~$ sudo render_list -a -f –z 18 -Z 18 x 8.5 X 9.8 y 43.03 Y 41.34 -      socket=/var/run/renderd/renderd.sock
Rendering client
Planet timestamp file (/var/lib/mod_tile//planet-import-complete) is missing
Starting 1 rendering threads
Rendering all tiles from zoom 0 to zoom 18
Rendering all tiles for zoom 0 from (0, 0) to (0, 0)
Rendering all tiles for zoom 1 from (0, 0) to (1, 1)
Rendering all tiles for zoom 2 from (0, 0) to (3, 3)
Rendering all tiles for zoom 3 from (0, 0) to (7, 7)
Rendering all tiles for zoom 4 from (0, 0) to (15, 15)
Rendering all tiles for zoom 5 from (0, 0) to (31, 31) 
Rendering all tiles for zoom 6 from (0, 0) to (63, 63)
socket connect failed for: /tmp/osm-renderd</code></pre>
<p>i think getting the error "planet timestamp file ..." is normal since is just downloaded the Corsica .. ( ? ) ps : i'm running on a virtual machine under ubuntu (18 allocated), since corsica is a pretty small area, i think this is enough .. or i hope this is enough ..</p>
<p>My first thought was that i didn't have the permissions for /var/ru/rendered/renderd.sock, i did a chmod .. didn't change anything .. My tile's folder is /var/lib/mod_tile (default)</p>
<p>Thank you for reading and helping, Regards, Guillaume.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pre-built" rel="tag" title="see questions tagged &#39;pre-built&#39;">pre-built</span> <span class="post-tag tag-link-render" rel="tag" title="see questions tagged &#39;render&#39;">render</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Apr '14, 10:11</strong></p>
<img src="https://secure.gravatar.com/avatar/8fb68885ff997c74135f182880395f56?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="guillaume&#39;s gravatar image" />
<p><span>guillaume</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="guillaume has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-32757" class="comments-container">
&#10;</div>
<div id="comment-tools-32757" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32757-form-container" class="comment-form-container">
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

<span id="32828"></span>

<div id="answer-container-32828" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32828-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32828-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-32828-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is ominous that you seem to instruct render_list to use <code>/var/run/renderd/renderd.sock</code> as a socket but later you have an error message that says a connection to <code>/tmp/osm-renderd</code> has failed. The only context in which that path is used in the current codebase is the python version of renderd which is not really supported or used by anyone. Are you sure that you are running the proper C renderd? Are you running any renderd at all (because you didn't mention anything about starting renderd)? If not, make sure to start renderd before running any render_... programs.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 May '14, 00:58</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-32828" class="comments-container">
&#10;</div>
<div id="comment-tools-32828" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32828-form-container" class="comment-form-container">
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

