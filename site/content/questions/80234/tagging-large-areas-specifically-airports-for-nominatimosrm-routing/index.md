+++
type = "question"
title = "tagging large areas (specifically airports) for Nominatim/osrm routing"
description = '''I would have thought this should have came up a long time before this but was wondering... Say I wanted to use OSRM or some other router that uses Nominatim. So I type in an airport name, such as &quot;Denver International Airport&quot;. However Nominatim ends up finding the big huge 33,000 acre plot of land ...'''
date = "2021-05-19T22:28:00Z"
lastmod = "2021-05-25T08:21:00Z"
weight = 80234
keywords = [ "osrm", "airport", "nominatim" ]
aliases = [ "/questions/80234" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tagging large areas (specifically airports) for Nominatim/osrm routing](/questions/80234/tagging-large-areas-specifically-airports-for-nominatimosrm-routing)

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
<span id="post-80234-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80234-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80234-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would have thought this should have came up a long time before this but was wondering...</p>
<p>Say I wanted to use OSRM or some other router that uses Nominatim. So I type in an airport name, such as "Denver International Airport". However Nominatim ends up finding the big huge 33,000 acre plot of land and probably does a weighted centroid of this plot of land as the target point, and OSRM goes and tries to send you to a taxiway for airplanes (try it!).</p>
<p>How should these large areas be tagged so that Nominatim will point you to a more sensible, drivable location? I suppose large cities have the same problem but chances are if it's a large city, it's dense enough and likely a road near the centroid, but for airports, especially Denver which by area is one of the largest in the world, this might not be the best location to drive to? Likely it's best to point to the terminal or at least the transit station in the airporit if at all possible IMHO.</p>
<p>Or perhaps this is outside the scope of OSM?</p>
<p>By the way: Example case: In OSRM or OSM website, try searching (with text) for a routing path between:</p>
<p>From: Boulder, Colorado To: Denver International Airport</p>
<p>The problem I see is that the OSRM router will use the service roads to get to the airport, again probably because Nominatim is picking the centroid of the aerodrome/airport. I've tried to mark all the gates and roads to be "private" in order to help the router not select these little alleys and service roads in hopes that the router will always select Peña Boulevard which leads to the terminal along with all ground transportation. Even if this area is still huge, it's more reasonable that a driver will see the signs and know what they're going for instead of getting stuck on a dirt road blocked by an electrified gate...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-airport" rel="tag" title="see questions tagged &#39;airport&#39;">airport</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 May '21, 22:28</strong></p>
<img src="https://secure.gravatar.com/avatar/c86f4c99960b2c3ffdeb1698ba833b52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gpserror&#39;s gravatar image" />
<p><span>gpserror</span><br />
<span class="score" title="171 reputation points">171</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gpserror has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 May '21, 12:47</strong> </span></p>
</div>
</div>
<div id="comments-container-80234" class="comments-container">
<span id="80251"></span>
<div id="comment-80251" class="comment">
<div id="post-80251-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Some other routers and applications are smart enough to navigate the carparks. There have also been talks about tagging pick-up &amp; drop-off spots.</p>
</div>
<div id="comment-80251-info" class="comment-info">
<span class="comment-age">(21 May '21, 12:03)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-80234" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80234-form-container" class="comment-form-container">
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

<span id="80250"></span>

<div id="answer-container-80250" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80250-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maybe you have to navigate to aeroway=terminal and not to aeroway=aerodrome. Besides there could be cases where terminal is too large... so you should go for entrances. See <a href="https://wiki.openstreetmap.org/wiki/Tag:aeroway%3Dterminal">terminal wiki</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 May '21, 10:13</strong></p>
<img src="https://secure.gravatar.com/avatar/d33efa30f05d8f3604e7210c48b24a8b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cascafico&#39;s gravatar image" />
<p><span>Cascafico</span><br />
<span class="score" title="283 reputation points">283</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cascafico has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 May '21, 10:13</strong> </span></p>
</div>
</div>
<div id="comments-container-80250" class="comments-container">
<span id="80252"></span>
<div id="comment-80252" class="comment">
<div id="post-80252-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So should this actually be a nominatim upgrade so that if an airport is searched for, it would select the terminal instead of the aerodrome?</p>
<p>Of course this wouldn't work for cities, and I'm sure there are other use cases where searching ends up with a large area. I suspect the default router should choose any route that would end up in the area in any way that makes sense - though trying to get past security is yet another issue...</p>
</div>
<div id="comment-80252-info" class="comment-info">
<span class="comment-age">(21 May '21, 12:38)</span> <span class="comment-user userinfo">gpserror</span>
</div>
</div>
<span id="80253"></span>
<div id="comment-80253" class="comment">
<div id="post-80253-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://github.com/osm-search/Nominatim/issues/536">https://github.com/osm-search/Nominatim/issues/536</a></p>
</div>
<div id="comment-80253-info" class="comment-info">
<span class="comment-age">(21 May '21, 13:33)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="80255"></span>
<div id="comment-80255" class="comment">
<div id="post-80255-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah I knew that I wasn't the first one to see this, alas it looks like there still isn't a good resolution yet... and even worse, this is not the only router out there. Heck OSRM and GraphHopper behave differently and I'd think both are using Nominatim.</p>
</div>
<div id="comment-80255-info" class="comment-info">
<span class="comment-age">(21 May '21, 18:06)</span> <span class="comment-user userinfo">gpserror</span>
</div>
</div>
<span id="80282"></span>
<div id="comment-80282" class="comment">
<div id="post-80282-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>AFAIK, overpass-turbo wizard understands some words as "airport" as a aeroway=aerodrome. Geocoders don't. Since implementing such a new feature in geocoders would take discussions, time and resources, I guess we have better to map airport names on terminal building also.</p>
<p>The following query should return aerodromes without terminal at admin=2 (France) scale.<br />
<a href="http://overpass-turbo.eu/s/17HY">http://overpass-turbo.eu/s/17HY</a></p>
</div>
<div id="comment-80282-info" class="comment-info">
<span class="comment-age">(25 May '21, 08:21)</span> <span class="comment-user userinfo">Cascafico</span>
</div>
</div>
</div>
<div id="comment-tools-80250" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80250-form-container" class="comment-form-container">
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

