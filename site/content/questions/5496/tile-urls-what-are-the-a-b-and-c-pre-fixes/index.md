+++
type = "question"
title = "Tile URLs: What are the a.*, b.* and c.* pre-fixes?"
description = '''I just ran into these &quot;prefixes&quot; and can&#x27;t figure them out. At first I saw a tile URL beginning with c. and was assuming it is a cached version. Then I noticed prefixes of a. and b.*. All of the prefixed URLs seem to be some sort of cached or older versions of the tiles in question  but what? I coul...'''
date = "2011-06-02T16:04:00Z"
lastmod = "2011-06-03T06:37:00Z"
weight = 5496
keywords = [ "tiles" ]
aliases = [ "/questions/5496" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Tile URLs: What are the a.\*, b.\* and c.\* pre-fixes?](/questions/5496/tile-urls-what-are-the-a-b-and-c-pre-fixes)

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
<span id="post-5496-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5496-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-5496-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I just ran into these "prefixes" and can't figure them out. At first I saw a tile URL beginning with c. <em>and was assuming it is a cached version. Then I noticed prefixes of a.</em> and b.*. All of the prefixed URLs seem to be some sort of cached or older versions of the tiles in question but what?</p>
<p>I couldn't find information in the Slippy map wiki article (<a href="http://wiki.openstreetmap.org/wiki/Slippy_Map)">http://wiki.openstreetmap.org/wiki/Slippy_Map)</a> and the related questions here don't seem to help either (<a href="http://help.openstreetmap.org/questions/4343/dirty-tiles">http://help.openstreetmap.org/questions/4343/dirty-tiles</a> &amp; <a href="http://help.openstreetmap.org/questions/1049/how-to-trigger-a-repaint-for-a-specific-osm-map-tile)">http://help.openstreetmap.org/questions/1049/how-to-trigger-a-repaint-for-a-specific-osm-map-tile)</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jun '11, 16:04</strong></p>
<img src="https://secure.gravatar.com/avatar/280f61ca58a2e8c3d7bc877ed8a3def2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jaakkoh&#39;s gravatar image" />
<p><span>jaakkoh</span><br />
<span class="score" title="548 reputation points">548</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jaakkoh has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-5496" class="comments-container">
&#10;</div>
<div id="comment-tools-5496" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5496-form-container" class="comment-form-container">
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

<span id="5502"></span>

<div id="answer-container-5502" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5502-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5502-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-5502-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Normaly the web browser would not simultaniously download more then a few urls from a server. This leads to slower download when browsing the map. To trick the browser to download more tiles faster OpenLayers have support for several servers. Therefore the tile server have several domains for the same server. This trick makes the browser open up more connections to the server witch leads to faster download.</p>
<p>The tile server have two cache servers in front that are load balanced by theese urls. This might cause some tiles to be older on one server then the other.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jun '11, 19:19</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-5502" class="comments-container">
&#10;</div>
<div id="comment-tools-5502" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5502-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5522"></span>

<div id="answer-container-5522" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5522-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5522-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-5522-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Round-robin load balancers?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jun '11, 06:37</strong></p>
<img src="https://secure.gravatar.com/avatar/ca446edd75e87c48db5dd850d9f394a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ivanatora&#39;s gravatar image" />
<p><span>ivanatora</span><br />
<span class="score" title="2740 reputation points"><span>2.7k</span></span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="55 badges"><span class="silver">●</span><span class="badgecount">55</span></span><span title="68 badges"><span class="bronze">●</span><span class="badgecount">68</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ivanatora has one accepted answer">7%</span></p>
</div>
</div>
<div id="comments-container-5522" class="comments-container">
&#10;</div>
<div id="comment-tools-5522" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5522-form-container" class="comment-form-container">
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

