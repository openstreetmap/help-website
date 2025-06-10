+++
type = "question"
title = "Disk usage for Europe (OpenStreetMap)"
description = '''I would like to know a disk space usage for Europe extract (Nominatim, tile server, both data structures and rendered tiles).  I have currently map server with an european country extract and I tried to estimate disk usage for Europe. My estimation is a very big number (about 1,3 - 1,4TB!). Is it po...'''
date = "2015-10-19T09:58:00Z"
lastmod = "2015-10-19T19:12:00Z"
weight = 45982
keywords = [ "europe", "disk_usage", "tiles", "nominatim", "tileserver" ]
aliases = [ "/questions/45982" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Disk usage for Europe (OpenStreetMap)](/questions/45982/disk-usage-for-europe-openstreetmap)

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
<span id="post-45982-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45982-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45982-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to know a disk space usage for Europe extract (Nominatim, tile server, both data structures and rendered tiles). I have currently map server with an european country extract and I tried to estimate disk usage for Europe. My estimation is a very big number (about 1,3 - 1,4TB!). Is it possible? Am i wrong? Can someone correct or confirm my estimation?</p>
<p>My calculation's ways are:</p>
<ol>
<li>Europe surface to country surface ratio</li>
<li>Europe osm.pbf file to country osm.pbf file ratio</li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-europe" rel="tag" title="see questions tagged &#39;europe&#39;">europe</span> <span class="post-tag tag-link-disk_usage" rel="tag" title="see questions tagged &#39;disk_usage&#39;">disk_usage</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Oct '15, 09:58</strong></p>
<img src="https://secure.gravatar.com/avatar/4c27973e9238243226a3c2f8b6237a88?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anadd&#39;s gravatar image" />
<p><span>Anadd</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anadd has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Oct '15, 19:10</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-45982" class="comments-container">
<span id="45984"></span>
<div id="comment-45984" class="comment">
<div id="post-45984-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What zoom levels (for rendered tiles) are you interested in? Do you want to pre-render all tiles but only render those tiles that people want on demand?</p>
</div>
<div id="comment-45984-info" class="comment-info">
<span class="comment-age">(19 Oct '15, 10:09)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="45987"></span>
<div id="comment-45987" class="comment">
<div id="post-45987-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>crosspost: <a href="https://gis.stackexchange.com/questions/166968/disk-usage-for-europe-openstreetmap">https://gis.stackexchange.com/questions/166968/disk-usage-for-europe-openstreetmap</a></p>
</div>
<div id="comment-45987-info" class="comment-info">
<span class="comment-age">(19 Oct '15, 10:46)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="45990"></span>
<div id="comment-45990" class="comment">
<div id="post-45990-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I want pre-render tiles because i had problems with country extract when tiles wasn't pre-rendered (pink tiles appeared). I think pre-rendering tiles to 16 zoom level for one country and to 14/15 (or even less) zoom level for other countries is a sufficient solution for me.</p>
</div>
<div id="comment-45990-info" class="comment-info">
<span class="comment-age">(19 Oct '15, 13:23)</span> <span class="comment-user userinfo">Anadd</span>
</div>
</div>
</div>
<div id="comment-tools-45982" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45982-form-container" class="comment-form-container">
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

<span id="45998"></span>

<div id="answer-container-45998" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45998-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45998-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45998-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think <a href="https://wiki.openstreetmap.org/wiki/Tile_disk_usage">https://wiki.openstreetmap.org/wiki/Tile_disk_usage</a> could help you</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Oct '15, 19:12</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-45998" class="comments-container">
&#10;</div>
<div id="comment-tools-45998" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45998-form-container" class="comment-form-container">
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

