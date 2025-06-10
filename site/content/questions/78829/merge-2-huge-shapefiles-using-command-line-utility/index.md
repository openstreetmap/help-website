+++
type = "question"
title = "Merge 2 huge shapefiles using command line utility"
description = '''Hi, I need to merge 2 huge shapefiles (~3.4GB each). I was using QGIS explorer to merge 2 shapefiles but the application runs out of memory and getting error can&#x27;t exceed 4 GB shapefile limit . I want the same way QGIS merges vectors but using commandline tool so that I can merge them on the cloud s...'''
date = "2021-02-13T09:36:00Z"
lastmod = "2021-02-14T21:43:00Z"
weight = 78829
keywords = [ "osrm" ]
aliases = [ "/questions/78829" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Merge 2 huge shapefiles using command line utility](/questions/78829/merge-2-huge-shapefiles-using-command-line-utility)

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
<span id="post-78829-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78829-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78829-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I need to merge 2 huge shapefiles (~3.4GB each). I was using QGIS explorer to merge 2 shapefiles but the application runs out of memory and getting error can't exceed 4 GB shapefile limit . I want the same way QGIS merges vectors but using commandline tool so that I can merge them on the cloud server.</p>
<p>I tried merging 2 separate .osm files but there is some issue in osrm-extraction.</p>
<p>What is the proper way to merge 2 shape files?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Feb '21, 09:36</strong></p>
<img src="https://secure.gravatar.com/avatar/7996417a96c5227404f348e863457405?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mukul2990&#39;s gravatar image" />
<p><span>Mukul2990</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mukul2990 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78829" class="comments-container">
&#10;</div>
<div id="comment-tools-78829" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78829-form-container" class="comment-form-container">
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

<span id="78830"></span>

<div id="answer-container-78830" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78830-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78830-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78830-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You cannot merge two 3.4 GB shape files. Shape files have a size limit of 2 GB, and some applications like GDAL will allow you to create up to 4 GB (using unsigned IDs internally) but will warn you that these files might not be readable with other software. More than 4 GB isn't possible with any software.</p>
<p>Depending on what you want to do, you might want to switch to SQLite files which can be readily processed with GDAL (ogr2ogr command line tool). You can convert the first shape file to SQLite and then append the second shape file to that existing SQLite file. QGIS can load SQLite files.</p>
<p>Note that this simply combines the file into one. If by "merge" you mean an actual merge operation on geometries, combining overlapping features into one, then that's a different ballgame that would require loading the data into PostGIS.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Feb '21, 11:31</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Feb '21, 11:32</strong> </span></p>
</div>
</div>
<div id="comments-container-78830" class="comments-container">
<span id="78838"></span>
<div id="comment-78838" class="comment">
<div id="post-78838-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was appending both shapefiles data to the table using this command to insert shapefile to PostGIS DB.</p>
<p>ogr2ogr -update -append -progress -f "ESRI Shapefile" PG:"dbname=postgres user=postgres port=5432 password=postgres" Shape1.shp -nln ShapeFilesData</p>
<p>But there were some issues with this approach. OSRM cluster was not showing the routes correctly.</p>
</div>
<div id="comment-78838-info" class="comment-info">
<span class="comment-age">(14 Feb '21, 05:35)</span> <span class="comment-user userinfo">Mukul2990</span>
</div>
</div>
<span id="78842"></span>
<div id="comment-78842" class="comment">
<div id="post-78842-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OSRM does not read shape files OR PostGIS database tables. If you want to do routing on PostGIS database tables, try PGRouting.</p>
</div>
<div id="comment-78842-info" class="comment-info">
<span class="comment-age">(14 Feb '21, 11:37)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="78852"></span>
<div id="comment-78852" class="comment">
<div id="post-78852-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No. What I mean to say is I was using the shapefile data loaded in QGIS and generate .osm files, then that osm will generate .pbf which is supplied to the osrm-extraction.</p>
</div>
<div id="comment-78852-info" class="comment-info">
<span class="comment-age">(14 Feb '21, 21:43)</span> <span class="comment-user userinfo">Mukul2990</span>
</div>
</div>
</div>
<div id="comment-tools-78830" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78830-form-container" class="comment-form-container">
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

