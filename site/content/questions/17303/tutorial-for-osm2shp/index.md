+++
type = "question"
title = "Tutorial for osm2shp"
description = '''Hi, I like to use the program osm2shp (https://trac.openstreetmap.org/browser/applications/utils/export/osm2shp) Is there somewhere a tutorial how to use it or some kind of instructions. I don&#x27;t know how to use a makefile nor have I experience in C++ Thanks, Uli'''
date = "2012-10-30T16:19:00Z"
lastmod = "2012-10-30T16:52:00Z"
weight = 17303
keywords = [ "shp", "osm2shp" ]
aliases = [ "/questions/17303" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Tutorial for osm2shp](/questions/17303/tutorial-for-osm2shp)

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
<span id="post-17303-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17303-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17303-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I like to use the program osm2shp (<a href="https://trac.openstreetmap.org/browser/applications/utils/export/osm2shp)">https://trac.openstreetmap.org/browser/applications/utils/export/osm2shp)</a></p>
<p>Is there somewhere a tutorial how to use it or some kind of instructions. I don't know how to use a makefile nor have I experience in C++</p>
<p>Thanks,</p>
<p>Uli</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shp" rel="tag" title="see questions tagged &#39;shp&#39;">shp</span> <span class="post-tag tag-link-osm2shp" rel="tag" title="see questions tagged &#39;osm2shp&#39;">osm2shp</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Oct '12, 16:19</strong></p>
<img src="https://secure.gravatar.com/avatar/e0304055ba107b43dc134e4a9e5a955c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wasus&#39;s gravatar image" />
<p><span>Wasus</span><br />
<span class="score" title="346 reputation points">346</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wasus has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17303" class="comments-container">
&#10;</div>
<div id="comment-tools-17303" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17303-form-container" class="comment-form-container">
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

<span id="17305"></span>

<div id="answer-container-17305" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17305-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17305-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17305-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Wasus has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am not aware of an osm2shp tutorial. You might want to try out <code>osmjs</code> instead, a JavaScript-based OSM data processor that comes with the Osmium framework and can be used to produce shape files. There's a little documentation here: <a href="https://github.com/joto/osmium/tree/master/osmjs">https://github.com/joto/osmium/tree/master/osmjs</a></p>
<p>If you are more familiar with the OGR world than with C++ and makefiles, you might also want to check out the OGR driver for reading OSM data: <a href="http://www.gdal.org/ogr/drv_osm.html">http://www.gdal.org/ogr/drv_osm.html</a> - the ogr2ogr utility can trivially be used to make shape files with that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Oct '12, 16:52</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-17305" class="comments-container">
&#10;</div>
<div id="comment-tools-17305" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17305-form-container" class="comment-form-container">
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

