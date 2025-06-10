+++
type = "question"
title = "Exporting OSM Tiles"
description = '''I am interested using a slippy map to download OSM tiles. In doing so, I intend to stay within OSM tile usage policies (such as setting up my own tile server, or renting space from a commercial server) for high volume use). I noticed the official openstreetmaps.org slippy map has an &#x27;export&#x27; tab, gr...'''
date = "2012-02-07T23:24:00Z"
lastmod = "2012-03-08T18:44:00Z"
weight = 10478
keywords = [ "extract", "export" ]
aliases = [ "/questions/10478" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Exporting OSM Tiles](/questions/10478/exporting-osm-tiles)

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
<span id="post-10478-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10478-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-10478-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am interested using a slippy map to download OSM tiles. In doing so, I intend to stay within OSM tile usage policies (such as setting up my own tile server, or renting space from a commercial server) for high volume use).</p>
<p>I noticed the official <a href="http://openstreetmaps.org">openstreetmaps.org</a> slippy map has an 'export' tab, grabbing sections of map at a given zoom level. I have a few questions about this:</p>
<ul>
<li>How would I deploy a slippy map with the 'export' tab enabled?</li>
<li>When exporting a tile layer (say, Mapnik) to an image format (jpeg or png) how is the bounding box determined? Is the export function grabbing the nearest whole tiles (grabbing extra tile area) or is it generating an image that aligns with the users' view window, cut to the pixel?</li>
<li>Is there an API sufficient to allow me to trigger this command programatically over a series of zoom levels, with the same bounding box?</li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Feb '12, 23:24</strong></p>
<img src="https://secure.gravatar.com/avatar/3704877a9e7005245fb52ad23d3a553f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="benford&#39;s gravatar image" />
<p><span>benford</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="benford has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-10478" class="comments-container">
&#10;</div>
<div id="comment-tools-10478" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10478-form-container" class="comment-form-container">
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

<span id="10480"></span>

<div id="answer-container-10480" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10480-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10480-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-10480-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="benford has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The export tab is a complex beast that does a number of technologically very different things.</p>
<p>For "Mapnik" style raster images, the request is forwarded to code that runs on the tile server, where a Mapnik installation and an up-to-date osm2pgsql-generated OSM database are available to generate custom renderings. This will not export tiles in any way, but render the precise rectangle in the precise resolution chosen. To mimick that, you would have to have the same technology in place. Essentially you could use <a href="http://generate_image.py">generate_image.py</a> or <a href="http://trac.mapnik.org/wiki/Nik2Img">nik2img.py</a> to simulate what goes on there; I would also suggest these command line utilities as your "API to allow you to trigger this command programmatically".</p>
<p>For raster images in the soon-to-be-removed "Osmarender" style, the backend will indeed use existing tiles and paste them into an image, cropping it to match the requested area. I don't know the exact implementation but it is bound to be something like the scripts featured on the <a href="http://wiki.openstreetmap.org/wiki/Static_map_images">Static map images</a> page on the Wiki. Those scripts are also what you would use if you had your own tile server and wanted to create static "pasted tiles" images of that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Feb '12, 10:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-10480" class="comments-container">
<span id="11060"></span>
<div id="comment-11060" class="comment">
<div id="post-11060-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's just what I was looking for, thanks. Would there be a publicly available source from which I can download the mentioned python scripts?</p>
</div>
<div id="comment-11060-info" class="comment-info">
<span class="comment-age">(08 Mar '12, 16:55)</span> <span class="comment-user userinfo">benford</span>
</div>
</div>
<span id="11061"></span>
<div id="comment-11061" class="comment">
<div id="post-11061-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://svn.openstreetmap.org/applications/rendering/mapnik/">http://svn.openstreetmap.org/applications/rendering/mapnik/</a> or <a href="http://code.google.com/p/mapnik-utils/wiki/Nik2Img,">http://code.google.com/p/mapnik-utils/wiki/Nik2Img,</a> respectively.</p>
</div>
<div id="comment-11061-info" class="comment-info">
<span class="comment-age">(08 Mar '12, 18:44)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-10480" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10480-form-container" class="comment-form-container">
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

