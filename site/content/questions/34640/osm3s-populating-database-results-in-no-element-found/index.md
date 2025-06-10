+++
type = "question"
title = "osm3s populating database results in &quot;no element found&quot;."
description = '''I&#x27;ve got a local installation of the osm3s running and it works fine with data from openstreetmap. I would like to use my own custom 3D data. I&#x27;ve got an entire 3D model of a city in Microstation. It&#x27;s in wireframes. I can set the projection to WGS84 and export it to KML and then convert it with ogr...'''
date = "2014-07-04T14:51:00Z"
lastmod = "2014-07-08T08:35:00Z"
weight = 34640
keywords = [ "dxf", "osm3s", "ogr2osm", "3d" ]
aliases = [ "/questions/34640" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osm3s populating database results in "no element found".](/questions/34640/osm3s-populating-database-results-in-no-element-found)

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
<span id="post-34640-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34640-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-34640-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've got a local installation of the osm3s running and it works fine with data from openstreetmap.</p>
<p>I would like to use my own custom 3D data. I've got an entire 3D model of a city in Microstation. It's in wireframes. I can set the projection to WGS84 and export it to KML and then convert it with ogr2osm. But when I try to populate the database for osm3s it return with "no elements found".</p>
<p>Looking at the .osm-file does show a lot of nodes etc.</p>
<p>What to do?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-dxf" rel="tag" title="see questions tagged &#39;dxf&#39;">dxf</span> <span class="post-tag tag-link-osm3s" rel="tag" title="see questions tagged &#39;osm3s&#39;">osm3s</span> <span class="post-tag tag-link-ogr2osm" rel="tag" title="see questions tagged &#39;ogr2osm&#39;">ogr2osm</span> <span class="post-tag tag-link-3d" rel="tag" title="see questions tagged &#39;3d&#39;">3d</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jul '14, 14:51</strong></p>
<img src="https://secure.gravatar.com/avatar/864bb2bd659ffa71e4c36bab6a92884d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="haasor&#39;s gravatar image" />
<p><span>haasor</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="haasor has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-34640" class="comments-container">
&#10;</div>
<div id="comment-tools-34640" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34640-form-container" class="comment-form-container">
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

<span id="34647"></span>

<div id="answer-container-34647" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34647-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34647-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-34647-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Does your generated OSM file contain negative id values (which is the default for ogr2osm)? This will most likely cause some undesired side effects when loading using update_database for Overpass API, such as strange node ids (e.g. "18446744073707268155").</p>
<p>Apart from that I can't really reproduce your issue. I converted some polygons from a PostGIS db to a shape file and then converted this via ogr2osm to an OSM file and loaded the file into Overpass API (latest github version) via update_database. I could query some of the nodes, although their id was completely screwed. This needs to be adjusted in the ogr2osm script.</p>
<p>I believe you need to provide much more details like version of the programs involved, sample OSM snippets, log files etc.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jul '14, 21:14</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jul '14, 21:24</strong> </span></p>
</div>
</div>
<div id="comments-container-34647" class="comments-container">
<span id="34717"></span>
<div id="comment-34717" class="comment">
<div id="post-34717-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is the top from the generated XML/OSM file: <a href="http://pastie.org/9366804">http://pastie.org/9366804</a></p>
</div>
<div id="comment-34717-info" class="comment-info">
<span class="comment-age">(08 Jul '14, 08:30)</span> <span class="comment-user userinfo">haasor</span>
</div>
</div>
<span id="34718"></span>
<div id="comment-34718" class="comment">
<div id="post-34718-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Programs involved are Microstation V8i, export to DXF, converted into osm via ogr2osm and loading into overpass-api/osm3s.</p>
</div>
<div id="comment-34718-info" class="comment-info">
<span class="comment-age">(08 Jul '14, 08:35)</span> <span class="comment-user userinfo">haasor</span>
</div>
</div>
</div>
<div id="comment-tools-34647" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34647-form-container" class="comment-form-container">
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

