+++
type = "question"
title = "A street map of the Chertsey Meads ward in Runnymede."
description = '''I have been asked to stand as a candidate in the Chertsey Meads by-election which will take place on 13 March. How can I find a street map of the Chertsey Meads ward with the names of all the streets, so that I can deliver leaflets and canvas local voters?'''
date = "2014-02-15T11:07:00Z"
lastmod = "2014-02-15T19:02:00Z"
weight = 30753
keywords = [ "streets", "chertseymeads", "canvassing" ]
aliases = [ "/questions/30753" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [A street map of the Chertsey Meads ward in Runnymede.](/questions/30753/a-street-map-of-the-chertsey-meads-ward-in-runnymede)

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
<span id="post-30753-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30753-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-30753-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been asked to stand as a candidate in the Chertsey Meads by-election which will take place on 13 March. How can I find a street map of the Chertsey Meads ward with the names of all the streets, so that I can deliver leaflets and canvas local voters?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-streets" rel="tag" title="see questions tagged &#39;streets&#39;">streets</span> <span class="post-tag tag-link-chertseymeads" rel="tag" title="see questions tagged &#39;chertseymeads&#39;">chertseymeads</span> <span class="post-tag tag-link-canvassing" rel="tag" title="see questions tagged &#39;canvassing&#39;">canvassing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Feb '14, 11:07</strong></p>
<img src="https://secure.gravatar.com/avatar/efce695eda2af1fa75b0d139154cfedf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Grahame%20Leon-Smith&#39;s gravatar image" />
<p><span>Grahame Leon...</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Grahame Leon-Smith has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Feb '14, 11:25</strong> </span></p>
</div>
</div>
<div id="comments-container-30753" class="comments-container">
&#10;</div>
<div id="comment-tools-30753" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30753-form-container" class="comment-form-container">
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

<span id="30757"></span>

<div id="answer-container-30757" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30757-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30757-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-30757-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you had been very lucky Chertsey Meads ward might have been present on OpenStreetMap. Unfortunately for you it is not. However, the Ordnance Survey Open Data Boundary Line does contain all ward boundaries: it is available <a href="http://data.gov.uk/dataset/boundary-line">here</a>.</p>
<p>The basic steps are:</p>
<ol>
<li>Find the ward boundary in a vector format</li>
<li>Download suitable OSM data</li>
<li>Clip the OSM data using the ward boundary</li>
<li>Create a map</li>
</ol>
<p>Simple isn't it! <strong>BUT</strong> to do what you wish requires quite a degree of technical knowledge: you may wish to pass these instructions onto to someone if you dont think your own background is suitable.</p>
<p>Firstly, you need to extract your ward boundary from the Boundary Line data. I would use <a href="http://www.qgis.org/en/site/">QGIS</a> to do this: it provides a relatively straightforward interface for looking at this type of data. You can then save just that ward boundary excluding all others (using the Save Selection As ... option in QGIS). Normally I save these as ESRI Shapefiles (the format the data comes in). The data is almost certainly in the British National Grid projection (EPSG code 27700). At some stage you will need to transform this to WGS84 (EPSG 4326), as this is the way in which OSM data is stored and most tools expect data in this projection. You can change the projection when you save the selection containing the ward, or you can do it in two steps.</p>
<p>Secondly, you need some local OSM data. The most convenient place to get this is from the Geofabrik download site. Conveniently they have an extract for <a href="http://download.geofabrik.de/europe/great-britain/england/surrey.html">Surrey</a>.</p>
<p>The third step is to use the polygon boundary of the ward to select only those OSM objects within the ward. There are two ways of doing this: a) in QGIS or b) using <a href="https://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a> or <a href="https://wiki.openstreetmap.org/wiki/Osmconvert#Clipping_based_on_a_Polygon">osmconvert</a>. I favour the latter because it gives you more options in the next step. With Osmosis it is possible to filter an OSM file using a polygon. To create your polygon you use the ward boundary and one of the tools mentioned <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Polygon_Filter_File_Format">here</a>. (QGIS used to have a simple to use plugin but it does not seem to be available for the current version). The basic format of the clipping command is like:</p>
<pre><code>osmosis --rb file=INPUTOSM.osm --bp file=WARDBOUNDARY.poly --wx file=WARDOSM.osm</code></pre>
<p>With the output file it is now possible to create the map. My feeling is that <a href="https://wiki.openstreetmap.org/wiki/Maposmatic">MapOSMatic</a> might be the most suitable for the kind of thing you want because it produces a street index. (I have not used this for quite a while).</p>
<p>I have taken time to detail these steps because your question is something it should be easier to do, and require fewer than 4 tools to achieve. However, I suspect I will only put you off.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Feb '14, 19:02</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-30757" class="comments-container">
&#10;</div>
<div id="comment-tools-30757" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30757-form-container" class="comment-form-container">
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

