+++
type = "question"
title = "Append data from Geofabric not shown in OSM"
description = '''Hi Guys, After successfully building a tile server and loading data into the DB&#x27;s with below command : osm2pgsql -d gis --create --slim -G --hstore --tag-transform-script ~/src/openstreetmap-carto/openstreetmap-carto.lua -C 10000 --number-processes 4 -S ~/src/openstreetmap-carto/openstreetmap-carto....'''
date = "2021-02-10T08:20:00Z"
lastmod = "2021-02-10T15:30:00Z"
weight = 78766
keywords = [ "geofabrik" ]
aliases = [ "/questions/78766" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Append data from Geofabric not shown in OSM](/questions/78766/append-data-from-geofabric-not-shown-in-osm)

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
<span id="post-78766-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78766-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78766-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi Guys,</p>
<p>After successfully building a tile server and loading data into the DB's with below command :</p>
<p>osm2pgsql -d gis <strong>--create</strong> --slim -G --hstore --tag-transform-script ~/src/openstreetmap-carto/openstreetmap-carto.lua -C 10000 --number-processes 4 -S ~/src/openstreetmap-carto/openstreetmap-carto.style ~/data/austria-latest.osm.pbf</p>
<p>Once i want to add data for another map , example for Liechtenstein to append it to Gis database , without removing the existing data , i am using below command and it finish successfully.</p>
<p>osm2pgsql -d gis <strong>--append</strong> --slim -G --hstore --tag-transform-script ~/src/openstreetmap-carto/openstreetmap-carto.lua -C 10500 --number-processes 4 -S ~/src/openstreetmap-carto/openstreetmap-carto.style /home/renderaccount/data/liechtenstein-latest.osm.pbf</p>
<p>However the map for Liechtenstein it's not shown in the browser , i still have only data for Austria. Am i doing something wrong, or additional commands should be execute after the append of data in order to be shown on the map. Can someone help me with this topic , or to provide a useful link.</p>
<p>Thanks guys in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geofabrik" rel="tag" title="see questions tagged &#39;geofabrik&#39;">geofabrik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Feb '21, 08:20</strong></p>
<img src="https://secure.gravatar.com/avatar/b4c6f7d35e4fd1b4561578e5e376ca06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DavorB0&#39;s gravatar image" />
<p><span>DavorB0</span><br />
<span class="score" title="22 reputation points">22</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DavorB0 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78766" class="comments-container">
&#10;</div>
<div id="comment-tools-78766" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78766-form-container" class="comment-form-container">
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

<span id="78776"></span>

<div id="answer-container-78776" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78776-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78776-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78776-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can't use osm2pgsql this way (or at least it's not designed for it). Append is for updates to your existing data, not for appending additional geographical regions. You should merge your data using Osmosis before uploading to PostGIS</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Feb '21, 13:58</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-78776" class="comments-container">
<span id="78787"></span>
<div id="comment-78787" class="comment">
<div id="post-78787-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you are using osm2pgsql 1.4.0 or newer you can also simply use both input files on the command line and import them in one go. Make sure all extracts that you are using are from the same point in time.</p>
<p>Do not try this with older osm2pgsql versions, though. It is not guaranteed that it will work correctly.</p>
</div>
<div id="comment-78787-info" class="comment-info">
<span class="comment-age">(10 Feb '21, 15:30)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
</div>
<div id="comment-tools-78776" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78776-form-container" class="comment-form-container">
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

