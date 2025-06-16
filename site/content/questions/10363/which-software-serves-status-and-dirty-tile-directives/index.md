+++
type = "question"
title = "Which software serves /status and /dirty tile directives ?"
description = '''The wiki mentions &quot;/status&quot; or &quot;/dirty&quot; tile directives: https://wiki.openstreetmap.org/wiki/Slippy_map#Mapnik_tile_rendering Which software serves these commands ? I searched in the source codes of the OSM Rails port and mod_tile, without finding anything. If someone can help me, thanks in advance!'''
date = "2012-02-01T16:40:00Z"
lastmod = "2012-02-16T23:12:00Z"
weight = 10363
keywords = [ "tile", "status", "commands", "dirty", "server" ]
aliases = [ "/questions/10363" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Which software serves /status and /dirty tile directives ?](/questions/10363/which-software-serves-status-and-dirty-tile-directives)

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
<span id="post-10363-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10363-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-10363-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The wiki mentions "/status" or "/dirty" tile directives: <a href="https://wiki.openstreetmap.org/wiki/Slippy_map#Mapnik_tile_rendering">https://wiki.openstreetmap.org/wiki/Slippy_map#Mapnik_tile_rendering</a></p>
<p>Which software serves these commands ?</p>
<p>I searched in the source codes of the OSM Rails port and mod_tile, without finding anything.</p>
<p>If someone can help me, thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tile" rel="tag" title="see questions tagged &#39;tile&#39;">tile</span> <span class="post-tag tag-link-status" rel="tag" title="see questions tagged &#39;status&#39;">status</span> <span class="post-tag tag-link-commands" rel="tag" title="see questions tagged &#39;commands&#39;">commands</span> <span class="post-tag tag-link-dirty" rel="tag" title="see questions tagged &#39;dirty&#39;">dirty</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Feb '12, 16:40</strong></p>
<img src="https://secure.gravatar.com/avatar/970d2e3e768d795b4014fde0aaf9f153?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cbenz&#39;s gravatar image" />
<p><span>cbenz</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cbenz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-10363" class="comments-container">
&#10;</div>
<div id="comment-tools-10363" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10363-form-container" class="comment-form-container">
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

<span id="10375"></span>

<div id="answer-container-10375" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10375-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10375-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-10375-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's right there in mod_tile.c, in the tile_translate function.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Feb '12, 18:02</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-10375" class="comments-container">
<span id="10379"></span>
<div id="comment-10379" class="comment">
<div id="post-10379-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is there perhaps a little more to it than that? If I follow <a href="http://en.flossmanuals.net/openstreetmap/setting-up-your-own-tile-server/">this book</a> I get a working tile server, but /dirty and /status aren't recognised as they are by <a href="http://X.tile.openstreetmap.org">X.tile.openstreetmap.org</a>. In mod_tile.c I can see various references to "dirty" and "status" but nothing that describes how those commands get to mod_tile from Apache via renderd.</p>
</div>
<div id="comment-10379-info" class="comment-info">
<span class="comment-age">(01 Feb '12, 22:26)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="10383"></span>
<div id="comment-10383" class="comment">
<div id="post-10383-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It is possible that there's something broken it the latest mod_tile. Checking out r26346 might work.</p>
</div>
<div id="comment-10383-info" class="comment-info">
<span class="comment-age">(02 Feb '12, 07:28)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="10384"></span>
<div id="comment-10384" class="comment">
<div id="post-10384-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I just checked in a fix into SVN for this. Thanks for reporting the bug.</p>
</div>
<div id="comment-10384-info" class="comment-info">
<span class="comment-age">(02 Feb '12, 07:53)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
<span id="10615"></span>
<div id="comment-10615" class="comment">
<div id="post-10615-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks - the latest svn version (and ./autogen.sh;./configure;make;sudo make install;sudo make install-mod_tile;sudo ldconfig) works</p>
</div>
<div id="comment-10615-info" class="comment-info">
<span class="comment-age">(16 Feb '12, 23:12)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-10375" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10375-form-container" class="comment-form-container">
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

