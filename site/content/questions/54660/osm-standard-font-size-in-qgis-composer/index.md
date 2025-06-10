+++
type = "question"
title = "OSM Standard font size in QGIS composer"
description = '''Hi, very very new to the QGIS and mapping world. If you have a solution for me, please provide baby steps! :) I created a map in QGIS composer with a few shape files and OSM Standard as the base layer for real world reference points. I&#x27;m working on a scale of 4000 and have the map filling up most of...'''
date = "2017-02-15T22:39:00Z"
lastmod = "2017-02-16T11:53:00Z"
weight = 54660
keywords = [ "qgis", "composer", "font_size", "names", "road" ]
aliases = [ "/questions/54660" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM Standard font size in QGIS composer](/questions/54660/osm-standard-font-size-in-qgis-composer)

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
<span id="post-54660-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54660-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54660-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, very very new to the QGIS and mapping world. If you have a solution for me, please provide baby steps! :)</p>
<p>I created a map in QGIS composer with a few shape files and OSM Standard as the base layer for real world reference points. I'm working on a scale of 4000 and have the map filling up most of the page. When I export it to PDF format, the roads have narrowed and their names have shrunk in comparison to what I view in the composer. Unfortunately it makes the names very difficult to read. Before I go reducing the scale and cutting my map in two, is there any way to prevent the base layer "shrinkage"?</p>
<p>Thank you kindly!</p>
<p>Alison</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span> <span class="post-tag tag-link-composer" rel="tag" title="see questions tagged &#39;composer&#39;">composer</span> <span class="post-tag tag-link-font_size" rel="tag" title="see questions tagged &#39;font_size&#39;">font_size</span> <span class="post-tag tag-link-names" rel="tag" title="see questions tagged &#39;names&#39;">names</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Feb '17, 22:39</strong></p>
<img src="https://secure.gravatar.com/avatar/26df486449f2459bf1cddb8ea4035315?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlisonF&#39;s gravatar image" />
<p><span>AlisonF</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlisonF has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54660" class="comments-container">
&#10;</div>
<div id="comment-tools-54660" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54660-form-container" class="comment-form-container">
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

<span id="54672"></span>

<div id="answer-container-54672" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54672-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54672-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-54672-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The OSM Standard style (CartoCSS) is designed for on-line viewing. Any printed version suffers from the problems you describe. In addition there are some other issues arising from it's nature as pre-rendered raster tiles:</p>
<ul>
<li>it's available at standard <a href="https://wiki.openstreetmap.org/wiki/Zoom_levels">zoom levels</a>. The layer is only likely to be readily readable when the scale you choose is very close to one of these zoom levels</li>
<li>the text elements are baked into the raster tile so font styling etc is no longer controllable.</li>
</ul>
<p>You will need to add additional layers in QGIS to achieve your goal.</p>
<p>Depending on your needs you could do one of the following:</p>
<ul>
<li>Add a number of OSM vector elements (the easiest ways is to use Overpass-Turbo and download geojson either directly or using a plugin within QGGIS) as QGIS layers, and style these in QGIS as an overlay. Often just place names help provide the relevant orientation information, but other features like the main road network may be necessary.</li>
<li>Download all the OSM data for your area and build your base map using QGIS Styles.</li>
</ul>
<p>In practice the former can lead gradually to the latter. There are probably already some decent resources which can help. It's always worth checking if Anita Graser (blog <a href="https://anitagraser.com/">here</a>) references anything.</p>
<p>PS. If I find anything I'll try &amp; add it to this answer.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Feb '17, 11:53</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-54672" class="comments-container">
&#10;</div>
<div id="comment-tools-54672" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54672-form-container" class="comment-form-container">
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

