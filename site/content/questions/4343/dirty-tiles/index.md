+++
type = "question"
title = "dirty tiles"
description = '''Hello, I am pretty sure the following tile needs to be re-rendered : link:(http://c.tile.openstreetmap.org/9/293/185.png) I read that the following url, request a new rendering... link:(http://c.tile.openstreetmap.org/9/293/185.png/dirty) But after that when I call this url link:(http://c.tile.opens...'''
date = "2011-04-08T17:44:00Z"
lastmod = "2011-06-02T15:37:00Z"
weight = 4343
keywords = [ "tile", "status", "tiles", "dirty" ]
aliases = [ "/questions/4343" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [dirty tiles](/questions/4343/dirty-tiles)

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
<span id="post-4343-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4343-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-4343-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I am pretty sure the following tile needs to be re-rendered :<br />
link:(<a href="http://c.tile.openstreetmap.org/9/293/185.png">http://c.tile.openstreetmap.org/9/293/185.png</a>)</p>
<p>I read that the following url, request a new rendering...<br />
link:(<a href="http://c.tile.openstreetmap.org/9/293/185.png/dirty">http://c.tile.openstreetmap.org/9/293/185.png/dirty</a>)</p>
<p>But after that when I call this url<br />
link:(<a href="http://c.tile.openstreetmap.org/9/293/185.png/status">http://c.tile.openstreetmap.org/9/293/185.png/status</a>)</p>
<p>I got :<br />
<em>Tile is clean. Last rendered at Thu <strong>Mar 17</strong> 04:40:53 2011</em> and today is <strong>April 8</strong> ?!?</p>
<p>What can I do ? to get my tile refreshed ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tile" rel="tag" title="see questions tagged &#39;tile&#39;">tile</span> <span class="post-tag tag-link-status" rel="tag" title="see questions tagged &#39;status&#39;">status</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-dirty" rel="tag" title="see questions tagged &#39;dirty&#39;">dirty</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Apr '11, 17:44</strong></p>
<img src="https://secure.gravatar.com/avatar/0348ab36fbb79434173c38691b3fe41a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fabyen&#39;s gravatar image" />
<p><span>Fabyen</span><br />
<span class="score" title="216 reputation points">216</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fabyen has 2 accepted answers">100%</span> </br></br></p>
</div>
</div>
<div id="comments-container-4343" class="comments-container">
&#10;</div>
<div id="comment-tools-4343" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4343-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="4346"></span>

<div id="answer-container-4346" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4346-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4346-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-4346-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In my experience high zoom levels (zoomed in far) are re-rendered very quickly, but when you zoom out a bunch (eg to level 9 as in your tile) it re-renders very infrequently. I suspect that lower zoom levels are on a schedule or something, and don't respond to the "dirty" system, or respond, but on a significantly different schedule. I'd love for someone to confirm this and share the details, as I haven't been able to find it documented anywhere.</p>
<p>Would be lovely to have it documented <a href="https://wiki.openstreetmap.org/wiki/Slippy_Map#Mapnik_tile_rendering">here</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Apr '11, 18:58</strong></p>
<img src="https://secure.gravatar.com/avatar/26d091a5db7b2fbea266e0a5d853affd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JasonWoof&#39;s gravatar image" />
<p><span>JasonWoof</span><br />
<span class="score" title="121 reputation points">121</span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JasonWoof has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-4346" class="comments-container">
<span id="4371"></span>
<div id="comment-4371" class="comment">
<div id="post-4371-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>would be lovely... thanks for the answer.</p>
</div>
<div id="comment-4371-info" class="comment-info">
<span class="comment-age">(10 Apr '11, 16:45)</span> <span class="comment-user userinfo">Fabyen</span>
</div>
</div>
</div>
<div id="comment-tools-4346" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4346-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="4368"></span>

<div id="answer-container-4368" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4368-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4368-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4368-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In case of the old tile eventually being cached in your browser's cache you may want to open the tile directly into your browser by right-clicking over it (choose "Open image" or whatever <em>your</em> browser writes) and press CTRL+F5 to fetch a clean copy from the server.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Apr '11, 14:25</strong></p>
<img src="https://secure.gravatar.com/avatar/bc6d0b055d631830f7891d3f89edb66b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="katpatuka&#39;s gravatar image" />
<p><span>katpatuka</span><br />
<span class="score" title="1041 reputation points"><span>1.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="katpatuka has 2 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-4368" class="comments-container">
<span id="4370"></span>
<div id="comment-4370" class="comment">
<div id="post-4370-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks about that. But I know about webbrowser cache, and the problem is not coming from there. Thanks anyway.</p>
</div>
<div id="comment-4370-info" class="comment-info">
<span class="comment-age">(10 Apr '11, 16:45)</span> <span class="comment-user userinfo">Fabyen</span>
</div>
</div>
</div>
<div id="comment-tools-4368" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4368-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5495"></span>

<div id="answer-container-5495" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5495-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5495-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-5495-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I just commented on this issue to another question at <a href="/questions/1049/how-to-trigger-a-repaint-for-a-specific-osm-map-tile?page=1#5494">https://help.openstreetmap.org/questions/1049/how-to-trigger-a-repaint-for-a-specific-osm-map-tile?page=1#5494</a> . What's the c.* in the URL? (I'm assuming that my guess in the linked comment may well not be correct..).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jun '11, 15:37</strong></p>
<img src="https://secure.gravatar.com/avatar/280f61ca58a2e8c3d7bc877ed8a3def2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jaakkoh&#39;s gravatar image" />
<p><span>jaakkoh</span><br />
<span class="score" title="548 reputation points">548</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jaakkoh has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-5495" class="comments-container">
&#10;</div>
<div id="comment-tools-5495" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5495-form-container" class="comment-form-container">
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

