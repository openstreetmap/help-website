+++
type = "question"
title = "Running tile server - Should I opt for more CPU or RAM?"
description = '''I am building a tile server that will be serving map tiles in Ontario, Canada only. The PBF file is about 680MB. I will be using DigitalOcean&#x27;s droplets to host my tiles. I have 2 options: $40 Standard Droplet  4 CPUs 8GB RAM  $40 Optimized Droplet  2 Dedicated CPUs 4GB RAM  For serving map tiles in...'''
date = "2019-02-23T20:53:00Z"
lastmod = "2019-02-23T21:51:00Z"
weight = 68121
keywords = [ "tiles", "tileserver" ]
aliases = [ "/questions/68121" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Running tile server - Should I opt for more CPU or RAM?](/questions/68121/running-tile-server-should-i-opt-for-more-cpu-or-ram)

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
<span id="post-68121-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68121-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68121-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am building a tile server that will be serving map tiles in Ontario, Canada only. The PBF file is about 680MB.</p>
<p>I will be using DigitalOcean's droplets to host my tiles. I have 2 options:</p>
<p>$40 Standard Droplet</p>
<ul>
<li>4 CPUs</li>
<li>8GB RAM</li>
</ul>
<p>$40 Optimized Droplet</p>
<ul>
<li>2 Dedicated CPUs</li>
<li>4GB RAM</li>
</ul>
<p>For serving map tiles in Ontario alone, should I go for more RAM, or superior processing power?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Feb '19, 20:53</strong></p>
<img src="https://secure.gravatar.com/avatar/b1e3fbb6f31c5e0144e7b18fcd7d5d33?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="valachio&#39;s gravatar image" />
<p><span>valachio</span><br />
<span class="score" title="41 reputation points">41</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="valachio has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Feb '19, 20:54</strong> </span></p>
</div>
</div>
<div id="comments-container-68121" class="comments-container">
&#10;</div>
<div id="comment-tools-68121" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68121-form-container" class="comment-form-container">
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

<span id="68122"></span>

<div id="answer-container-68122" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68122-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="valachio has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's a bit of a "how long is a piece of string" question, because you don't say what sort of tiles you're hosting (e.g. vector or raster) and what map style, whether you're trying to keep it up to date, and how much traffic you expect.</p>
<p>To give an example, <a href="https://map.atownsend.org.uk/maps/map/map.html">this</a> server has a 1.1Gb .pbf loaded into it, has a probably more detailed (raster) map style than OSM Carto, and fitted nicely into a 4GB RAM, 2CPU, 100Gb SSD server before I upgraded. It doesn't get much traffic, which may be relevant. If you're rendering raster tiles using OSM's standard style I'd expect you'd fit into that spec (probably into the 80GB SSD that comes with your "standard" droplet) - choose fast disk over fast CPU. $40 per month seems a bit on the high side compared to European providers, though - something like €9 should cover what you want.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Feb '19, 21:23</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-68122" class="comments-container">
<span id="68123"></span>
<div id="comment-68123" class="comment">
<div id="post-68123-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry about the lack of details. I'm not experienced with operating map servers (I had no idea the difference between raster and vector tiles until you mentioned it).</p>
<p>My goal is to replicate the performance of Google Maps (as I am switching over from using Google Maps API). So I will be using raster tiles along with satellite tiles (users will be able to switch between map &amp; satellite view).</p>
<p>Our site's current traffic is about 5,000 users per day, and about 8,000 sessions per day.</p>
<p>I plan to create custom styling as I am not a big fan of OSM's default style.</p>
<p>I have no issues paying a bit more every month as this map server is supported by a business.</p>
<p>The server you linked is quite nice. It is basically what I'm looking for, except I just want the area of Ontario, Canada (about half the size of yours).</p>
</div>
<div id="comment-68123-info" class="comment-info">
<span class="comment-age">(23 Feb '19, 21:39)</span> <span class="comment-user userinfo">valachio</span>
</div>
</div>
<span id="68124"></span>
<div id="comment-68124" class="comment">
<div id="post-68124-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>By the way. Was there a particular tutorial you used to build your map server? I am using this one - <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a></p>
</div>
<div id="comment-68124-info" class="comment-info">
<span class="comment-age">(23 Feb '19, 21:40)</span> <span class="comment-user userinfo">valachio</span>
</div>
</div>
<span id="68125"></span>
<div id="comment-68125" class="comment">
<div id="post-68125-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Be aware that OSM does not have satellite imagery. You will either have to use tiles from a different server, or host them yourself; hosting high-resolution satellite imagery will likely use several 100 GB for Ontario.</p>
</div>
<div id="comment-68125-info" class="comment-info">
<span class="comment-age">(23 Feb '19, 21:47)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="68126"></span>
<div id="comment-68126" class="comment">
<div id="post-68126-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Pretty similar - I'm following <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1804_tileserver_load">this</a>, although obviously ignoring the virtualbox stuff as you don't need to worry about that with a cloud server.</p>
</div>
<div id="comment-68126-info" class="comment-info">
<span class="comment-age">(23 Feb '19, 21:51)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-68122" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68122-form-container" class="comment-form-container">
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

