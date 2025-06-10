+++
type = "question"
title = "Ogr2Osm: Imported data shifted by 176m, 222°(exported from ArcGIS)"
description = '''We were given city administrative boundary data as .shp files with the permission to import those to OSM / use on AddisMap.com. I have used the Ogr2Osm scripts to convert this data to the OSM format. I tried all three versions (old SVN, UVM rewrite, pnorman&#x27;s updated version) which are linked in the...'''
date = "2012-12-03T13:00:00Z"
lastmod = "2013-08-18T19:36:00Z"
weight = 18166
keywords = [ "shapefile", "import", "gis", "ogr2osm", "arcgis" ]
aliases = [ "/questions/18166" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Ogr2Osm: Imported data shifted by 176m, 222°(exported from ArcGIS)](/questions/18166/ogr2osm-imported-data-shifted-by-176m-222exported-from-arcgis)

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
<span id="post-18166-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18166-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18166-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We were given city administrative boundary data as .shp files with the permission to import those to OSM / use on <a href="http://www.addismap.com">AddisMap.com</a>.</p>
<p>I have used the <a href="http://wiki.openstreetmap.org/wiki/Ogr2osm">Ogr2Osm</a> scripts to convert this data to the OSM format. I tried all three versions (old SVN, UVM rewrite, pnorman's updated version) which are linked in the Wiki.</p>
<p>All of them produce the same results, but when I load the data in JOSM and compare them with the existing city data (Addis Ababa, Ethiopia), the imported data seems to be shifted by 176m, 222° (I measured this by drawing a way from the point where it should be to the imported point in JOSM)</p>
<p>When using Ogr2Osm it produces the following output:</p>
<pre><code>Detected projection metadata:
PROJCS[&quot;Adindan_UTM_Zone_37N&quot;,
    GEOGCS[&quot;GCS_Adindan&quot;,
        DATUM[&quot;Adindan&quot;,
            SPHEROID[&quot;Clarke_1880_RGS&quot;,6378249.145,293.465]],
        PRIMEM[&quot;Greenwich&quot;,0.0],
        UNIT[&quot;Degree&quot;,0.0174532925199433]],
    PROJECTION[&quot;Transverse_Mercator&quot;],
    PARAMETER[&quot;False_Easting&quot;,500000.0],
    PARAMETER[&quot;False_Northing&quot;,0.0],
    PARAMETER[&quot;Central_Meridian&quot;,39.0],
    PARAMETER[&quot;Scale_Factor&quot;,0.9996],
    PARAMETER[&quot;Latitude_Of_Origin&quot;,0.0],
    UNIT[&quot;Meter&quot;,1.0]]</code></pre>
<p>The .prj file we received has the following content:</p>
<pre><code>PROJCS[&quot;Adindan_UTM_Zone_37N&quot;,GEOGCS[&quot;GCS_Adindan&quot;,DATUM[&quot;D_Adindan&quot;,SPHEROID[&quot;Clarke_1880_RGS&quot;,6378249.145,293.465]],PRIMEM[&quot;Greenwich&quot;,0.0],UNIT[&quot;Degree&quot;,0.0174532925199433]],PROJECTION[&quot;Transverse_Mercator&quot;],PARAMETER[&quot;False_Easting&quot;,500000.0],PARAMETER[&quot;False_Northing&quot;,0.0],PARAMETER[&quot;Central_Meridian&quot;,39.0],PARAMETER[&quot;Scale_Factor&quot;,0.9996],PARAMETER[&quot;Latitude_Of_Origin&quot;,0.0],UNIT[&quot;Meter&quot;,1.0]]</code></pre>
<p>The data was exported from ArcGIS.</p>
<p>What can be the source for the error? How can it be fixed?</p>
<p>EDIT: Same problem when I use ogr2ogr and shp2osm</p>
<pre><code>ogr2ogr -t_srs WGS84 -s_srs &quot;ESRI::subcities.prj&quot; &quot;subcities_converted.shp&quot; &quot;subcities.shp&quot; 
perl shp2osm.pl subcities_converted.shp &gt; subcities.osm</code></pre>
<p><em>Semi cross-posted to <a href="http://gis.stackexchange.com/questions/42965/what-can-go-wrong-in-utm-to-wgs1984-conversion-shifted-data">Stackexchange GIS</a></em></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-gis" rel="tag" title="see questions tagged &#39;gis&#39;">gis</span> <span class="post-tag tag-link-ogr2osm" rel="tag" title="see questions tagged &#39;ogr2osm&#39;">ogr2osm</span> <span class="post-tag tag-link-arcgis" rel="tag" title="see questions tagged &#39;arcgis&#39;">arcgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Dec '12, 13:00</strong></p>
<img src="https://secure.gravatar.com/avatar/9ac1de0d402dfdf47bd4c4d664156c64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AddisMap_Alexander&#39;s gravatar image" />
<p><span>AddisMap_Ale...</span><br />
<span class="score" title="1120 reputation points"><span>1.1k</span></span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AddisMap_Alexander has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Apr '15, 09:54</strong> </span></p>
</div>
</div>
<div id="comments-container-18166" class="comments-container">
&#10;</div>
<div id="comment-tools-18166" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18166-form-container" class="comment-form-container">
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

<span id="18189"></span>

<div id="answer-container-18189" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18189-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18189-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-18189-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As found out on <a href="http://gis.stackexchange.com/questions/42965/what-can-go-wrong-in-utm-to-wgs1984-conversion-shifted-data/43095#43095">GIS.stackexchange</a> I need to specify the projection string manually, because the ogr library does not detect it properly / does not do the datum conversion:</p>
<pre><code>python ogr2osm.py -p &quot;+proj=utm +zone=37 +ellps=clrk80 +towgs84=-166,-15,204,0,0,0,0 +units=m +no_defs&quot; inputfile.osm</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Dec '12, 14:26</strong></p>
<img src="https://secure.gravatar.com/avatar/9ac1de0d402dfdf47bd4c4d664156c64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AddisMap_Alexander&#39;s gravatar image" />
<p><span>AddisMap_Ale...</span><br />
<span class="score" title="1120 reputation points"><span>1.1k</span></span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AddisMap_Alexander has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18189" class="comments-container">
<span id="25380"></span>
<div id="comment-25380" class="comment">
<div id="post-25380-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think we used to have a similar problem with EPSG:27700.</p>
</div>
<div id="comment-25380-info" class="comment-info">
<span class="comment-age">(14 Aug '13, 18:52)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="25557"></span>
<div id="comment-25557" class="comment">
<div id="post-25557-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@SK53</span>: did you solve it the same way? Or another?</p>
</div>
<div id="comment-25557-info" class="comment-info">
<span class="comment-age">(18 Aug '13, 18:28)</span> <span class="comment-user userinfo">AddisMap_Ale...</span>
</div>
</div>
<span id="25560"></span>
<div id="comment-25560" class="comment">
<div id="post-25560-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yes I added the explicit Helmert factors (the 7 towgs84 parameters), Chris Hill blogged about it at the time (<a href="http://chris-osm.blogspot.co.uk/2010/04/getting-boundaries-right.html),">http://chris-osm.blogspot.co.uk/2010/04/getting-boundaries-right.html),</a> but IIRC there were still bugs in proj4 (and therefore ogr2ogr, PostGIS) relating to WGS84 and OSGB transformations in 2011.</p>
<p>A useful test if you have postgis, but I expect can be done with ogr2ogr is to use a well-defined point and perform transforms between various projections to test accuracy (particularly if there is a non-porj4 transformation available for comparison, as was the case for OSGB).</p>
</div>
<div id="comment-25560-info" class="comment-info">
<span class="comment-age">(18 Aug '13, 19:36)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-18189" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18189-form-container" class="comment-form-container">
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

