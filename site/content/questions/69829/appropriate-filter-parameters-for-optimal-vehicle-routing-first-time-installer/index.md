+++
type = "question"
title = "Appropriate filter parameters for optimal vehicle routing?  First Time Installer"
description = '''I&#x27;ve recently realized that OpenStreetMap is more than just roads and boundaries. It&#x27;s incredible. I had no idea. A true masterpiece of community collaboration. However, that creates a small problem. I&#x27;m looking to stand up a basic vehicle routing service without all the additional data bells and wh...'''
date = "2019-07-01T18:06:00Z"
lastmod = "2019-07-02T20:30:00Z"
weight = 69829
keywords = [ "osrm", "import", "osmfilter", "installation", "routing" ]
aliases = [ "/questions/69829" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Appropriate filter parameters for optimal vehicle routing? First Time Installer](/questions/69829/appropriate-filter-parameters-for-optimal-vehicle-routing-first-time-installer)

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
<span id="post-69829-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69829-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69829-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've recently realized that OpenStreetMap is more than just roads and boundaries. It's incredible. I had no idea. A true masterpiece of community collaboration. However, that creates a small problem. I'm looking to stand up a basic vehicle routing service without all the additional data bells and whistles. (Very cool never the less).</p>
<p>I found osmfilter - <a href="https://journocode.com/2018/01/08/extract-geodata-openstreetmap-osmfilter/">https://journocode.com/2018/01/08/extract-geodata-openstreetmap-osmfilter/</a></p>
<p>As well as the categories - <a href="https://wiki.openstreetmap.org/wiki/Map_Features">https://wiki.openstreetmap.org/wiki/Map_Features</a></p>
<p>That's a lot of possible combinations and potential relationships within the data that if I remove may have unexpected consequences. I'd be looking for some direction on what categories to keep and drop to hit the goal below.</p>
<p>Goals:</p>
<ul>
<li>List item</li>
<li>Look/data similar to google directions.</li>
<li>Vehicle routing within city limits.</li>
<li>Dataset for the entire USA.</li>
<li>Needs to render and serve tiles.</li>
<li>Should I use OSRM in docker or the switch2osm 18.04 tutorial?</li>
<li>Expected Disk space needed and RAM. I've found that 24 GB and 60 GB of disk space wasn't enough but that was a full import without any category drops via osmfilter. Smaller is better in RAM and Disk but quality shouldn't suffer for vehicle directions.</li>
</ul>
<p>Thank you for your help.</p>
<p>Casey</p>
<p>Ref URLs:</p>
<ul>
<li><a href="https://github.com/Project-OSRM/osrm-backend/">https://github.com/Project-OSRM/osrm-backend/</a></li>
<li><a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/manually-building-a-tile-server-18-04-lts/</a></li>
<li><a href="http://project-osrm.org/docs/v5.22.0/api/?language=Python#general-options">http://project-osrm.org/docs/v5.22.0/api/?language=Python#general-options</a></li>
<li><a href="https://openlayers.org/">https://openlayers.org/</a></li>
<li><a href="https://overpass-turbo.eu/">https://overpass-turbo.eu/</a></li>
<li><a href="https://download.geofabrik.de/">https://download.geofabrik.de/</a></li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jul '19, 18:06</strong></p>
<img src="https://secure.gravatar.com/avatar/2f2802a91a7b23b9a654d5d1f3e4b917?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chavenor1&#39;s gravatar image" />
<p><span>chavenor1</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chavenor1 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Jul '19, 18:12</strong> </span></p>
</div>
</div>
<div id="comments-container-69829" class="comments-container">
&#10;</div>
<div id="comment-tools-69829" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69829-form-container" class="comment-form-container">
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

<span id="69847"></span>

<div id="answer-container-69847" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69847-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69847-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-69847-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Routing and tile rendering are entirely separate toolchains.</p>
<p>OSM data can power both, but you'll need to process it separately for each application, and run two different servers (those servers can, of course, be on the same box!). Typically to render raster map tiles you'll use the switch2osm workflow, loading data into a PostGIS database with osm2pgsql, and then rendering as tiles with Mapnik, renderd and mod_tile. For routing, you'll use software like OSRM, Graphhopper or Valhalla, each of which has a preparation step and then a route server.</p>
<p>Note that OSRM's fast Contraction Hierarchies routing algorithm is very memory-hungry, so if "smaller is better in RAM", you might prefer to choose a tool which offers a slower but more memory-efficient algorithm.</p>
<p>By default, each tool chooses a set of features from OSM to render or route along. You can change these by redesigning the stylesheet for the tileserver, or the "routing profile" for the routing tool. The tools have their own filtering abilities so you probably won't need osmfilter.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jul '19, 14:28</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jul '19, 14:30</strong> </span></p>
</div>
</div>
<div id="comments-container-69847" class="comments-container">
<span id="69849"></span>
<div id="comment-69849" class="comment">
<div id="post-69849-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can I slim down the Postgres DB by filtering out stuff I don't need for the tile server? Like I don't need to know where all the bus stops are and so on. Any advice on how to trim it down. For the OSRM -- is one better than the other?</p>
</div>
<div id="comment-69849-info" class="comment-info">
<span class="comment-age">(02 Jul '19, 16:14)</span> <span class="comment-user userinfo">chavenor1</span>
</div>
</div>
<span id="69851"></span>
<div id="comment-69851" class="comment">
<div id="post-69851-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, you can slim the Postgres db by editing the "style file" which tells osm2pgsql which columns to import. Note, however, that you'll then need to edit the stylesheet so that it doesn't try to retrieve data from the columns you've dropped, and that's not necessarily trivial.</p>
<p>When you say "is one better than the other", one what?</p>
</div>
<div id="comment-69851-info" class="comment-info">
<span class="comment-age">(02 Jul '19, 20:30)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-69847" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69847-form-container" class="comment-form-container">
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

