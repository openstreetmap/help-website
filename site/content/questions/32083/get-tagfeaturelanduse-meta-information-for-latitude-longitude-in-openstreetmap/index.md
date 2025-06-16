+++
type = "question"
title = "Get tag/feature/landuse meta information for latitude longitude in openstreetmap"
description = '''Hey guys! I need the possibility to find the underlying ground information of a given location (set by latLng) - not an area! I already tried the nominatim reverse search, but it lacks the landuse information. Here&#x27;s an example query: http://nominatim.openstreetmap.org/reverse?format=json&amp;amp;lat=52...'''
date = "2014-04-02T22:48:00Z"
lastmod = "2014-04-04T15:46:00Z"
weight = 32083
keywords = [ "latitude", "query", "landuse", "reversegeocoding" ]
aliases = [ "/questions/32083" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get tag/feature/landuse meta information for latitude longitude in openstreetmap](/questions/32083/get-tagfeaturelanduse-meta-information-for-latitude-longitude-in-openstreetmap)

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
<span id="post-32083-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32083-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32083-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey guys! I need the possibility to find the underlying ground information of a given location (set by latLng) - not an area!</p>
<p>I already tried the nominatim reverse search, but it lacks the landuse information. Here's an example query: <a href="http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=52.5487429714954&amp;lon=-1.81602098644987&amp;zoom=18&amp;addressdetails=1">http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=52.5487429714954&amp;lon=-1.81602098644987&amp;zoom=18&amp;addressdetails=1</a></p>
<p>How do I enforce the output of the landuse here, which would likely be "residential".</p>
<p>Greets, Kai</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-latitude" rel="tag" title="see questions tagged &#39;latitude&#39;">latitude</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-landuse" rel="tag" title="see questions tagged &#39;landuse&#39;">landuse</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Apr '14, 22:48</strong></p>
<img src="https://secure.gravatar.com/avatar/0e5a8621c193b0e8b5722a83f78a883a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krnlde&#39;s gravatar image" />
<p><span>krnlde</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krnlde has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Apr '14, 10:17</strong> </span></p>
</div>
</div>
<div id="comments-container-32083" class="comments-container">
<span id="32124"></span>
<div id="comment-32124" class="comment">
<div id="post-32124-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I guess currently there is no reversegeocoder with a focus on landuse. You might try to create your own prototype by using the Overpass API and add a small server based analysers as a frontend.</p>
</div>
<div id="comment-32124-info" class="comment-info">
<span class="comment-age">(04 Apr '14, 08:03)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="32125"></span>
<div id="comment-32125" class="comment">
<div id="post-32125-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for your comment. Since I'm not that familiar with the capabilities of Overpass API I put something together to ask if it is the right way to do. Would you please review this <a href="http://overpass-turbo.eu/s/2X7">http://overpass-turbo.eu/s/2X7</a></p>
</div>
<div id="comment-32125-info" class="comment-info">
<span class="comment-age">(04 Apr '14, 09:14)</span> <span class="comment-user userinfo">krnlde</span>
</div>
</div>
<span id="32134"></span>
<div id="comment-32134" class="comment">
<div id="post-32134-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>to check your results (I have got only 4 ways tagges with landuse=* ) you can try the overpass turbo wizard to do a query for landuse=anything without any coordinates, but only zoomed to the area you are interested in.</p>
<p>Maybe other landuse-objects are so big that they are not "covered" by your lat-lon-query?</p>
</div>
<div id="comment-32134-info" class="comment-info">
<span class="comment-age">(04 Apr '14, 14:35)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="32135"></span>
<div id="comment-32135" class="comment">
<div id="post-32135-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yep, I think the problem in my query is that it doesn't catch the way (polygon) it is in. I need sth like an extrapolation for this polygon. In my example on overpass-turbo I'm standing on grass next to a basin, but the query only catches objects next to me (the basin), not the area/way I'm "in" (the grass). Any suggestions?</p>
</div>
<div id="comment-32135-info" class="comment-info">
<span class="comment-age">(04 Apr '14, 15:22)</span> <span class="comment-user userinfo">krnlde</span>
</div>
</div>
<span id="32136"></span>
<div id="comment-32136" class="comment">
<div id="post-32136-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It might be worth asking in the #osm-dev IRC channel - someone there might have a suggestion.</p>
</div>
<div id="comment-32136-info" class="comment-info">
<span class="comment-age">(04 Apr '14, 15:24)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="32137"></span>
<div id="comment-32137" class="comment not_top_scorer">
<div id="post-32137-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great idea! I'll try this tonight and let you guys know later :) Thank you all</p>
</div>
<div id="comment-32137-info" class="comment-info">
<span class="comment-age">(04 Apr '14, 15:26)</span> <span class="comment-user userinfo">krnlde</span>
</div>
</div>
</div>
<div id="comment-tools-32083" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-32083-form-container" class="comment-form-container">
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

<span id="32138"></span>

<div id="answer-container-32138" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32138-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32138-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32138-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I asked in the #osm-dev IRC Channel and got the following: First, this is a feature planned for osm.org based on the overpass API. Second, overpass2 DEV API already returns information about the enclosing areas: <a href="http://overpass2.apis.dev.openstreetmap.org/query?lat=51.7972&amp;lon=8.8686">http://overpass2.apis.dev.openstreetmap.org/query?lat=51.7972&amp;lon=8.8686</a></p>
<p>This is done by this algorithms <a href="https://github.com/tomhughes/openstreetmap-website/blob/overpass/app/assets/javascripts/index/query.js#L235">https://github.com/tomhughes/openstreetmap-website/blob/overpass/app/assets/javascripts/index/query.js#L235</a></p>
<h2 id="tldr">TL,DR;</h2>
<p><code>is_in</code> is the key command to get the enclosing area with all it's tags available.</p>
<p>Unfortunately <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Query_for_areas">is_in</a> only appears to be covering areas with names in it. Other areas/ways can be covered by <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Around">around</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Apr '14, 15:46</strong></p>
<img src="https://secure.gravatar.com/avatar/0e5a8621c193b0e8b5722a83f78a883a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krnlde&#39;s gravatar image" />
<p><span>krnlde</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krnlde has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Apr '14, 14:14</strong> </span></p>
</div>
</div>
<div id="comments-container-32138" class="comments-container">
&#10;</div>
<div id="comment-tools-32138" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32138-form-container" class="comment-form-container">
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

