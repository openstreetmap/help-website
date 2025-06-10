+++
type = "question"
title = "Load/save, import/export .osm file map extent only and not include the map data"
description = '''I have several old .osm files that I have already uploaded. I plan to revisit the map extents in all of those files to check for updates if there is anything that needs more mapping. However, my disk is getting short of space since I have many of these .osm files which contain lots of map data. I wo...'''
date = "2022-01-24T09:12:00Z"
lastmod = "2022-01-24T13:33:00Z"
weight = 83178
keywords = [ "josm", "map_extent", "osm", "extent" ]
aliases = [ "/questions/83178" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Load/save, import/export .osm file map extent only and not include the map data](/questions/83178/loadsave-importexport-osm-file-map-extent-only-and-not-include-the-map-data)

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
<span id="post-83178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83178-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have several old <code>.osm</code> files that I have already uploaded. I plan to revisit the map extents in all of those files to check for updates if there is anything that needs more mapping. However, my disk is getting short of space since I have many of these <code>.osm</code> files which contain lots of map data. I would not like to delete these files since it would be very cumbersome to scout for those exact extents again.</p>
<p>Is there a way to save only, or export the map extent a <code>.osm</code> file, and not include the data? It would also be useful if there is an option to load only the map extent of the existing <code>.osm</code> file, so that you can just update the map with the Update data (<code>CTRL+U</code>) option. Is there a way to do or a workaround for this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-map_extent" rel="tag" title="see questions tagged &#39;map_extent&#39;">map_extent</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-extent" rel="tag" title="see questions tagged &#39;extent&#39;">extent</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jan '22, 09:12</strong></p>
<img src="https://secure.gravatar.com/avatar/fb34d7bed35464f64bba89dba8f34f95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JAT86&#39;s gravatar image" />
<p><span>JAT86</span><br />
<span class="score" title="240 reputation points">240</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JAT86 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83178" class="comments-container">
<span id="83179"></span>
<div id="comment-83179" class="comment">
<div id="post-83179-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>At the risk of stating the bleeding obvious, if you're running out of disk space and have large .osm files lying around - compress them until you need them?</p>
</div>
<div id="comment-83179-info" class="comment-info">
<span class="comment-age">(24 Jan '22, 09:20)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-83178" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83178-form-container" class="comment-form-container">
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

<span id="83182"></span>

<div id="answer-container-83182" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83182-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83182-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-83182-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JAT86 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Does the "Irregular Bookmarks" portion of <a href="https://wiki.openstreetmap.org/wiki/JOSM/Advanced_Tricks">this page</a> do what you need?</p>
<p>NB I think it might be worth emphasising the "in a text editor" part otherwise you risk marking those objects for deletion in your next session.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jan '22, 13:33</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-83182" class="comments-container">
&#10;</div>
<div id="comment-tools-83182" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83182-form-container" class="comment-form-container">
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

