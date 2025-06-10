+++
type = "question"
title = "Muscat, Oman map download"
description = '''Hi Team, Need you help to download map tiles for getting zoom level upto 10. I tried with the JTileDownloader but during the download it showing a error message that some tiles are forbidden. Using retry button though it is downloaded by skipping those forbidden tiles but when i import this tiles in...'''
date = "2016-04-18T12:50:00Z"
lastmod = "2016-04-18T15:05:00Z"
weight = 49283
keywords = [ "jtiledownloader" ]
aliases = [ "/questions/49283" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Muscat, Oman map download](/questions/49283/muscat-oman-map-download)

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
<span id="post-49283-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49283-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49283-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi Team,</p>
<p>Need you help to download map tiles for getting zoom level upto 10. I tried with the JTileDownloader but during the download it showing a error message that some tiles are forbidden.</p>
<p>Using retry button though it is downloaded by skipping those forbidden tiles but when i import this tiles in my application nothing is showing in the map some X sign are coming.</p>
<p>Thanks for any kind of support/Suggestions</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-jtiledownloader" rel="tag" title="see questions tagged &#39;jtiledownloader&#39;">jtiledownloader</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Apr '16, 12:50</strong></p>
<img src="https://secure.gravatar.com/avatar/e841eff251f32375117a360c4e67f331?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nepal%20Chandra%20Paul&#39;s gravatar image" />
<p><span>Nepal Chandr...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nepal Chandra Paul has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49283" class="comments-container">
&#10;</div>
<div id="comment-tools-49283" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49283-form-container" class="comment-form-container">
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

<span id="49284"></span>

<div id="answer-container-49284" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49284-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49284-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-49284-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>See <a href="https://wiki.openstreetmap.org/wiki/JTileDownloader">JTileDownloader</a> in the OSM wiki, especially the big red message stating</p>
<blockquote>
<p>JTileDownloader user agents [...] blocked entirely [...]. Please use other tile servers, like MapQuest Open.</p>
</blockquote>
<p>Downloading tiles, especially high zoom tiles, puts a big load on tile servers. OSM's tile servers run on donated resources and thus will block any software trying to overload them. See the <a href="https://wiki.openstreetmap.org/wiki/Tile_usage_policy">tile usage policy</a> for details.</p>
<p>Try a different <a href="https://wiki.openstreetmap.org/wiki/Tile_servers">tile server</a>. Ideally one that is run by a large company and has a less strict usage policy or a <a href="https://switch2osm.org/providers/">paid tile provider</a>. Alternatively you can use <a href="https://wiki.openstreetmap.org/wiki/TileMill">TileMill</a> or <a href="https://wiki.openstreetmap.org/wiki/Maperitive">Maperitive</a> for generating tiles on your own or <a href="https://switch2osm.org/serving-tiles/">install your own tile server</a>.</p>
<p>Other questions about <a href="https://help.openstreetmap.org/tags/offlinemaps/">offline maps</a> might also help you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Apr '16, 15:05</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Apr '16, 15:24</strong> </span></p>
</div>
</div>
<div id="comments-container-49284" class="comments-container">
&#10;</div>
<div id="comment-tools-49284" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49284-form-container" class="comment-form-container">
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

