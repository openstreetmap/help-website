+++
type = "question"
title = "What is the easiest way to import polygons from the Corine Land Cover?"
description = '''I would like to import some forest and farmland polygons from the Corine Land Cover. I have downloaded the Corine Land Cover shapefiles. I have also viewed them in QGIS and extracted the areas I want to work with to a smaller set. What is an easy way to import these polygons to OSM? Both for a small...'''
date = "2011-10-07T10:57:00Z"
lastmod = "2011-10-13T09:52:00Z"
weight = 8335
keywords = [ "import", "shapefiles", "corine-land-cover" ]
aliases = [ "/questions/8335" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What is the easiest way to import polygons from the Corine Land Cover?](/questions/8335/what-is-the-easiest-way-to-import-polygons-from-the-corine-land-cover)

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
<span id="post-8335-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8335-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8335-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to import some forest and farmland polygons from the Corine Land Cover. I have downloaded the Corine Land Cover shapefiles. I have also viewed them in QGIS and extracted the areas I want to work with to a smaller set.</p>
<p>What is an easy way to import these polygons to OSM? Both for a smaller set and also if I import a larger set of polygons? Is it possible to do so that the polygons get the correct tags, so I don't need to use another tool to edit them after upload to OSM?</p>
<p>I have read <a href="http://wiki.openstreetmap.org/wiki/WikiProject_Corine_Land_Cover/Corine_Data_Import">WikiProject Corine Land Cover/Corine Data Import</a> but that process seem to be complicated since it require a local PostGIS database, many tools and also download of OSM data.</p>
<p><strong>UPDATE</strong> I have now tried with what Frederik Ramm suggested, by importing shapefiles in Potlatch. But I can't get it working. See <a href="http://help.openstreetmap.org/questions/8428/how-to-use-a-shapefile-in-potlatch">How to use a Shapefile in Potlatch?</a></p>
<p>I have also tried to open the shapefile with polygons in QGIS, then transform the polygons to linestrings and export the linestrings to a GPX file. But when I import the GPX file to OpenStreetMap, it fails because the GPX files doesn't have a any timestamps.</p>
<p>Is there any other way I can import a few polygons from Corine Land Cover shapefiles to OpenStreetMaps?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-shapefiles" rel="tag" title="see questions tagged &#39;shapefiles&#39;">shapefiles</span> <span class="post-tag tag-link-corine-land-cover" rel="tag" title="see questions tagged &#39;corine-land-cover&#39;">corine-land-cover</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Oct '11, 10:57</strong></p>
<img src="https://secure.gravatar.com/avatar/b1d217a3a6e04cf4654372068beef20d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonas_&#39;s gravatar image" />
<p><span>Jonas_</span><br />
<span class="score" title="662 reputation points">662</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonas_ has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Oct '11, 18:36</strong> </span></p>
</div>
</div>
<div id="comments-container-8335" class="comments-container">
&#10;</div>
<div id="comment-tools-8335" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8335-form-container" class="comment-form-container">
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

<span id="8336"></span>

<div id="answer-container-8336" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8336-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-8336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When importing data, it is very important to discuss the issue with other local mappers before you do. Even if the data source is legally suitable, there might be many other reasons against an import.</p>
<p>As the importer, you have the responsibility of doing things right - technically <em>and</em> socially. There might be people who dislike the import, especially if it interferes with data that already exists. There is a reason why the documented process is complex: It is easy to break things, or import them in a way that is technically wrong. For example, if you simply convert shape files to OSM then you will likely create duplicate nodes where two land cover areas meet - when the correct way would be at least re-using the nodes, but in some cases also using multipolygons and re-using the boundary line between the two.</p>
<p>If you find that the documented process is too complicated. then I suggest that you do not import anything at all. It is easy to harm OSM with a badly executed import - the map might have more colours afterwards, but you could upset the community and create data that is hard to edit.</p>
<p>Potlatch has a vector background layer where you can load a shape file and copy selected shapes from it, manually. Maybe that is an alternative for you. Adding data for areas you know personally is more rewarding, and more sustainable, than plastering the whole country with land cover data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Oct '11, 11:14</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-8336" class="comments-container">
<span id="8429"></span>
<div id="comment-8429" class="comment">
<div id="post-8429-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have now tried to use a shapefile in Potlatch, but I got an error: <a href="http://help.openstreetmap.org/questions/8428/how-to-use-a-shapefile-in-potlatch">http://help.openstreetmap.org/questions/8428/how-to-use-a-shapefile-in-potlatch</a></p>
</div>
<div id="comment-8429-info" class="comment-info">
<span class="comment-age">(13 Oct '11, 09:52)</span> <span class="comment-user userinfo">Jonas_</span>
</div>
</div>
</div>
<div id="comment-tools-8336" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8336-form-container" class="comment-form-container">
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

