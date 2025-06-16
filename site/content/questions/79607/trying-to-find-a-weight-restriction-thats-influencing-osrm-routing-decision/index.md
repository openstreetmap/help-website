+++
type = "question"
title = "Trying to find a weight restriction that&#x27;s influencing OSRM routing decision"
description = '''Hi all, I am experimenting with the &quot;Open Source Routing Machine&quot; (OSRM) and it&#x27;s profiles. Currently I am facing a phenomenom I discovered running OSRM via docker in my custom setup: A route changes noticeably if the weight of the vehicle is changed in the car.lua profile. So I think that somewhere...'''
date = "2021-04-11T16:02:00Z"
lastmod = "2021-04-11T18:05:00Z"
weight = 79607
keywords = [ "osrm", "truck.lua", "car.lua", "weight", "restriction" ]
aliases = [ "/questions/79607" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Trying to find a weight restriction that's influencing OSRM routing decision](/questions/79607/trying-to-find-a-weight-restriction-thats-influencing-osrm-routing-decision)

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
<span id="post-79607-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79607-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79607-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I am experimenting with the "Open Source Routing Machine" (OSRM) and it's profiles. Currently I am facing a phenomenom I discovered running OSRM via docker in my custom setup: A route changes noticeably if the weight of the vehicle is changed in the car.lua profile.</p>
<p>So I think that somewhere in the route there must be a node/way/relation with restrictions of weigth, which causes the discrepancy. How can I search for weight restrictions in a route? Or does anyone has a alternative explanation for the discrepancy?</p>
<p>The affected route starts in Burghasungen and ends in Melsungen. Both locations are cities in Hessen, Germany. Using the OSM routing service with default car.lua you can see the route here: <a href="https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&amp;route=51.3246%2C9.2777%3B51.1298%2C9.5437#map=10/51.2391/9.1763">https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&amp;route=51.3246%2C9.2777%3B51.1298%2C9.5437#map=10/51.2391/9.1763</a></p>
<p>In my setup the discrepancy looks like this: <img src="/upfiles/route.png" alt="alt text" /></p>
<p>Even with the weight of 6000 kg I would expect the route to continue up to the end of A44 and not to leave the A44 premature (A44 should be tagged highway=motorway).</p>
<p>I case you wonder what my motivation is: Actually I would like to use a profile called "truck soft", which <a href="https://github.com/Project-OSRM/osrm-profiles-contrib/tree/master/5/21/truck-soft">can be found here</a>. This truck profile uses car.lua as default and changes different aspects. But using this truck profile I discovered the above described discrepancy. Thus I stepped back, took the default car.lua and tried to applied the changes one after another. By this I found out, that only changing the "vehicle_weight" (leaving the rest untouched!) leads to the differing route. The data I used is the sub region Hessen <a href="http://download.geofabrik.de/europe/germany/hessen-latest.osm.pbf">kindly provided by Geofabrik</a>. Interesting additional detail: Using an older dataset, which is round about 4,5 years old, the route does not change on different weights.</p>
<p>Thanks and greetings, rebos</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-truck.lua" rel="tag" title="see questions tagged &#39;truck.lua&#39;">truck.lua</span> <span class="post-tag tag-link-car.lua" rel="tag" title="see questions tagged &#39;car.lua&#39;">car.lua</span> <span class="post-tag tag-link-weight" rel="tag" title="see questions tagged &#39;weight&#39;">weight</span> <span class="post-tag tag-link-restriction" rel="tag" title="see questions tagged &#39;restriction&#39;">restriction</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Apr '21, 16:02</strong></p>
<img src="https://secure.gravatar.com/avatar/8b492a48055eb8eb8fa8cc10a91bfd83?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="osmrebos&#39;s gravatar image" />
<p><span>osmrebos</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="osmrebos has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-79607" class="comments-container">
&#10;</div>
<div id="comment-tools-79607" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79607-form-container" class="comment-form-container">
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

<span id="79609"></span>

<div id="answer-container-79609" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79609-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79609-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-79609-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maxweight of <a href="https://www.openstreetmap.org/way/34287495">way 34287495</a> and a few other ways on the eastbound carriageway appear to be tagged as 3.5, with the default unit being metric tonnes. <a href="https://www.openstreetmap.org/changeset/70382652">Changeset 70382652</a> also has the comment "A44 gesperrt 3,5 ton " so I assume this is not accidental.</p>
<p>Found via an overpass turbo <a href="https://overpass-turbo.eu/s/1605">query</a> on the <a href="https://wiki.openstreetmap.org/wiki/Key:maxweight">maxweight</a> tag.</p>
<p>As always, please be sure to check on site, or with very recent street level imagery before making any changes to the mapped data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Apr '21, 17:59</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-79609" class="comments-container">
<span id="79610"></span>
<div id="comment-79610" class="comment">
<div id="post-79610-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>My curiosity got the better of me: <a href="https://www.hna.de/lokales/kreis-kassel/sperrung-fuer-lastkraftwagen-ueber-3-5-tonnen-voraussichtlich-ab-januar-umleitung-ueber-a-49-10789570.html">here's an article</a> about the change.</p>
</div>
<div id="comment-79610-info" class="comment-info">
<span class="comment-age">(11 Apr '21, 18:05)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-79609" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79609-form-container" class="comment-form-container">
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

