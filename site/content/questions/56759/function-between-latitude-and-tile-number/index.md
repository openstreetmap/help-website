+++
type = "question"
title = "function between latitude and tile number"
description = '''Hi, I am a developer and I need the function y=f(x)=? between the latitude (=x; -90 &amp;lt;= x &amp;lt;= 90) and the tile number on zoom level 16 (=y; 0 &amp;lt;= y &amp;lt;= 65536) for my mobile game. I exported the osm tiles with Maperitive and I need to convert the gps position of the phone to the tile number (...'''
date = "2017-06-26T18:53:00Z"
lastmod = "2017-06-26T20:26:00Z"
weight = 56759
keywords = [ "function", "tiles", "maperitive" ]
aliases = [ "/questions/56759" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [function between latitude and tile number](/questions/56759/function-between-latitude-and-tile-number)

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
<span id="post-56759-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56759-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56759-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am a developer and I need the function y=f(x)=? between the latitude (=x; -90 &lt;= x &lt;= 90) and the tile number on zoom level 16 (=y; 0 &lt;= y &lt;= 65536) for my mobile game. I exported the osm tiles with Maperitive and I need to convert the gps position of the phone to the tile number (x, y). I already have an algorithm to determine the x value of the tile number but I need the y value too. I can get the function by myself, but I would need to spend days on getting an accurate function because it seems to be a function with a degree over 10.<br />
So anyone knows the function? Or maybe how to convert the tile numbers to meters? If you're wondering why I don't just simply implement osm to my game ... one reason is that I need to deactivate some labels for my game.</p>
<p>I attached three screenshots with the graph, the value table and the tiles for better understanding.</p>
<p>Full graph:</p>
<p><img src="https://help.openstreetmap.org/upfiles/graph.JPG" alt="full graph" /></p>
<p>Part of the graph with value table:</p>
<p><img src="https://help.openstreetmap.org/upfiles/function.JPG" alt="alt text" /></p>
<p>Tiles generated with Maperitive (zoom level 16):</p>
<p><img src="https://help.openstreetmap.org/upfiles/tiles.JPG" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-function" rel="tag" title="see questions tagged &#39;function&#39;">function</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-maperitive" rel="tag" title="see questions tagged &#39;maperitive&#39;">maperitive</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jun '17, 18:53</strong></p>
<img src="https://secure.gravatar.com/avatar/a3785e3269a7d2d075eb016f6534709d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Time2Design&#39;s gravatar image" />
<p><span>Time2Design</span><br />
<span class="score" title="15 reputation points">15</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Time2Design has no accepted answers">0%</span> </br></p>
</img>
</div>
</div>
<div id="comments-container-56759" class="comments-container">
&#10;</div>
<div id="comment-tools-56759" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56759-form-container" class="comment-form-container">
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

<span id="56761"></span>

<div id="answer-container-56761" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56761-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56761-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-56761-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Time2Design has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Take a look at <a href="http://wiki.openstreetmap.org/wiki/Slippy_map_tilenames">http://wiki.openstreetmap.org/wiki/Slippy_map_tilenames</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jun '17, 19:20</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</img>
</div>
</div>
<div id="comments-container-56761" class="comments-container">
<span id="56762"></span>
<div id="comment-56762" class="comment">
<div id="post-56762-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thank you!</p>
</div>
<div id="comment-56762-info" class="comment-info">
<span class="comment-age">(26 Jun '17, 20:26)</span> <span class="comment-user userinfo">Time2Design</span>
</div>
</div>
</div>
<div id="comment-tools-56761" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56761-form-container" class="comment-form-container">
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

