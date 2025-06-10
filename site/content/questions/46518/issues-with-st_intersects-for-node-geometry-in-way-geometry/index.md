+++
type = "question"
title = "Issues with ST_INTERSECTS for node geometry in way geometry"
description = '''Hello I am trying to work with the full history file. I&#x27;ve used Mazderminds scripts to load an excerpt into a Postgres database.  Some spatial queries are giving me the results I expect, however I&#x27;ve found that none of nodes intersect the ways.  For example using way id : 3565059, version 5 and node...'''
date = "2015-11-10T22:38:00Z"
lastmod = "2015-12-28T22:41:00Z"
weight = 46518
keywords = [ "postgis" ]
aliases = [ "/questions/46518" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Issues with ST_INTERSECTS for node geometry in way geometry](/questions/46518/issues-with-st_intersects-for-node-geometry-in-way-geometry)

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
<span id="post-46518-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46518-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46518-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello</p>
<p>I am trying to work with the full history file. I've used Mazderminds scripts to load an excerpt into a Postgres database.</p>
<p>Some spatial queries are giving me the results I expect, however I've found that none of nodes intersect the ways.</p>
<p>For example using way id : 3565059, version 5 and node id 17543678, version 5 MUST intersect. However ST_INTERSECTS returns FALSE.</p>
<p>On the same query using ST_DWITHIN returns TRUE using parameter of 0.1 metres, but FALSE with any greater precision.</p>
<p>Has anyone else encountered the same issue or can shed some light on this problem ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Nov '15, 22:38</strong></p>
<img src="https://secure.gravatar.com/avatar/e812dbc1b44368299ea35a9a0a0f2b20?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sam75&#39;s gravatar image" />
<p><span>Sam75</span><br />
<span class="score" title="71 reputation points">71</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sam75 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Nov '15, 22:40</strong> </span></p>
</div>
</div>
<div id="comments-container-46518" class="comments-container">
&#10;</div>
<div id="comment-tools-46518" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46518-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="46913"></span>

