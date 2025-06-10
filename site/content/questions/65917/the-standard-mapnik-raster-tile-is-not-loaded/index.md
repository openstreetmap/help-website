+++
type = "question"
title = "The standard Mapnik raster tile is not loaded"
description = '''Hello. I&#x27;m from Ukraine and a few days ago I have encountered a problem: the standard Mapnik raster tile stopped downloading. I tried to open on several internet server providers, in various browsers, devices and map services that use this layer with no success. The ping and trace on tile.openstreet...'''
date = "2018-09-16T12:23:00Z"
lastmod = "2018-09-17T04:39:00Z"
weight = 65917
keywords = [ "openstreetmap", "ukraine", "tiles", "mapnik", "blocked" ]
aliases = [ "/questions/65917" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [The standard Mapnik raster tile is not loaded](/questions/65917/the-standard-mapnik-raster-tile-is-not-loaded)

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
<span id="post-65917-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65917-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65917-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello. I'm from Ukraine and a few days ago I have encountered a problem: the standard Mapnik raster tile stopped downloading. I tried to open on several internet server providers, in various browsers, devices and map services that use this layer with no success. The ping and trace on tile.openstreetmap.org does not pass, but shows that the connection goes to the server with the IP address 5.45.248.21, here is the description of this server <a href="https://hardware.openstreetmap.org/servers/gorynych.openstreetmap.org/">https://hardware.openstreetmap.org/servers/gorynych.openstreetmap.org/</a> It looks like either a tile has started distributed from a new server located in Russia and from blocked Yandex IP addresses ranges, or it got recently blocked. Is it possible to distribute tiles from another server?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-ukraine" rel="tag" title="see questions tagged &#39;ukraine&#39;">ukraine</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-blocked" rel="tag" title="see questions tagged &#39;blocked&#39;">blocked</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Sep '18, 12:23</strong></p>
<img src="https://secure.gravatar.com/avatar/e86e4180b6c0f5bda768f1ed3dfdf226?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andergrin&#39;s gravatar image" />
<p><span>andergrin</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andergrin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65917" class="comments-container">
<span id="65928"></span>
<div id="comment-65928" class="comment">
<div id="post-65928-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have managed to contact to admins via e-mail, and he changed tile server. Now everything working fine.</p>
</div>
<div id="comment-65928-info" class="comment-info">
<span class="comment-age">(17 Sep '18, 04:39)</span> <span class="comment-user userinfo">andergrin</span>
</div>
</div>
</div>
<div id="comment-tools-65917" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65917-form-container" class="comment-form-container">
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

<span id="65926"></span>

<div id="answer-container-65926" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65926-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65926-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65926-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your analysis of the situation was likely correct, however the tile cache setup was changed later this afternoon to not serve tiles to the Ukraine from Russia so the problem should have gone away by now.</p>
<p>Note this kind of issue is better raised on the <a href="https://github.com/openstreetmap/operations/issues">Operations issue tracker</a> or on the the #osm-dev IRC channel.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Sep '18, 22:47</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-65926" class="comments-container">
&#10;</div>
<div id="comment-tools-65926" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65926-form-container" class="comment-form-container">
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

