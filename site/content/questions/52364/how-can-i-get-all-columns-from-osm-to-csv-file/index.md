+++
type = "question"
title = "how can i get all columns from osm to csv file ?"
description = '''Hello, i have got a file osm form ..geofabric and i want to get from that file infomration like - street name , city name , housenumber and coordinates to csv file. to achive that i used osmconverter  and almost everything is fine but , how can i know the name od columns used in osm file ? how can g...'''
date = "2016-10-04T12:05:00Z"
lastmod = "2016-10-17T10:01:00Z"
weight = 52364
keywords = [ "osmconvert", "csv" ]
aliases = [ "/questions/52364" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how can i get all columns from osm to csv file ?](/questions/52364/how-can-i-get-all-columns-from-osm-to-csv-file)

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
<span id="post-52364-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52364-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52364-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>i have got a file osm form ..geofabric and i want to get from that file infomration like - street name , city name , housenumber and coordinates to csv file. to achive that i used osmconverter</p>
<p>and almost everything is fine but , how can i know the name od columns used in osm file ? how can gat all columns from osm file ?</p>
<p>i used a comand like this osmconvert and.osm --csv="<a href="http://help.openstreetmap.org/users/260/idoneus">@id</a> <a href="http://help.openstreetmap.org/users/148/osmnoase">@o</a>name osm_id <a href="http://help.openstreetmap.org/users/148/osmnoase">@o</a> type <a href="http://help.openstreetmap.org/users/1350/longestaugust">@lon</a> <a href="http://help.openstreetmap.org/users/5110/latroc">@lat</a> @version @uid <a href="http://help.openstreetmap.org/users/6901/user">@user</a> smoking designation addr:postcode addr:city a ddr:street addr:housenumber @" --csv-headline --out-csv -o="final.csv"</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Oct '16, 12:05</strong></p>
<img src="https://secure.gravatar.com/avatar/e428257506ff5b82e7e4e7d044396a09?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="marbo4&#39;s gravatar image" />
<p><span>marbo4</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="marbo4 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Oct '16, 12:07</strong> </span></p>
</div>
</div>
<div id="comments-container-52364" class="comments-container">
&#10;</div>
<div id="comment-tools-52364" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52364-form-container" class="comment-form-container">
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

<span id="52365"></span>

<div id="answer-container-52365" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52365-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52365-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52365-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM data doesn't have a fixed number of attributes.</p>
<p>If you need to get "all" tag information from a specific OSM extract in to a fixed format column format you will need to first do a pass over the file to determine all keys that are present, or simply write a small script that does this in one pass (which might be a bit painful for a large extract).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Oct '16, 12:40</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-52365" class="comments-container">
<span id="52514"></span>
<div id="comment-52514" class="comment">
<div id="post-52514-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hm, hm Thnx for answer.</p>
<p>But i don't know how can I Pass over the file ? which program ? QGIS ? I try to use Qgis with plugin QuickOSM but it's crashes every time . File are to large.</p>
</div>
<div id="comment-52514-info" class="comment-info">
<span class="comment-age">(13 Oct '16, 07:29)</span> <span class="comment-user userinfo">marbo4</span>
</div>
</div>
</div>
<div id="comment-tools-52365" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52365-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="52566"></span>

<div id="answer-container-52566" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52566-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52566-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52566-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As Simon said, you need to know the structure before you can create a csv. I can imagine some sort of parser to do this, but that only makes sense if you often have this problem. What I would do myself is use the PBF download from Geofabrik, then convert to spatialite. This can then easily be queried in QGIS. Common tags already are their own column, less common tags are merged together in an "other tags" column. These can still be queried with some creativity, but you can also edit the config file behind the process to get the columns straight into your spatialite database.</p>
<p>Here's a step by step:</p>
<ul>
<li><a href="http://trac.osgeo.org/osgeo4w/">Download OSGEO4W</a> (if you're on windows, and don't use GDAL/OGR already):</li>
<li>Install and make sure to include GDAL and QGIS.</li>
<li>Open the Osgeo shell. An icon should have been added to your desktop.</li>
<li>It looks just like a DOS terminal. Use the cd command to navigate to where your .pbf is</li>
<li><p>This command will create your spatialite database:</p>
<p>ogr2ogr -f SQLITE -dsco SPATIALITE=yes yourdatabasefile.sqlite themapyoudownloaded.osm.pbf</p></li>
<li><p>You can use the sqlite file in an easy program like <a href="http://www.gaia-gis.it/gaia-sins/windows-bin-x86/">Gaia GIS</a>. This will often work better than QGIS for heavier data manipulation.</p></li>
<li>You can drag and drop the data into QGIS and query the data there to create map layers.</li>
<li>Exactly how the data is treated in the conversion from PBF to SQLITE is defined in osmconf.ini (if you have more than one QGIS installs, you might have several of these files!). This is quite easy to adapt to your needs.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Oct '16, 10:01</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-52566" class="comments-container">
&#10;</div>
<div id="comment-tools-52566" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52566-form-container" class="comment-form-container">
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

