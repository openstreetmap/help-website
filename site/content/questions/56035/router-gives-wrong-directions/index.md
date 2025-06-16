+++
type = "question"
title = "Router gives wrong directions"
description = '''If one tries this routing from SVG airport to Preikestolen, a popular tourist attraction in Norway the router is very misleading.  From this picture one can see that the router tries to navigate south of the fjord (marked in blue) and I marked the expected road in red marker and the expected footpat...'''
date = "2017-05-04T19:10:00Z"
lastmod = "2017-05-05T08:34:00Z"
weight = 56035
keywords = [ "osrm", "norway", "routing", "tagging" ]
aliases = [ "/questions/56035" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Router gives wrong directions](/questions/56035/router-gives-wrong-directions)

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
<span id="post-56035-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56035-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56035-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If one tries this <a href="https://www.openstreetmap.org/directions?engine=osrm_car&amp;route=58.8809%2C5.6254%3B58.9864%2C6.1886#map=11/58.9027/5.9254">routing from SVG airport to Preikestolen</a>, a popular tourist attraction in Norway the router is very misleading.</p>
<p>From this picture one can see that the router tries to navigate south of the fjord (marked in blue) and I marked the expected road in red marker and the expected footpath from there with yellow marker.</p>
<p><img src="/upfiles/Screenshot_from_2017-05-04_20-02-56.png" alt="Routing from OSM.org" /></p>
<p>Is there a way to tag to help the router here?<br />
Or is this a bug in the Open Source Routing Machine?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-norway" rel="tag" title="see questions tagged &#39;norway&#39;">norway</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 May '17, 19:10</strong></p>
<img src="https://secure.gravatar.com/avatar/f882e7865ffe23339fbaa71c9f576065?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FredrikLindseth&#39;s gravatar image" />
<p><span>FredrikLindseth</span><br />
<span class="score" title="815 reputation points">815</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FredrikLindseth has 2 accepted answers">13%</span> </br></p>
</img>
</div>
</div>
<div id="comments-container-56035" class="comments-container">
&#10;</div>
<div id="comment-tools-56035" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56035-form-container" class="comment-form-container">
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

<span id="56037"></span>

<div id="answer-container-56037" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56037-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56037-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-56037-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="FredrikLindseth has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The OSRM instance used by the Openstreetmap.org site only does vehicle routing. Since it looks like the end of the road on the south side is a bit closer to the destination than the end of the road on the north side, it's probably routing as close as it can by road and then leaving the rest up to the user to figure out. This leads to a wildly-incorrect result in this scenario as you've demonstrated.</p>
<p>Unfortunately, I'm not sure there's anything that could be done to the tagging to fix OSRM's routing in this case. OSRM would need to be modified to be able to route on trails to get a more useful result.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 May '17, 20:49</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 May '17, 20:52</strong> </span></p>
</div>
</div>
<div id="comments-container-56037" class="comments-container">
&#10;</div>
<div id="comment-tools-56037" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56037-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="56042"></span>

<div id="answer-container-56042" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56042-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56042-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-56042-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Currently all routers accessible via openstreetmap.org are restricted to one specific mode of transportation. If you want to use multiple modes of transportation then you have to calculate multiple individual routes. Example: <a href="https://www.openstreetmap.org/directions?engine=osrm_car&amp;route=58.8809%2C5.6254%3B58.9914%2C6.1396">Car route up to the nearest road of your destination</a>, <a href="https://www.openstreetmap.org/directions?engine=graphhopper_foot&amp;route=58.9937%2C6.1391%3B58.9864%2C6.1886">foot route from this road to your destination</a>.</p>
<p>To improve this behavior we have to improve the routing engines, not the map data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 May '17, 08:34</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-56042" class="comments-container">
&#10;</div>
<div id="comment-tools-56042" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56042-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="56038"></span>

<div id="answer-container-56038" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56038-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56038-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56038-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I agree with Alester answer. If you move the end marker only two hundred meters NW the route will be recalculated to your expected red route.. Initially I thought there was a problem with the mapping which i would have tested by doing this:- I would test it section by section by putting start( green) end (red) flags on smaller legs of the expected route. You should be able to pinpoint where the problem is. Next check for unconnected nodes, followed by Tags. Changing the routing choice between car, foot and bike may also give clues the problem, if it works for bike or foot the way could be connected ok but the ways do not allow cars, but that could be tagged correctly, that will need checking.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 May '17, 22:41</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 May '17, 23:15</strong> </span></p>
</div>
</div>
<div id="comments-container-56038" class="comments-container">
&#10;</div>
<div id="comment-tools-56038" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56038-form-container" class="comment-form-container">
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

