+++
type = "question"
title = "Lossy and Lossless Methods Getting OSM Data"
description = '''This is a question pertaining to osm2pgsql, osm2pgrouting and nominatim. As I understand it, these are &#x27;lossy&#x27; methods for getting data from OSM and into a PostGIS database. I was wondering:   In which ways are these methods &#x27;lossy&#x27; (what data is lost)?  and  are there any known methods that are los...'''
date = "2013-05-30T15:31:00Z"
lastmod = "2013-06-14T20:02:00Z"
weight = 22889
keywords = [ "nominatim", "osm2pgsql", "postgis", "database" ]
aliases = [ "/questions/22889" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Lossy and Lossless Methods Getting OSM Data](/questions/22889/lossy-and-lossless-methods-getting-osm-data)

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
<span id="post-22889-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22889-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22889-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This is a question pertaining to osm2pgsql, osm2pgrouting and nominatim.</p>
<p>As I understand it, these are 'lossy' methods for getting data from OSM and into a PostGIS database.</p>
<p>I was wondering:</p>
<ul>
<li>In which ways are these methods 'lossy' (what data is lost)?</li>
</ul>
<p>and</p>
<ul>
<li>are there any known methods that are lossless?</li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 May '13, 15:31</strong></p>
<img src="https://secure.gravatar.com/avatar/8a28a2bb64d641dfb063564bbc283316?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FortyLashes&#39;s gravatar image" />
<p><span>FortyLashes</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FortyLashes has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 May '13, 19:25</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-22889" class="comments-container">
&#10;</div>
<div id="comment-tools-22889" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22889-form-container" class="comment-form-container">
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

<span id="22892"></span>

<div id="answer-container-22892" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22892-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22892-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-22892-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="FortyLashes has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, these are lossy methods. For example, osm2pgsql drops coastlines, and the main outputs manipulate data into OGC simple features, which loses information regarding routing relationships.</p>
<p>You can load osm data into postgres in a lossless fashion using osmosis and the <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage#API_Database_Tasks">--write-apidb</a> or <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage#PostGIS_Tasks_.28Snapshot_Schema.29">--write-pgsql</a> outputs, depending on what schema you wish to use.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 May '13, 19:12</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-22892" class="comments-container">
<span id="23378"></span>
<div id="comment-23378" class="comment">
<div id="post-23378-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Andy Allan</span> Sorry for not getting back sooner! Thank you for that! I have been looking into Osmosis - that is awesome you can do lossless!</p>
</div>
<div id="comment-23378-info" class="comment-info">
<span class="comment-age">(14 Jun '13, 18:06)</span> <span class="comment-user userinfo">FortyLashes</span>
</div>
</div>
</div>
<div id="comment-tools-22892" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22892-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="23380"></span>

<div id="answer-container-23380" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23380-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23380-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-23380-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The most common lossless DB schemas are apidb, pgsnapshot, pgsimple and OSM3S.</p>
<p>apidb</p>
<ul>
<li>can store history</li>
<li>is not spatially enabled</li>
<li>uses postgresql</li>
<li>takes weeks to import</li>
<li>takes more than 1TB</li>
</ul>
<p>pgsnapshot</p>
<ul>
<li>is current data only</li>
<li>is spatially enabled</li>
<li>uses postgresql + postgis</li>
<li>can have geometries built for ways</li>
<li>takes days to import</li>
<li>takes a couple hundred GB</li>
<li>uses hstore to store tags</li>
</ul>
<p>pgsimple is pgsnapshot with separate tables for tags instead of hstore</p>
<p>OSM3S</p>
<ul>
<li>is current data only</li>
<li>is custom database software</li>
<li>is primary used by overpass API</li>
</ul>
<p>None of them are well-suited for rendering. The main uses for these database types are analysis and when you want to be able to produce a .osm file for an area.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jun '13, 20:02</strong></p>
<img src="https://secure.gravatar.com/avatar/5634c46072077e10f5b7c0da9b4bbb62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pnorman&#39;s gravatar image" />
<p><span>pnorman</span><br />
<span class="score" title="2352 reputation points"><span>2.4k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pnorman has 9 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-23380" class="comments-container">
&#10;</div>
<div id="comment-tools-23380" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23380-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="22904"></span>

<div id="answer-container-22904" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22904-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22904-score" class="post-score" title="current number of votes">
-5
</div>
<span id="post-22904-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I assume that by "OSM data" you mean the OSM source data and by "lossy method" you mean that the output dataset, after processing it by a "method", contains at least one less (missing) or changed object compared to the input dataset. If these assumptions are correct my answers to your questions are:<br />
-Yes, all "methods" are lossy (regardless of the programing language and source type in apps). Namely, the OSM source data contains many (but really many) errors of formal and logical nature. Some of the erroneous objects must be ignored and many of them are changed by a data-preparation "method". But the data-preparation is done by teams and as a rule teams have different filings for criteria what to ignore, what and how to change and so on. Therefor the "lossy" nature of the "methods" considerably vary. In my opinion/experience about 90% of all errors may be repaired.<br />
-Yes, downloading the latest regular OSM dump will provide you with exactly the same objects as they are in the database of the OSM source data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 May '13, 08:12</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span> </br></br></p>
</div>
</div>
<div id="comments-container-22904" class="comments-container">
&#10;</div>
<div id="comment-tools-22904" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22904-form-container" class="comment-form-container">
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

