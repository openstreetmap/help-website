+++
type = "question"
title = "Dynamically generate tiles with different Mapnik XML file without restarting renderd"
description = '''I am attempting to allow users to view a map and use UI components, such as checkboxes, to toggle certain layers of data on or off. Each time a user toggles a layer on, it should send a request to my tile server with the layers that should be visible (LayerX status=&quot;on&quot;, LayerY status=&quot;on&quot;).  The de...'''
date = "2017-10-17T19:30:00Z"
lastmod = "2017-10-17T21:59:00Z"
weight = 60155
keywords = [ "renderd", "mapnik", "mod_tile" ]
aliases = [ "/questions/60155" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dynamically generate tiles with different Mapnik XML file without restarting renderd](/questions/60155/dynamically-generate-tiles-with-different-mapnik-xml-file-without-restarting-renderd)

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
<span id="post-60155-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60155-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60155-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am attempting to allow users to view a map and use UI components, such as checkboxes, to toggle certain layers of data on or off. Each time a user toggles a layer on, it should send a request to my tile server with the layers that should be visible (LayerX status="on", LayerY status="on").</p>
<p>The default for all of my layers in the Mapnik XML style file is status="off". Is there currently a method of passing these parameters to the renderd service and dynamically changing the XML file before rendering the tiles?</p>
<p>Since each request has the possibility to generate a new version of a tile, I would not like to cache each request. How can I turn off mod_tile's caching abilities to prevent tiles with the wrong data being returned the the client?</p>
<p>From what I have noticed, after every change to the XML file, renderd is required to be restarted. Is it possible to not restart renderd, but modify the XML file to display different layers?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Oct '17, 19:30</strong></p>
<img src="https://secure.gravatar.com/avatar/57a3221d36da383f5c0a6f5b29f611cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pantaphobic&#39;s gravatar image" />
<p><span>pantaphobic</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pantaphobic has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60155" class="comments-container">
<span id="60156"></span>
<div id="comment-60156" class="comment">
<div id="post-60156-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No idea about within Mapnik, but could you perhaps have different layers of tiles turned on and off within Leaflet?</p>
</div>
<div id="comment-60156-info" class="comment-info">
<span class="comment-age">(17 Oct '17, 19:32)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="60157"></span>
<div id="comment-60157" class="comment">
<div id="post-60157-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am not currently using and am not planning on using leaflet. I am using the google maps API to get the base world map and adding transparent tiles overtop of that rendered by Mapnik.</p>
</div>
<div id="comment-60157-info" class="comment-info">
<span class="comment-age">(17 Oct '17, 20:09)</span> <span class="comment-user userinfo">pantaphobic</span>
</div>
</div>
</div>
<div id="comment-tools-60155" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60155-form-container" class="comment-form-container">
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

<span id="60159"></span>

<div id="answer-container-60159" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60159-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60159-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-60159-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You'll probably not want to use renderd and mod_tile, but instead something like "LiveTiles" (<a href="https://github.com/openstreetmap/mapnik-stylesheets/blob/master/livetiles/livetiles.wsgi">https://github.com/openstreetmap/mapnik-stylesheets/blob/master/livetiles/livetiles.wsgi</a> - but there are other similar implementations). This never caches tiles. You'll have to add a little code that parses a layer list from the tile URL and switches on the layers before actually rendering the tile but that's only a few lines of code.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Oct '17, 21:38</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-60159" class="comments-container">
<span id="60160"></span>
<div id="comment-60160" class="comment">
<div id="post-60160-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This looks exactly like what I need, but I am a bit concerned with the following line in their documentation: "render live mapnik tiles on request which is handy for maintenance of mapnik styles and completely unsuitable for a production tileserver." Do you think for my unique use case this should be ignored?</p>
</div>
<div id="comment-60160-info" class="comment-info">
<span class="comment-age">(17 Oct '17, 21:43)</span> <span class="comment-user userinfo">pantaphobic</span>
</div>
</div>
<span id="60161"></span>
<div id="comment-60161" class="comment">
<div id="post-60161-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>According to open street maps documentation, it looks like this tool was replaced by TileLite. I will look into it further, thank you for the recommendation! <a href="http://wiki.openstreetmap.org/wiki/User:Stanton/Mapnik_Test_Server#Live_Rendering_with_LiveTiles_TileLite">http://wiki.openstreetmap.org/wiki/User:Stanton/Mapnik_Test_Server#Live_Rendering_with_LiveTiles_TileLite</a></p>
</div>
<div id="comment-60161-info" class="comment-info">
<span class="comment-age">(17 Oct '17, 21:49)</span> <span class="comment-user userinfo">pantaphobic</span>
</div>
</div>
<span id="60162"></span>
<div id="comment-60162" class="comment">
<div id="post-60162-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The whole approach of rendering <em>all</em> tiles on demand is unsuitable for a production server if you are using a style that comes anywhere near the standard style in complexity. However, if your layers are relatively simple and your database small then you can get away with it. The problem with the approach is that not only does it not cache tiles, it also doesn't do meta tiles which leads to a higher load on the database. For your particular use case, TileLite or LiveTiles probably does not make a difference.</p>
</div>
<div id="comment-60162-info" class="comment-info">
<span class="comment-age">(17 Oct '17, 21:59)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-60159" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60159-form-container" class="comment-form-container">
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

