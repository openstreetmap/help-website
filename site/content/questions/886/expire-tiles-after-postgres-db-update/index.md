+++
type = "question"
title = "Expire tiles after Postgres DB update"
description = '''I am creating my own tile server for OSM using Windows Server 2003. I need help on how to make tiles expire and create new tiles after updating my postgres DB with osm diffs. Since I am using Windows 2003, I can not use mod_tile. Here is my stack so far:  Data: OSM Planet dump DB: Postgres with Post...'''
date = "2010-09-21T15:47:00Z"
lastmod = "2010-09-21T20:54:00Z"
weight = 886
keywords = [ "diff", "tiles", "expiry" ]
aliases = [ "/questions/886" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Expire tiles after Postgres DB update](/questions/886/expire-tiles-after-postgres-db-update)

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
<span id="post-886-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-886-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-886-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am creating my own tile server for OSM using Windows Server 2003.<br />
I need help on how to make tiles expire and create new tiles after updating my postgres DB with osm diffs.</p>
<p>Since I am using Windows 2003, I can not use mod_tile. Here is my stack so far:</p>
<ol>
<li>Data: OSM Planet dump</li>
<li>DB: Postgres with PostGIS</li>
<li>Web Server: Apache Tomcat</li>
<li>OS: Windows Server 2003</li>
<li>UI: OpenLayers</li>
<li>DB loader: osm2pgsql</li>
<li>Tile Maker: Mapnik</li>
</ol>
<p>I am currently serving up tiles from a folder on my server using the OpenLayers.Layer.OSM class, i.e. I am not using TileCache or anything else. I see you can you use the --expire-tiles option within osm2pgsql to create a list of expired tiles after you append new OSM data into the DB.<br />
How do I use this option to then create new tiles? Is this the right way to even proceed?<br />
Any help would be greatly appreciated. Please feel free to be as detailed as you can afford ;-)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-diff" rel="tag" title="see questions tagged &#39;diff&#39;">diff</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-expiry" rel="tag" title="see questions tagged &#39;expiry&#39;">expiry</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Sep '10, 15:47</strong></p>
<img src="https://secure.gravatar.com/avatar/fbb15843641ffaf1c2259cc7ebb4735c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maw269&#39;s gravatar image" />
<p><span>maw269</span><br />
<span class="score" title="115 reputation points">115</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maw269 has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Sep '10, 16:13</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></br></p>
</div>
</div>
<div id="comments-container-886" class="comments-container">
<span id="898"></span>
<div id="comment-898" class="comment">
<div id="post-898-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>May I ask where mod_tile fails on windows? Given that it is a apache module, it should be crossplatform capable. I don't know of anyone who has tried it though, so it might well need some tweeks to get it to build.</p>
</div>
<div id="comment-898-info" class="comment-info">
<span class="comment-age">(21 Sep '10, 20:54)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
</div>
<div id="comment-tools-886" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-886-form-container" class="comment-form-container">
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

<span id="895"></span>

<div id="answer-container-895" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-895-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-895-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-895-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="maw269 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First of all, you have to understand that this is not a high performance setup and that you will not be able to keep a current set of tiles for anything larger than a small country with this. With no on-demand tile rendering you will always struggle to keep every single tile current, spending lots of CPU cycles for nothing.</p>
<p>You are probably using generate-tiles.py from the OSM Mapnik SVN. There is a function in there that calculates a single tile. With a little bit of Python you should be able to adapt the script to actually read the file generated by osm2pgsql and call the tile compute routine for each tile in that file. I am not aware of a ready-made solution for that in a renderd setup you could use render_expired but you'll have to do it that way.</p>
<p>You can request osm2pgsql to output a list of modified tiles for a whole range of zoom levels. Be aware that if you include small zoom levels then the tiles on these zoom levels will be rendered very often; you might want to employ some grep/sort magic and re-render those only once every few days.</p>
<p>All in all, the mechanisms involved are complex and PostGIS caching performance is less if you render a flurry of new tiles across a large area compared to systematically rendering all tiles. You might find that with the rather small area you're able to cover with your setup anyway, it might be easier and not even slower to just re-render the whole lot once in a while rather than trying to process updates.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Sep '10, 19:31</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-895" class="comments-container">
&#10;</div>
<div id="comment-tools-895" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-895-form-container" class="comment-form-container">
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

