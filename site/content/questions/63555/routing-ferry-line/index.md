+++
type = "question"
title = "Routing ferry line"
description = '''There is a routing error, which I cannot get to grips with even after consulting top-level users in Scandinavia.  Ferry line between Oskarshamn and Visby on the island of Gotland. Routing by foot or cycle is ok. But motorvehicles will be sent northover to Nynäshamn for ferry from there to Visby. The...'''
date = "2018-05-18T12:44:00Z"
lastmod = "2018-05-23T11:04:00Z"
weight = 63555
keywords = [ "ferry", "route", "vehicle" ]
aliases = [ "/questions/63555" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Routing ferry line](/questions/63555/routing-ferry-line)

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
<span id="post-63555-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63555-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63555-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There is a routing error, which I cannot get to grips with even after consulting top-level users in Scandinavia. Ferry line between Oskarshamn and Visby on the island of Gotland. Routing by foot or cycle is ok. But motorvehicles will be sent northover to Nynäshamn for ferry from there to Visby. The funny thing is when I move the green marker in Oskarshamn directly on to ferry-route-line - beyond amenity=ferry_terminal - then routing is ok. I have tried all sorts of possible tags and values without avail.</p>
<p>1.) <a href="https://www.openstreetmap.org/directions?engine=graphhopper_car&amp;route=57.2633%2C16.4443%3B57.6379%2C18.2980#map=8/58.247/17.230">https://www.openstreetmap.org/directions?engine=graphhopper_car&amp;route=57.2633%2C16.4443%3B57.6379%2C18.2980#map=8/58.247/17.230</a></p>
<p>2.) <a href="https://graphhopper.com/maps/?point=57.263868%2C16.458024&amp;point=57.633617%2C18.277903&amp;locale=sv-SE&amp;vehicle=car&amp;weighting=fastest&amp;elevation=true&amp;use_miles=false&amp;layer=Omniscale">https://graphhopper.com/maps/?point=57.263868%2C16.458024&amp;point=57.633617%2C18.277903&amp;locale=sv-SE&amp;vehicle=car&amp;weighting=fastest&amp;elevation=true&amp;use_miles=false&amp;layer=Omniscale</a></p>
<p>3.) <a href="https://maps.openrouteservice.org/directions?n1=58.242312&amp;n2=17.236997&amp;n3=8&amp;a=57.260721,16.451082,57.639707,18.314506&amp;b=0&amp;c=0&amp;k1=en-US&amp;k2=km">https://maps.openrouteservice.org/directions?n1=58.242312&amp;n2=17.236997&amp;n3=8&amp;a=57.260721,16.451082,57.639707,18.314506&amp;b=0&amp;c=0&amp;k1=en-US&amp;k2=km</a></p>
<p>Anyone who can help? Lot of thanks in advance! /archie</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ferry" rel="tag" title="see questions tagged &#39;ferry&#39;">ferry</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-vehicle" rel="tag" title="see questions tagged &#39;vehicle&#39;">vehicle</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 May '18, 12:44</strong></p>
<img src="https://secure.gravatar.com/avatar/e5cdbb738a386589d67441a7ed484205?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="archie&#39;s gravatar image" />
<p><span>archie</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="archie has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63555" class="comments-container">
<span id="63559"></span>
<div id="comment-63559" class="comment">
<div id="post-63559-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It works fine with OSRM. It looks like there have been a number of changes made over the last couple of days, so you may want to just leave it for a few days to allow the other routers to get the new data and see if there's still a problem.</p>
</div>
<div id="comment-63559-info" class="comment-info">
<span class="comment-age">(18 May '18, 16:46)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="63645"></span>
<div id="comment-63645" class="comment">
<div id="post-63645-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can also try creating a <a href="https://github.com/graphhopper/graphhopper/issues">new issue</a> at the GraphHopper GitHub project page if this issue exists only with GraphHopper.</p>
</div>
<div id="comment-63645-info" class="comment-info">
<span class="comment-age">(23 May '18, 11:04)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-63555" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63555-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

