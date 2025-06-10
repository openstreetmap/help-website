+++
type = "question"
title = "Setting up my own tile server"
description = '''Hi I followed the following tutorial: http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/ to set up a tile-server on my ubuntu machine. It seems to work the same as how the tutorial says it should i.e. If I navigate to http://localhost/osm_tiles2/0/0/0.png I get a image of the...'''
date = "2012-10-27T16:02:00Z"
lastmod = "2012-10-27T17:22:00Z"
weight = 17225
keywords = [ "renderd", "switch2osm", "osm2pgsql", "mapnik" ]
aliases = [ "/questions/17225" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Setting up my own tile server](/questions/17225/setting-up-my-own-tile-server)

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
<span id="post-17225-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17225-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17225-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I followed the following tutorial: <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/"><code>http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/</code></a> to set up a tile-server on my ubuntu machine.</p>
<p>It seems to work the same as how the tutorial says it should i.e. If I navigate to <a href="http://localhost/osm_tiles2/0/0/0.png"><code>http://localhost/osm_tiles2/0/0/0.png</code></a> I get a image of the world.</p>
<p>One of my questions is where is the folder: osm_tiles2? I have run numerous searches but can't find it anywhere. I am not sure where apache2 goes to when I type localhost.</p>
<p>Another question is where do I go from here to get the map data stored in the PostGIS database to load instead of the picture of the world? The tutorial loads the whole planet OSM into a PostGIS DB and I decided to load just a single city however only the small png of the world displays.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-switch2osm" rel="tag" title="see questions tagged &#39;switch2osm&#39;">switch2osm</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Oct '12, 16:02</strong></p>
<img src="https://secure.gravatar.com/avatar/8f19a0a6b0afe902c224e03a8eb38ece?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srose&#39;s gravatar image" />
<p><span>srose</span><br />
<span class="score" title="161 reputation points">161</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srose has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17225" class="comments-container">
&#10;</div>
<div id="comment-tools-17225" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17225-form-container" class="comment-form-container">
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

<span id="17226"></span>

<div id="answer-container-17226" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17226-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17226-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17226-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="srose has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>"osm_tiles2" is defined in /usr/local/etc/renderd.conf:</p>
<pre><code>[default]
URI=/osm_tiles2/</code></pre>
<p>The "<code>osm_tiles2</code>" folder doesn't actually exist. The tiles aren't stored as .png files on disk - they're stored as <a href="http://wiki.openstreetmap.org/wiki/Meta_tiles">metatiles</a> below "/var/lib/mod_tile/default".</p>
<p>If you actually want to generate some real tiles you can do so with "generate_tiles.py" (in the mapnik-style folder).</p>
<p>If you've followed the instructions you'll already have your imported data in the database. If you want to quickly check that the city that you've imported is in there, navigate to it on the main OSM site, zoom in quite a lot, and right click and select "view image". You'll get a URL like:</p>
<pre><code>http://a.tile.openstreetmap.org/16/32486/21104.png</code></pre>
<p>Change that to the equivalent one on your tile server:</p>
<pre><code>http://localhost/osm_tiles2/16/32486/21104.png</code></pre>
<p>and (after a short time rendering) you should see part of your imported city.<br />
</p>
<p>On the switch2osm site there's also a "<a href="http://switch2osm.org/serving-tiles/">serving tiles</a>" section that allows you to set up a slippymap like the main OSM site.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Oct '12, 17:22</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span> </br></p>
</div>
</div>
<div id="comments-container-17226" class="comments-container">
&#10;</div>
<div id="comment-tools-17226" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17226-form-container" class="comment-form-container">
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

