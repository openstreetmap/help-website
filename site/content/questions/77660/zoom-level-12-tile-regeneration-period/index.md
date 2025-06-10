+++
type = "question"
title = "Zoom level 12 tile regeneration period?"
description = '''Hi there, I&#x27;ve been editing some forest areas in eastern China for some time. But it seems the changes are still not visible on the map of levels less than 13. It&#x27;s visible on level 13 and higher. Is it because of caching or tile regeneration settings? Level 13 with forest: https://www.openstreetmap...'''
date = "2020-11-22T13:33:00Z"
lastmod = "2020-11-25T20:40:00Z"
weight = 77660
keywords = [ "tiles", "cache" ]
aliases = [ "/questions/77660" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Zoom level 12 tile regeneration period?](/questions/77660/zoom-level-12-tile-regeneration-period)

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
<span id="post-77660-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77660-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77660-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there,</p>
<p>I've been editing some forest areas in eastern China for some time. But it seems the changes are still not visible on the map of levels less than 13. It's visible on level 13 and higher. Is it because of caching or tile regeneration settings?</p>
<p>Level 13 with forest: <a href="https://www.openstreetmap.org/search?query=wenzhou#map=13/27.8766/120.4281">https://www.openstreetmap.org/search?query=wenzhou#map=13/27.8766/120.4281</a></p>
<p>Level 12 with no forest: <a href="https://www.openstreetmap.org/search?query=wenzhou#map=12/27.8587/120.4347">https://www.openstreetmap.org/search?query=wenzhou#map=12/27.8587/120.4347</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-cache" rel="tag" title="see questions tagged &#39;cache&#39;">cache</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Nov '20, 13:33</strong></p>
<img src="https://secure.gravatar.com/avatar/e39830800041c01c0ad201916e2c4065?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="strongwillow&#39;s gravatar image" />
<p><span>strongwillow</span><br />
<span class="score" title="65 reputation points">65</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="strongwillow has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Nov '20, 21:40</strong> </span></p>
</div>
</div>
<div id="comments-container-77660" class="comments-container">
&#10;</div>
<div id="comment-tools-77660" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77660-form-container" class="comment-form-container">
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

<span id="77661"></span>

<div id="answer-container-77661" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77661-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77661-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77661-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>At time of writing the tile statcs for <a href="https://tile.openstreetmap.org/12/3417/1717.png/status">https://tile.openstreetmap.org/12/3417/1717.png/status</a> is showing as</p>
<blockquote>
<p>Tile is clean. Last rendered at Sun Oct 25 03:26:30 2020. Last accessed at Sun Nov 22 14:11:48 2020. Stored in file:///srv/tile.openstreetmap.org/tiles/default/12/0/0/214/91/128.meta</p>
<p>(Dates might not be accurate. Rendering time might be reset to an old date for tile expiry. Access times might not be updated on all file systems)</p>
</blockquote>
<p>To me that seems a little old to be considered fresh. You could try <a href="https://wiki.openstreetmap.org/wiki/Slippy_Map#OpenStreetMap_.22Standard.22_tile_server">manually marking</a> them as dirty</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Nov '20, 21:00</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Nov '20, 21:01</strong> </span></p>
</div>
</div>
<div id="comments-container-77661" class="comments-container">
<span id="77662"></span>
<div id="comment-77662" class="comment">
<div id="post-77662-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for the answer. I manually marked the tile as dirty and it indeed gets regenerated. But there are many tiles at different z levels. I shouldn't do it manually for all right?</p>
</div>
<div id="comment-77662-info" class="comment-info">
<span class="comment-age">(22 Nov '20, 21:45)</span> <span class="comment-user userinfo">strongwillow</span>
</div>
</div>
<span id="77679"></span>
<div id="comment-77679" class="comment">
<div id="post-77679-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You shouldn't have to mark them all individually, I think it should notice that they're old when requested.</p>
</div>
<div id="comment-77679-info" class="comment-info">
<span class="comment-age">(23 Nov '20, 21:00)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="77710"></span>
<div id="comment-77710" class="comment">
<div id="post-77710-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I just saw <a href="https://help.openstreetmap.org/questions/55425/bug-zooms-12-and-below-not-marked-dirty-so-never-re-rendered">this question</a> pop up as a relative to another render question. It seems more relevant here.</p>
</div>
<div id="comment-77710-info" class="comment-info">
<span class="comment-age">(25 Nov '20, 20:40)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-77661" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77661-form-container" class="comment-form-container">
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

