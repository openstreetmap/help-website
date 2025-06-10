+++
type = "question"
title = "Tile server hardware to support 18k requests/min"
description = '''What kind of hardware would be required for tile server(s) to support 18k map-view requests per minute? I know there are a lot of variables involved, but a ballpark estimate would be fine.'''
date = "2016-07-06T02:52:00Z"
lastmod = "2016-07-15T07:42:00Z"
weight = 50649
keywords = [ "hardware", "performance", "server", "hardwarerequirements", "tileserver" ]
aliases = [ "/questions/50649" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Tile server hardware to support 18k requests/min](/questions/50649/tile-server-hardware-to-support-18k-requestsmin)

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
<span id="post-50649-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50649-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50649-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What kind of hardware would be required for tile server(s) to support 18k map-view requests per minute? I know there are a lot of variables involved, but a ballpark estimate would be fine.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-hardware" rel="tag" title="see questions tagged &#39;hardware&#39;">hardware</span> <span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span> <span class="post-tag tag-link-hardwarerequirements" rel="tag" title="see questions tagged &#39;hardwarerequirements&#39;">hardwarerequirements</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jul '16, 02:52</strong></p>
<img src="https://secure.gravatar.com/avatar/cd69e47c37e8042d0367ec2657357e5a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bengsp&#39;s gravatar image" />
<p><span>bengsp</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bengsp has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50649" class="comments-container">
<span id="50657"></span>
<div id="comment-50657" class="comment">
<div id="post-50657-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please explain what you mean by "map view". Does that include zooming and panning, or is it a new "map view" every time the user does something? How big is the map display?</p>
</div>
<div id="comment-50657-info" class="comment-info">
<span class="comment-age">(06 Jul '16, 08:08)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="50691"></span>
<div id="comment-50691" class="comment">
<div id="post-50691-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Each request would = 1 tile. We can assume zoom levels 0-12 would be pre-rendered, but the remaining levels would need to be rendered on the fly and delivered to the client within a reasonable amount of time, so within a couple seconds.</p>
</div>
<div id="comment-50691-info" class="comment-info">
<span class="comment-age">(06 Jul '16, 21:29)</span> <span class="comment-user userinfo">bengsp</span>
</div>
</div>
<span id="50692"></span>
<div id="comment-50692" class="comment">
<div id="post-50692-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are you updating the OSM data that you're storing? If so, presumably you're doing something with "dirty" tiles (rerender, mark as dirty or delete) and that needs to be factored in.</p>
<p>If I was being asked for an answer to that question at $dayjob, the first thing that I'd ask for is more information - possibly via a chat with the potential customer. You might find you get more luck in a more interactive channel such as #osm-dev - without more details any answers are bound to be a bit "how long is a piece of string".</p>
</div>
<div id="comment-50692-info" class="comment-info">
<span class="comment-age">(06 Jul '16, 21:35)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="50693"></span>
<div id="comment-50693" class="comment">
<div id="post-50693-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, the OSM data would be updated and tiles would be re-rendered afterward, but this would be a high-availability setup and that could be done while one or more other tile servers handle the load. For simplicity, I would leave that as a non-factor and it will be refactored in later.</p>
<p>Basically I just want to know necessary system requirements to handle serving of 18k tiles/minute. Since I don't know the exact % of total requests that would fall on each zoom level, we can be conservative and say 80% of total requests (~14k) will need rendered on the fly.</p>
<p>So what hardware (storage, RAM, &amp; compute) would be required to render roughly 14k tiles/minute? Are we talking 4-core 32GB RAM and a single enterprise SSD, or something like 40-core 512GB RAM and enterprise-class IO accelerator PCI-E storage?</p>
</div>
<div id="comment-50693-info" class="comment-info">
<span class="comment-age">(07 Jul '16, 01:31)</span> <span class="comment-user userinfo">bengsp</span>
</div>
</div>
</div>
<div id="comment-tools-50649" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50649-form-container" class="comment-form-container">
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

<span id="50695"></span>

<div id="answer-container-50695" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50695-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50695-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-50695-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="bengsp has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In my experience, a "standard" server (enterprise SSD, quad-core processor, 32 GB RAM*) will do around 1 metatiles per second (that's 64 tiles) on the "easy" zoom levels (14 and above), giving you about 4000 tiles per minute. That's the rendering performance, and not taking into account potential updates; delivering the tiles is something else but usually not critical. Your assumption that 80% will require rendering on the fly is un-realistic for most use cases since most use cases will have "hot spots" - either along the motorway network if you're monitoring cars, or at event locations if you're monitoring events, etc. - leading to a much higher cache hit rate.</p>
<p>Load-balancing the creation of tiles is a bit tricky as if you're doing it wrong you'll just waste time by having the same tiles created on multiple machines. My suggestion would be to go with a 64 GB dual-quad core system with 1 TB of NVMe disks and if you find that's not good enough for you, add a couple proxies to lighten the tile access load.</p>
<p>(*) note that more than 32 GB of RAM might be required to do a data import, depending on how you build your infrastructure.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jul '16, 07:40</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-50695" class="comments-container">
<span id="50742"></span>
<div id="comment-50742" class="comment">
<div id="post-50742-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What method would you recommend for load balancing such that high-availability is maintained (database, rendering, &amp; serving), but rendering isn't duplicated on multiple systems? Is there a way to push a rendered tile out to the other systems when it's first rendered so that they only have to read it from cache?</p>
</div>
<div id="comment-50742-info" class="comment-info">
<span class="comment-age">(09 Jul '16, 01:00)</span> <span class="comment-user userinfo">bengsp</span>
</div>
</div>
<span id="50760"></span>
<div id="comment-50760" class="comment">
<div id="post-50760-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There are many ways but one possible way is to use a "pinning" load balancer that tries to route all requests from the same client to the same server. Then you could use serveral Tirex (not renderd) based tile servers and have them synchronize their caches with tirex-syncd, or you could use renderd based tile servers that don't use a local tile cache but one that resides on a reliable network file system.</p>
</div>
<div id="comment-50760-info" class="comment-info">
<span class="comment-age">(09 Jul '16, 20:39)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="50911"></span>
<div id="comment-50911" class="comment">
<div id="post-50911-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Would using something like lsyncd be an option to keep tile cache synced between servers while continuing to use renderd? If renderd uses the database or something else to keep track of what tiles have already been rendered then I expect that wouldn't work, but I don't know if that's the case.</p>
</div>
<div id="comment-50911-info" class="comment-info">
<span class="comment-age">(14 Jul '16, 22:09)</span> <span class="comment-user userinfo">bengsp</span>
</div>
</div>
<span id="50912"></span>
<div id="comment-50912" class="comment">
<div id="post-50912-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It would work but consider this: You use some sort of load balancing that randomly distributes requests across all your servers. Someone views the map on his browsers and generates 20 different tile requests. All happen to be on a single 8x8 meta but the requests are distributed across 10 servers. Now all 10 servers have to compute the <em>same</em> meta tile - which means your performance isn't any better than if you only had one server. This problem can be reduced by pinning requests from the same client to the same backend server. DNS round robin <em>may</em> work in many cases too if browsers cache DNS lookup results.</p>
</div>
<div id="comment-50912-info" class="comment-info">
<span class="comment-age">(14 Jul '16, 22:24)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="50913"></span>
<div id="comment-50913" class="comment">
<div id="post-50913-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So as long as there's a persistence profile in place that keeps a user pinned to the same server (with a timeout of at least, say, 15-20 sec) then syncing the tile cache directory would work? Renderd doesn't rely on the database for information about what tiles have already been rendered?</p>
</div>
<div id="comment-50913-info" class="comment-info">
<span class="comment-age">(15 Jul '16, 01:06)</span> <span class="comment-user userinfo">bengsp</span>
</div>
</div>
<span id="50917"></span>
<div id="comment-50917" class="comment not_top_scorer">
<div id="post-50917-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes it would work (at least for the standard file backend in renderd). There's no status being kept about finished jobs outside of the meta tile tree in the file system.</p>
</div>
<div id="comment-50917-info" class="comment-info">
<span class="comment-age">(15 Jul '16, 07:42)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-50695" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-50695-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="50650"></span>

<div id="answer-container-50650" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50650-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50650-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50650-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can get infos on the osmf servers from here;<a href="http://wiki.openstreetmap.org/wiki/Servers">http://wiki.openstreetmap.org/wiki/Servers</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jul '16, 06:06</strong></p>
<img src="https://secure.gravatar.com/avatar/3c7cffe544d6a1c46c97a25b2fdcdedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yvecai&#39;s gravatar image" />
<p><span>yvecai</span><br />
<span class="score" title="1481 reputation points"><span>1.5k</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yvecai has 7 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-50650" class="comments-container">
&#10;</div>
<div id="comment-tools-50650" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50650-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="50659"></span>

<div id="answer-container-50659" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50659-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50659-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50659-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is not from the OpenStreetMap ecosystem of software, but I think you will find the ESRI maintained <strong>System Design Strategies</strong> pages a good read.</p>
<p><a href="http://wiki.gis.com/wiki/index.php/System_Design_Strategies_Preface">http://wiki.gis.com/wiki/index.php/System_Design_Strategies_Preface</a></p>
<p>Since the basic processes of creating web maps and tiles are similar, the benchmarks and graphs ESRI is showing, should give you some idea of the kind of hardware required.</p>
<p>Especially the <strong>Platform Performance</strong> page should potentially be of help:</p>
<p><a href="http://wiki.gis.com/wiki/index.php/Platform_Performance">http://wiki.gis.com/wiki/index.php/Platform_Performance</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jul '16, 10:08</strong></p>
<img src="https://secure.gravatar.com/avatar/dc8a1ef54d3e25744ee52d1ad1459a81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mboeringa&#39;s gravatar image" />
<p><span>mboeringa</span><br />
<span class="score" title="1542 reputation points"><span>1.5k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mboeringa has 4 accepted answers">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Jul '16, 10:09</strong> </span></p>
</div>
</div>
<div id="comments-container-50659" class="comments-container">
&#10;</div>
<div id="comment-tools-50659" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50659-form-container" class="comment-form-container">
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

