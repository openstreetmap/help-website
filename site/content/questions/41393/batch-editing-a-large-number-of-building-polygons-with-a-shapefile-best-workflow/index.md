+++
type = "question"
title = "Batch editing a large number of building polygons with a shapefile - best workflow?"
description = '''HI all, I am interested in cleaning up the building traces at UC Davis, California, by using their official GIS shapefile which was derived from AutoCAD files. This shapefile is public domain and therefore OK to use in OSM. You can see the shapefile in their official campus map as a layer in Google ...'''
date = "2015-02-26T18:51:00Z"
lastmod = "2015-02-27T09:02:00Z"
weight = 41393
keywords = [ "building", "shapefile", "editing", "polygon", "batch" ]
aliases = [ "/questions/41393" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Batch editing a large number of building polygons with a shapefile - best workflow?](/questions/41393/batch-editing-a-large-number-of-building-polygons-with-a-shapefile-best-workflow)

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
<span id="post-41393-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41393-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-41393-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>HI all, I am interested in cleaning up the building traces at UC Davis, California, by using their official GIS shapefile which was derived from AutoCAD files. This shapefile is public domain and therefore OK to use in OSM.</p>
<p>You can see the shapefile in their official campus map as a layer in Google Maps here: <a href="http://campusmap.ucdavis.edu/">http://campusmap.ucdavis.edu/</a> (It's all of the brown buildings)</p>
<p>As you can probably tell, these building polygons are more accurate than the user-contributed satellite traces currently in OSM.</p>
<p>What would be the most efficient workflow for me to correct each of these building polygons with the vector data from this official shapefile?</p>
<p>Thanks for your advice!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-batch" rel="tag" title="see questions tagged &#39;batch&#39;">batch</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Feb '15, 18:51</strong></p>
<img src="https://secure.gravatar.com/avatar/1d9ea916f72f265748b2f1f1c41c88f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MattSidor&#39;s gravatar image" />
<p><span>MattSidor</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MattSidor has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-41393" class="comments-container">
&#10;</div>
<div id="comment-tools-41393" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41393-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="41394"></span>

<div id="answer-container-41394" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41394-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41394-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-41394-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have not verified how large that area is, but generally I would start in the OSM wiki about <a href="http://wiki.openstreetmap.org/wiki/Import/Guidelines">Import Gudelines</a>.</p>
<p>Read carefully there, and try to get in contact with local mappers in the US community.</p>
<p>When that area is not too small, you can open a new sub article in OSM wiki and document all your workflow, thus others can evaluate and assist if necessary.</p>
<p>EDIT: see also <a href="http://wiki.openstreetmap.org/wiki/Import/Software">Import/Software</a>, <a href="http://wiki.openstreetmap.org/wiki/Shapefiles">Shapefiles</a> and <a href="http://wiki.openstreetmap.org/wiki/Converting_map_data_between_formats">Converting_map_data_between_formats</a> ... and urgently recommended to use/preview in JOSM offline editor, not in potlatch2 or iD.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Feb '15, 19:50</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Feb '15, 22:37</strong> </span></p>
</div>
</div>
<div id="comments-container-41394" class="comments-container">
<span id="41397"></span>
<div id="comment-41397" class="comment">
<div id="post-41397-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, this is a great set of general guidelines.</p>
<p>I am still looking for a more technical and detailed set of workflow instructions for adding a large amount of polygons from a shapefile. e.g., Do I have to import them as a background layer using Potlatch2 and then adjust each polygon by hand to line up with my shapefile, or is there a way I can automate this process?</p>
</div>
<div id="comment-41397-info" class="comment-info">
<span class="comment-age">(26 Feb '15, 21:38)</span> <span class="comment-user userinfo">MattSidor</span>
</div>
</div>
<span id="41399"></span>
<div id="comment-41399" class="comment">
<div id="post-41399-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I would recommend JOSM for this type of work. JOSM can import shapefiles(via <a href="http://wiki.openstreetmap.org/wiki/JOSM/Plugins/OpenData">OpenData plugin</a> and you can replace existing geometry with new geometry with the <a href="http://josm.openstreetmap.de/wiki/Help/Plugin/UtilsPlugin2">UtilsPlugin2</a></p>
</div>
<div id="comment-41399-info" class="comment-info">
<span class="comment-age">(27 Feb '15, 06:32)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-41394" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41394-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="41400"></span>

<div id="answer-container-41400" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41400-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41400-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-41400-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The area and number of polygons doesn't look too large. It might be easier and faster to just "manually import" it. You can use JOSM to load a shapefile data with the OpenData plugin, then replace the geometry on buildings that are already there with the UtilsPlugins2. If there is no building in OSM, then just copy it directly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Feb '15, 09:02</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-41400" class="comments-container">
&#10;</div>
<div id="comment-tools-41400" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41400-form-container" class="comment-form-container">
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

