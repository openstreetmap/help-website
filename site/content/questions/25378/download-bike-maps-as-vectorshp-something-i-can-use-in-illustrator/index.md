+++
type = "question"
title = "Download BIKE maps as vector/.shp/ something I can use in Illustrator?!!"
description = '''Dear all! This is a bit urgent, as I am working on a research project with a tight schedule and upcoming deadline... Basically my question is: How can I download the OSM Bike Map in a way that I can use in Adobe Illustrator or other vector based program? I tried to export as .svg, but it is all the ...'''
date = "2013-08-14T16:44:00Z"
lastmod = "2013-08-14T18:51:00Z"
weight = 25378
keywords = [ "arcgis", "vector", "gis", "bikemap", "illustrator" ]
aliases = [ "/questions/25378" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Download BIKE maps as vector/.shp/ something I can use in Illustrator?!!](/questions/25378/download-bike-maps-as-vectorshp-something-i-can-use-in-illustrator)

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
<span id="post-25378-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25378-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-25378-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear all!</p>
<p>This is a bit urgent, as I am working on a research project with a tight schedule and upcoming deadline...</p>
<p>Basically my question is: How can I download the OSM Bike Map in a way that I can use in Adobe Illustrator or other vector based program? I tried to export as .svg, but it is all the time the main map that is exported. I also downloaded the .shp files from <a href="http://extract.bbbike.org/">http://extract.bbbike.org/</a> to use in ArcGIS, but there is no layer for biking routes.</p>
<p>Let me know if you have any suggestions, or if I am unclear!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-arcgis" rel="tag" title="see questions tagged &#39;arcgis&#39;">arcgis</span> <span class="post-tag tag-link-vector" rel="tag" title="see questions tagged &#39;vector&#39;">vector</span> <span class="post-tag tag-link-gis" rel="tag" title="see questions tagged &#39;gis&#39;">gis</span> <span class="post-tag tag-link-bikemap" rel="tag" title="see questions tagged &#39;bikemap&#39;">bikemap</span> <span class="post-tag tag-link-illustrator" rel="tag" title="see questions tagged &#39;illustrator&#39;">illustrator</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Aug '13, 16:44</strong></p>
<img src="https://secure.gravatar.com/avatar/bbf4c4615992f85dbd60d4bf5b419980?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="annerala&#39;s gravatar image" />
<p><span>annerala</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="annerala has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Aug '13, 16:57</strong> </span></p>
</div>
</div>
<div id="comments-container-25378" class="comments-container">
&#10;</div>
<div id="comment-tools-25378" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25378-form-container" class="comment-form-container">
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

<span id="25379"></span>

<div id="answer-container-25379" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25379-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25379-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-25379-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenCycleMap is a personal project of Andy Allan (Gravitystorm), the styles used to create it are not available, and even if they were would not be much use for pulling into Illustrator.</p>
<p>You will need to use a basic OSM extract (such as those available at BBBike) and select the features which you require either using various OSM tools, such as Osmosis of osmfilter, or using ShapeFiles in ArcGIS or QGIS. Basically you will need at a minimum all highways tagged with <code>highway=cycleway</code>, or <code>cycleway=yes</code> or (<code>highway=footway</code> AND <code>cycle=yes</code>) <code>ncn|rcn|lcn=*</code> or <code>ncn_ref|rcn-ref|lcn_ref=*</code> or <code>cycleway:lane=*</code>. You may also wish to see barriers, cycle parking, cycle crossings etc. You are unlikely to replicate anything like OpenCycleMap because it represents at least 5 years of effort by Andy, but you may get a reasonable approximation. Note that tagging of cycleways varies according to local circumstances.</p>
<p>Printed cycle maps have been produced from OpenStreetMap data, for instance by David Earl ("What I learned making a real map on real paper for real people and real money", David Earl at <a href="http://vimeo.com/14806373">Sotm2010</a>, Girona). If you watch the video you will see that it is a complex and involved process, not something to do at the last minute.</p>
<p>I am sure that one of the OSM service providers would be able to provide you with a suitable extract, but I imagine not at a price you would be comfortable with.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Aug '13, 18:51</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-25379" class="comments-container">
&#10;</div>
<div id="comment-tools-25379" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25379-form-container" class="comment-form-container">
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

