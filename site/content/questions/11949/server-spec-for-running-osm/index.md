+++
type = "question"
title = "Server Spec for running OSM"
description = '''I&#x27;m looking to run an OSM tile server and have been wondering what spec machine to get. I expect fairly heavy usage across a full planet of data and have taken the current yevaud spec as a benchmark of a high usage web-server. http://wiki.openstreetmap.org/wiki/Servers/yevaud My only question on thi...'''
date = "2012-04-12T22:08:00Z"
lastmod = "2017-05-29T05:19:00Z"
weight = 11949
keywords = [ "setup", "server" ]
aliases = [ "/questions/11949" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Server Spec for running OSM](/questions/11949/server-spec-for-running-osm)

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
<span id="post-11949-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11949-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-11949-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm looking to run an OSM tile server and have been wondering what spec machine to get. I expect fairly heavy usage across a full planet of data and have taken the current yevaud spec as a benchmark of a high usage web-server.</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Servers/yevaud">http://wiki.openstreetmap.org/wiki/Servers/yevaud</a></p>
<p>My only question on this is what is the SSD disk used for in particular setup? it's not big enough to cover the storage of the tiles (stated at ~1.2Tb). What is being kept on this disk? the disk itself would seem to represent half the cost of the server.<br />
</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-setup" rel="tag" title="see questions tagged &#39;setup&#39;">setup</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Apr '12, 22:08</strong></p>
<img src="https://secure.gravatar.com/avatar/9ef4e665e6e82f6b5f08952ff8c69d23?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John%20Perrin&#39;s gravatar image" />
<p><span>John Perrin</span><br />
<span class="score" title="76 reputation points">76</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John Perrin has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-11949" class="comments-container">
&#10;</div>
<div id="comment-tools-11949" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11949-form-container" class="comment-form-container">
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

<span id="11951"></span>

