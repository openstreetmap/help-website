+++
type = "question"
title = "Using R to get lat and lon from OSM_ids (without assistance of external software e.g. QGIS)"
description = '''Hello,  I was wondering if there is an algortihm in R that will extract the lat and lons for OSM_ids. Ideally, it would give one lat and lon (as opposed to a Polygon). I have been using QGIS and post gis to extract them via the attribute table - copied and pasted to Libre Office/Excel. I have looked...'''
date = "2014-06-18T10:56:00Z"
lastmod = "2014-07-25T12:45:00Z"
weight = 34080
keywords = [ "latitude", "r", "longitude", "osm_id" ]
aliases = [ "/questions/34080" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Using R to get lat and lon from OSM_ids (without assistance of external software e.g. QGIS)](/questions/34080/using-r-to-get-lat-and-lon-from-osm_ids-without-assistance-of-external-software-eg-qgis)

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
<span id="post-34080-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34080-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-34080-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I was wondering if there is an algortihm in R that will extract the lat and lons for OSM_ids. Ideally, it would give one lat and lon (as opposed to a Polygon).</p>
<p>I have been using QGIS and post gis to extract them via the attribute table - copied and pasted to Libre Office/Excel. I have looked at some of the methods for getting the lat and longs for nodes, ways, relations via the osm api or overpass api, but they don't seem to do OSM_ids (at least as far as I can determine).</p>
<p>Ideally, I would like to try an algorthim that doesn't involve extracting the information from an external source, but rather one that extracts the lat and long tidily from the OSM_id, i.e. reverse engineering.</p>
<p>I would any assistance you could offer. Many thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-latitude" rel="tag" title="see questions tagged &#39;latitude&#39;">latitude</span> <span class="post-tag tag-link-r" rel="tag" title="see questions tagged &#39;r&#39;">r</span> <span class="post-tag tag-link-longitude" rel="tag" title="see questions tagged &#39;longitude&#39;">longitude</span> <span class="post-tag tag-link-osm_id" rel="tag" title="see questions tagged &#39;osm_id&#39;">osm_id</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jun '14, 10:56</strong></p>
<img src="https://secure.gravatar.com/avatar/599cf814d746d24710bc2550658779cb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Student&#39;s gravatar image" />
<p><span>Student</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Student has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-34080" class="comments-container">
<span id="34082"></span>
<div id="comment-34082" class="comment">
<div id="post-34082-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't quite understand what you mean by "I have looked at some of the methods for getting the lat and longs for nodes, ways, relations via the osm api or overpass api, but they don't seem to do OSM_ids".<br />
</p>
<p>Can you give an example of an "OSM_id" so that we can be sure we're talking about the same thing? I'm not aware of a globally unique "OSM_id" though of course nodes, ways and relations have unique IDs - but (for example) there's both a node 133449728 and a way 133449728.</p>
</div>
<div id="comment-34082-info" class="comment-info">
<span class="comment-age">(18 Jun '14, 11:12)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="34083"></span>
<div id="comment-34083" class="comment">
<div id="post-34083-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes I will post an example of an OSM_id later. It would be very useful if node ids (or way ids or relation ids) and OSM_ids were the same thing. Although I dont think so because i obtained node ids for the same dataset using osmconvert and they turned for to be different to the osm_id , in that the node ids were much longer. Anyhow, I will post you an example later (I dont have my laptop on me now). Thanks for the quick reply!</p>
</div>
<div id="comment-34083-info" class="comment-info">
<span class="comment-age">(18 Jun '14, 11:35)</span> <span class="comment-user userinfo">Student</span>
</div>
</div>
<span id="34117"></span>
<div id="comment-34117" class="comment not_top_scorer">
<div id="post-34117-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>wkt_geom gid osm_id POLYGON((-6.33255269999999992 53.28642250000000047,-6.33246350000000024 53.28647680000000264,-6.3323330999999996 53.28646859999999919,-6.33258360000000042 53.28635700000000242,-6.33255269999999992 53.28642250000000047)) 396 25857740 POLYGON((-6.34702140000000004 53.40131290000000064,-6.34636050000000029 53.40164039999999801,-6.34611160000000041 53.40146130000000113,-6.34678970000000042 53.40113379999999665,-6.34702140000000004 53.40131290000000064)) 256 23750977</p>
<p>above is an example of the data I copy from the attribute table in QGIS. If you are interested it is from the OSM buildings shape file for Ireland. It gives the osm_id and the lats and longs. Which is what I need. But I would like to get the same thing, only, tidier in R, i.e. the osm_id and lat lon.</p>
<p>I guess if somebody has done this type of work previously they will have some ideas :)</p>
</div>
<div id="comment-34117-info" class="comment-info">
<span class="comment-age">(18 Jun '14, 19:49)</span> <span class="comment-user userinfo">Student</span>
</div>
</div>
<span id="34121"></span>
<div id="comment-34121" class="comment not_top_scorer">
<div id="post-34121-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That last number looks suspiciously like the way ID for this building near Blanchardstown:</p>
<p><a href="https://www.openstreetmap.org/way/23750977">https://www.openstreetmap.org/way/23750977</a></p>
<p>The other one (25857740) is a building south of the Tallaght M50 junction, which would make sense if it's from the shapefile for Irish buildings.</p>
<p>Of the data that you've quoted, which do you consider to be the "osm_id"? I'd expect that QGIS will have an internal ID for the shapefile, which won't be in OSM.</p>
</div>
<div id="comment-34121-info" class="comment-info">
<span class="comment-age">(18 Jun '14, 23:08)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="34129"></span>
<div id="comment-34129" class="comment not_top_scorer">
<div id="post-34129-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>osm_id would be 25857740 and 23750977 in this example. The osm_id covers nodes, ways, relations. Yes I think QGIS apply the osm_id and it is not a generic id. There are lots of questions online about coverting the osm_id to lat and lon but the answers suggest using overpass api or osm api. I was hoping that there is a method of obtaining the latitude and longitude from the osm_id in the same way the apis do but without a necessity to indicate if it is a node, way, relation. Any assistance would be greatly appreciated.</p>
</div>
<div id="comment-34129-info" class="comment-info">
<span class="comment-age">(19 Jun '14, 08:23)</span> <span class="comment-user userinfo">Student</span>
</div>
</div>
<span id="34131"></span>
<div id="comment-34131" class="comment">
<div id="post-34131-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This is not possible because the ID is only unique <em>within</em> the same <a href="https://wiki.openstreetmap.org/wiki/Elements">element</a> type. Or in other words: There can and will be different elements with the same ID (e.g. a <a href="https://www.openstreetmap.org/node/123">node</a>, a <a href="https://www.openstreetmap.org/way/123">way</a> and a (now deleted) <a href="https://www.openstreetmap.org/relation/123">relation</a> all having the ID <em>123</em>). Therefore you have to know the element type a specific ID belongs to.</p>
</div>
<div id="comment-34131-info" class="comment-info">
<span class="comment-age">(19 Jun '14, 08:32)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="34132"></span>
<div id="comment-34132" class="comment not_top_scorer">
<div id="post-34132-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the fast response. OK, I guess an if else statement in code might do the trick. Do you, or does anyone else know if it is possible to extract lat and lon from osm_id - with knowledge of whether it's a node or way - but without using an api. I mean how do the apis do it ? Can that be reproduced in R ?</p>
</div>
<div id="comment-34132-info" class="comment-info">
<span class="comment-age">(19 Jun '14, 08:43)</span> <span class="comment-user userinfo">Student</span>
</div>
</div>
<span id="34133"></span>
<div id="comment-34133" class="comment">
<div id="post-34133-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Are you aware that there is an OSM package for R? See <a href="http://osmar.r-forge.r-project.org/">http://osmar.r-forge.r-project.org/</a> and search for various blog posts about it.</p>
</div>
<div id="comment-34133-info" class="comment-info">
<span class="comment-age">(19 Jun '14, 08:59)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="34134"></span>
<div id="comment-34134" class="comment">
<div id="post-34134-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>thanks for the reply, yes I used osmar, it basically involves using the api to get the information. Was hoping to see what the api does and apply it in R, rather than using the api via an R package. Anyhow, if that's all that's available, I may just have to work with it. Thanks to all who have contributed, its been useful discussing it.</p>
</div>
<div id="comment-34134-info" class="comment-info">
<span class="comment-age">(19 Jun '14, 10:08)</span> <span class="comment-user userinfo">Student</span>
</div>
</div>
</div>
<div id="comment-tools-34080" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-34080-form-container" class="comment-form-container">
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

<span id="35176"></span>

<div id="answer-container-35176" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35176-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35176-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35176-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I found a work-around to this question. It gives you the lat and lon coordinates for the shape file which you can then bind with the shape file columns to create a new data set. Thanks to the r-sig-Geo email list and <a href="http://www.inside-r.org/packages/cran/rgdal/docs/ogrInfo.">http://www.inside-r.org/packages/cran/rgdal/docs/ogrInfo.</a></p>
<pre><code>library(rgdal)
shape&lt;-readOGR(&quot;location of shape file/folder&quot;,layer=&quot;buildings&quot;)
names(shape)
[[1] &quot;osm_id&quot; &quot;name&quot;   &quot;type&quot;
&#10;lat &lt;- coordinates(shape)[,1]</code></pre>
<p>lon &lt;- coordinates(shape)[,2]</p>
<p>a&lt;-as.data.frame(shape$osm_id)</p>
<p>b&lt;-as.data.frame(shape$name)</p>
<p>c&lt;-as.data.frame(shape$type)</p>
<p>data &lt;- cbind(lat,lon,a,b,c)</p>
<p>you can then name the columns if you so wish. you now have lat &amp; lon coordinates for the osm_id</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jul '14, 12:45</strong></p>
<img src="https://secure.gravatar.com/avatar/599cf814d746d24710bc2550658779cb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Student&#39;s gravatar image" />
<p><span>Student</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Student has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jul '14, 15:16</strong> </span></p>
</div>
</div>
<div id="comments-container-35176" class="comments-container">
&#10;</div>
<div id="comment-tools-35176" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35176-form-container" class="comment-form-container">
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

