+++
type = "question"
title = "Contours not displaying on local mapnik rendering"
description = '''I have a Ubuntu 11.10 VM running the Ubuntu Tile Server as described on the wiki. I&#x27;ve imported the Geofabrik Oxfordshire extract and the usual OSM data is rendering well. I cannot, however, get any contour lines to display.  I have followed the wiki&#x27;d instructions covering the PostGIS Approach, usi...'''
date = "2012-05-13T19:11:00Z"
lastmod = "2012-05-13T19:11:00Z"
weight = 12698
keywords = [ "rendering", "contours", "mapnik", "ubuntu" ]
aliases = [ "/questions/12698" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Contours not displaying on local mapnik rendering](/questions/12698/contours-not-displaying-on-local-mapnik-rendering)

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
<span id="post-12698-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12698-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12698-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a Ubuntu 11.10 VM running the <a href="http://wiki.openstreetmap.org/wiki/Ubuntu_tile_server">Ubuntu Tile Server</a> as described on the wiki. I've imported the Geofabrik Oxfordshire extract and the usual OSM data is rendering well. I cannot, however, get any contour lines to display.</p>
<p>I have followed the wiki'd instructions covering the <a href="http://wiki.openstreetmap.org/wiki/Contours#The_PostGIS_approach">PostGIS Approach</a>, using the import script provided to add the following files to my database:</p>
<ul>
<li><a href="http://dds.cr.usgs.gov/srtm/version2_1/SRTM3/Eurasia/N51E115.hgt.zip">http://dds.cr.usgs.gov/srtm/version2_1/SRTM3/Eurasia/N51E115.hgt.zip</a></li>
<li><a href="http://dds.cr.usgs.gov/srtm/version2_1/SRTM3/Eurasia/N51E117.hgt.zip">http://dds.cr.usgs.gov/srtm/version2_1/SRTM3/Eurasia/N51E117.hgt.zip</a></li>
<li><a href="http://dds.cr.usgs.gov/srtm/version2_1/SRTM3/Eurasia/N51E118.hgt.zip">http://dds.cr.usgs.gov/srtm/version2_1/SRTM3/Eurasia/N51E118.hgt.zip</a></li>
<li><a href="http://dds.cr.usgs.gov/srtm/version2_1/SRTM3/Eurasia/N50E115.hgt.zip">http://dds.cr.usgs.gov/srtm/version2_1/SRTM3/Eurasia/N50E115.hgt.zip</a></li>
<li><a href="http://dds.cr.usgs.gov/srtm/version2_1/SRTM3/Eurasia/N50E116.hgt.zip">http://dds.cr.usgs.gov/srtm/version2_1/SRTM3/Eurasia/N50E116.hgt.zip</a></li>
<li><a href="http://dds.cr.usgs.gov/srtm/version2_1/SRTM3/Eurasia/N50E117.hgt.zip">http://dds.cr.usgs.gov/srtm/version2_1/SRTM3/Eurasia/N50E117.hgt.zip</a></li>
<li><a href="http://dds.cr.usgs.gov/srtm/version2_1/SRTM3/Eurasia/N52E115.hgt.zip">http://dds.cr.usgs.gov/srtm/version2_1/SRTM3/Eurasia/N52E115.hgt.zip</a></li>
<li><a href="http://dds.cr.usgs.gov/srtm/version2_1/SRTM3/Eurasia/N52E116.hgt.zip">http://dds.cr.usgs.gov/srtm/version2_1/SRTM3/Eurasia/N52E116.hgt.zip</a></li>
<li><a href="http://dds.cr.usgs.gov/srtm/version2_1/SRTM3/Eurasia/N52E117.hgt.zip">http://dds.cr.usgs.gov/srtm/version2_1/SRTM3/Eurasia/N52E117.hgt.zip</a></li>
</ul>
<p>These files, I imagined, would correspond my existing OSM data.</p>
<p>To <em>/etc/mapnik-osm-data/osm.xml</em> I have added the line:</p>
<p><em>&amp;layer-contours;</em></p>
<p>To <em>/etc/mapnik-osm-data/inc/layers.xml.inc</em> I have added the line:</p>
<p><em>!ENTITY layer-contours SYSTEM "layer-contours.xml.inc</em></p>
<p>(note, I've removed some tags as the formatting was making my line disappear. This line is formatted the same as the others)</p>
<p>The file <em>/etc/mapnik-osm-data/inc/layer-contours.xml.inc</em> is as <a href="http://pastebin.com/w74iKZ7W">pasted here</a></p>
<p>I restarted renderd and got the same permissions error as described <a href="http://lists.openstreetmap.org/pipermail/dev/2010-November/021045.html">here</a>. Since granting the gis user select on geometry_columns the error has been removed, but I still cannot see any contours.</p>
<p>I have connected to the database remotely to verify that there is data in the contours table.</p>
<p>I've not done anything with extents here - are they required? Anything else I'm missing?</p>
<p>Help greatly appreciated.</p>
<p>Thanks, Joseph</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-contours" rel="tag" title="see questions tagged &#39;contours&#39;">contours</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 May '12, 19:11</strong></p>
<img src="https://secure.gravatar.com/avatar/50ac30a0553308fb00e6ac3126224239?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="IknowJoseph&#39;s gravatar image" />
<p><span>IknowJoseph</span><br />
<span class="score" title="226 reputation points">226</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="IknowJoseph has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12698" class="comments-container">
&#10;</div>
<div id="comment-tools-12698" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12698-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

