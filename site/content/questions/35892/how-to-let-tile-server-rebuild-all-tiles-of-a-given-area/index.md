+++
type = "question"
title = "How to let tile server rebuild all tiles of a given area?"
description = '''If I need to dirty all tiles of a given zoomlevel and area, how do I do that? Is there a way to find out the URLs of the tiles currently displayed, to then append /dirty to them? e.g. https://www.openstreetmap.org/#map=16/44.2611/15.2978 I know that it rerenders them after some period of time after b...'''
date = "2014-08-16T16:38:00Z"
lastmod = "2014-08-17T10:44:00Z"
weight = 35892
keywords = [ "zoomlevel", "tiles", "dirty" ]
aliases = [ "/questions/35892" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to let tile server rebuild all tiles of a given area?](/questions/35892/how-to-let-tile-server-rebuild-all-tiles-of-a-given-area)

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
<span id="post-35892-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35892-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-35892-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If I need to dirty all tiles of a given zoomlevel and area, how do I do that? Is there a way to find out the URLs of the tiles currently displayed, to then append /dirty to them?</p>
<p>e.g. <a href="https://www.openstreetmap.org/#map=16/44.2611/15.2978">https://www.openstreetmap.org/#map=16/44.2611/15.2978</a></p>
<p>I know that it rerenders them after some period of time after beeing last accessed. But in the map posted above it has rendered one of the tiles one half and cut of the parking sign and the restaurant.</p>
<p>Edit: Now it has rerendere the faulty tile automatically. But the questions remains.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zoomlevel" rel="tag" title="see questions tagged &#39;zoomlevel&#39;">zoomlevel</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-dirty" rel="tag" title="see questions tagged &#39;dirty&#39;">dirty</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Aug '14, 16:38</strong></p>
<img src="https://secure.gravatar.com/avatar/0b590312e396aae3377e31b3a3291d1e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Linutux&#39;s gravatar image" />
<p><span>Linutux</span><br />
<span class="score" title="76 reputation points">76</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Linutux has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Aug '14, 18:47</strong> </span></p>
</div>
</div>
<div id="comments-container-35892" class="comments-container">
<span id="35902"></span>
<div id="comment-35902" class="comment">
<div id="post-35902-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't have a ready solution, but here are the <a href="https://wiki.openstreetmap.org/wiki/Tile_expire_methods">manual instructions</a> to trigger renderd.</p>
</div>
<div id="comment-35902-info" class="comment-info">
<span class="comment-age">(16 Aug '14, 22:27)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="35911"></span>
<div id="comment-35911" class="comment">
<div id="post-35911-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As a bit of background, it might be worth looking at <a href="/questions/178/how-often-does-the-main-mapnik-map-get-updated">this previous question</a>, which explains how the rerendering process works. One exception to the "normally updates within a few minutes" conclusion of the main answer there is after the "standard" stylesheet has changed, as all tiles are effectively out of date. IF you look at <a href="/questions/527/how-can-i-make-sense-of-muninopenstreetmaporg/528">this other previous answer</a> it explains a bit about this - and the second link from that answer is to a munin graph showing the <a href="http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/renderd_queue.html">queue of tiles to be rendered</a>.</p>
<p>What this means is that if you spot an area that's out of date it might be because a stylesheet update has just happened (the project for that is <a href="https://github.com/gravitystorm/openstreetmap-carto">here</a>; after a release is made there it is usually taken live on osm.org by the admins shortly afterwards).</p>
</div>
<div id="comment-35911-info" class="comment-info">
<span class="comment-age">(17 Aug '14, 10:44)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-35892" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35892-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

