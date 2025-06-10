+++
type = "question"
title = "Create several medium svg/jpg images with marker and road names to serve with Django"
description = '''I would like to create several (200/day) map images of max size 400x400. Those images will be served online -to anyone- using Django. The desired contents and properties of each image include:  Road names Zoom 17 or 18  A marker at the center which represents the coordinates of interest. Max size 40...'''
date = "2016-07-19T16:13:00Z"
lastmod = "2016-07-19T16:13:00Z"
weight = 50986
keywords = [ "marker", "svg", "mapnik", "staticmap" ]
aliases = [ "/questions/50986" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Create several medium svg/jpg images with marker and road names to serve with Django](/questions/50986/create-several-medium-svgjpg-images-with-marker-and-road-names-to-serve-with-django)

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
<span id="post-50986-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50986-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50986-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to create several (200/day) map images of max size 400x400.</p>
<p>Those images will be served online -to anyone- using Django.</p>
<p>The desired contents and properties of each image include:</p>
<ul>
<li>Road names</li>
<li>Zoom 17 or 18</li>
<li>A marker at the center which represents the coordinates of interest.</li>
<li>Max size 400x400</li>
<li>svg format (jpg -at least- for smaller filesize compared to png)</li>
</ul>
<p>A <a href="http://wiki.openstreetmap.org/wiki/Static_map_images">static map image</a> seems not to be an option because the services that may provide it either:</p>
<ul>
<li>Are not free after a number of requests</li>
<li>Do not provide svg or jpg formats</li>
<li>Do not provide a marker</li>
</ul>
<p>The most realistic idea might be to create the images on my server(s)(or home box somehow) with a call to a script, for the first time, and then serve the created file while keep runing a task of updating the older images.</p>
<p>Searching around for such a setup, I find that I have to use <a href="http://wiki.openstreetmap.org/wiki/Mapnik">mapnik</a> on a <a href="http://wiki.openstreetmap.org/wiki/PostGIS/Installation">postgis</a> installation.</p>
<p>Supposing that svg is the prefered format due to its quality of display on retina images:</p>
<ul>
<li>Is there a simpler or more capable solution for this task?</li>
</ul>
<p>If not, I have scatterly read the following issues for svg images and mapnik:</p>
<ul>
<li>Mapnik may produce <a href="http://wiki.openstreetmap.org/wiki/SVG">clunky svg files (on a cairo surface)</a>.</li>
<li>An svg image may not include the road names.</li>
</ul>
<p>Are the above difficult to resolve on a self-hosted setup?</p>
<p>Some help or a different approach is very much appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-svg" rel="tag" title="see questions tagged &#39;svg&#39;">svg</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-staticmap" rel="tag" title="see questions tagged &#39;staticmap&#39;">staticmap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jul '16, 16:13</strong></p>
<img src="https://secure.gravatar.com/avatar/f2f6dc29829d698cb1f763a6da99bb48?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="raratiru&#39;s gravatar image" />
<p><span>raratiru</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="raratiru has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jul '16, 23:19</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-50986" class="comments-container">
&#10;</div>
<div id="comment-tools-50986" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50986-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

