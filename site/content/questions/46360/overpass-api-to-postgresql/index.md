+++
type = "question"
title = "Overpass API to PostgreSQL ?"
description = '''Hello again, I would like to know how can i use the overpass api of pyhton to store information into my Postgresql database (i have a PostGIS extencion) . My idea was to get the &quot;id&quot; of the nodes and then creating an &quot;id&quot; camp on the database gather the information of the tags in question. Thank you...'''
date = "2015-11-03T10:09:00Z"
lastmod = "2015-11-04T12:03:00Z"
weight = 46360
keywords = [ "postgresql", "newbie", "postgis", "overpass-api" ]
aliases = [ "/questions/46360" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API to PostgreSQL ?](/questions/46360/overpass-api-to-postgresql)

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
<span id="post-46360-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46360-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46360-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello again,</p>
<p>I would like to know how can i use the overpass api of pyhton to store information into my Postgresql database (i have a PostGIS extencion) . My idea was to get the "id" of the nodes and then creating an "id" camp on the database gather the information of the tags in question.</p>
<p>Thank you again for all the help,</p>
<p>Francisco Costa</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Nov '15, 10:09</strong></p>
<img src="https://secure.gravatar.com/avatar/2d5201d8b00ecd21e515f37b627df3b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FrancisCosta&#39;s gravatar image" />
<p><span>FrancisCosta</span><br />
<span class="score" title="0 reputation points">0</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FrancisCosta has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-46360" class="comments-container">
&#10;</div>
<div id="comment-tools-46360" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46360-form-container" class="comment-form-container">
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

<span id="46374"></span>

<div id="answer-container-46374" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46374-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46374-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-46374-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, You can use the overpass API to get data from OSM and then OGR to write it to PostgreSQL. You can do it on the command line or within Python. The intermediate format can be the native OSM XML format, or you can change to JSON.</p>
<p>Example on command line:</p>
<pre><code>wget &#39;http://overpass-api.de/api/interpreter?data=way[&quot;highway&quot;=&quot;residential&quot;][&quot;name&quot;](41.8942593,12.4812841,41.9030756,12.4945021);out;&#39; -O rome.osm 
osm2pgsql -H localhost -s -U geobox -d geotuga -c rome.osm</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Nov '15, 11:10</strong></p>
<img src="https://secure.gravatar.com/avatar/b4a923f887dc2b8e233085d0355e2aae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jorge%20Gustavo%20Rocha&#39;s gravatar image" />
<p><span>Jorge Gustav...</span><br />
<span class="score" title="67 reputation points">67</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jorge Gustavo Rocha has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-46374" class="comments-container">
&#10;</div>
<div id="comment-tools-46374" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46374-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="46369"></span>

<div id="answer-container-46369" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46369-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46369-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46369-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maybe you can try QGIS for this task?</p>
<p>QGIS has a plugin called QuickOSM where you can query for OSM data via overpassAPI.</p>
<p>And QGIS has an interface to Postgresql databases, or not? But I have no clue whether that interface is a oneway connection just to load data from database in QGIS.</p>
<p>Have NOT tried that on my own.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Nov '15, 16:35</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-46369" class="comments-container">
<span id="46378"></span>
<div id="comment-46378" class="comment">
<div id="post-46378-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I regularly pull GEOJSON from Overpass into QGIS &amp; push to PostGIS: but this is a distinctly non-automated approach.</p>
</div>
<div id="comment-46378-info" class="comment-info">
<span class="comment-age">(04 Nov '15, 11:50)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="46379"></span>
<div id="comment-46379" class="comment">
<div id="post-46379-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/647/sk53"></a><a href="https://help.openstreetmap.org/users/647/sk53">@SK53</a>: just to clarify your statement: I guess you mean "pull GeoJSON from overpass turbo"? The difference is quite important, as Overpass API doesn't provide GeoJSON out of the box. It provides some custom JSON format only, which doesn't really qualify as GeoJSON.</p>
</div>
<div id="comment-46379-info" class="comment-info">
<span class="comment-age">(04 Nov '15, 12:03)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-46369" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46369-form-container" class="comment-form-container">
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

