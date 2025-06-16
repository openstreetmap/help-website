+++
type = "question"
title = "Railway map with routes and stations"
description = '''I am building a .net (Silverlight) application for railway companies. I would like to use openstreetmap but just with the base layer and a layer with all the European railway routes/tracks and the stations with their names. How can I get this information ? Thanks for you answer. Martijn'''
date = "2011-02-28T14:22:00Z"
lastmod = "2016-03-01T18:12:00Z"
weight = 3447
keywords = [ "railway", "layer" ]
aliases = [ "/questions/3447" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Railway map with routes and stations](/questions/3447/railway-map-with-routes-and-stations)

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
<span id="post-3447-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3447-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-3447-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am building a .net (Silverlight) application for railway companies. I would like to use openstreetmap but just with the base layer and a layer with all the European railway routes/tracks and the stations with their names.</p>
<p>How can I get this information ?</p>
<p>Thanks for you answer. Martijn</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-railway" rel="tag" title="see questions tagged &#39;railway&#39;">railway</span> <span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Feb '11, 14:22</strong></p>
<img src="https://secure.gravatar.com/avatar/919d3436c46da45fab5f9fca24e751d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Martijn%20Loois&#39;s gravatar image" />
<p><span>Martijn Loois</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Martijn Loois has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Mar '11, 12:41</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/bc6d0b055d631830f7891d3f89edb66b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="katpatuka&#39;s gravatar image" />
<p><span>katpatuka</span><br />
<span class="score" title="1041 reputation points"><span>1.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span></p>
</div>
</div>
<div id="comments-container-3447" class="comments-container">
&#10;</div>
<div id="comment-tools-3447" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3447-form-container" class="comment-form-container">
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

<span id="3448"></span>

<div id="answer-container-3448" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3448-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3448-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-3448-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Martin,</p>
<p>If by "use OpenStreetMap" you mean use the OpenStreetMap data. Your steps will include:</p>
<ol>
<li>acquiring the OSM data by downloading the <a href="http://planet.osm.org/">planet</a> or <a href="http://download.geofabrik.de/osm/">extracts</a></li>
<li>building a local <a href="https://wiki.openstreetmap.org/wiki/Minutely_Mapnik">OSM stack</a></li>
<li>loading your local database</li>
<li>rendering the maps to suit your requirements</li>
<li>presenting your rendered map to your audience</li>
</ol>
<p>If by "use OpenStreetMap" you mean you want to click a few check boxes on a web service then consume that web service and present it to your audience, then the steps will differ.<br />
</p>
<ol>
<li>find a base layer you like</li>
<li>find a railway layer you like</li>
<li>combine them in a pleasing fashion</li>
<li>present them to your audience</li>
</ol>
<p>Finding available layers that you like will have to consider their terms of use, etc.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Feb '11, 14:41</strong></p>
<img src="https://secure.gravatar.com/avatar/d90ea04df82d77f534659f08894dd889?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard%20Weait&#39;s gravatar image" />
<p><span>Richard Weait</span><br />
<span class="score" title="3044 reputation points"><span>3.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="34 badges"><span class="silver">●</span><span class="badgecount">34</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard Weait has 8 accepted answers">17%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Mar '11, 12:39</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/bc6d0b055d631830f7891d3f89edb66b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="katpatuka&#39;s gravatar image" />
<p><span>katpatuka</span><br />
<span class="score" title="1041 reputation points"><span>1.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span></p>
</div>
</div>
<div id="comments-container-3448" class="comments-container">
<span id="3455"></span>
<div id="comment-3455" class="comment">
<div id="post-3455-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Maybe a nice example is presented in the videos of <a href="https://wiki.openstreetmap.org/wiki/TileMill">https://wiki.openstreetmap.org/wiki/TileMill</a> at <a href="http://vimeo.com">http://vimeo.com</a></p>
</div>
<div id="comment-3455-info" class="comment-info">
<span class="comment-age">(28 Feb '11, 20:26)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-3448" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3448-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48440"></span>

<div id="answer-container-48440" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48440-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48440-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48440-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>some intreating options are pre made with colour/b&amp;w options at www.openrailwaymap.org as well as useful guides to tags tey promote.</p>
<p>the wiki has a lot of detail on tagging used on railways and is very helpful for navigating though raw data you get above:- <a href="https://wiki.openstreetmap.org/wiki/Main_Page">https://wiki.openstreetmap.org/wiki/Main_Page</a> more than 500 entries:- <a href="https://wiki.openstreetmap.org/w/index.php?search=Rail&amp;title=Special%3ASearch&amp;fulltext=Search">https://wiki.openstreetmap.org/w/index.php?search=Rail&amp;title=Special%3ASearch&amp;fulltext=Search</a> simpler starting guide:- <a href="https://wiki.openstreetmap.org/wiki/Key:railway">https://wiki.openstreetmap.org/wiki/Key:railway</a> <a href="https://wiki.openstreetmap.org/wiki/Map_Features#Public_Transport">https://wiki.openstreetmap.org/wiki/Map_Features#Public_Transport</a></p>
<p>It is worth remembering that contributers are increasing detail on a continious basis in the areas they cover so results can be patchy if you want lots of detail with out adding the missing bits yourself into the main database.</p>
<p>The Rail Infrastructure companies in the EU (or maybe the whole EEA can oftern provide additional data source that you can blend with OSM data to give more infomation on your map Links to meny such source site can resuchered through the European Railway Agency at <a href="http://www.era.europa.eu/">http://www.era.europa.eu/</a> they also take enquires to the contacts given there in a helpful manner.</p>
<p>The UK has verious networks in vious states of documentation but the maimline services are available from Network Rail <a href="http://www.networkrail.co.uk/industry-partners/using-our-network-index.aspx">http://www.networkrail.co.uk/industry-partners/using-our-network-index.aspx</a> they also has live and open data programs in addition to their layout guides.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Mar '16, 18:12</strong></p>
<img src="https://secure.gravatar.com/avatar/30d90feb3a40fa6255767f95a8cd7943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Govanus&#39;s gravatar image" />
<p><span>Govanus</span><br />
<span class="score" title="154 reputation points">154</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Govanus has one accepted answer">3%</span></p>
</div>
</div>
<div id="comments-container-48440" class="comments-container">
&#10;</div>
<div id="comment-tools-48440" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48440-form-container" class="comment-form-container">
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

