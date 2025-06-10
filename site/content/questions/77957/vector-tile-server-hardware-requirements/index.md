+++
type = "question"
title = "Vector tile server hardware requirements"
description = '''Hi there, I&#x27;m planning to create my own tile server to allow customize style and also allow me to get the vector tiles instead of raster tiles. But my budget is limited, so I want to know the minimum hardware requirement of vector tiles server. I read some Q&amp;amp;A like this, but all about raster til...'''
date = "2020-12-16T18:04:00Z"
lastmod = "2020-12-17T03:09:00Z"
weight = 77957
keywords = [ "hardware", "tiles", "vector", "tileserver", "custom_tiles" ]
aliases = [ "/questions/77957" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Vector tile server hardware requirements](/questions/77957/vector-tile-server-hardware-requirements)

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
<span id="post-77957-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77957-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77957-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there,</p>
<p>I'm planning to create my own tile server to allow customize style and also allow me to get the vector tiles instead of raster tiles. But my budget is limited, so I want to know the minimum hardware requirement of <strong>vector tiles</strong> server.</p>
<p>I read some Q&amp;A like this, but all about raster tiles, not vector tiles. If I understand right, the vector tiles server will lighter than raster because it can serve the vector directly to client without render (<a href="https://github.com/osm2vectortiles/osm2vectortiles/issues/457),">https://github.com/osm2vectortiles/osm2vectortiles/issues/457),</a> then client can use Leaflet of OpenLayer to style and display them.</p>
<p>So below are jobs that I think my server will do:</p>
<ul>
<li><p>Import/Sync data from OSM to postgresql using osm2pgsql (Maybe one time each month for Asia and America only).</p></li>
<li><p>Pre-create vector tiles for above data (I'm not sure I need this step or not).</p></li>
<li><p>Serve vector tiles to client on request.</p></li>
</ul>
<p>With above jobs, please help to let me know the minimum hardware requirement. Thank you so much!</p>
<p>Additional, I researched two days and it seems that all the free tile servers only served raster tiles (<a href="http://leaflet-extras.github.io/leaflet-providers/preview/).">http://leaflet-extras.github.io/leaflet-providers/preview/).</a> That is why I must create a tile server myself with a limited budget:sad:</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-hardware" rel="tag" title="see questions tagged &#39;hardware&#39;">hardware</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-vector" rel="tag" title="see questions tagged &#39;vector&#39;">vector</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span> <span class="post-tag tag-link-custom_tiles" rel="tag" title="see questions tagged &#39;custom_tiles&#39;">custom_tiles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Dec '20, 18:04</strong></p>
<img src="https://secure.gravatar.com/avatar/611ff06dfd6b8165defd20ce36a68fab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bahung1221&#39;s gravatar image" />
<p><span>bahung1221</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bahung1221 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Dec '20, 18:04</strong> </span></p>
</div>
</div>
<div id="comments-container-77957" class="comments-container">
<span id="77958"></span>
<div id="comment-77958" class="comment">
<div id="post-77958-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not really an answer to your question but regarding your last line I believe Mapbox has vector tiles and a <a href="https://www.mapbox.com/pricing/">free tier</a>.</p>
</div>
<div id="comment-77958-info" class="comment-info">
<span class="comment-age">(16 Dec '20, 20:53)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="77961"></span>
<div id="comment-77961" class="comment">
<div id="post-77961-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I considered Mapbox before, but some people say that Mapbox has a rate limit for maximum tiles each user can download (for offline usage). <a href="https://stackoverflow.com/questions/37781166/ios-mapbox-map-offline-price.">https://stackoverflow.com/questions/37781166/ios-mapbox-map-offline-price.</a> is it right?</p>
</div>
<div id="comment-77961-info" class="comment-info">
<span class="comment-age">(17 Dec '20, 03:06)</span> <span class="comment-user userinfo">bahung1221</span>
</div>
</div>
<span id="77962"></span>
<div id="comment-77962" class="comment">
<div id="post-77962-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I also curious about how they calculate "Active User Monthly", what they say on the pricing page makes me a bit confused. Maybe I should contact them about this question. Anyway, thanks for your help</p>
</div>
<div id="comment-77962-info" class="comment-info">
<span class="comment-age">(17 Dec '20, 03:09)</span> <span class="comment-user userinfo">bahung1221</span>
</div>
</div>
</div>
<div id="comment-tools-77957" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77957-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

