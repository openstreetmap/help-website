+++
type = "question"
title = "OSM for commercial truck routing"
description = '''Hello everyone, Please bear with me as I am completely new to maps and routing. The company I&#x27;m working for wants to determine routes for trucks. Primarily in the USA and have the ability to extend to the rest of the world. I&#x27;ve looked at OSM and it appears that the routing available is only for car...'''
date = "2020-04-22T21:46:00Z"
lastmod = "2020-04-23T08:53:00Z"
weight = 74336
keywords = [ "truck", "routing" ]
aliases = [ "/questions/74336" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [OSM for commercial truck routing](/questions/74336/osm-for-commercial-truck-routing)

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
<span id="post-74336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74336-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone,</p>
<p>Please bear with me as I am completely new to maps and routing. The company I'm working for wants to determine routes for trucks. Primarily in the USA and have the ability to extend to the rest of the world. I've looked at OSM and it appears that the routing available is only for cars, walking and bicycling. Does anyone know if there's commercial truck routing data that we can use in conjunction with OSM maps? The desired behavior is to have a REST service in place that returns routes in response to requests.</p>
<p>Thanks very much, Eugen</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-truck" rel="tag" title="see questions tagged &#39;truck&#39;">truck</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Apr '20, 21:46</strong></p>
<img src="https://secure.gravatar.com/avatar/ad8f49d67fd7b8e25376900e86f57542?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eugen_nw&#39;s gravatar image" />
<p><span>eugen_nw</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eugen_nw has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Apr '20, 21:49</strong> </span></p>
</div>
</div>
<div id="comments-container-74336" class="comments-container">
&#10;</div>
<div id="comment-tools-74336" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74336-form-container" class="comment-form-container">
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

<span id="74337"></span>

<div id="answer-container-74337" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74337-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74337-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-74337-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="eugen_nw has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To have routing for trucks you need three things: The data, the software, and someone who runs the software for you.</p>
<p>The data is basically there in OpenStreetMap, though some restrictions that may be relevant to truck routing might be missing in OSM. Remember, the data is collected by volunteers, and perhaps not every volunteer will make it a priority to record bridge heights or maximum weight restrictions. The situation is slowly improving but as of today, commercial data might be more complete for truck routing than OSM is.</p>
<p>The software is basically there as well; you can activate a truck routing profile in all popular OSM routing engines e.g. Graphhopper, OSRM, or Valhalla. They might differ in what attributes they look at in the OSM data, and if you are keen on doing stuff like routing for heavy or large vehicles where height or weight restrictions start playing a role, you might have to adapt the profiles to your needs. (That you don't find truck routing in available public offers e.g. on openstreetmap.org is mostly due to the fact that each additional routing type uses more resources, and the offers concentrate on frequent use cases.)</p>
<p>Which brings us to the third issue, someone to run the server for you. Publicly available instances of OSM routing services are mostly for demo purposes or donation-financed offers for the community. They are not meant to be a free-of-charge resource that can be monetised by commercial users. For that reason alone - but also for reasons of flexibility and customisation - you will likely want to run your own instance of the routing software, which isn't a problem because both data and software are open and free to download and use.</p>
<p>The alternative to doing it yourself is of course buying services, either from a commercial supplier of OSM-based routing services (most will use the same software listed above), or from someone who helps you set up the software for yourself. See <a href="https://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services">https://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services</a> for an inoffical list maintainted by the suppliers themselves.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Apr '20, 22:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Apr '20, 22:17</strong> </span></p>
</div>
</div>
<div id="comments-container-74337" class="comments-container">
<span id="74338"></span>
<div id="comment-74338" class="comment">
<div id="post-74338-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks very much for the info Frederik! The fact that the OSM data may not be complete enough for truck routing sounds scary. From what I've read there are more restrictions on trucks than tunnel/bridge heights and weight: <a href="https://www.developer.here.com/documentation/routing-api/dev_guide/topics/use-cases/truck-routing.html">https://www.developer.here.com/documentation/routing-api/dev_guide/topics/use-cases/truck-routing.html</a></p>
</div>
<div id="comment-74338-info" class="comment-info">
<span class="comment-age">(22 Apr '20, 23:07)</span> <span class="comment-user userinfo">eugen_nw</span>
</div>
</div>
<span id="74339"></span>
<div id="comment-74339" class="comment">
<div id="post-74339-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"you might have to adapt the profiles to your needs": how do I do that please?</p>
</div>
<div id="comment-74339-info" class="comment-info">
<span class="comment-age">(22 Apr '20, 23:10)</span> <span class="comment-user userinfo">eugen_nw</span>
</div>
</div>
<span id="74342"></span>
<div id="comment-74342" class="comment">
<div id="post-74342-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/18251/eugen_nw">@eugen_nw</a>, at least you know beforehand that OSM is not complete, but no map offering is complete (e.g. Google, TomTom and the like also have missing or wrong data).</p>
</div>
<div id="comment-74342-info" class="comment-info">
<span class="comment-age">(23 Apr '20, 04:37)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="74344"></span>
<div id="comment-74344" class="comment">
<div id="post-74344-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Every routing engine has its own system to define routing profiles; some take configuration files in something that looks almost like a programming language, while for others you have write code in the actual programming language of the routing engine. In most cases you have to use the routing profile already during the data import step, because it can then find out which roads to omit entirely and how to preprocess the data. There are <em>some</em> routing engines - e.g. BRouter - that are so versatile that you can actually specify your routing profile when making a routing request instead of when loading the data, but the price for that flexibility is speed. -- This is the car profile for the OSRM routing engine: <a href="https://github.com/Project-OSRM/osrm-backend/blob/master/profiles/car.lua">https://github.com/Project-OSRM/osrm-backend/blob/master/profiles/car.lua</a> someone has made a truck adaptation: <a href="https://github.com/Project-OSRM/osrm-profiles-contrib/tree/master/5/21/truck-soft">https://github.com/Project-OSRM/osrm-profiles-contrib/tree/master/5/21/truck-soft</a> -- In Graphhopper, the profiles are called "Flag Encoders" and they are here <a href="https://github.com/graphhopper/graphhopper/tree/master/core/src/main/java/com/graphhopper/routing/util;">https://github.com/graphhopper/graphhopper/tree/master/core/src/main/java/com/graphhopper/routing/util;</a> GraphHopper's paid service offers a ready-made truck profile but that seems not to be open source.</p>
</div>
<div id="comment-74344-info" class="comment-info">
<span class="comment-age">(23 Apr '20, 08:53)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-74337" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74337-form-container" class="comment-form-container">
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