<div id="answer-container-11951" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11951-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11951-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-11951-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="John Perrin has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need the SSD for the PostGIS tablespace in order to be able to quickly render tiles when somebody requests them. Remember, a tile server is not a passive component that just hands out tiles - they will often have to be computed on the fly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '12, 22:33</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-11951" class="comments-container">
<span id="11952"></span>
<div id="comment-11952" class="comment">
<div id="post-11952-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! So this will hold the data files that are downloaded from planet.osm? That's actually a relief as i thought I was going to have to recreate Smaug as well!</p>
</div>
<div id="comment-11952-info" class="comment-info">
<span class="comment-age">(12 Apr '12, 22:36)</span> <span class="comment-user userinfo">John Perrin</span>
</div>
</div>
<span id="11953"></span>
<div id="comment-11953" class="comment">
<div id="post-11953-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You don't need Smaug, but you do need a database on the tile server itself. You will download the planet file and process it with osm2pgsql, whereby it will be written to the PostGIS database and onto the SSD. This will currently require about 280 GB of SSD space - less if you don't want updates, more if you want to add extra columns that are not in the standard OSM style.</p>
</div>
<div id="comment-11953-info" class="comment-info">
<span class="comment-age">(12 Apr '12, 22:46)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-11951" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11951-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11958"></span>

<div id="answer-container-11958" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11958-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11958-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-11958-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are two main components to the storage system of a tile server, each of which can have different requirements depending on the circumstances</p>
<p>1) Tile storage cache</p>
<p>For the tile storage usually one needs quite a bit of space, but performance isn't quite as critical. For a general purpose world wide map you will likely need somewhere on the order of above 600 GB. The full world wide tile set is considerably larger than that, but rendering on the fly of e.g. z18 ocean tiles is usually possible without too much problems. I don't know the exact scaling, but it seems like above somewhere between 300 - 600 GB the cache hit rate only increases slowly with size of the cache.</p>
<p>Performance wise, it appears like 1000 tiles/s will generate somewhere on the order of 300 - 500 iops on the disk system, although that obviously depends on the size of ram of the server and the distribution of areas served. This is a level of performance that you can probably get out a raid array of a few sata disks. The performance requirement on this part of the disks likely scale fairly straightforward with the number of tiles served per second. Adding a reverse proxy in front of the tile server can also help reasonably to distribute load for tile serving. For most tile servers I have seen so far tile serving hasn't really been much of an issue, but in the order above 1000 Tiles/s you probably do need to consider it as well.</p>
<p>2) Rendering database</p>
<p>The rendering database is where for most people the disk performance bottlenecks are. For the full planet, the postgis database with indexes is around 300 - 400GB in size. This is as others have pointed out where some people use SSDs for. Quite a bit of performance is consumed in keeping the database up to date with minutely diffs from OSM. This performance does not depend at all on how many tiles you serve, but only the rate of editing in OSM. From what I have seen (and other might correct me), a 2 - 4 disk sata raid array might not be able to keep up with edits during absolute peak editing times (e.g. Sunday afternoon European time), but should catch back up during the night. On top of that is the actual rendering of tiles. As typically one doesn't re-render tiles in advance (other than low zoom tiles), but only once they are actually viewed. Rendering performance does to some degree depend on the tile serving performance. If it doesn't matter how up to date rendered tiles are, rendering requests can be queued and rendered during quiet periods, which considerably reduces the performance requirements on the database.</p>
<p>So overall whether you need an SSD for the database mostly depends on how up-to-date you want to me with respect to OSM edits. If you want to be in the order of minutes behind OSM, you probably will need an SSD. Given that a fast update is important for mappers as reward for their work, the SSD in osm's tile server has been a big win. If daily updates or less are fine, then you might not need one. Once you get down to monthly updates, you are likely best not using an "updateable database" but do full reimports, the size of the database reduces typically to less than half the size.</p>
<p>It also depends on how spatially distributed your requests are. If e.g. your site has a "bunch of locations" around which it displays local maps. I.e. the same locations are shown over and over again, the rendering load is much less than if you offer "Downloading country wide tiles for offline use in a mobile app" even with the same amount of serving load.</p>
<p>If you don't need a world wide map, then hardware requirements also considerably reduce and once you get down to only e.g. a country like e.g. Italy or the UK, you possibly don't really have to worry about the database anymore at all, as any modern hardware is probably sufficient.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Apr '12, 02:42</strong></p>
<img src="https://secure.gravatar.com/avatar/32c974c4ca8b246698c2b82c64924da5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="apmon&#39;s gravatar image" />
<p><span>apmon</span><br />
<span class="score" title="6527 reputation points"><span>6.5k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="apmon has 9 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-11958" class="comments-container">
<span id="56348"></span>
<div id="comment-56348" class="comment">
<div id="post-56348-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/65/apmon"></a><a href="https://help.openstreetmap.org/users/65/apmon">@apmon</a> - I know this is old, but wondering if you could elaborate on optimizing IOPS for the SSD. You mention 300 - 500 IOPS for storage cache, but what is that also sufficient for the rendering database disk? I am considering using a AWS SSD with pre-provisioned IOPS. They make you pay for IOPS as well as storage so I don't want to over do it, but also don't want a bottleneck.</p>
</div>
<div id="comment-56348-info" class="comment-info">
<span class="comment-age">(29 May '17, 05:19)</span> <span class="comment-user userinfo">rgwozdz</span>
</div>
</div>
</div>
<div id="comment-tools-11958" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11958-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53557"></span>

<div id="answer-container-53557" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53557-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53557-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53557-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi,</p>
<p>I'm trying to instal my own OSM server but it always fails at full disk. I have this server <a href="https://www.hetzner.de/de/hosting/produkte_rootserver/ex51ssd">https://www.hetzner.de/de/hosting/produkte_rootserver/ex51ssd</a> with 500GB SSD. I have tried to import the DB for whole planet without slim tables but there is not enough RAM, and also with flat-nodes but no luck. Please can somebody write here what are current server requirements? What size of disk it needs for successful import and also some raw estimate for cache size?</p>
<p>Thank you very much.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Dec '16, 09:33</strong></p>
<img src="https://secure.gravatar.com/avatar/72017dd262b7afa7e109cabc5bfd879e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mariansedivy&#39;s gravatar image" />
<p><span>mariansedivy</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mariansedivy has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Dec '16, 15:51</strong> </span></p>
</div>
</div>
<div id="comments-container-53557" class="comments-container">
<span id="53560"></span>
<div id="comment-53560" class="comment">
<div id="post-53560-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are you running a full planet import? Or only a specific country/city?</p>
</div>
<div id="comment-53560-info" class="comment-info">
<span class="comment-age">(15 Dec '16, 12:32)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="53561"></span>
<div id="comment-53561" class="comment">
<div id="post-53561-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, I want full planet.</p>
</div>
<div id="comment-53561-info" class="comment-info">
<span class="comment-age">(15 Dec '16, 12:50)</span> <span class="comment-user userinfo">mariansedivy</span>
</div>
</div>
<span id="53570"></span>
<div id="comment-53570" class="comment">
<div id="post-53570-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please see if these are helpful for you. <a href="http://wiki.openstreetmap.org/wiki/Servers">servers</a> and <a href="https://hardware.openstreetmap.org/">servers</a></p>
</div>
<div id="comment-53570-info" class="comment-info">
<span class="comment-age">(16 Dec '16, 03:32)</span> <span class="comment-user userinfo">Gagan</span>
</div>
</div>
</div>
<div id="comment-tools-53557" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53557-form-container" class="comment-form-container">
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

