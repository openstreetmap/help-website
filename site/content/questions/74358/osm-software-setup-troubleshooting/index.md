+++
type = "question"
title = "OSM software setup troubleshooting"
description = '''I&#x27;m done with my first suite setup attempt =&amp;gt; the maps render blank and I have no idea how to troubleshoot. Any tips on where should I start please? To make things worse, I&#x27;m both OSM and Linux novice too. For what it&#x27;s worth, I ran &quot;sudo -u renderaccount -- /usr/local/bin/renderd -fc /usr/local/...'''
date = "2020-04-25T03:32:00Z"
lastmod = "2020-05-04T22:15:00Z"
weight = 74358
keywords = [ "setup", "osm", "software" ]
aliases = [ "/questions/74358" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [OSM software setup troubleshooting](/questions/74358/osm-software-setup-troubleshooting)

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
<span id="post-74358-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74358-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74358-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm done with my first suite setup attempt =&gt; the maps render blank and I have no idea how to troubleshoot. Any tips on where should I start please? To make things worse, I'm both OSM and Linux novice too.</p>
<p>For what it's worth, I ran "sudo -u renderaccount -- /usr/local/bin/renderd -fc /usr/local/etc/renderd.conf" manually and did not notice any errors. Some .meta files are getting generated in directories under /var/lib/mod_tile/ajt. For rendering I used this example <a href="https://switch2osm.github.io/using-tiles/getting-started-with-leaflet/">https://switch2osm.github.io/using-tiles/getting-started-with-leaflet/</a> and did replace 'https://{s}.tile.openstreetmap.org' with 'http://ip address'.</p>
<p>I followed the instructions at <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/</a> and am wondering if the various pieces of software/ styles/ fonts that will be used for rendering - starting from osm2pgsql in the list - do those need to be installed logged in as the user who'll do the rendering? In this particular document renderaccount.</p>
<p>Also, if I'll have to throw away the VM and redo the setup again, are there any better setup instructions?</p>
<p>Thanks very much, Eugen</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-setup" rel="tag" title="see questions tagged &#39;setup&#39;">setup</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-software" rel="tag" title="see questions tagged &#39;software&#39;">software</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Apr '20, 03:32</strong></p>
<img src="https://secure.gravatar.com/avatar/ad8f49d67fd7b8e25376900e86f57542?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eugen_nw&#39;s gravatar image" />
<p><span>eugen_nw</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eugen_nw has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Apr '20, 03:46</strong> </span></p>
</div>
</div>
<div id="comments-container-74358" class="comments-container">
&#10;</div>
<div id="comment-tools-74358" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74358-form-container" class="comment-form-container">
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

<span id="74366"></span>

<div id="answer-container-74366" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74366-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74366-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74366-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>Some .meta files are getting generated in directories</p>
</blockquote>
<p>That means that it's rendering tiles, which is the hard bit, and we just need to figure out why you can't see them in a browser.</p>
<p>What I'd suggest first is to use the web developer tools in your browser (usually via f12) to have a look at any errors and to see what's not loading.</p>
<p>When you tried "http://yourserveripaddress/hot/0/0/0.png" did that work? Did you try the html file “sample_leaflet.html” in mod_tile’s “extras” folder?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Apr '20, 23:12</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Apr '20, 01:12</strong> </span></p>
</div>
</div>
<div id="comments-container-74366" class="comments-container">
<span id="74429"></span>
<div id="comment-74429" class="comment">
<div id="post-74429-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks very much <a href="https://help.openstreetmap.org/users/387/someoneelse"></a><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> for having looked into this!</p>
<p>"http://yourserveripaddress/hot/0/0/0.png" works, it shows a small &amp; blank map of the world.</p>
<p>I cleared everything under /var/lib/mod_tile/ajtk, ran "sudo -u renderaccount -- /usr/local/bin/renderd -fc /usr/local/etc/renderd.conf" manually and did not notice any error. The browser's developer view complains only about not being able to find favicon.ico, other than that it loads successfully various .PNG files.</p>
<p>I loaded into postgres the data from us-pacific-latest.osm.pbf that I downloaded from <a href="https://download.geofabrik.de/north-america.html">https://download.geofabrik.de/north-america.html</a></p>
<p>I took a quick peek into the gis database and the tables seem to be populated with data:</p>
<p>gis=# SELECT COUNT(*) FROM "planet_osm_ways"; -[ RECORD 1 ]- count | 486952</p>
<p>gis=# SELECT COUNT(*) FROM "planet_osm_nodes"; -[ RECORD 1 ]-- count | 9573637</p>
<p>Right on the Linux VM where I have this running I opened the ~/src/mod_tile/extra/sample_leaflet.html file in FireFox and I see only a blank map.</p>
<p>I'd guess that the expected behavior would be that if I zoom into the west coast of the N. American continent to see some map being rendered. I see only a blank map.</p>
</div>
<div id="comment-74429-info" class="comment-info">
<span class="comment-age">(28 Apr '20, 01:08)</span> <span class="comment-user userinfo">eugen_nw</span>
</div>
</div>
<span id="74430"></span>
<div id="comment-74430" class="comment">
<div id="post-74430-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is there a way we can see the Mapnik component's log? Is there a possibility that it cannot read the data from the Postgres database?</p>
</div>
<div id="comment-74430-info" class="comment-info">
<span class="comment-age">(28 Apr '20, 01:12)</span> <span class="comment-user userinfo">eugen_nw</span>
</div>
</div>
<span id="74431"></span>
<div id="comment-74431" class="comment">
<div id="post-74431-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Assuming you're running renderd in the background as you zoom around you should see "renderd" messages to /var/log/syslog .</p>
</div>
<div id="comment-74431-info" class="comment-info">
<span class="comment-age">(28 Apr '20, 01:28)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="74488"></span>
<div id="comment-74488" class="comment not_top_scorer">
<div id="post-74488-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As I run renderd interactively, I see in renderd's output START/DONE TILE information and that it writes data into metafiles. In the browser's F12 window I do see calls like 'http://51.141.179.146/osm_tiles/7/20/43.png' displayed in red and with (canceled) Status. That may very well explain the behavior that I'm experiencing and shows that the rendering is not very successful.</p>
<p>This begs the question on what logs I should start looking at to diagnose this problem and where are those logs located? Alternatively, what do I need to do in order to enable the required logs to get generated? From what I've seen so far, renderd appears to be doing the right thing, so it could be either Mapnik, Postgres or some fault in the data import process.</p>
</div>
<div id="comment-74488-info" class="comment-info">
<span class="comment-age">(30 Apr '20, 01:25)</span> <span class="comment-user userinfo">eugen_nw</span>
</div>
</div>
<span id="74496"></span>
<div id="comment-74496" class="comment">
<div id="post-74496-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you demand a tile at zoom 7 by the browser which had not been rendered before, your browser would have to wait minutes and minutes for that (meta)tile to render and caps the connection before the rendering is finished. Tiles below zoom 12 have to better be pre-rendered by render_list.</p>
</div>
<div id="comment-74496-info" class="comment-info">
<span class="comment-age">(30 Apr '20, 07:29)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="74506"></span>
<div id="comment-74506" class="comment not_top_scorer">
<div id="post-74506-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks very much <a href="https://help.openstreetmap.org/users/17439/spiekerooger"></a><a href="https://help.openstreetmap.org/users/17439/spiekerooger">@Spiekerooger</a> for having looked into this! I can certainly run render_list beforehand.</p>
<p>The required .PNG files are getting generated during rendering, right? Where are they cached please? In the subdirectories of my /var/lib/mod_tile/ equivalent directory I see only *.meta files.</p>
<p>I see information like below in renderd's output which made me believe that the rendering completed.</p>
<p>renderd[13515]: DEBUG: START TILE ajt 6 8-15 16-23, new metatile<br />
renderd[13515]: Rendering projected coordinates 6 8 16 -&gt; -15028131.257100|5009377.085700 -10018754.171400|10018754.171400 to a 8 x 8 tile<br />
renderd[13515]: DEBUG: DONE TILE ajt 6 8-15 16-23 in 0.757 seconds debug: Creating and writing a metatile to /datadrive/caches/osm_tiles/ajt/6/0/0/0/1/128.meta</p>
</div>
<div id="comment-74506-info" class="comment-info">
<span class="comment-age">(30 Apr '20, 11:09)</span> <span class="comment-user userinfo">eugen_nw</span>
</div>
</div>
<span id="74507"></span>
<div id="comment-74507" class="comment">
<div id="post-74507-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>They are only cached as metatitle in /var/lib/mod_tile or its equivalent. mod_tile (the apache module) retrieves the acutal tiles from the meta tile to display them.</p>
<p>What did you changed the TileLayer URL in your leaflet setup to?</p>
<p>It should be <a href="http://51.141.179.146/osm_tiles/%7Bz%7D/%7Bx%7D/%7By%7D.png">http://51.141.179.146/osm_tiles/{z}/{x}/{y}.png</a> if "osm_tiles" is the url as defined in the renderd.conf.</p>
</div>
<div id="comment-74507-info" class="comment-info">
<span class="comment-age">(30 Apr '20, 12:43)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="74516"></span>
<div id="comment-74516" class="comment not_top_scorer">
<div id="post-74516-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks very much again!</p>
<p>Yes I have it set to 'http://51.141.179.146/osm_tiles/{z}/{x}/{y}.png' The problem was that I did not have mod_tile configured in Apache2. I did configure it and now all the 'http://51.141.179.146/osm_tiles/7/20/43.png' type calls sent from the browser are successful. However, the map is still blank so now I'll start looking at the data in the Postgres database as I guess that missing/unreadable data may cause the tiles to display empty.</p>
<p>Alternatively, is it possible to enable logging in mod_tile so I can get an idea on what it does?</p>
</div>
<div id="comment-74516-info" class="comment-info">
<span class="comment-age">(30 Apr '20, 19:44)</span> <span class="comment-user userinfo">eugen_nw</span>
</div>
</div>
</div>
<div id="comment-tools-74366" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-74366-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74615"></span>

<div id="answer-container-74615" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74615-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74615-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74615-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think that <a href="https://help.openstreetmap.org/users/17439/spiekerooger">@Spiekerooger</a> suggestion to run render_list got my maps to show, thanks very much!</p>
<p>I am not certain though because I did lots of tweaking using various pieces of information from two other OMS setup instructions websites. As of right now, I think that <a href="https://www.linuxbabe.com/ubuntu/openstreetmap-tile-server-ubuntu-18-04-osm">https://www.linuxbabe.com/ubuntu/openstreetmap-tile-server-ubuntu-18-04-osm</a> has the best list of setup instructions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 May '20, 22:15</strong></p>
<img src="https://secure.gravatar.com/avatar/ad8f49d67fd7b8e25376900e86f57542?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eugen_nw&#39;s gravatar image" />
<p><span>eugen_nw</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eugen_nw has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-74615" class="comments-container">
&#10;</div>
<div id="comment-tools-74615" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74615-form-container" class="comment-form-container">
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

