+++
type = "question"
title = "[closed] optimizing map tile trees"
description = '''I am building my own map tiles using the OSM data, with PostGIS and Mapnik (as explained, for instance, here). I am going to be serving these tiles from my own server, so I have a lot of flexibility in how I process a request for a tile. I have a few closely related questions: (1) When I&#x27;m running t...'''
date = "2011-08-20T00:53:00Z"
lastmod = "2011-08-20T01:17:00Z"
weight = 7209
keywords = [ "generate_tiles", "tiles", "optimization" ]
aliases = [ "/questions/7209" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [\[closed\] optimizing map tile trees](/questions/7209/optimizing-map-tile-trees)

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
<span id="post-7209-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7209-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7209-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am building my own map tiles using the OSM data, with PostGIS and Mapnik (as explained, for instance, <a href="http://www.bostongis.com/PrinterFriendly.aspx?content_name=generating_osm_tiles">here</a>).</p>
<p>I am going to be serving these tiles from my own server, so I have a lot of flexibility in how I process a request for a tile.</p>
<p>I have a few closely related questions:</p>
<p>(1) When I'm running the script to generate the tiles (<a href="http://generate_tiles_multiprocess.py"><code>generate_tiles_multiprocess.py</code></a>, in my case), for a huge percentage of the output tiles it writes "Empty Tile" to the script output line. My understanding is that "Empty Tile" actually means "a tile of just one color". So it might be all blue in a water area, or all green in a park area, or all gray in some other area. My question is whether there is a deeper meaning to "Empty Tile", specifically whether it means that all sub-tiles generated at higher levels will also be empty? For instance, if I generate a level 16 tile that is a gray "Empty Tile", does it mean when I generate level 17, and I am generating the four level 17 tiles that correspond to that one level 16 tile, that those four tiles will also be gray "Empty Tile", and the same for the 16 sub-tiles at level 18? Or, in contrast, is it possible for features that weren't visible in the level 16 tile to "appear" in that area at level 17 or level 18? Another way of saying it: Does "Empty Tile" mean that the tile is "empty all the way down"?</p>
<p>(2) Regardless of the answer to question to (1) above, suppose I have generated a full tree of tiles for a given area, all the way to level 18. Suppose there is a tile on level 15 that is all gray, and it turns that the four corresponding tiles on level 16, the 16 corresponding tiles on level 17, and the 64 corresponding tiles on level 18, are also all gray. A natural optimization of the tree is just to delete those level 16, 17, and 18 tiles (84 total tiles) from the tree altogether. Then, when the server goes to serve a tile and it's not present in the tree, it knows to "look up" to the parent levels of the tree as far as necessary until it finds a tile, and it knows that that tile (the all gray tile in this case) is good to use for the originally requested tile. My questions are: what is that optimization called? Is it commonly used? Is it discussed somewhere?</p>
<p>(3) Finally, I notice that many of the output tiles are very simple. First of all there is the huge number of one-color tiles. But there are also many two-color tiles with a very simple shape, such as a single line dividing a blue area from a gray area. I see that the one-color tiles are 103 byte .png files. The simple two-color tiles are typically anywhere from 1.0k to 1.5k. So it seems like a natural compression technique for these would be to use just three bytes ( R, G, B ) for the one-color files, and a simple run-length encoding scheme for the two-color files. Of course, to make this really save space on the disk it would be necessary to combine lots of these small files into some kind of multi-file that would be cached in memory on the server. But anyway for both storage and transmittal (as well as helping reduce cache missing when actually serving the data) it seems like there are many optimizations like this that could be employed. Can you tell me if these optimizations make sense, and where I can find documentation of how others have implemented stuff like this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-generate_tiles" rel="tag" title="see questions tagged &#39;generate_tiles&#39;">generate_tiles</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-optimization" rel="tag" title="see questions tagged &#39;optimization&#39;">optimization</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Aug '11, 00:53</strong></p>
<img src="https://secure.gravatar.com/avatar/8c7b62703cf744bb00d8064af6f73d04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Michael%20Katz&#39;s gravatar image" />
<p><span>Michael Katz</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michael Katz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>20 Aug '11, 01:05</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-7209" class="comments-container">
&#10;</div>
<div id="comment-tools-7209" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7209-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Unsuitable for help.osm" by Frederik Ramm 20 Aug '11, 01:05

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7210"></span>

<div id="answer-container-7210" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7210-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7210-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7210-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Michael Katz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This series of questions is not really suitable for a help system like this as it is very unlikely that there's one "good" answer for it. The <a href="http://lists.openstreetmap.org/listinfo/dev">dev mailing list</a> is a good place to discuss such complex issues. I have taken the liberty of moving your question there.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Aug '11, 01:04</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-7210" class="comments-container">
<span id="7211"></span>
<div id="comment-7211" class="comment">
<div id="post-7211-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>ok, thanks</p>
</div>
<div id="comment-7211-info" class="comment-info">
<span class="comment-age">(20 Aug '11, 01:17)</span> <span class="comment-user userinfo">Michael Katz</span>
</div>
</div>
</div>
<div id="comment-tools-7210" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7210-form-container" class="comment-form-container">
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

