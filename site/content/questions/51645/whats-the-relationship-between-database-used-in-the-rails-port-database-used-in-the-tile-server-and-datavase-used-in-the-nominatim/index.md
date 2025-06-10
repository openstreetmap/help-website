+++
type = "question"
title = "What&#x27;s the relationship between database used in the rails port, database used in the tile server and datavase used in the nominatim?"
description = '''As i know, there are three database used in the OSM, database used in the rails port, database used in the tile server and datavase used in the nominatim. Let me call the three database as openstreetmap, gis and nominatim. And I have two question about these three database.  1)I have installed the r...'''
date = "2016-08-22T15:30:00Z"
lastmod = "2016-08-23T09:23:00Z"
weight = 51645
keywords = [ "tileserver", "nominatim", "railsport" ]
aliases = [ "/questions/51645" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What's the relationship between database used in the rails port, database used in the tile server and datavase used in the nominatim?](/questions/51645/whats-the-relationship-between-database-used-in-the-rails-port-database-used-in-the-tile-server-and-datavase-used-in-the-nominatim)

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
<span id="post-51645-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51645-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51645-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>As i know, there are three database used in the OSM, database used in the rails port, database used in the tile server and datavase used in the nominatim. Let me call the three database as openstreetmap, gis and nominatim. And I have two question about these three database.</p>
<p>1)I have installed the rails port and built up my local tile server, but the tables in the openstreetmap and gis are so different, and the table structure in gis and nominatim are so similiar, so what's the relationship or differences between openstreetmap,gis and nominatim?</p>
<p>2)How do the three database have the same data index to keep the consistency？ The mean is a node id in the three database is same.</p>
<p>Anyone can help me is so kindness.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-railsport" rel="tag" title="see questions tagged &#39;railsport&#39;">railsport</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Aug '16, 15:30</strong></p>
<img src="https://secure.gravatar.com/avatar/3522efac952d508cf251cd2590e68ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yuyy&#39;s gravatar image" />
<p><span>yuyy</span><br />
<span class="score" title="236 reputation points">236</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yuyy has one accepted answer">20%</span></p>
</div>
</div>
<div id="comments-container-51645" class="comments-container">
&#10;</div>
<div id="comment-tools-51645" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51645-form-container" class="comment-form-container">
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

<span id="51647"></span>

<div id="answer-container-51647" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51647-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51647-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-51647-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="yuyy has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The databases you mention are not the only ones; every service based on OSM usually has their own specialist database, like the ones used by routing engines, or Overpass, or taginfo, or analytics web sites. Each of them have their own database schema or structure that is optimised for the purpose they are serving.</p>
<p>With tile server and Nominatim databases, what OSM does is produce "diff" files from the openstreetmap database (with the Osmosis utility). These are published on a web site and downloaded, again by Osmosis, on the machines running tile server and Nominatim, and consumed on these machines with osm2pgsql in append mode. Different parameters to osm2pgsql are used for the tile and Nominatim databases, resulting in different database schemas.</p>
<p>If you want to set up your own copy of the OSM database with your own edits that are different from those edits made in OSM, then you will have to produce diffs from your own database and consume them on tile and Nominatim (the order is not important). If you want to keep your own copy of OSM and simply mirror all edits made to OSM, then you have to consume the diffs produced by OSM in all of your three databases (your own OSM, tile, and Nominatim). Again the order is not important since you don't have these databases linked to each other at all!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Aug '16, 17:14</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Aug '16, 08:50</strong> </span></p>
</div>
</div>
<div id="comments-container-51647" class="comments-container">
<span id="51668"></span>
<div id="comment-51668" class="comment">
<div id="post-51668-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks very much to your reply, and i leart a lot from your answers. But what's the mean of "diffs" you mentioned above？ How can i produce diffs from my own database or OSM and how can i consume them?</p>
</div>
<div id="comment-51668-info" class="comment-info">
<span class="comment-age">(23 Aug '16, 09:11)</span> <span class="comment-user userinfo">yuyy</span>
</div>
</div>
<span id="51669"></span>
<div id="comment-51669" class="comment">
<div id="post-51669-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>OSM diffs are published on planet.openstreetmap.org in the replication directories. If you want to produce your own diffs because you make your own private edits to your own copy of the data, then you will have to run Osmosis to make the diffs like OSM does on their server.</p>
</div>
<div id="comment-51669-info" class="comment-info">
<span class="comment-age">(23 Aug '16, 09:15)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="51670"></span>
<div id="comment-51670" class="comment">
<div id="post-51670-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks very much,then i will take a look at Osmosis.</p>
</div>
<div id="comment-51670-info" class="comment-info">
<span class="comment-age">(23 Aug '16, 09:23)</span> <span class="comment-user userinfo">yuyy</span>
</div>
</div>
</div>
<div id="comment-tools-51647" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51647-form-container" class="comment-form-container">
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

