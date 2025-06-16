+++
type = "question"
title = "What is the best way to use OSM data in QGIS"
description = '''Thank you for response to this question (problems were associated with QGIS plugin failing with 64-bit OSM IDs).  Bearing in mind that this is something I hope to help other communities learn (who are not from a GIS background), which of the alternative methods would you recommend to enable us to vi...'''
date = "2013-03-30T16:06:00Z"
lastmod = "2013-03-30T16:34:00Z"
weight = 21088
keywords = [ "qgis", "visualization", "analysis" ]
aliases = [ "/questions/21088" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What is the best way to use OSM data in QGIS](/questions/21088/what-is-the-best-way-to-use-osm-data-in-qgis)

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
<span id="post-21088-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21088-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21088-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Thank you for response to <a href="/questions/21078/my-lines-and-polygons-have-turned-to-nodes-when-exported-as-osm-xml-data-and-imported-into-qgis">this question</a> (problems were associated with QGIS plugin failing with 64-bit OSM IDs).</p>
<p>Bearing in mind that this is something I hope to help other communities learn (who are not from a GIS background), which of the alternative methods would you recommend to enable us to visualise OSM data in QGIS?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span> <span class="post-tag tag-link-visualization" rel="tag" title="see questions tagged &#39;visualization&#39;">visualization</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Mar '13, 16:06</strong></p>
<img src="https://secure.gravatar.com/avatar/404e0195647cf997c0820219a9f38536?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="paulgeorgie&#39;s gravatar image" />
<p><span>paulgeorgie</span><br />
<span class="score" title="71 reputation points">71</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="paulgeorgie has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> converted <strong>30 Mar '13, 16:11</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></p>
</div>
</div>
<div id="comments-container-21088" class="comments-container">
&#10;</div>
<div id="comment-tools-21088" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21088-form-container" class="comment-form-container">
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

<span id="21092"></span>

<div id="answer-container-21092" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21092-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21092-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21092-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think there are three broad options for visualising and manipulating OSM data in QGIS:</p>
<ol>
<li>Directly with <strong>OSM XML</strong> files (i.e., using the very dated plugin). This still works if all ids are in the 32-bit domain. A suitable workaround is to load the XML into JOSM, copy everything into a new layer (therefore resetting all ids) and save this as an OSM file for loading into QGIS. Apart from the dangers of importing the same data again, this is very simple and requires no additional skills to be learnt. Once loaded in QGIS I would suggest creating shapefiles from the OSM layers for further work.</li>
<li>Use prebuilt <strong>ESRI Shapefiles.</strong> The files provided by Geofabrik are suitable for most purposes, but if you need specific tags can be a little frustrating.</li>
<li>Import OSM data into a <strong>Postgres</strong> database. The most useful way is using the osm2pgsql routine which creates tables with a rich set of attributes. As osm2pgsql supports hstore all tags are ultimately accessible. Additionally the base tables can be extended to add additional geometry columns for other projections of interest (such as OSGB). Postgres has a simple installation program on windows, and osm2pgsql and QGIS can be used with little knowledge of Postgres.</li>
</ol>
<p>Personally I have found the latter method by far the most flexible, as it lends itself more readily to the creating multiple layers both for analysis and visualisation which is QGIS forte. It also provides the best method for reusing QGIS projects and refreshing the data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Mar '13, 16:34</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-21092" class="comments-container">
&#10;</div>
<div id="comment-tools-21092" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21092-form-container" class="comment-form-container">
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

