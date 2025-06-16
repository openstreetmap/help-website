+++
type = "question"
title = "After installation of OSM , how can i change the Map style (tile)"
description = '''Hi Guys, After successfully following next guide and setup of OSM https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/ and loading of a map from Geofabric into Postgre, now i would like to change the Map style to be different that i have locally on the server. As example i...'''
date = "2021-02-04T08:41:00Z"
lastmod = "2021-02-05T12:38:00Z"
weight = 78657
keywords = [ "stylesheet" ]
aliases = [ "/questions/78657" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [After installation of OSM , how can i change the Map style (tile)](/questions/78657/after-installation-of-osm-how-can-i-change-the-map-style-tile)

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
<span id="post-78657-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78657-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78657-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi Guys,</p>
<p>After successfully following next guide and setup of OSM <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/</a> and loading of a map from Geofabric into Postgre, now i would like to change the Map style to be different that i have locally on the server. As example i have now the below one :</p>
<p><img src="/upfiles/img_osm.PNG" alt="alt text" /></p>
<p>but eventually if i want to integrate let's say dark style from here <a href="https://github.com/openmaptiles/dark-matter-gl-style">https://github.com/openmaptiles/dark-matter-gl-style</a> what are the required steps to do it ? Or can you provide me a link with a guide how can i achive this.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-stylesheet" rel="tag" title="see questions tagged &#39;stylesheet&#39;">stylesheet</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Feb '21, 08:41</strong></p>
<img src="https://secure.gravatar.com/avatar/b4c6f7d35e4fd1b4561578e5e376ca06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DavorB0&#39;s gravatar image" />
<p><span>DavorB0</span><br />
<span class="score" title="22 reputation points">22</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DavorB0 has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-78657" class="comments-container">
&#10;</div>
<div id="comment-tools-78657" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78657-form-container" class="comment-form-container">
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

<span id="78679"></span>

<div id="answer-container-78679" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78679-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78679-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78679-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You've built a tile server for serving raster tiles. The style you mentioned is a vector tile style. The technical setup for those two are quite different.</p>
<p>You could setup a tileserver-gl (see <a href="https://tileserver.readthedocs.io/en/latest/">https://tileserver.readthedocs.io/en/latest/</a> ) for serving vector tiles in the dark-matter-gl-style. that you first have to produce (see more here: <a href="https://openmaptiles.org/docs/generate/generate-openmaptiles/">https://openmaptiles.org/docs/generate/generate-openmaptiles/</a> ).</p>
<p>Otherwise if you would rather stay in the raster tile world, you would have to rework the openstreetmap-carto style to suit your needs or find a another mapnik/cartocss raster style that fits your needs.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Feb '21, 12:38</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-78679" class="comments-container">
&#10;</div>
<div id="comment-tools-78679" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78679-form-container" class="comment-form-container">
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

