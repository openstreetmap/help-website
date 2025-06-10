+++
type = "question"
title = "Why does searching for &quot;Pinneberg, Bahnhof&quot; find the Train station in Wedel?"
description = '''To reproduce:  1. open openstreetmap.org  2. In the search field, enter &quot;Pinneberg, Bahnhof&quot; and click &quot;Go&quot;  3. Observe that the train station shown on the map is not in Pinneberg, but in Wedel, a different town 21km south of Pinneberg. Interestingly, searching for &quot;Bahnhof Pinneberg&quot; gives the corr...'''
date = "2022-04-03T20:13:00Z"
lastmod = "2022-04-12T13:46:00Z"
weight = 84087
keywords = [ "nominatim", "geocoding" ]
aliases = [ "/questions/84087" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why does searching for "Pinneberg, Bahnhof" find the Train station in Wedel?](/questions/84087/why-does-searching-for-pinneberg-bahnhof-find-the-train-station-in-wedel)

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
<span id="post-84087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84087-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>To reproduce: 1. open openstreetmap.org 2. In the search field, enter "Pinneberg, Bahnhof" and click "Go" 3. Observe that the train station shown on the map is not in Pinneberg, but in Wedel, a different town 21km south of Pinneberg.</p>
<p>Interestingly, searching for "Bahnhof Pinneberg" gives the correct result.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Apr '22, 20:13</strong></p>
<img src="https://secure.gravatar.com/avatar/49242364fa70a9f44b7a2b1f1f636042?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_Bj&#39;s gravatar image" />
<p><span>_Bj</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_Bj has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Apr '22, 12:09</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-84087" class="comments-container">
&#10;</div>
<div id="comment-tools-84087" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84087-form-container" class="comment-form-container">
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

<span id="84089"></span>

<div id="answer-container-84089" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84089-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84089-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84089-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The search engine on openstreetmap.org works with some fixed phrases to search for specific objects. You can search for <em>Bahnhof Pinneberg</em>, <em>Bahnhof in Pinneberg</em> or <em>Bahnhof bei Pinneberg</em> to find Pinneberg station. Even <em>Pinneberg Bahnhof</em> works but not if you separate the two terms with a comma.</p>
<p>Note that you might have to click on <em>Mehr Treffer</em> to get the desired feature shown.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Apr '22, 21:16</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-84089" class="comments-container">
<span id="84153"></span>
<div id="comment-84153" class="comment">
<div id="post-84153-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer.</p>
<p>Of course I could stop using a comma in OSM queries which would solve this issue for me.</p>
<p>However, there are two more aspects to this: a) When the search engine cannot find what I am looking for, then answering with a train station in a completely different city is highly confusing and can lead to substantial real-world problems for instance when the user uses the result for planning a journey. It would be much better when the search engine would tell the user that it could not find "Pinneberg, Bahnhof".</p>
<p>b) using comma to separate different levels in a hierarchy is pretty common. I highly doubt that I am the only person doing this. Google Maps has no problem with this. Maybe it would be worthwhile to add support for this to OSM as well?</p>
</div>
<div id="comment-84153-info" class="comment-info">
<span class="comment-age">(10 Apr '22, 23:07)</span> <span class="comment-user userinfo">_Bj</span>
</div>
</div>
<span id="84158"></span>
<div id="comment-84158" class="comment">
<div id="post-84158-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://www.openstreetmap.org/">https://www.openstreetmap.org/</a> is originally not a map application users are supposed to use. The search is run by <a href="https://nominatim.openstreetmap.org/">https://nominatim.openstreetmap.org/</a> to verify the data structure. You should see if actual apps using OSM data (including: OSMAnd, Organic Maps, Qwant Maps, Arcane Maos, Mapy.cz, Magic Earth, or even Apple Maps) can provide the search result you need. They are allowed to use different search engines, and add other data from sources incomaptible with this database (you can add add-ons yourself too, eg OpenAddresses in OSMAnd). You can also search the location in another app (eg Acastus Photon, or even Google), then open the result position in the map app you want to use.</p>
</div>
<div id="comment-84158-info" class="comment-info">
<span class="comment-age">(11 Apr '22, 16:50)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
<span id="84161"></span>
<div id="comment-84161" class="comment">
<div id="post-84161-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The <a href="https://www.openstreetmap.org/node/1895255302">result shown for your query</a> was obviously not what you had looked for but it was not wrong. The result was not the "Bahnhof Pinneberg" but an object (a bicycle rental station actually) called "Bahnhof" which is located within "Kreis Pinneberg".</p>
<p>A comma might separate hierarchical items and the search engine Nominatim generally supports this use (e.g. you could have searched for "Bahnhof in Pinneberg, Schleswig-Holstein, Deutschland"). But station and city are not different levels of a hierarchy. Nominatim builds a geographical hierarchy (country, state, county, ...) from OSM data but station is an attribute of an object outside this hierarchy.<br />
(1/2)</p>
</div>
<div id="comment-84161-info" class="comment-info">
<span class="comment-age">(12 Apr '22, 13:45)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="84162"></span>
<div id="comment-84162" class="comment">
<div id="post-84162-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>When you search for "Pinneberg, Bahnhof" Nominatim first returns the bicycle rental (an object named "Bahnhof" in "Kreis Pinneberg"), secondly a mail box with reference "Bahnhof" in "Kreis Pinneberg", and only on third rank your desired Pinneberg station (order of results is also influenced from where you start on the map so you might see a different order). Nominatim does not have any (or at least no advanced) logic built in predicting what the most likely result is a user is looking for. You need to scroll further down the result list or try some of the other search methods pointed out by Kovoschiz. (2/2)</p>
</div>
<div id="comment-84162-info" class="comment-info">
<span class="comment-age">(12 Apr '22, 13:46)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-84089" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84089-form-container" class="comment-form-container">
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

