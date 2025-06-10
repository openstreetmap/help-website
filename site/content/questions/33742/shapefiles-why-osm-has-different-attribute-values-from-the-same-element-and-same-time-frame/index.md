+++
type = "question"
title = "Shapefiles: Why OSM has different attribute values from the same element and same time frame?"
description = '''(COPIED AND PASTED FROM my own question in GIS.STACKexchange.com. More details and discussion on the previous link.) Here is my question: Does anyone know why OSM has different attribute values from the same element and same frame time? The example explains itself, when I try the Shapefile from diff...'''
date = "2014-06-05T23:05:00Z"
lastmod = "2014-06-06T10:54:00Z"
weight = 33742
keywords = [ "qgis", "attributes", "shapefile", "change", "oneway" ]
aliases = [ "/questions/33742" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Shapefiles: Why OSM has different attribute values from the same element and same time frame?](/questions/33742/shapefiles-why-osm-has-different-attribute-values-from-the-same-element-and-same-time-frame)

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
<span id="post-33742-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33742-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33742-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><span class="small">(COPIED AND PASTED FROM my own <a href="http://gis.stackexchange.com/questions/100101/why-osm-data-has-different-attribute-values-from-the-same-element-and-same-time">question in GIS.STACKexchange.com</a>. More details and discussion on the previous link.)</span></p>
<p>Here is my question: Does anyone know why OSM has different attribute values from the same element and same frame time?</p>
<p>The example explains itself, when I try the Shapefile from different mirrors like Planet.osm.org , bbbike.org and geofabrik.de; I find that they have a mistake with the Direction of Travel on its attribute value.</p>
<p><img src="http://i.stack.imgur.com/3dEUJ.png" alt="example" /></p>
<p>When I check in the website: here the <a href="http://www.openstreetmap.org/way/91521461#map=18/38.00867/-1.15468">link</a> , I see on its attribute value that there is no mistake at all and has its right value.</p>
<p>----- E D I T ------</p>
<p>I've tried the GIS software QGIS (Version 2.2) with OSM Plugin. I've just tested with an small .map file and surprisingly, I have exported a Shapefile with all its original attributes. Here's what I have when I open in an ArcGIS session:</p>
<p><img src="http://help.openstreetmap.org/upfiles/06-06-2014_21-57-38.jpg" alt="Select by" /></p>
<p>So, at least, I'll have YES/NO/ /-1, and I could manage it in a better way.</p>
<p>Thanks for your support!!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span> <span class="post-tag tag-link-attributes" rel="tag" title="see questions tagged &#39;attributes&#39;">attributes</span> <span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-change" rel="tag" title="see questions tagged &#39;change&#39;">change</span> <span class="post-tag tag-link-oneway" rel="tag" title="see questions tagged &#39;oneway&#39;">oneway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jun '14, 23:05</strong></p>
<img src="https://secure.gravatar.com/avatar/08a1997e1df43be5dc7f39f07baeaa86?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="juasmilla&#39;s gravatar image" />
<p><span>juasmilla</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="juasmilla has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Jun '14, 21:02</strong> </span></p>
</div>
</div>
<div id="comments-container-33742" class="comments-container">
&#10;</div>
<div id="comment-tools-33742" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33742-form-container" class="comment-form-container">
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

<span id="33744"></span>

<div id="answer-container-33744" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33744-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33744-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-33744-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="juasmilla has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The Geofabrik shape only knows oneway=0 or oneway=1. In cases where OSM has oneway=-1, the Geofabrik shape <strong>should</strong> revert the direction of the way, and label it oneway=1. However upon closer inspection I found that there was a bug in the creation of the shapes, and the reversal was not triggered. I have now fixed that, and updated shape files should be available within 24 hours. They will still not have a -1 but they will have a reversed geometry in such cases.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jun '14, 23:51</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</img>
</div>
</div>
<div id="comments-container-33744" class="comments-container">
<span id="33746"></span>
<div id="comment-33746" class="comment">
<div id="post-33746-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks @FrederikRamm ,just to clear up: What do you mean when you talk about working on the reversed geometry? What I have understood or what I think is that the Fist point and Last point from each reverted line will be commuted, isn't it?</p>
</div>
<div id="comment-33746-info" class="comment-info">
<span class="comment-age">(06 Jun '14, 08:29)</span> <span class="comment-user userinfo">juasmilla</span>
</div>
</div>
<span id="33747"></span>
<div id="comment-33747" class="comment">
<div id="post-33747-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span></span><span>@juasmilla</span>: A <span>way</span> is an ordered list of nodes. So to reverse its direction (e.g. affecting the "oneway" direction) the full list of the way's nodes needs to be reversed. This includes swapping its first and last node, yes.</p>
</div>
<div id="comment-33747-info" class="comment-info">
<span class="comment-age">(06 Jun '14, 10:30)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="33748"></span>
<div id="comment-33748" class="comment">
<div id="post-33748-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes of course <span></span><span>@aseerel4c26</span>, I didn't express well. Thanks!</p>
</div>
<div id="comment-33748-info" class="comment-info">
<span class="comment-age">(06 Jun '14, 10:54)</span> <span class="comment-user userinfo">juasmilla</span>
</div>
</div>
</div>
<div id="comment-tools-33744" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33744-form-container" class="comment-form-container">
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

