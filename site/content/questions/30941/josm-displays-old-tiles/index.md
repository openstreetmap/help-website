+++
type = "question"
title = "JOSM displays old tiles"
description = '''I like to use the Mapnik and GPS traces imagery layer in JOSM, but they don&#x27;t seem to get updated often. I have uploaded changes and GPS traces a couple of days ago that are already showing up on the main website, but they don&#x27;t seem to be showing up in JOSM. I&#x27;m assuming tile.openstreetmap.org (whe...'''
date = "2014-02-23T08:33:00Z"
lastmod = "2014-02-23T09:41:00Z"
weight = 30941
keywords = [ "josm", "tiles", "old" ]
aliases = [ "/questions/30941" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [JOSM displays old tiles](/questions/30941/josm-displays-old-tiles)

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
<span id="post-30941-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30941-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-30941-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I like to use the Mapnik and GPS traces imagery layer in JOSM, but they don't seem to get updated often. I have uploaded changes and GPS traces a couple of days ago that are already showing up on the main website, but they don't seem to be showing up in JOSM.</p>
<p>I'm assuming tile.openstreetmap.org (where JOSM is getting its tiles from) is not updated as frequently-- so how often does it get updated?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-old" rel="tag" title="see questions tagged &#39;old&#39;">old</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Feb '14, 08:33</strong></p>
<img src="https://secure.gravatar.com/avatar/d440ea77d50e6cba9b345ed6fcccb184?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WZ%20Bzrandt&#39;s gravatar image" />
<p><span>WZ Bzrandt</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WZ Bzrandt has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Feb '14, 09:43</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-30941" class="comments-container">
&#10;</div>
<div id="comment-tools-30941" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30941-form-container" class="comment-form-container">
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

<span id="30943"></span>

<div id="answer-container-30943" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30943-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30943-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-30943-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="WZ Bzrandt has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is the same URL your browser uses, there is no special tile URL for JOSM. Instead the reason will be most probably JOSM's tile cache. You can flush it by deleting one of the following directories:</p>
<ul>
<li>Linux: <code>/tmp/JMapViewerTiles_username/</code></li>
<li>Windows: <code>%TEMP%\JMapViewerTiles_username\</code></li>
</ul>
<p>Or open JOSM's preferences and go to <em>WMS/TMS</em> -&gt; <em>settings</em> where the <em>Tile cache directory</em> setting can be changed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Feb '14, 09:41</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-30943" class="comments-container">
&#10;</div>
<div id="comment-tools-30943" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30943-form-container" class="comment-form-container">
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

