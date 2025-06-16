+++
type = "question"
title = "Lat and Long for a set of node from a way"
description = '''Hi, I&#x27;m mapping areas for fire-stations and we use a &quot;tactical grid&quot; over our map. I want to get all street names from the fire-service area and then create a list saying eg:  Nelson Street - A5 Duty Road - B6  where A5 is a square in our tactical grid and so on. I&#x27;ve a routine, converting GPS Lat a...'''
date = "2014-12-29T18:06:00Z"
lastmod = "2020-07-15T05:04:00Z"
weight = 39908
keywords = [ "latitude", "nodes", "set", "longitude", "way" ]
aliases = [ "/questions/39908" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Lat and Long for a set of node from a way](/questions/39908/lat-and-long-for-a-set-of-node-from-a-way)

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
<span id="post-39908-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39908-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-39908-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm mapping areas for fire-stations and we use a "tactical grid" over our map. I want to get all street names from the fire-service area and then create a list saying eg:</p>
<ul>
<li>Nelson Street - A5</li>
<li>Duty Road - B6</li>
</ul>
<p>where A5 is a square in our tactical grid and so on. I've a routine, converting GPS Lat and Long to our grid system.</p>
<p>The problem is that when I export OSM file (using eg this: <a href="https://www.openstreetmap.org/export#map=14/51.4898/-0.0882&amp;layers=N">https://www.openstreetmap.org/export#map=14/51.4898/-0.0882&amp;layers=N</a> )I get a file where the "real node" have their GPS values, but streets has only the "nd" reference of their node, <strong>without</strong> the GPS values.</p>
<p>Of course, I can ask OSM server for Lat and Long for each "nd", one bye one using : <a href="http://api.openstreetmap.org/api/0.6/node/2639002010">http://api.openstreetmap.org/api/0.6/node/2639002010</a> but it will take time: I need the GPS values for each point, in case of a street overlapping more than one square of our grid;</p>
<p>How can I get, in one call, GPS values of all "nd"? Is-it possible to get an OSM file, directly with them, or is there a way to send a "pack" of "nd" references to the server and get pack in one call, all Lat and Long fo each of them?</p>
<p>Thanks a lot</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-latitude" rel="tag" title="see questions tagged &#39;latitude&#39;">latitude</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-set" rel="tag" title="see questions tagged &#39;set&#39;">set</span> <span class="post-tag tag-link-longitude" rel="tag" title="see questions tagged &#39;longitude&#39;">longitude</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Dec '14, 18:06</strong></p>
<img src="https://secure.gravatar.com/avatar/bcba673681b143c7f0d7a381a4765627?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ANSB&#39;s gravatar image" />
<p><span>ANSB</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ANSB has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-39908" class="comments-container">
&#10;</div>
<div id="comment-tools-39908" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39908-form-container" class="comment-form-container">
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

<span id="39911"></span>

<div id="answer-container-39911" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39911-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39911-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-39911-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The export you mention already contains the lat/lon for all nodes. If a way says</p>
<pre><code>&lt;nd ref=&quot;1234&quot; /&gt;</code></pre>
<p>then there will be a</p>
<pre><code>&lt;node id=&quot;1234&quot; lat=&quot;1.234&quot; lon=&quot;2.345&quot; ... /&gt;</code></pre>
<p>later in the file.</p>
<p>You might however be approaching this in a way that causes you more headache and the OSM server more load than necessary. You could simply download all the data for your region of interest, import it into PostGIS with osm2pgsql (use the -l flag) and then with relative ease query the database for all roads that are inside a certain rectangle - with a query like</p>
<pre><code>SELECT name 
FROM planet_osm_line
WHERE highway is not null AND
   way &amp;&amp; ST_MakeBox2D(
       ST_Point(lon, lat), -- place lower left coordinates of box here
       ST_Point(lon, lat)) -- place upper right coordinates of box here</code></pre>
<p>Another alternative is using the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#Streets_and_other_ways">Overpass API</a> to return all highway-type ways in a given bounding box.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Dec '14, 18:51</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-39911" class="comments-container">
<span id="39914"></span>
<div id="comment-39914" class="comment">
<div id="post-39914-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Frederik! I've tried this but made a mistake for my "search" so I believed these were other nodes! Thanks again!</p>
</div>
<div id="comment-39914-info" class="comment-info">
<span class="comment-age">(29 Dec '14, 19:41)</span> <span class="comment-user userinfo">ANSB</span>
</div>
</div>
</div>
<div id="comment-tools-39911" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39911-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75710"></span>

<div id="answer-container-75710" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75710-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75710-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75710-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>for those who ask for : lon, lat from planet_osm_nodes, here is your response : "select lon::numeric/10000000 as lon, lat::numeric/10000000 as lat from planet_osm_nodes".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jul '20, 05:04</strong></p>
<img src="https://secure.gravatar.com/avatar/dfa634dabd6dbf14e4eb454ff60740d0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Abdelkader&#39;s gravatar image" />
<p><span>Abdelkader</span><br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Abdelkader has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75710" class="comments-container">
&#10;</div>
<div id="comment-tools-75710" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75710-form-container" class="comment-form-container">
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

