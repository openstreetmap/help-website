+++
type = "question"
title = "Where to find lake shapes/data for Sweden?"
description = '''I have looked into the extracts for Sweden provided by Geofabrik but cannot seem to find any data for lakes in Sweden. I&#x27;m new with the community and using TileMill for styling layers which only include the basic natural earth shapes for each country. Any help or ideas will be much appreciated. Solu...'''
date = "2013-03-18T18:27:00Z"
lastmod = "2014-09-03T15:24:00Z"
weight = 20797
keywords = [ "shapefile", "extracts", "osm", "sweden", "lakes" ]
aliases = [ "/questions/20797" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Where to find lake shapes/data for Sweden?](/questions/20797/where-to-find-lake-shapesdata-for-sweden)

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
<span id="post-20797-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20797-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20797-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have looked into the <a href="http://download.geofabrik.de/europe/sweden.html">extracts for Sweden</a> provided by Geofabrik but cannot seem to find any data for lakes in Sweden.</p>
<p>I'm new with the community and using TileMill for styling layers which only include the basic natural earth shapes for each country.</p>
<p>Any help or ideas will be much appreciated.</p>
<p><strong>Solution:</strong></p>
<p>I downloaded the (global) lakes file from <a href="http://www.naturalearthdata.com/downloads/10m-physical-vectors/">Natural Earth</a>.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-extracts" rel="tag" title="see questions tagged &#39;extracts&#39;">extracts</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-sweden" rel="tag" title="see questions tagged &#39;sweden&#39;">sweden</span> <span class="post-tag tag-link-lakes" rel="tag" title="see questions tagged &#39;lakes&#39;">lakes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Mar '13, 18:27</strong></p>
<img src="https://secure.gravatar.com/avatar/c403e57d333f479a0e04ddf875b47347?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ptz0n&#39;s gravatar image" />
<p><span>ptz0n</span><br />
<span class="score" title="25 reputation points">25</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ptz0n has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Mar '13, 14:04</strong> </span></p>
</div>
</div>
<div id="comments-container-20797" class="comments-container">
<span id="36549"></span>
<div id="comment-36549" class="comment">
<div id="post-36549-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I can't find any major lakes in the Geofabrik data either (using QGIS), so thanks for pointing me to the Natural Earth files!</p>
</div>
<div id="comment-36549-info" class="comment-info">
<span class="comment-age">(03 Sep '14, 10:03)</span> <span class="comment-user userinfo">rotsee</span>
</div>
</div>
</div>
<div id="comment-tools-20797" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20797-form-container" class="comment-form-container">
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

<span id="36552"></span>

<div id="answer-container-36552" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36552-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36552-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-36552-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You cannot find all area objects in Geofabrik shapefiles. As said <a href="http://www.geofabrik.de/en/data/shapefiles.html">on their website</a>, these shapefiles do not contain so called multipolygons. <a href="https://wiki.openstreetmap.org/wiki/Multipolygon">Multipolygons</a> are used for mapping large area (like Lake Vättern) and areas with holes (lakes with islands).</p>
<p>Not only a lot of lakes may be missing, these shapefiles may also not contain some landuse areas, some forests etc. Geofabrik wants to earn money and processing multipolygons and other types of relations takes a lot of time.</p>
<p>There are two solutions:</p>
<ol>
<li>either you pay for a shapefile containing more data</li>
<li>or you use their extracts in PBF oder OSM-XML format. This extracts are raw data extracts (small pieces of the OSM planet file, i.e. without version history of all objects) and contain everything.</li>
</ol>
<p>If you use option (2), then you have to use a PostgresSQL database as data source in TileMill. There are several tools to import OSM data in a PostgresSQL database – <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql">osm2pgsql</a>, <a href="https://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a>, <a href="http://imposm.org/">Imposm</a></p>
<p>Or if you still want to use Shapefiles, you have to build shapefiles on your own. This is usually done using a PostgresSQL database.</p>
<p>If you do not want to use a database you can use Maperitive as renderer. It does not use a database and that's why it is not suitable for large datasets.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Sep '14, 11:05</strong></p>
<img src="https://secure.gravatar.com/avatar/d2a3b905e2632430b47dd9b8de3d8ba0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nakaner&#39;s gravatar image" />
<p><span>Nakaner</span><br />
<span class="score" title="610 reputation points">610</span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nakaner has 3 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-36552" class="comments-container">
&#10;</div>
<div id="comment-tools-36552" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36552-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="36561"></span>

<div id="answer-container-36561" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36561-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36561-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-36561-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think Natural Earth is the way to go, but just for the record, if you wanted, you could run a crude Overpass API query such as this (warning: very large file!):</p>
<p><a href="http://www.overpass-api.de/api/xapi?*%5Bnatural=water%5D%5Bbbox=7.73437,55.628,25.66406,69.13127%5D">http://www.overpass-api.de/api/xapi?*[natural=water][bbox=7.73437,55.628,25.66406,69.13127]</a></p>
<p>and get an OSM-formatted file. You could then use OGR or some other tool to convert that into a shapefile.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Sep '14, 15:24</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-36561" class="comments-container">
&#10;</div>
<div id="comment-tools-36561" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36561-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="20800"></span>

<div id="answer-container-20800" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20800-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20800-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20800-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you cannot <strong><em>see</em></strong> the lakes you are looking for when rendering the OSM data tilemill it is a matter of the renderer itself, because I am quite sure that the lake data <strong>is</strong> included in the raw OSM data that you can download from the servers of geofabrik on format osm or pbf ...</p>
<p>Without telling us how your rendering rules of tilemill look like we are quite not able to find your errors.</p>
<p>Or ask the guys from mapbox directly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Mar '13, 19:28</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-20800" class="comments-container">
&#10;</div>
<div id="comment-tools-20800" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20800-form-container" class="comment-form-container">
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

