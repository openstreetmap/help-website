+++
type = "question"
title = "Need clarification on tile creation strategy"
description = '''Hello, I&#x27;m new to all things OSM. I&#x27;m quite confused on all of the different directions I need to go to get the result I want. I want to convert our website slippy maps from google maps api maps to OSM maps, either as background terrain OSM baselayer within the Google MAPs API, or as terrain OSM til...'''
date = "2012-02-16T19:01:00Z"
lastmod = "2012-02-17T10:23:00Z"
weight = 10614
keywords = [ "openlayers", "tilemill", "switch2osm", "terrain", "tiles" ]
aliases = [ "/questions/10614" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Need clarification on tile creation strategy](/questions/10614/need-clarification-on-tile-creation-strategy)

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
<span id="post-10614-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10614-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-10614-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I'm new to all things OSM. I'm quite confused on all of the different directions I need to go to get the result I want. I want to convert our website slippy maps from google maps api maps to OSM maps, either as background terrain OSM baselayer within the Google MAPs API, or as terrain OSM tiles within an OpenLayers UI. I'd prefer to do everything with OpenLayers and serve my own OSM tiles if possible, but I've come to enjoy the ease of data management using Google's Fusion tables for my point data. I guess I can't have it all. I have FTP access to our hosted website (which has PostgreSQL databases) but I don't have command line access (though it is a unix based server). I have a spare machine I could load up with some sort of LAMP type of setup, but I can't have that on the internet, it would only be for generating a tile set for the area in question, and then copying those tiles to my real webhost for serving tiles for an OpenLayers Map.</p>
<p>I've browsed the <a href="http://switch2osm.org">switch2osm.org</a> site, and it was a little helpful in explaining that I need to generate tiles, then serve those tiles somehow on my webhost. My tiles don't need to change over time, so I only need to generate them once. I've seen that Michal Migurski has created a collection of files on Github for generating a US OSM terrain map (<a href="https://github.com/Citytracking/Terrain)">https://github.com/Citytracking/Terrain)</a> but I'm confused on how to use this. I've downloaded TillMill for windows, and from what I gather this is supposed to allow me to use OSM data to create terrain tiles. I only want to create tiles for an area of about 5 states. I'm confused as to what to do next in order to create these terrain tiles. Can anyone provide any suggestions on my strategy to create those terrain tiles, and if my end result of using and serving those tiles on my own webhost is possible? Any thoughts would be welcome to this confused beginner. Thank you. _Jan</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-tilemill" rel="tag" title="see questions tagged &#39;tilemill&#39;">tilemill</span> <span class="post-tag tag-link-switch2osm" rel="tag" title="see questions tagged &#39;switch2osm&#39;">switch2osm</span> <span class="post-tag tag-link-terrain" rel="tag" title="see questions tagged &#39;terrain&#39;">terrain</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Feb '12, 19:01</strong></p>
<img src="https://secure.gravatar.com/avatar/78bee09d80e970fdf31f7a0b7ae994cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JLD_in_DC&#39;s gravatar image" />
<p><span>JLD_in_DC</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JLD_in_DC has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-10614" class="comments-container">
&#10;</div>
<div id="comment-tools-10614" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10614-form-container" class="comment-form-container">
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

<span id="10620"></span>

<div id="answer-container-10620" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10620-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10620-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-10620-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Pre-generating tiles for "just 5 [USA] states" would already take a <a href="http://help.openstreetmap.org/questions/6062/how-large-in-disk-size-is-a-current-complete-tile-set">huge amount of disk space</a> if you're interested in the higher zooms. I wouldn't pre-generate tiles for anything bigger than, say, France, and even then only if you have a lot of disk space and CPU to throw at it.</p>
<p>The other prliminary question is : do you really need to generate and serve your own tiles ? Unless you want a custom map rendering or know that you will outgrow the <a href="http://wiki.openstreetmap.org/wiki/Tile_usage_policy">tile usage policy</a>, you can use one of the existing tiles provider and add you own data on top of it using OpenLayers. You'll save yourself a lot of trouble, and the tiles will be kept up to date.</p>
<p>If after that you still want to (pre)render you own tiles, check <a href="http://wiki.openstreetmap.org/wiki/Mapnik">mapnik</a> which is the most common way to do things. There's quite a lot more information on the wiki and many techniques depending on use-case, but it's getting out of my area of expertise so I'll let somebody else answer.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Feb '12, 10:23</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-10620" class="comments-container">
&#10;</div>
<div id="comment-tools-10620" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10620-form-container" class="comment-form-container">
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

