+++
type = "question"
title = "Where to find/How to extract, world populated places (polygon) at city level?"
description = '''We have built a tile server for the whole planet using Mapnik and Mod_tile, however rendering is slow for populated regions (there are a lot of points and lines to be rendered). I implemented a simple application that pre-renders tiles for a given polygon. Now I want to use this app for all populate...'''
date = "2016-03-29T12:17:00Z"
lastmod = "2016-03-29T12:27:00Z"
weight = 48895
keywords = [ "shapefile", "generate_tiles", "mod_tile" ]
aliases = [ "/questions/48895" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Where to find/How to extract, world populated places (polygon) at city level?](/questions/48895/where-to-findhow-to-extract-world-populated-places-polygon-at-city-level)

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
<span id="post-48895-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48895-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48895-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We have built a tile server for the whole planet using Mapnik and Mod_tile, however rendering is slow for populated regions (there are a lot of points and lines to be rendered). I implemented a simple application that pre-renders tiles for a given polygon. Now I want to use this app for all populated places in the world.</p>
<p>Since we don't want to pre-render tiles for the whole planet, the polygons should be at city level and cover small portion of the planet. After searching on the Internet I could only find shape files with points, or with polygons but at country level which are not useful in our case</p>
<p>Is there anyway to extract this data directly from OSM database?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-generate_tiles" rel="tag" title="see questions tagged &#39;generate_tiles&#39;">generate_tiles</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Mar '16, 12:17</strong></p>
<img src="https://secure.gravatar.com/avatar/ca009706fa6df2b33eb931f781ff57f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="khamooshi&#39;s gravatar image" />
<p><span>khamooshi</span><br />
<span class="score" title="146 reputation points">146</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="khamooshi has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-48895" class="comments-container">
&#10;</div>
<div id="comment-tools-48895" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48895-form-container" class="comment-form-container">
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

<span id="48896"></span>

<div id="answer-container-48896" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48896-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48896-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-48896-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="khamooshi has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Interesting approach.</p>
<p>The only available data set which I'm aware of is the Natural Earth one at <a href="http://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-urban-area/">1:10M resolution</a>. This has faults but might be fine for your needs.</p>
<p>I have been exploring how one might create such data directly from OSM, but this is very much work in progress, see various posts on <a href="http://sk53-osm.blogspot.co.uk/search/label/Urban%20Areas">my blog</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Mar '16, 12:27</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-48896" class="comments-container">
&#10;</div>
<div id="comment-tools-48896" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48896-form-container" class="comment-form-container">
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

