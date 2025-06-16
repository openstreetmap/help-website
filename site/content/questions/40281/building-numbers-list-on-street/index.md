+++
type = "question"
title = "Building numbers list on street"
description = '''What is the best way to get street name by part of street name and to get list of all building numbers on street. Which software and services need I to install on my own server? I want use it without connection to OSM servers. Is it possible to make it by Overpass Api or by Nominatim? How will queri...'''
date = "2015-01-13T10:38:00Z"
lastmod = "2015-01-14T15:57:00Z"
weight = 40281
keywords = [ "building", "search", "street" ]
aliases = [ "/questions/40281" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Building numbers list on street](/questions/40281/building-numbers-list-on-street)

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
<span id="post-40281-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40281-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40281-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What is the best way to get street name by part of street name and to get list of all building numbers on street. Which software and services need I to install on my own server? I want use it without connection to OSM servers. Is it possible to make it by Overpass Api or by Nominatim? How will queries look for Nominatim, Overpass API and PostgreSQL? Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jan '15, 10:38</strong></p>
<img src="https://secure.gravatar.com/avatar/aeafd4156483ce12e60c02d426635abe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yaahor&#39;s gravatar image" />
<p><span>yaahor</span><br />
<span class="score" title="61 reputation points">61</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yaahor has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Jan '15, 12:25</strong> </span></p>
</div>
</div>
<div id="comments-container-40281" class="comments-container">
<span id="40344"></span>
<div id="comment-40344" class="comment">
<div id="post-40344-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you explain what is the level and scale of your needs ? is it just locally or for an application (web, mobile) ? is it just for one town, for a country, the world ?</p>
</div>
<div id="comment-40344-info" class="comment-info">
<span class="comment-age">(14 Jan '15, 12:15)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="40345"></span>
<div id="comment-40345" class="comment">
<div id="post-40345-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It will be used on website. It is for one town (maybe in future for country).</p>
</div>
<div id="comment-40345-info" class="comment-info">
<span class="comment-age">(14 Jan '15, 12:23)</span> <span class="comment-user userinfo">yaahor</span>
</div>
</div>
<span id="40349"></span>
<div id="comment-40349" class="comment">
<div id="post-40349-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Then a local instance of nominatim can help you to find the full street name then you can retrieve the data yourself on your local copy of osm dataset. overpass is only usefull when you work online and don't want a local database.</p>
</div>
<div id="comment-40349-info" class="comment-info">
<span class="comment-age">(14 Jan '15, 13:54)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="40356"></span>
<div id="comment-40356" class="comment">
<div id="post-40356-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I thought <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/install">https://wiki.openstreetmap.org/wiki/Overpass_API/install</a> allow install Overpass API locally. Did I err? I have understood how make my task using Overpass API. Nominatim can help me really? Can you write Nominatim query?</p>
</div>
<div id="comment-40356-info" class="comment-info">
<span class="comment-age">(14 Jan '15, 15:57)</span> <span class="comment-user userinfo">yaahor</span>
</div>
</div>
</div>
<div id="comment-tools-40281" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40281-form-container" class="comment-form-container">
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

<span id="40336"></span>

<div id="answer-container-40336" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40336-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-40336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="yaahor has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Normally, you don't need a special software with spacial queries. If the street numbers are correctly tagged, the link between the number and its street is already in OSM. To simplify, currently they are two methods to link the street number of a building to its street (also <a href="https://wiki.openstreetmap.org/wiki/Key:addr">documented in the wiki</a>) (which method is used is a contributor decision):<br />
- two tags "addr:housenumber=&lt; a number&gt;" + "addr:street=&lt; the street name&gt;" set on the same OSM element, a node or a closed way (a polygon) or a relation (most probably a relation for a multipolygon)<br />
- one tag "addr:housenumber=&lt; a number&gt;" set on the OSM element, node or way like above, and attached to a relation of type "<a href="https://wiki.openstreetmap.org/wiki/Relation:associatedStreet">associatedStreet</a>" with the role "house" and where the street name is the relation tag "name". The polyline(s) of the street itself is(are) also member of this relation with the role "street" (see the wiki). So, once you find an OSM node or way with a tag "addr:housenumber", you can check if it is part of a relation "associatedStreet" and get the related street.</p>
<p>Statistically, the second method with a relation is much less popular than the first (less intuitive and newcomers are relunctant to edit/create relations) and is present only on some areas (like in France), this depends on how the method is popularized locally. So basically, if you find a housenumber without one of the two methods listed above, we generally consider this as incomplete in OSM. But sSome people still consider that the street can be linked by the distance between the OSM element and the nearest street (way tagged "highway") but there is a large consensus to consider this as too vague/imprecise and leading to errors especially near intersections- Geofabrik is providing a slippy map, OSM Inspector, showing if the address can be linked to a street and by which method here : <a href="http://tools.geofabrik.de/osmi/">http://tools.geofabrik.de/osmi/</a></p>
<p>What you should do first is download the OSM data (or some sample) into JOSM and look up how addresses are tagged in your area of interest.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jan '15, 09:50</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Jan '15, 11:54</strong> </span></p>
</div>
</div>
<div id="comments-container-40336" class="comments-container">
&#10;</div>
<div id="comment-tools-40336" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40336-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="40290"></span>

<div id="answer-container-40290" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40290-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40290-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40290-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are many ways to do what you want. One way to load an <a href="http://download.geofabrik.de/">OSM file</a> into PostGIS with <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql">osm2pgsql</a>, and do some geo SQL queries on the results.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jan '15, 14:14</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-40290" class="comments-container">
<span id="40346"></span>
<div id="comment-40346" class="comment">
<div id="post-40346-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you write example of query to DB?</p>
</div>
<div id="comment-40346-info" class="comment-info">
<span class="comment-age">(14 Jan '15, 13:05)</span> <span class="comment-user userinfo">yaahor</span>
</div>
</div>
</div>
<div id="comment-tools-40290" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40290-form-container" class="comment-form-container">
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

