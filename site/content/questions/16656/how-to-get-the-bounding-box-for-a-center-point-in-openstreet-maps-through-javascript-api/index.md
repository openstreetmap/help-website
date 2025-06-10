+++
type = "question"
title = "[closed] How to get the bounding box for a center point in OpenStreet maps through Javascript API?"
description = '''Like Google maps have functions like getBounds (), getNorthEast (), and getSouthWest () for finding the corners in a viewport, do OpenStreet maps have anything similar? Question: How to get the bounding box for a center point in OpenStreet maps through Javascript API? Is this link of some relevance ...'''
date = "2012-10-04T12:24:00Z"
lastmod = "2012-10-05T12:23:00Z"
weight = 16656
keywords = [ "boundaries", "openstreetmap" ]
aliases = [ "/questions/16656" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [\[closed\] How to get the bounding box for a center point in OpenStreet maps through Javascript API?](/questions/16656/how-to-get-the-bounding-box-for-a-center-point-in-openstreet-maps-through-javascript-api)

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
<span id="post-16656-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16656-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16656-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Like Google maps have functions like <code>getBounds ()</code>, <code>getNorthEast ()</code>, and <code>getSouthWest ()</code> for finding the corners in a viewport, do <code>OpenStreet</code> maps have anything similar?</p>
<p>Question: <strong>How to get the bounding box for a center point in <code>OpenStreet</code> maps through <code>Javascript</code> API?</strong></p>
<p>Is this link of some relevance here?<br />
<a href="http://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#Tile_bounding_box">http://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#Tile_bounding_box</a></p>
<p>From that link:</p>
<pre><code>class BoundingBox {
    double north;
    double south;
    double east;
    double west;   
  }
  BoundingBox tile2boundingBox(final int x, final int y, final int zoom) {
    BoundingBox bb = new BoundingBox();
    bb.north = tile2lat(y, zoom);
    bb.south = tile2lat(y + 1, zoom);
    bb.west = tile2lon(x, zoom);
    bb.east = tile2lon(x + 1, zoom);
    return bb;
  }
&#10;  static double tile2lon(int x, int z) {
     return x / Math.pow(2.0, z) * 360.0 - 180;
  }
&#10;  static double tile2lat(int y, int z) {
    double n = Math.PI - (2.0 * Math.PI * y) / Math.pow(2.0, z);
    return Math.toDegrees(Math.atan(Math.sinh(n)));
  }</code></pre>
<p>In this code, what are the north east and south west coordinates?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Oct '12, 12:24</strong></p>
<img src="https://secure.gravatar.com/avatar/0848a0cab04ba90c16abc4c8f32904d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anisha%20Kaul&#39;s gravatar image" />
<p><span>Anisha Kaul</span><br />
<span class="score" title="29 reputation points">29</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anisha Kaul has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>04 Oct '12, 14:20</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-16656" class="comments-container">
<span id="16666"></span>
<div id="comment-16666" class="comment">
<div id="post-16666-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@SomeoneElse</span> I have read the FAQ. In which way do you think this is offtopic? Can't we have an bounding box solution for openstreet maps?</p>
</div>
<div id="comment-16666-info" class="comment-info">
<span class="comment-age">(04 Oct '12, 15:13)</span> <span class="comment-user userinfo">Anisha Kaul</span>
</div>
</div>
<span id="16669"></span>
<div id="comment-16669" class="comment">
<div id="post-16669-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The reason why questions that start "Like Google maps..." get closed here is that often they refer to the use of external Javascript libraries, which are documented elsewhere - the three links below are excellent places to start.<br />
</p>
<p>Openstreetmap is essentially "all about the data", and you can do with it what you like whereas with Google you're presented with only one way of interacting with map data - their "API".</p>
<p>(and actually, it wasn't me that originally closed the question - I reopened it to add a comment to it!)</p>
</div>
<div id="comment-16669-info" class="comment-info">
<span class="comment-age">(04 Oct '12, 16:32)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="16670"></span>
<div id="comment-16670" class="comment">
<div id="post-16670-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@SomeoneElse</span> The google maps thing was just an "example" - just to show that I made an effort. In fact I even linked a page there to ask for confirmation if I am looking in the right direction.</p>
<p>Is there a way that I can make it look on topic?</p>
</div>
<div id="comment-16670-info" class="comment-info">
<span class="comment-age">(04 Oct '12, 16:36)</span> <span class="comment-user userinfo">Anisha Kaul</span>
</div>
</div>
<span id="16671"></span>
<div id="comment-16671" class="comment">
<div id="post-16671-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>First, I'd have a read of the links below.<br />
</p>
<p>Specifically, if you read the Leaflet docs page you'll see "getBounds()" mentioned pretty near the top, which does exactly what you want. I'm sure that OpenLayers offers something similar.</p>
<p>However, until you've read a bit of background on how the OSM slippy map works (follow the <a href="http://wiki.openstreetmap.org/wiki/Slippy_Map">http://wiki.openstreetmap.org/wiki/Slippy_Map</a> link from the top of the page in your question) some of the references may be a bit confusing.</p>
</div>
<div id="comment-16671-info" class="comment-info">
<span class="comment-age">(04 Oct '12, 16:52)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="16673"></span>
<div id="comment-16673" class="comment">
<div id="post-16673-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@SomeoneElse</span> You've been helpful and thanks for that.</p>
</div>
<div id="comment-16673-info" class="comment-info">
<span class="comment-age">(04 Oct '12, 18:44)</span> <span class="comment-user userinfo">Anisha Kaul</span>
</div>
</div>
</div>
<div id="comment-tools-16656" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16656-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by SomeoneElse 04 Oct '12, 14:20

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16657"></span>

<div id="answer-container-16657" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16657-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16657-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-16657-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Anisha Kaul has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As OpenStreetMap is only a dataset it does not have those functions. You would have to look at javascript libraries for slippy maps like <a href="http://www.openlayers.org/">OpenLayers</a> or <a href="http://leaflet.cloudmade.com/">Leaflet</a> for that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Oct '12, 12:38</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span> </br></br></p>
</div>
</div>
<div id="comments-container-16657" class="comments-container">
<span id="16664"></span>
<div id="comment-16664" class="comment">
<div id="post-16664-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>And you might want to start looking <a href="http://switch2osm.org/using-tiles/">here</a>.</p>
</div>
<div id="comment-16664-info" class="comment-info">
<span class="comment-age">(04 Oct '12, 14:19)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="16693"></span>
<div id="comment-16693" class="comment">
<div id="post-16693-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Gnonthgol, I have found your leaflet link helpful. I am using that API now. Thanks to @SomeonElse too.</p>
</div>
<div id="comment-16693-info" class="comment-info">
<span class="comment-age">(05 Oct '12, 12:23)</span> <span class="comment-user userinfo">Anisha Kaul</span>
</div>
</div>
</div>
<div id="comment-tools-16657" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16657-form-container" class="comment-form-container">
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