<div id="answer-container-46913" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46913-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46913-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-46913-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I believe the problem lies in the fact the point geometry in the database created by MaZdermind's scripts is rounded to 6 decimal places, while the vertices in the line geometry is not rounded. The below query on a full history extract on nepal shows this. In the results ST_INTERSECTS will return True on record 2. The remainder returns False, but returns True using a max resolution of 0.000001 m and ST_DWITHIN.</p>
<p>The actual precision of the node_point geometry on the OSM database can be manually verified through the URL(openstreetmap.org/node/...(way id)../history)and paging down to the corresponding version number. Equally the point can be confirmed and being part of a way by the same method.</p>
<pre><code> --Create a function to find the closest vertex in a linestring to a given point (http://gis.stackexchange.com/questions/111711/find-the-closest-line-vertex-from-the-linestring-using-postgis)
&#10;CREATE OR REPLACE FUNCTION ST_AsMultiPoint(geometry) RETURNS geometry AS  &#39;SELECT ST_Union((d).geom) FROM ST_DumpPoints($1) AS d;&#39;LANGUAGE sql IMMUTABLE STRICT COST 10;
&#10;--Select a subset of data from a full history node table
&#10;WITH pointsub as (Select * FROM hist_point LIMIT 600) ,
&#10;--Find records in the full history way table (hist_line) where the nodes subset is 0.000001 metres from the way (hist_line). Add condition on time stamp creation to make sure you have found points in the lines. Display the vertex in the linestring which is closest to that point, compare against point geom
&#10;results1 as (SELECT hist_line.id line_id,pointsub.id point_id,pointsub.version point_version,hist_line.version,ST_AsText(ST_ClosestPoint(ST_AsMultiPoint(hist_line.geom), pointsub.geom)) closest_vertex_in_line,ST_AsText(pointsub.geom) point_geom
FROM hist_line,pointsub WHERE ST_DWITHIN(pointsub.geom, hist_line.geom,0.000001)AND hist_line.valid_from = pointsub.valid_from),
&#10;--As there are many versions of the lines. select 1 instance of the line where the geometry relates to each unique point
&#10;results2 as (SELECT *,ROW_NUMBER() OVER(PARTITION by results1.point_id) as rn FROM results1)
&#10;SELECT results2.point_id,results2.point_version,results2.line_id,
results2.line_version,results2.point_geom,results2.closest_vertex_in_line 
FROM results2 WHERE rn = 1</code></pre>
<p><img src="http://help.openstreetmap.org/upfiles/Issues-with-St_intersects_tCg8JYe.png" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '15, 22:52</strong></p>
<img src="https://secure.gravatar.com/avatar/e812dbc1b44368299ea35a9a0a0f2b20?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sam75&#39;s gravatar image" />
<p><span>Sam75</span><br />
<span class="score" title="71 reputation points">71</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sam75 has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Dec '15, 10:02</strong> </span></p>
</div>
</div>
<div id="comments-container-46913" class="comments-container">
<span id="46939"></span>
<div id="comment-46939" class="comment">
<div id="post-46939-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>We used to have a similar issue with osm2pgsql that I fixed a couple of years back. If you don't reproject on import I don't really see a reason for rounding in the first place (in case of osm2pgsql you would typically reproject resulting in many digits of nonsense so rounding is sensible).</p>
</div>
<div id="comment-46939-info" class="comment-info">
<span class="comment-age">(02 Dec '15, 18:58)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="46940"></span>
<div id="comment-46940" class="comment">
<div id="post-46940-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the comment Simon.The above data is unprojected (at import). Can you help me fix this bug? In order to identify rollbacks I need the full precision. Perhaps, could you give me a clue where abouts to look in the sea of scripts for Madzermind's importer tool and the Osmium framework they are built upon ?</p>
</div>
<div id="comment-46940-info" class="comment-info">
<span class="comment-age">(02 Dec '15, 22:09)</span> <span class="comment-user userinfo">Sam75</span>
</div>
</div>
<span id="46948"></span>
<div id="comment-46948" class="comment">
<div id="post-46948-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This will need some glaring at the code in question, I'll see if joto can help before we waste too much time.</p>
</div>
<div id="comment-46948-info" class="comment-info">
<span class="comment-age">(03 Dec '15, 14:00)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-46913" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46913-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="46529"></span>

<div id="answer-container-46529" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46529-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46529-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46529-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would regard this as much more likely to be a question about PostGIS processing. There are numerous examples of problems with queries of this kind on GIS Stackinfo &amp; Stackinfo. Various generic techniques can be used to mitigate against such issue: such as forcing valdity st_makevalid and checkgeometry, checking validity st_isvalid, pre-snapping objects with st_snap.</p>
<p>Also remember that there is no guarantee that any given polygon OSM way or relation at a particular time will make always be well formed for PostGIS. I <a href="http://sk53-osm.blogspot.co.uk/2011/02/exploration-of-bad-polygons.html">wrote something</a> about this a while back.</p>
<p>More detail of what you are doing may help as well. I presume these queries are against hist_view_line etc. as described MaZdermind's <a href="https://github.com/MaZderMind/osm-history-renderer">write-up</a> on github.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Nov '15, 10:37</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-46529" class="comments-container">
<span id="46538"></span>
<div id="comment-46538" class="comment">
<div id="post-46538-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the response. As I believe the problem is related to the underlying data or the transformation I hoped to have more success on this forum than stackoverflow. But I do appreciate this forum is weighted towards contributions, rather than consumption.</p>
<p>The queries are from hist_point against hist_line. I am doing some analysis on rollbacks and looking to see which rolled back nodes haved effected which ways. Spatial queries within the tables work perfectly, the issue arises on queries between tables.</p>
</div>
<div id="comment-46538-info" class="comment-info">
<span class="comment-age">(12 Nov '15, 09:27)</span> <span class="comment-user userinfo">Sam75</span>
</div>
</div>
<span id="46539"></span>
<div id="comment-46539" class="comment">
<div id="post-46539-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Well the other place is against MaZdermind's repo. This is a fairly involved technical area, and relatively few people have a setup which can test the issue. Certainly, I'd only really start to worry if it wasnt resolved with the techniques I suggest.</p>
</div>
<div id="comment-46539-info" class="comment-info">
<span class="comment-age">(12 Nov '15, 12:06)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-46529" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46529-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="46953"></span>

<div id="answer-container-46953" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46953-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46953-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46953-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I suspect line 106 here <a href="https://github.com/MaZderMind/osm-history-renderer/blob/master/importer/handler.hpp">https://github.com/MaZderMind/osm-history-renderer/blob/master/importer/handler.hpp</a> is the culprit. This sets the total number of decimal places used and setting that to 8 would cause exactly the results you see above.</p>
<p>Removing "&lt;&lt; std::setprecision(8)" and reimporting should fix the issue.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Dec '15, 16:38</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-46953" class="comments-container">
<span id="46963"></span>
<div id="comment-46963" class="comment">
<div id="post-46963-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Many thanks for looking at this Simon. Unfortunately I had already tried your suggestion, &lt;&lt; std::setprecision(8)" can also be found in line 260 of handler file and line 48 of the geombuilder file. Changing the precision or removing any of these lines, does not change the output format, the point geom remains rounded to precision 8 (or 6 decimal places - I have not imported files that with geometries above 100 degrees longitude). The linestring vertices precision are as per the url of the node. Any advice from Jochen Topf?</p>
</div>
<div id="comment-46963-info" class="comment-info">
<span class="comment-age">(03 Dec '15, 21:09)</span> <span class="comment-user userinfo">Sam75</span>
</div>
</div>
<span id="46964"></span>
<div id="comment-46964" class="comment">
<div id="post-46964-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did you reimport? The rounding is done when writing to the database (I would suggest testing on a small extract naturally). Jochen is not aware of any rounding in OSMIUM (but the tools in question are using a very old version in any case).</p>
</div>
<div id="comment-46964-info" class="comment-info">
<span class="comment-age">(03 Dec '15, 21:11)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="46967"></span>
<div id="comment-46967" class="comment not_top_scorer">
<div id="post-46967-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Correct, amended script(s) and dropped existing tables and reimported. For good measure I set up a fresh database. I am aware it uses the older version of OSMIUM. There were two warnings when unpacking osmium regarding the xml tag on the doxyfile, I was given the option to update or remove, I chose to update. Since Madzermind's application is based on the original OSMIUM I assume it is best not to play with that. When you fixed the bug in OSM2PGSQL was it as simple as resetting a precision parameter ?</p>
</div>
<div id="comment-46967-info" class="comment-info">
<span class="comment-age">(03 Dec '15, 22:13)</span> <span class="comment-user userinfo">Sam75</span>
</div>
</div>
<span id="46971"></span>
<div id="comment-46971" class="comment not_top_scorer">
<div id="post-46971-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Do you think it could be something in the WKB writer : <a href="http://geos.osgeo.org/doxygen/WKBWriter_8h_source.html">http://geos.osgeo.org/doxygen/WKBWriter_8h_source.html</a> and its point class dependency <a href="http://geos.osgeo.org/doxygen/Point_8h_source.html.">http://geos.osgeo.org/doxygen/Point_8h_source.html.</a></p>
</div>
<div id="comment-46971-info" class="comment-info">
<span class="comment-age">(03 Dec '15, 23:48)</span> <span class="comment-user userinfo">Sam75</span>
</div>
</div>
<span id="46973"></span>
<div id="comment-46973" class="comment not_top_scorer">
<div id="post-46973-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Looking at line 117 it writes out WKT and IMHO that should be correct if you remove the setPrecision, what -dows- look wrong there is the SRID spec, given that you should be writing lat lon, but maybe I missed something.</p>
</div>
<div id="comment-46973-info" class="comment-info">
<span class="comment-age">(04 Dec '15, 13:33)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="46981"></span>
<div id="comment-46981" class="comment not_top_scorer">
<div id="post-46981-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't have a reason or good enough understanding to disagree with your rationale, but removing lines of code with setprecision definitely does not work for me. Nonetheless, many thanks for your efforts, it's much appreciated.</p>
</div>
<div id="comment-46981-info" class="comment-info">
<span class="comment-age">(04 Dec '15, 20:56)</span> <span class="comment-user userinfo">Sam75</span>
</div>
</div>
<span id="46982"></span>
<div id="comment-46982" class="comment not_top_scorer">
<div id="post-46982-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not fully understanding your problem, but the <em>default</em> precision in C++ is (often? always?) 6. So removing <code>std::setprecision()</code> doesn't necessarily lead to a higher precision. Instead it might be necessary to increase the specified precision or even add <code>std::setprecision()</code> at some places. So in this specific case <code>std::setprecision(8)</code> was not meant to lower the precision but to raise it instead.</p>
</div>
<div id="comment-46982-info" class="comment-info">
<span class="comment-age">(04 Dec '15, 22:18)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="46983"></span>
<div id="comment-46983" class="comment not_top_scorer">
<div id="post-46983-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I have also tried raising the precision, and tried std ::setprecision() just now, again no change. This line of code can't be causing the bug.</p>
</div>
<div id="comment-46983-info" class="comment-info">
<span class="comment-age">(04 Dec '15, 22:33)</span> <span class="comment-user userinfo">Sam75</span>
</div>
</div>
<span id="46988"></span>
<div id="comment-46988" class="comment">
<div id="post-46988-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>IMHO one us will actually have to install the software and test .. will however take a couple of days.</p>
</div>
<div id="comment-46988-info" class="comment-info">
<span class="comment-age">(05 Dec '15, 00:18)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="47297"></span>
<div id="comment-47297" class="comment">
<div id="post-47297-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>setprecision(8) is not enough. You need 7 digits after the decimal point to get the full precision OSM supports, plus 3 digits before it, makes 10. So setprecision(10) should be correct. Removing the setprecision() will get you the default of 6 which is definitely not enough.</p>
</div>
<div id="comment-47297-info" class="comment-info">
<span class="comment-age">(27 Dec '15, 16:28)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
<span id="47304"></span>
<div id="comment-47304" class="comment">
<div id="post-47304-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Many thanks Simon, Alex and Jochen. Increasing setprecision solves the problem. I had failed with earlier attempts as I had not remade the executable file after amending the 'setprecision' in the handler and geombuilder files. As Jochen says setprecision(10) allows for the full OSM precision.</p>
</div>
<div id="comment-47304-info" class="comment-info">
<span class="comment-age">(28 Dec '15, 22:41)</span> <span class="comment-user userinfo">Sam75</span>
</div>
</div>
</div>
<div id="comment-tools-46953" class="comment-tools">
<span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-46953-form-container" class="comment-form-container">
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

