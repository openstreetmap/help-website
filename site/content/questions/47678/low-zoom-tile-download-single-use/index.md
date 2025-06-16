+++
type = "question"
title = "Low zoom tile download single use"
description = '''Hi, My objective is to get tiles for the whole world, at zoom levels 0-9, one time, for offline use. I&#x27;m trying to figure out the best way to do this. I know the &quot;proper&quot; method is to download OSM data and then run a tile server. However, this seems overly complicated considering the application. I ...'''
date = "2016-01-27T18:33:00Z"
lastmod = "2016-01-28T13:06:00Z"
weight = 47678
keywords = [ "download", "tiles" ]
aliases = [ "/questions/47678" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Low zoom tile download single use](/questions/47678/low-zoom-tile-download-single-use)

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
<span id="post-47678-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47678-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-47678-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, My objective is to get tiles for the whole world, at zoom levels 0-9, one time, for offline use. I'm trying to figure out the best way to do this.</p>
<p>I know the "proper" method is to download OSM data and then run a tile server. However, this seems overly complicated considering the application. I think I'd have to download the entire (60+GB?) OSM data set, despite having no need for most of the data that would only be valuable at higher zoom levels, and I would have to figure out how to set up style sheets, mapnik, etc, all to just run once.</p>
<p>I know there are ways to download tiles directly (eg JTileDownloader). I also know there is a tile usage policy which says not to download large amounts of tile data. <a href="https://wiki.openstreetmap.org/wiki/Tile_usage_policy.">https://wiki.openstreetmap.org/wiki/Tile_usage_policy.</a> At what point is downloading considered excessive, eg I'd be doing a few hundred thousand tiles, once per year (or even less frequent), not multi-million tiles on a regular basis. And the tiles are already rendered/cached, I would not need them regenerated. So I think my application is not putting a major load on the servers, but perhaps someone could clarify that? (Or should I just try to contact a system administrator directly to make this request?)</p>
<p>If there are other options, please let me know. I know various resources say that Mapquest tiles can be bulk downloaded, but I'm not totally sure if terms have recently changed.</p>
<p>Thanks for your feedback!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jan '16, 18:33</strong></p>
<img src="https://secure.gravatar.com/avatar/710db8195bd1bae2793a15ec42aa538d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sacrawford&#39;s gravatar image" />
<p><span>sacrawford</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sacrawford has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47678" class="comments-container">
<span id="47704"></span>
<div id="comment-47704" class="comment">
<div id="post-47704-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, that page says "To avoid having your access blocked, please discuss your requirement with system administrators either via their wiki pages or on the IRC channel prior to starting." https://wiki.openstreetmap.org/wiki/System_Administrators <a href="https://wiki.openstreetmap.org/wiki/IRC">https://wiki.openstreetmap.org/wiki/IRC</a> , so that's probably where I would start. Hundreds of thousands of tiles does sound significant, especially since most of those tiles would be empty (open sea) tiles.</p>
</div>
<div id="comment-47704-info" class="comment-info">
<span class="comment-age">(28 Jan '16, 13:06)</span> <span class="comment-user userinfo">Piskvor</span>
</div>
</div>
</div>
<div id="comment-tools-47678" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47678-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

