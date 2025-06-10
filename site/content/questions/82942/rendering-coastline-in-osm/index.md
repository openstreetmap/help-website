+++
type = "question"
title = "rendering coastline in osm"
description = '''Hi, when i improve osm, after my saving, I can see the result a few minutes later at bigger zoom, a little more late for smaller zoom but it is quite quick. But when I improve the coastline, the render is very long : for example I have changed the position of the coastline here 3 days ago and it is ...'''
date = "2022-01-04T15:11:00Z"
lastmod = "2022-01-14T01:08:00Z"
weight = 82942
keywords = [ "rendering", "coastline" ]
aliases = [ "/questions/82942" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [rendering coastline in osm](/questions/82942/rendering-coastline-in-osm)

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
<span id="post-82942-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82942-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82942-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>when i improve osm, after my saving, I can see the result a few minutes later at bigger zoom, a little more late for smaller zoom but it is quite quick.</p>
<p>But when I improve the coastline, the render is very long : for example I have changed the position of the coastline <a href="https://www.openstreetmap.org/#map=19/4.94291/-52.33543">here</a> 3 days ago and it is still invisible in osm.</p>
<p>Why this difference ? And how long do I have to wait to see it ?</p>
<p>Best regards</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-coastline" rel="tag" title="see questions tagged &#39;coastline&#39;">coastline</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jan '22, 15:11</strong></p>
<img src="https://secure.gravatar.com/avatar/33b586336c1978cc33b67e8b3cff9cb6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fred73000&#39;s gravatar image" />
<p><span>Fred73000</span><br />
<span class="score" title="54 reputation points">54</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fred73000 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82942" class="comments-container">
&#10;</div>
<div id="comment-tools-82942" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82942-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="82944"></span>

<div id="answer-container-82944" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82944-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-82944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Coastline rendering <a href="https://wiki.openstreetmap.org/wiki/Coastline#Rendering_in_Standard_tile_layer_on_openstreetmap.org">is special</a>. It requires a fair amount of processing to determine what's land/sea for large continents. To protect against accidental "flooding" of continents the new shapes aren't released to the renderer if the difference in area is too big between updates. For the reasons behind the most recent stoppage see <a href="https://lists.openstreetmap.org/pipermail/talk/2022-January/087194.html">this thread</a> on the talk mailing list.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jan '22, 20:26</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-82944" class="comments-container">
<span id="82945"></span>
<div id="comment-82945" class="comment">
<div id="post-82945-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, thanks for this clear answer.</p>
<p>Another question about coastline : is it a good idea to put on the same way natural=coastline + barrier=retain_wall ? This way is a wall to protect a city from the waves and the hightide is on this wall so it is the coastline too.</p>
<p>I don't like to have 2 ways one on the other when you have relations on them (and with coastline we always have a lot of boundary relations) : a lot of time I broke a relation because I unintentionally put the 2 ways in the relation and it is impossible to see that, when you look at the relation on ID it seems closed.</p>
<p>But because of your last answer, I wonder if to have 2 different tags is ok for the rendering ?</p>
</div>
<div id="comment-82945-info" class="comment-info">
<span class="comment-age">(05 Jan '22, 00:16)</span> <span class="comment-user userinfo">Fred73000</span>
</div>
</div>
<span id="82978"></span>
<div id="comment-82978" class="comment">
<div id="post-82978-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>According to this <a href="https://osmdata.openstreetmap.de/data/land-polygons.html">page</a>, it is OK now but the rendering is still bad. Why ?</p>
</div>
<div id="comment-82978-info" class="comment-info">
<span class="comment-age">(06 Jan '22, 22:42)</span> <span class="comment-user userinfo">Fred73000</span>
</div>
</div>
</div>
<div id="comment-tools-82944" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82944-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="83075"></span>

<div id="answer-container-83075" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83075-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83075-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83075-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Ok, I fix that by myself, using "dirty" on each bad tile like explain here <a href="https://wiki.openstreetmap.org/wiki/Slippy_Map#OpenStreetMap_.22Standard.22_tile_server">https://wiki.openstreetmap.org/wiki/Slippy_Map#OpenStreetMap_.22Standard.22_tile_server</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jan '22, 01:08</strong></p>
<img src="https://secure.gravatar.com/avatar/33b586336c1978cc33b67e8b3cff9cb6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fred73000&#39;s gravatar image" />
<p><span>Fred73000</span><br />
<span class="score" title="54 reputation points">54</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fred73000 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83075" class="comments-container">
&#10;</div>
<div id="comment-tools-83075" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83075-form-container" class="comment-form-container">
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

