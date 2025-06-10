+++
type = "question"
title = "Vector Tiles with MapZen/multi-polygon lists"
description = '''Hi, is anyone here familiar with using the vector tiles supplied from MapZen? I am currently having an issue with the layering of the geometry, there seems to be a lack of documentation on this matter, or none that I can find, so as an example if I layer ocean geometry behind land geometry then rive...'''
date = "2016-01-12T12:24:00Z"
lastmod = "2016-01-12T12:24:00Z"
weight = 47475
keywords = [ "tiles", "vector", "mapzen" ]
aliases = [ "/questions/47475" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Vector Tiles with MapZen/multi-polygon lists](/questions/47475/vector-tiles-with-mapzenmulti-polygon-lists)

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
<span id="post-47475-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47475-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47475-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, is anyone here familiar with using the vector tiles supplied from MapZen? I am currently having an issue with the layering of the geometry, there seems to be a lack of documentation on this matter, or none that I can find, so as an example if I layer ocean geometry behind land geometry then river mouths and other details along coastal regions are not visible, but if I layer ocean in front of land I get pretty much the same effect, the ocean overlaps some of the coastal detail again in different areas, where the other none visible details are now visible. Also i'm not sure if I am handling MultiPolygon groups correctly, for multi-polygon groups I am creating a bunch of separate polygons from the lists, should they be stitched together in some way? it could be possible that if I am not handling polygons correctly this is giving me bugs, ill attach a couple of images to better illustrate what is happening and it may make it easier to outline the bugs. this is what it looks like with ocean behind: <a href="http://imgur.com/3ggXvGF">http://imgur.com/3ggXvGF</a> and this is what it looks like with ocean in front: <a href="http://imgur.com/57t0rt4">http://imgur.com/57t0rt4</a></p>
<p>also its worth noting that this is implemented with opengl using vbo's, I know there is no issue with the data upload to the graphics card as I have been using this opengl code base for plenty of other things, the only issue that side could be with the coordinate generation.</p>
<p>Edit: Ok after looking into the issue further I believe it is an issue with the way i am treating multi-polygons, after doing some research on them it seems that multi-polygon lists are complex polygons, i.e polygons with holes in them, with this in mind I can think of a pretty simple way to render the polygons with holes using the stencil buffer inside opengl, where i use all the sub polys, i.e the holes as my stencils, I have made a quick attempt at doing this but the stencil shapes that I am getting don't make sense for the layer they are on and the associated polygon that they are holes for, does anyone know the definitive way to decode the multi-polygon lists?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-vector" rel="tag" title="see questions tagged &#39;vector&#39;">vector</span> <span class="post-tag tag-link-mapzen" rel="tag" title="see questions tagged &#39;mapzen&#39;">mapzen</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jan '16, 12:24</strong></p>
<img src="https://secure.gravatar.com/avatar/3689cee31406e90cdaa2f29817cc60b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jikoriko&#39;s gravatar image" />
<p><span>Jikoriko</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jikoriko has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jan '16, 18:20</strong> </span></p>
</div>
</div>
<div id="comments-container-47475" class="comments-container">
&#10;</div>
<div id="comment-tools-47475" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47475-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

