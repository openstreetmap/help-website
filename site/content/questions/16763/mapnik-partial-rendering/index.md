+++
type = "question"
title = "mapnik Partial rendering"
description = '''i have set up a tile server for Faroe Islands everything is working as expected. except i am getting a strange partial rendering in one area  the problem is that only highway=footway is rendered in this part of the map nothing else, i am missing the buildings and house numbers i think it is just in ...'''
date = "2012-10-09T18:20:00Z"
lastmod = "2012-10-10T10:48:00Z"
weight = 16763
keywords = [ "rendering", "mapnik" ]
aliases = [ "/questions/16763" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [mapnik Partial rendering](/questions/16763/mapnik-partial-rendering)

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
<span id="post-16763-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16763-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16763-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>i have set up a tile server for Faroe Islands everything is working as expected. except i am getting a strange partial rendering in one area</p>
<p>the problem is that only highway=footway is rendered in this part of the map nothing else, i am missing the buildings and house numbers</p>
<p>i think it is just in this part of the map the problem is, i haven't found the same problem in another part of the map</p>
<p>it should look like this <a href="http://www.openstreetmap.org/?zoom=17&amp;lat=62.10338&amp;lon=-7.64377&amp;layers=B0">this</a></p>
<p>insted i get <a href="http://old.stamps.fo:8080/osm/slippymap.html?zoom=17&amp;lat=62.10338&amp;lon=-7.64377&amp;layers=B0">this</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Oct '12, 18:20</strong></p>
<img src="https://secure.gravatar.com/avatar/29b31c0372424ea87e8a9f12f8f18a46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LiFo&#39;s gravatar image" />
<p><span>LiFo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LiFo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16763" class="comments-container">
<span id="16774"></span>
<div id="comment-16774" class="comment">
<div id="post-16774-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It might be helpful if you could fill in details about which set of instructions you were following, what software and server versions you're using, which data you downloaded and imported and whether you cut it e.g. with osmosis prior to load.</p>
<p>For info I have a tile server, built following <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/">these instructions</a>, loaded with <a href="http://download.geofabrik.de/openstreetmap/">Geofabrik Europe data</a> as of the licence change and updated using hourly osc files up to 22nd September. On that, your area looks correct, like this:</p>
<p><img src="http://help.openstreetmap.org/upfiles/example_5.png" alt="picture showing buildings" /></p>
</div>
<div id="comment-16774-info" class="comment-info">
<span class="comment-age">(09 Oct '12, 21:51)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="16776"></span>
<div id="comment-16776" class="comment">
<div id="post-16776-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I followed the <a href="http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/">instructions</a> from Switch2Osm. Downloaded <a href="http://download.geofabrik.de/openstreetmap/europe/faroe_islands.osm.pbf">this data</a> from Geofabric and imported with osm2pgsql, just simple osm2pgsql faroe_islands.osm.pbf</p>
<p>i reimported also with osm2pgsql, before i restarded renderd i deleted all the metatiles, i can see that the changes i have made are rendered ok, but just not in this area ?</p>
</div>
<div id="comment-16776-info" class="comment-info">
<span class="comment-age">(09 Oct '12, 22:51)</span> <span class="comment-user userinfo">LiFo</span>
</div>
</div>
<span id="16801"></span>
<div id="comment-16801" class="comment">
<div id="post-16801-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I have tried on a different VM insance of ubuntu 12.04 with the same data, and then i tried to insert some test osm data and this is the</p>
<p>test data in JOSM <img src="http://help.openstreetmap.org/upfiles/josmData.jpg" alt="alt text" /></p>
<p>and this is the result</p>
<p><img src="http://help.openstreetmap.org/upfiles/test.png" alt="alt text" /> the strange thing is that in other parts of my map the buildings and house numbers are ok. i have tryed to query for the way 44651223 (building above the word test )and it exists in the database</p>
</div>
<div id="comment-16801-info" class="comment-info">
<span class="comment-age">(10 Oct '12, 10:48)</span> <span class="comment-user userinfo">LiFo</span>
</div>
</div>
</div>
<div id="comment-tools-16763" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16763-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

