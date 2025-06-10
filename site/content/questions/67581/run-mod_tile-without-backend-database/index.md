+++
type = "question"
title = "Run mod_tile without backend database?"
description = '''If you have all the tiles rendered using render_list the way you want them and you don&#x27;t need to update them regularly, is it possible to host a server that just has the .meta files? Or if perhaps you are going to load balance, you really only need one server to have the database to rerender everyth...'''
date = "2019-01-14T18:45:00Z"
lastmod = "2019-01-14T22:02:00Z"
weight = 67581
keywords = [ "renderd", "mod_tile" ]
aliases = [ "/questions/67581" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Run mod_tile without backend database?](/questions/67581/run-mod_tile-without-backend-database)

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
<span id="post-67581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67581-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If you have all the tiles rendered using render_list the way you want them and you don't need to update them regularly, is it possible to host a server that just has the .meta files?</p>
<p>Or if perhaps you are going to load balance, you really only need one server to have the database to rerender everything, on all the other servers couldn't you just host the rendered tiles and use rsync on a cronjob to keep them all updated?</p>
<p>What would I do if that is possible? In the Apache configuration it gives the sock location:</p>
<pre><code>LoadTileConfigFile /usr/local/etc/renderd.conf
ModTileRenderdSocketName /var/run/renderd/renderd.sock</code></pre>
<p>So you would assume you have to run the renderd process:</p>
<pre><code>renderd -f -c /usr/local/etc/renderd.conf</code></pre>
<p>But if you try running that without the Postgres server, it doesn't work.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Jan '19, 18:45</strong></p>
<img src="https://secure.gravatar.com/avatar/93573f3d1be0b4baf9865075d0540781?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ajhalls&#39;s gravatar image" />
<p><span>ajhalls</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ajhalls has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Jan '19, 18:46</strong> </span></p>
</div>
</div>
<div id="comments-container-67581" class="comments-container">
&#10;</div>
<div id="comment-tools-67581" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67581-form-container" class="comment-form-container">
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

<span id="67585"></span>

<div id="answer-container-67585" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67585-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67585-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-67585-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is possible. You don't need renderd; mod_tile will attempt to connect to renderd only when it thinks a tile needs to be rendered.</p>
<p>mod_tile will attempt to render a tile if (a) it is considered outdated, or (b) it is missing. If this happens and renderd is not available, mod_tile will serve (a) the old tile, (b) a 404 error.</p>
<p>You can ensure that mod_tile never considers a tile outdated by creating an empty file named "planet-import-complete" in /var/lib/mod_tile that has a time stamp older than your oldest tile.</p>
<p>You cannot keep mod_tile from attempting to render non-existing tiles on demand, but with renderd not available this should fail quickly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jan '19, 22:02</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-67585" class="comments-container">
&#10;</div>
<div id="comment-tools-67585" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67585-form-container" class="comment-form-container">
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

