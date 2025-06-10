+++
type = "question"
title = "mapnik rendering error : icesheet relation error"
description = '''Hi i ve followed the tutorial from switch2osm.org to render osm maps using mapnik. i get errors after the command renderd -f -c /usr/local/etc/renderd.conf : renderd[6862]: An error occurred while loading the map layer &#x27;ajt&#x27;: Postgis Plugin: ERREUR: la relation « icesheet_polygons » n&#x27;existe pas LIN...'''
date = "2020-09-30T17:16:00Z"
lastmod = "2020-09-30T18:26:00Z"
weight = 76904
keywords = [ "rendering", "switch2osm", "relation", "icesheet", "mapnik" ]
aliases = [ "/questions/76904" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [mapnik rendering error : icesheet relation error](/questions/76904/mapnik-rendering-error-icesheet-relation-error)

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
<span id="post-76904-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76904-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76904-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi i ve followed the tutorial from switch2osm.org to render osm maps using mapnik. i get errors after the command renderd -f -c /usr/local/etc/renderd.conf :</p>
<p>renderd[6862]: An error occurred while loading the map layer 'ajt': Postgis Plugin: ERREUR: la relation « icesheet_polygons » n'existe pas LINE 1: SELECT ST_SRID("way") AS srid FROM icesheet_polygons WHERE "... ^ in executeQuery Full sql was: 'SELECT ST_SRID("way") AS srid FROM icesheet_polygons WHERE "way" IS NOT NULL LIMIT 1;' encountered during parsing of layer 'icesheet-poly' in Layer at line 5895 of '/home/user/src/openstreetmap-carto/mapnik.xml' renderd[6862]: An error occurred while loading the map layer 'ajt': Postgis Plugin: ERREUR: la relation « icesheet_polygons » n'existe pas LINE 1: SELECT ST_SRID("way") AS srid FROM icesheet_polygons WHERE "... ^</p>
<p>I was told about getting into lua coding to understand and tweak relations in the osm.pbf files but i didnt go into that yet. Where would the error come from please and how can i fix it? thank you regards</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-switch2osm" rel="tag" title="see questions tagged &#39;switch2osm&#39;">switch2osm</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-icesheet" rel="tag" title="see questions tagged &#39;icesheet&#39;">icesheet</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Sep '20, 17:16</strong></p>
<img src="https://secure.gravatar.com/avatar/3b06e83c0577f4870b867ce1811da81c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kr1p&#39;s gravatar image" />
<p><span>kr1p</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kr1p has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76904" class="comments-container">
&#10;</div>
<div id="comment-tools-76904" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76904-form-container" class="comment-form-container">
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

<span id="76905"></span>

<div id="answer-container-76905" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76905-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76905-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76905-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A susbsequent conversation on IRC (with someone who may be the same person) suggests that the "Shapefile download" bits of <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/</a> weren't done.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Sep '20, 18:26</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-76905" class="comments-container">
&#10;</div>
<div id="comment-tools-76905" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76905-form-container" class="comment-form-container">
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

