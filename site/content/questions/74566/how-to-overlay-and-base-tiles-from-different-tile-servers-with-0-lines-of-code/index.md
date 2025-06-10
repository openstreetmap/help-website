+++
type = "question"
title = "How to overlay and base tiles from different tile servers with 0 lines-of-code"
description = '''Does anyone know of a free tile server that returns a png tile combining two (or more) layer tiles from different base and layer tile servers in one layer? For instance, I want to combine (without any coding by me please) the following base and layer tiles:  https://a.tile.openstreetmap.org/${z}/${x...'''
date = "2020-05-03T14:27:00Z"
lastmod = "2020-05-03T17:27:00Z"
weight = 74566
keywords = [ "tile_server", "overlay", "flatten", "base", "combining" ]
aliases = [ "/questions/74566" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to overlay and base tiles from different tile servers with 0 lines-of-code](/questions/74566/how-to-overlay-and-base-tiles-from-different-tile-servers-with-0-lines-of-code)

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
<span id="post-74566-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74566-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74566-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Does anyone know of a free tile server that returns a png tile combining two (or more) layer tiles from different base and layer tile servers in one layer? For instance, I want to combine (without any coding by me please) the following base and layer tiles: <a href="https://a.tile.openstreetmap.org/$%7Bz%7D/$%7Bx%7D/$%7By%7D.png">https://a.tile.openstreetmap.org/${z}/${x}/${y}.png</a> <a href="http://tiles.openseamap.org/seamark/$%7Bz%7D/$%7Bx%7D/$%7By%7D.png">http://tiles.openseamap.org/seamark/${z}/${x}/${y}.png</a></p>
<p>It would be great if I could query a server like this: I specify on this ‘flattening meta tile server’ the two or Maybe more tile servers (in the right order of the layers), in return the server issues some unique identifier, for instance ‘12345’, and after that I can get my tiles using: <a href="https://flattened.tiles.openstreetmap.org/12345/$%7Bz%7D/$%7Bx%7D/$%7By%7D.png">https://flattened.tiles.openstreetmap.org/12345/${z}/${x}/${y}.png</a></p>
<p>Kind regards, Jasper</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tile_server" rel="tag" title="see questions tagged &#39;tile_server&#39;">tile_server</span> <span class="post-tag tag-link-overlay" rel="tag" title="see questions tagged &#39;overlay&#39;">overlay</span> <span class="post-tag tag-link-flatten" rel="tag" title="see questions tagged &#39;flatten&#39;">flatten</span> <span class="post-tag tag-link-base" rel="tag" title="see questions tagged &#39;base&#39;">base</span> <span class="post-tag tag-link-combining" rel="tag" title="see questions tagged &#39;combining&#39;">combining</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 May '20, 14:27</strong></p>
<img src="https://secure.gravatar.com/avatar/3d509943e71a0f9306faf574e3baca30?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jjddgg&#39;s gravatar image" />
<p><span>jjddgg</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jjddgg has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74566" class="comments-container">
<span id="74572"></span>
<div id="comment-74572" class="comment">
<div id="post-74572-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>There ain't no such things as a free lunch - someone, somewhere, is going to have to may hosting and bandwidth costs, and these are going to be significant since every time you make a tile request it's going to have to hit this third-party server, which is then going to have to query two other tile servers.</p>
<p>Why not just overlay <a href="http://tiles.openseamap.org/seamark/12/2049/1323.png">seamarks</a> over <a href="https://a.tile.openstreetmap.org/12/2049/1323.png">other tiles</a> using leaflet?</p>
<p>There are lots of examples on the <a href="https://leafletjs.com/examples.html">leaflet site</a>. If you want to see an example, have a look at the overlays <a href="https://map.atownsend.org.uk/maps/map/map.html">here</a>. The <a href="https://github.com/SomeoneElseOSM/SomeoneElse-map/blob/master/map/Scripts/leaflet_embed_small.js#L68">code</a> for that is simple - not 0 lines of code, but only about 6 - 3 to define a map layer used as an overlay and 3 to use it.</p>
</div>
<div id="comment-74572-info" class="comment-info">
<span class="comment-age">(03 May '20, 17:27)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-74566" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74566-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

