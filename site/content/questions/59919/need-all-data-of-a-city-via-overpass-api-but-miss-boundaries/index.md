+++
type = "question"
title = "need all data of a city via Overpass API, but miss boundaries"
description = '''Hi! I need to get all the data of a city (including its boundaries) with the overpass API and use Overpass Turbo. I did the query like this: [out:xml]; (  node(48.2315, 17.9596, 48.3909, 18.2497);  &amp;lt;; ); out; within this bounding box is the city Nitra (slovakai). after downloading the data as an ...'''
date = "2017-10-02T14:06:00Z"
lastmod = "2017-10-16T07:27:00Z"
weight = 59919
keywords = [ "qgis", "overpass", "boundaries", "overpass-turbo", "overpass-api" ]
aliases = [ "/questions/59919" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [need all data of a city via Overpass API, but miss boundaries](/questions/59919/need-all-data-of-a-city-via-overpass-api-but-miss-boundaries)

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
<span id="post-59919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59919-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-59919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi! I need to get all the data of a city (including its boundaries) with the overpass API and use Overpass Turbo. I did the query like this:</p>
<p>[out:xml]; ( node(48.2315, 17.9596, 48.3909, 18.2497); &lt;; ); out;</p>
<p>within this bounding box is the city Nitra (slovakai).</p>
<p>after downloading the data as an .osm-file I generated a SpatiaLite-DB in QGIS and afterwards I generated Points-, Lines-, and Polygonlayers in QGIS. BUT I CANNOT FIND THE TAG "BOUNDARY" IN THE DATASET, what am I doing wrong?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Oct '17, 14:06</strong></p>
<img src="https://secure.gravatar.com/avatar/b679fe1416854d423dcc8d61793531ae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sim_93&#39;s gravatar image" />
<p><span>sim_93</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sim_93 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-59919" class="comments-container">
&#10;</div>
<div id="comment-tools-59919" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59919-form-container" class="comment-form-container">
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

<span id="59968"></span>

<div id="answer-container-59968" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59968-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59968-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-59968-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi <a href="https://help.openstreetmap.org/users/14271/sim_93">@sim_93</a>. If you use the vector tools menu from QGIS you can only get points, lines and polygon layers thus no relations (multipolygons and boundaries). Instead, you can use the <code>ogr2ogr</code> command to generate a Spatialite *.db file and then connect to it in QGIS and you'll get relations (multilines and multipolygons along with boundaries).</p>
<p>This is a sample command:</p>
<pre><code>ogr2ogr -f &quot;SQLite&quot; -dsco SPATIALITE=YES dbfile.db osmfile.osm</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Oct '17, 11:13</strong></p>
<img src="https://secure.gravatar.com/avatar/15d45a99f101e06c9e79916af33f8336?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Privatemajory&#39;s gravatar image" />
<p><span>Privatemajory</span><br />
<span class="score" title="1125 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Privatemajory has 4 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-59968" class="comments-container">
<span id="59971"></span>
<div id="comment-59971" class="comment">
<div id="post-59971-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi <a href="https://help.openstreetmap.org/users/14163/privatemajory">@Privatemajory</a> ! Thanks for your answer :) i'm a total beginner and have no idea how to handle it.. i have the .osm-file and QGIS, can you tell me how to go through it in detail? it would be such a great help!! :) btw if its relevant, i have a mac... greetings</p>
</div>
<div id="comment-59971-info" class="comment-info">
<span class="comment-age">(05 Oct '17, 13:56)</span> <span class="comment-user userinfo">sim_93</span>
</div>
</div>
<span id="59975"></span>
<div id="comment-59975" class="comment">
<div id="post-59975-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have never used a Mac but all I know is that ogr2ogr is part of GDAL. If you have QGIS then GDAL should already be installed as well. If not, install it. You can try running the command above on a terminal and see what it gives. Regards</p>
</div>
<div id="comment-59975-info" class="comment-info">
<span class="comment-age">(05 Oct '17, 15:20)</span> <span class="comment-user userinfo">Privatemajory</span>
</div>
</div>
<span id="60034"></span>
<div id="comment-60034" class="comment">
<div id="post-60034-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>@ Privatemajory, thanky a lot, i've installed GDAL now, but when i try to run the command i get the answer "Unable to open datasource `nitra.osm' with the following drivers. -&gt; PCIDSK -&gt; netCDF -&gt; ... " what did i wrong? regards</p>
</div>
<div id="comment-60034-info" class="comment-info">
<span class="comment-age">(10 Oct '17, 07:49)</span> <span class="comment-user userinfo">sim_93</span>
</div>
</div>
<span id="60039"></span>
<div id="comment-60039" class="comment">
<div id="post-60039-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14271/sim_93">@sim_93</a> I don't know why it doesn't work but you can still check if your GDAL version is not too old (better use the newest version possible). Or maybe it's the format of your OSM file (I don't know about formats generated by Overpass API as I have only tested this on a OSM file exported directly from OpenStreetMap's site using their Export tool). May someone experimented come to help you as I don't know this well.</p>
</div>
<div id="comment-60039-info" class="comment-info">
<span class="comment-age">(10 Oct '17, 09:27)</span> <span class="comment-user userinfo">Privatemajory</span>
</div>
</div>
<span id="60077"></span>
<div id="comment-60077" class="comment">
<div id="post-60077-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14163/privatemajory">@Privatemajory</a> ok, but thanks for your help anyway! :) i hav the newest version of GDAL and the standard ism-file... i will see if i find a way.. thanks!</p>
</div>
<div id="comment-60077-info" class="comment-info">
<span class="comment-age">(12 Oct '17, 07:40)</span> <span class="comment-user userinfo">sim_93</span>
</div>
</div>
</div>
<div id="comment-tools-59968" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59968-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60098"></span>

<div id="answer-container-60098" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60098-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60098-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60098-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your Overpass API query only queries nodes in the area of interest. Ways and relations are retrieved by your use of the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_up_.28.3C.29">recurse up</a> feature (the &lt; sign). This returns only ways which use one of the nodes and relations which use one of the nodes.</p>
<p>boundary=* is used on relations (for areas) and often on unclosed ways (the boundary line).</p>
<p>The boundary relation you queried might not contain any your area of interest because the only nodes boundary relations contain are admin centre nodes and sometimes labelling hints (as nodes).</p>
<p>The correct query would be</p>
<pre><code>[out:xml];
rel(48.2315, 17.9596, 48.3909, 18.2497)-&gt;.rels;
(
  way(r.rels)(48.2315, 17.9596, 48.3909, 18.2497);
  node(r.rels)(48.2315, 17.9596, 48.3909, 18.2497);
)-&gt;.relmembers;
(
  way.relmembers;
  node.relmembers;
  way(48.2315, 17.9596, 48.3909, 18.2497);
  node(48.2315, 17.9596, 48.3909, 18.2497);
)-&gt;.nonrels;
.rels out;
.nonrels out;
.nonrels &gt;-&gt;.nonrelsreferred;
.nonrelsreferred out;</code></pre>
<p>If you need all members of all relations in the result set, use the following (slower) query:</p>
<pre><code>[out:xml];
(
  rel(48.2315, 17.9596, 48.3909, 18.2497);
  way(48.2315, 17.9596, 48.3909, 18.2497);
  node(48.2315, 17.9596, 48.3909, 18.2497);
)-&gt;.result;
.result out;
.result &gt;-&gt;.recurseresult;
.recurseresult out;</code></pre>
<p>I suggest you to use the Slovakia extract from Geofabrik instead and extract your area of interest using either <a href="https://wiki.openstreetmap.org/wiki/Osmconvert">osmconvert</a> or the <a href="http://osmcode.org/osmium-tool/">Osmium tool</a> (command <a href="http://osmcode.org/osmium-tool/manual.html#creating-geographic-extracts">extract</a>).</p>
<p>Please keep in mind that many programs expect OSM data to be sorted by type (first nodes, then ways, then relations) and the objects in these three sections ascending by ID. <a href="https://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a> can sort OSM files.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Oct '17, 10:57</strong></p>
<img src="https://secure.gravatar.com/avatar/d2a3b905e2632430b47dd9b8de3d8ba0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nakaner&#39;s gravatar image" />
<p><span>Nakaner</span><br />
<span class="score" title="610 reputation points">610</span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nakaner has 3 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-60098" class="comments-container">
<span id="60146"></span>
<div id="comment-60146" class="comment">
<div id="post-60146-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/8569/nakaner"></a><a href="https://help.openstreetmap.org/users/8569/nakaner">@Nakaner</a> Thanks for the info! but don't have a way and a relation contains nodes anyway? so why can't i do this with the recurse up feature?</p>
<p>and does the geofabirik-file include all features? because you can often read that at the geofarbik-files there are often missing multipolygons and relations.. regards simon</p>
</div>
<div id="comment-60146-info" class="comment-info">
<span class="comment-age">(16 Oct '17, 07:27)</span> <span class="comment-user userinfo">sim_93</span>
</div>
</div>
</div>
<div id="comment-tools-60098" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60098-form-container" class="comment-form-container">
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

