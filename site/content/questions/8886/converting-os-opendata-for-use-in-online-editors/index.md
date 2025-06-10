+++
type = "question"
title = "Converting OS OpenData for use in online editors"
description = '''I am interested to use OS OpenData products as references and to upload local civil parish boundaries in my area of South Oxfordshire, perhaps. My preferred online editor is JOSM. My guess is that there are numerous means of converting the OpenData ESRI Shapefiles into .gpx or .osm file formats to o...'''
date = "2011-11-08T11:44:00Z"
lastmod = "2011-11-08T11:44:00Z"
weight = 8886
keywords = [ "opendata", "josm" ]
aliases = [ "/questions/8886" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Converting OS OpenData for use in online editors](/questions/8886/converting-os-opendata-for-use-in-online-editors)

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
<span id="post-8886-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8886-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8886-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am interested to use OS OpenData products as references and to upload local civil parish boundaries in my area of South Oxfordshire, perhaps. My preferred online editor is JOSM. My guess is that there are numerous means of converting the OpenData ESRI Shapefiles into .gpx or .osm file formats to open in JOSM. As I understand it, online .shp files can be viewed in Potlatch, also. I use MapInfo for processing where I can because I have amassed so much reference material with it and I am able to make small extractions of OpenData very easily by this means. I have made six .gpx files:</p>
<ol>
<li>using QGIS to reproject to WGS84 in ESRI .shp format</li>
<li>using QGIS to reproject to WGS84 in MapInfo .mif format<br />
</li>
<li>using FWTools and ogr2ogr to reproject to WGS84 from the original OpenData .prj file</li>
<li>using FWTools and ogr2ogr to reproject to WGS84 from a modified .prj file created by user SK53</li>
<li>using FWTools and ogr2ogr to reproject to WGS84 entering EPSG:27700 as the .prj file</li>
<li>using MapInfo to convert from British National Grid to WGS84</li>
</ol>
<p>I opened every reprojected file in MapInfo, made my extractions and used its Universal Translator tool to make new .shp files. I used MN DNR-Garmin to create .gpx files.<br />
Opening these files in JOSM over a downloaded area of South Oxfordshire in which woodland data from VectorMap District has been uploaded already, I find the following differences in my data position to that already present:</p>
<ol>
<li>1.9 metres north</li>
<li>1.6 metres north</li>
<li>1.9 metres north</li>
<li>1.6 metres north</li>
<li>1.9 metres north</li>
<li>3.4 metres south</li>
</ol>
<p>I have contacted the creator of the woodland area in question but have received no reply, so I cannot yet know what method he employed. I have yet to try other methods such as ogr2osm. As I have commented previously, I am pretty hopeless with DOS and command lines. I am grateful to Chris Hill and Ed Loach, though, for pointing me in the right direction and I have downloaded Python. It remains to be seen whether I can create a .osm file for further comparison without assistance.</p>
<p>The reason I submit this post is to determine what other contributors to OSM think about minor differences in data positions, bearing in mind our GPSr devices are only accurate to + or - three metres, say. On the other hand, should not third-party data occupy one single position, and what is the preferred method to achieve this? I should feel happier, armed with this knowledge, to upload some OpenData.</p>
<p>I apologise, in advance, for the long-winded nature of my post!</p>
<p>Bob Hawkins</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-opendata" rel="tag" title="see questions tagged &#39;opendata&#39;">opendata</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Nov '11, 11:44</strong></p>
<img src="https://secure.gravatar.com/avatar/ffcc41f13929627742b4936ec178c6f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="silver%20mapper&#39;s gravatar image" />
<p><span>silver mapper</span><br />
<span class="score" title="256 reputation points">256</span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="27 badges"><span class="silver">●</span><span class="badgecount">27</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="silver mapper has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Nov '11, 12:09</strong> </span></p>
</div>
</div>
<div id="comments-container-8886" class="comments-container">
&#10;</div>
<div id="comment-tools-8886" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8886-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

