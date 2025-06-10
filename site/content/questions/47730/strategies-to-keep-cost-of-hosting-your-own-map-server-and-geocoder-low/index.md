+++
type = "question"
title = "Strategies to keep cost of hosting your own map server and geocoder low"
description = '''I already asked this over at gis.stackexchange.com, but the response was very little. Also, I think it suits much better here. I&#x27;m currently thinking about setting up my own tile server (mapnik, mod_tile, renderd) and geocoder (nominatim) for my application. In short, the application aims to let a u...'''
date = "2016-01-29T11:23:00Z"
lastmod = "2016-01-29T22:11:00Z"
weight = 47730
keywords = [ "cost", "tileserver", "geocoding", "server" ]
aliases = [ "/questions/47730" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Strategies to keep cost of hosting your own map server and geocoder low](/questions/47730/strategies-to-keep-cost-of-hosting-your-own-map-server-and-geocoder-low)

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
<span id="post-47730-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47730-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-47730-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I already asked this over at gis.stackexchange.com, but the response was very little. Also, I think it suits much better here.</p>
<p>I'm currently thinking about setting up my own tile server (mapnik, mod_tile, renderd) and geocoder (nominatim) for my application. In short, the application aims to let a user specify his location via address, which is then converted into coordinates. Furthermore, the user is able to create POI. The given address of the POI is also geocoded to acquire the coordinates. The least level of interactiveness required is that the maps is able to display pins of the user location and the location of the POIs.</p>
<p>Currently, the app encompasses only one country, Germany. The map doesn't have to be totally up-to-date. I'm still a bit worried that the Nominatim and Map databases impose too much of a burden on the hardware and finally the costs of hosting. So my questions is:</p>
<p>Are there any strategies to alleviate the hosting costs like pre-rendering? I just used this tool <a href="http://tools.geofabrik.de/calc/">http://tools.geofabrik.de/calc/</a> to determine the data size of all tiles in Germany. It seems to be 83GB in total at zoom level 17. Is it viable to pre-render all the tiles up to this zoom level and to do this e.g. once per month for updates? It should make the displaying of maps "free" of hardware after the rendering, or am I wrong?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-cost" rel="tag" title="see questions tagged &#39;cost&#39;">cost</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jan '16, 11:23</strong></p>
<img src="https://secure.gravatar.com/avatar/055b275d9a8bb0b7226912b5fc163948?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Emtschikay&#39;s gravatar image" />
<p><span>Emtschikay</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Emtschikay has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47730" class="comments-container">
<span id="47731"></span>
<div id="comment-47731" class="comment">
<div id="post-47731-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You'll still need to serve the tiles (so hosting costs are always there); the load of running Nominatim and db are negligible, except for the initial import. Also, the biggest storage cost would be for zooms 17+18, but I'd guess that not every of those tiles would be actually requested.</p>
</div>
<div id="comment-47731-info" class="comment-info">
<span class="comment-age">(29 Jan '16, 11:43)</span> <span class="comment-user userinfo">Piskvor</span>
</div>
</div>
<span id="47732"></span>
<div id="comment-47732" class="comment">
<div id="post-47732-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, I'm aware of that, but the computation for rendering the tiles should be gone? On second thought, I'm probably wrong. If I'll prerender all tiles, tiles are rendered that are maybe not even requested. Consequently, rendering on the fly is cheaper in terms of computation of I don't update my data?</p>
</div>
<div id="comment-47732-info" class="comment-info">
<span class="comment-age">(29 Jan '16, 11:52)</span> <span class="comment-user userinfo">Emtschikay</span>
</div>
</div>
</div>
<div id="comment-tools-47730" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47730-form-container" class="comment-form-container">
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

<span id="47733"></span>

<div id="answer-container-47733" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47733-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47733-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47733-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A Nominatim for Germany can be 50-100GB as well. I don't have a recent installation to check. On a 16core, 48GB RAM, SSD drives it took half a day to create the initial index. I wouldn't attempt the index build with less than 8GB RAM, it might still take several days. During query time Nominatim (or rather PostgreSQL) works best with more RAM, I'd say 4GB and more for Germany.</p>
<p>For tiles you have to remember that only a tiny fraction is seen by users.</p>
<p>It sounds like such a POI website would need more frequent updates as users/mappers want feedback "has this been added now?" when they come back the next day (or next hour, or check the next 10 minutes).</p>
<p>Personally I would concentrate on a static website (hosting cost $0 with github pages or every cheap regardless) and pay of tiles and geocoding. Let others worry about hardware costs, installation and keeping the data (worldwide, minutely) uptodate with OSM. I'm biased, I run a hosted geocoder, and will only point to website listing several geocoder options <a href="http://wiki.openstreetmap.org/wiki/Nominatim">http://wiki.openstreetmap.org/wiki/Nominatim</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jan '16, 13:12</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-47733" class="comments-container">
<span id="47738"></span>
<div id="comment-47738" class="comment">
<div id="post-47738-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer. The problem with most offered geocoders and mapservice is, that they have restrictions in their usage (not allowed to stored coordinates etc. - see Mapbox). I don't think that we would be the primary ressource for mappers to check whether their additions are already visible in our maps and they are also not really the audience we are targeting (needless to say that we still value their work, OSM is an amazing project). So, in the end, I hardly see any other solution than hosting it ourselves, since quotas or restrictions in the ToS force us to do so.</p>
</div>
<div id="comment-47738-info" class="comment-info">
<span class="comment-age">(29 Jan '16, 14:48)</span> <span class="comment-user userinfo">Emtschikay</span>
</div>
</div>
<span id="47740"></span>
<div id="comment-47740" class="comment">
<div id="post-47740-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You choose to save money, that's fine. But I disagree that you're forced to host yourself. Compare how many hours you'll spend installing and administering systems over time. My advice is to build the system using hosted services and only if it gets enough users/traction install your own map tile and geocoding systems. You'll have enough work with the app itself and user registration (users have to agree to the OSM terms of service, save data in their name). It's entirely possible the application won't be used as much as you're planning. Mapbox wasn't listed on the URL I gave in my last answer, others don't have the saving restriction.</p>
</div>
<div id="comment-47740-info" class="comment-info">
<span class="comment-age">(29 Jan '16, 15:10)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="47743"></span>
<div id="comment-47743" class="comment">
<div id="post-47743-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah, you're probably right. I'!! have a look at the alternarives in your URL. Thanks a lot for your tips!</p>
</div>
<div id="comment-47743-info" class="comment-info">
<span class="comment-age">(29 Jan '16, 18:21)</span> <span class="comment-user userinfo">Emtschikay</span>
</div>
</div>
<span id="47746"></span>
<div id="comment-47746" class="comment">
<div id="post-47746-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OpenCage sure looks nice and simple!</p>
</div>
<div id="comment-47746-info" class="comment-info">
<span class="comment-age">(29 Jan '16, 22:11)</span> <span class="comment-user userinfo">Emtschikay</span>
</div>
</div>
</div>
<div id="comment-tools-47733" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47733-form-container" class="comment-form-container">
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

