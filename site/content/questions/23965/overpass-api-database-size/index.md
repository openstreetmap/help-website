+++
type = "question"
title = "Overpass API database size"
description = '''Hey, I&#x27;m just about to setup a server with the overpass API. I had a look at the installation guides and all quote, that with minutely updates and metadata the DB size is up to 150GB and that without updates and metadata one could push this down to 50gb.. So I decided to go with 130GB server harddis...'''
date = "2013-07-04T11:19:00Z"
lastmod = "2015-11-29T13:12:00Z"
weight = 23965
keywords = [ "size", "overpass", "api", "disk", "database" ]
aliases = [ "/questions/23965" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API database size](/questions/23965/overpass-api-database-size)

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
<span id="post-23965-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23965-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23965-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey, I'm just about to setup a server with the overpass API. I had a look at the installation guides and all quote, that with minutely updates and metadata the DB size is up to 150GB and that without updates and metadata one could push this down to 50gb.. So I decided to go with 130GB server harddisk, because I do not want metadata and minutely updates.. But what I see is that I get ~93gb of database size when I create the database without metadata. I use the cloning-mechanism.</p>
<p>This is a bit too much, how can I reduce the size of the database? Do I have more options on this when I create the DB on my own (saying from a planet.osm file directly, not by cloning)? I need ~50 gb for other data on the server, so I would need the Overpass database to consume max. 80gb</p>
<p>And also I'm still a bit confused because the documentation states: "40 GB of hard disk space (80-100 GB if you want minutely updates, less if you use a smaller extract file)"</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-size" rel="tag" title="see questions tagged &#39;size&#39;">size</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-disk" rel="tag" title="see questions tagged &#39;disk&#39;">disk</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jul '13, 11:19</strong></p>
<img src="https://secure.gravatar.com/avatar/17ea9f02cec3c354c58f177b84718170?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sequarell&#39;s gravatar image" />
<p><span>sequarell</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sequarell has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-23965" class="comments-container">
<span id="46888"></span>
<div id="comment-46888" class="comment">
<div id="post-46888-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm just importing greece-latest.osm.bz2 (about 200MB) but after importing the data the database is almost 10GB. How will that scale if I import the whole planet? Greece is less than 1% of the whole planet but my db is already about 8% of the estimated total planet db size.</p>
</div>
<div id="comment-46888-info" class="comment-info">
<span class="comment-age">(29 Nov '15, 11:38)</span> <span class="comment-user userinfo">kgaitanis</span>
</div>
</div>
<span id="46891"></span>
<div id="comment-46891" class="comment">
<div id="post-46891-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/11689/kgaitanis">@kgaitanis</a>: from where do you got the estimate? Keep in mind, that <a href="https://wiki.openstreetmap.org/wiki/Stats#Nodes.2C_ways_and_relations">OSM is growing</a>. Could it be that the estimate is quite old?</p>
</div>
<div id="comment-46891-info" class="comment-info">
<span class="comment-age">(29 Nov '15, 13:08)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="46892"></span>
<div id="comment-46892" class="comment">
<div id="post-46892-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>well in that case if my db keeps growing at the same pace while I'm adding regions to it, it should take more than 1TB for the whole planet. I'm just making quick calculations here assuming that greece represents 1% of the planet (in reality it should be less). Can anybody tell me how much disk space is needed for the database for the whole planet? I mean with recent data.</p>
</div>
<div id="comment-46892-info" class="comment-info">
<span class="comment-age">(29 Nov '15, 13:12)</span> <span class="comment-user userinfo">kgaitanis</span>
</div>
</div>
</div>
<div id="comment-tools-23965" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23965-form-container" class="comment-form-container">
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

<span id="23968"></span>

<div id="answer-container-23968" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23968-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23968-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-23968-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="http://overpass-api.de/no_frills.html#startup">Overpass installation instructions</a> explain how you can import from a Planet file, but this probably won't achieve what you want since the planet file includes every piece of information in OpenStreetMap and will almost certainly mean a larger DB. If you're only interested in one country or area, you could import an Planet file extract, such as <a href="http://download.geofabrik.de/">those available from Geofabrik</a>, but you won't be able to keep this up to date with diffs.</p>
<p>Equally you could download the entire Planet and filter out any data you aren't interested in using <a href="http://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a>, but this will be slow and will still need lots of disk space for the two Planet files you will end up storing.</p>
<p>The simplest answer is probably just to get a bigger hard drive, especially since the amount of data in OpenStreetMap is only going to get larger over time.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jul '13, 11:34</strong></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonathan Bennett has 21 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-23968" class="comments-container">
<span id="23971"></span>
<div id="comment-23971" class="comment">
<div id="post-23971-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello Jonathan,</p>
<p>thanks for the information. As you perhaps noticed I'm pretty new to all this stuff :) OK, so what I want is data of the whole globe, but not all data.. Mainly I need all kinds of streets and only basic topographic data. So I'll try to create my own planet file with osmosis. CPU/Ram and disk space is no big manner here, I can create the file on a workstation with enough ressources and then transfer it to the server.</p>
<p>Thanks again! Florian</p>
</div>
<div id="comment-23971-info" class="comment-info">
<span class="comment-age">(04 Jul '13, 12:36)</span> <span class="comment-user userinfo">sequarell</span>
</div>
</div>
</div>
<div id="comment-tools-23968" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23968-form-container" class="comment-form-container">
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

