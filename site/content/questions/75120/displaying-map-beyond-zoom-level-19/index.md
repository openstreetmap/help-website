+++
type = "question"
title = "Displaying map beyond zoom level 19"
description = '''Hello, For an XXL scale project (where I need sub-metric details for a small outdoor project, note that accuracy is not a big deal, I just want to draw and display small points, lines and polygons relative to each others), I&#x27;m searching for a background OSM-based map which displays beyond zoom level...'''
date = "2020-06-03T15:21:00Z"
lastmod = "2020-06-03T17:17:00Z"
weight = 75120
keywords = [ "zoomlevel" ]
aliases = [ "/questions/75120" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Displaying map beyond zoom level 19](/questions/75120/displaying-map-beyond-zoom-level-19)

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
<span id="post-75120-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75120-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-75120-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>For an XXL scale project (where I need sub-metric details for a small outdoor project, note that accuracy is not a big deal, I just want to draw and display small points, lines and polygons relative to each others), I'm searching for a background OSM-based map which displays beyond zoom level 19, I would say up to 24-26.</p>
<p>Do you know some URL which serve tiles matching this format: <code>//{s}.tile.domain.org/{z}/{x}/{y}.png</code> for such large zoom levels?</p>
<p>If no, I guess I have to build my own tilling service, but I don't want to reinvent the wheel.<br />
Do you know some tools to quickly build my own web service based on OSM data?</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zoomlevel" rel="tag" title="see questions tagged &#39;zoomlevel&#39;">zoomlevel</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jun '20, 15:21</strong></p>
<img src="https://secure.gravatar.com/avatar/93c67fbeb492e14f45072515ab416289?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="s-k&#39;s gravatar image" />
<p><span>s-k</span><br />
<span class="score" title="46 reputation points">46</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="s-k has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jun '20, 15:28</strong> </span></p>
</div>
</div>
<div id="comments-container-75120" class="comments-container">
&#10;</div>
<div id="comment-tools-75120" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75120-form-container" class="comment-form-container">
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

<span id="75125"></span>

<div id="answer-container-75125" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75125-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75125-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-75125-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>With regard to creating your own tiles, see <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/mod_tile_28">here</a> for displaying zoom levels up to 28. A branch of a fork of mod_tile with that in it is <a href="https://github.com/SomeoneElseOSM/mod_tile/tree/zoom">here</a> - just use that in place of the normal one. If that isn't enough, see <a href="https://github.com/openstreetmap/mod_tile/issues/118#issuecomment-384648654">here</a> for zoom levels up to 30.</p>
<p>The tiles underneath <a href="https://map.atownsend.org.uk"></a><a href="https://map.atownsend.org.uk">https://map.atownsend.org.uk</a> cover Ireland and the UK at zoom levels up to 24.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jun '20, 17:17</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-75125" class="comments-container">
&#10;</div>
<div id="comment-tools-75125" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75125-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75124"></span>

<div id="answer-container-75124" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75124-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75124-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75124-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For your first question, I've never seen that. Sometimes it goes as far as 20 (maybe 21) but never seen more.</p>
<p>For the second question, the reference is <a href="https://switch2osm.org/">switch2osm.org</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jun '20, 17:02</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-75124" class="comments-container">
&#10;</div>
<div id="comment-tools-75124" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75124-form-container" class="comment-form-container">
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

