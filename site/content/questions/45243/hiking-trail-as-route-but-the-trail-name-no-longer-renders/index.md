+++
type = "question"
title = "Hiking trail as route? But the trail name no longer renders?!"
description = '''I&#x27;ve update a local hiking trail in OSM, which required breaking it into smaller segments (ways), so that the smaller segments could be appropriately tagged with track/path, surface, bridge, etc. At the same time, I wanted to add overall trail information: name, ref, maintainer, etc. Rather than add...'''
date = "2015-09-14T23:27:00Z"
lastmod = "2015-09-15T19:39:00Z"
weight = 45243
keywords = [ "not_shown", "trail", "route", "relations", "hiking" ]
aliases = [ "/questions/45243" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Hiking trail as route? But the trail name no longer renders?!](/questions/45243/hiking-trail-as-route-but-the-trail-name-no-longer-renders)

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
<span id="post-45243-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45243-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-45243-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've update a local hiking trail in OSM, which required breaking it into smaller segments (ways), so that the smaller segments could be appropriately tagged with track/path, surface, bridge, etc. At the same time, I wanted to add overall trail information: name, ref, maintainer, etc. Rather than add that information to each individual segment, I created a Hiking Route relation to contain all the segments, and added the trail info to that. However, when the OSM map tiles refreshed, the trail name no longer rendered. It must only render the name of the way, not a relation that it is part of. This made me wonder if I did the wrong thing.</p>
<p>What is the correct way to do this? Should the trail info be duplicated on each segment?</p>
<p>For some trail systems in the area there are segments that are considered part of multiple routes, which would be possible to represent with the route approach.</p>
<p>What is the best practice advice for this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-not_shown" rel="tag" title="see questions tagged &#39;not_shown&#39;">not_shown</span> <span class="post-tag tag-link-trail" rel="tag" title="see questions tagged &#39;trail&#39;">trail</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-hiking" rel="tag" title="see questions tagged &#39;hiking&#39;">hiking</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Sep '15, 23:27</strong></p>
<img src="https://secure.gravatar.com/avatar/a942f2f266b5c76bfb13e52f09d321a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Elerius&#39;s gravatar image" />
<p><span>Elerius</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Elerius has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Sep '15, 06:51</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-45243" class="comments-container">
&#10;</div>
<div id="comment-tools-45243" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45243-form-container" class="comment-form-container">
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

<span id="45244"></span>

<div id="answer-container-45244" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45244-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45244-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-45244-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It sounds like <span>you are doing</span> it right (adding route information only to the relation; compare with <a href="/questions/39179/how-to-map-a-hiking-trail-that-spans-over-several-different-existing-ways">this other question</a> or <a href="/questions/407/how-should-i-tag-hiking-trails">that question</a>)<br />
… but the map you are looking at is just not displaying hiking routes. Are other hiking routes shown? Check at e.g. <a href="http://hiking.waymarkedtrails.org">http://hiking.waymarkedtrails.org</a> (<a href="http://hiking.waymarkedtrails.org/?zoom=13&amp;lat=45.25034&amp;lon=-121.90888&amp;hill=0#">your new hiking trail</a>) or other <span>hiking maps/services</span>.</p>
<p>Info about the usual tagging is at <a href="https://wiki.openstreetmap.org/wiki/Hiking#Tagging_walking_and_hiking_Route_Networks">https://wiki.openstreetmap.org/wiki/Hiking#Tagging_walking_and_hiking_Route_Networks</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Sep '15, 06:06</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Sep '15, 06:33</strong> </span></p>
</div>
</div>
<div id="comments-container-45244" class="comments-container">
<span id="45252"></span>
<div id="comment-45252" class="comment">
<div id="post-45252-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the advice. I wasn't aware of that waymarked trails, which is good to know about. However, it appears to be using tiles that are served up from osm.org tile server, which is the tile set that doesn't have trail labels for hiking trails unless it is on the way itself.</p>
<p>I still feel like I'm doing it right, and that this just reflects a deficiency in that specific tile renderer. Like I said, the relation approach is the only way to capture certain data. I might wait until the cycle map tiles refresh, which I think are more useful for hiking trail maps anyway.</p>
</div>
<div id="comment-45252-info" class="comment-info">
<span class="comment-age">(15 Sep '15, 16:04)</span> <span class="comment-user userinfo">Elerius</span>
</div>
</div>
<span id="45255"></span>
<div id="comment-45255" class="comment">
<div id="post-45255-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/11465/elerius"></a><a href="http://help.openstreetmap.org/users/11465/elerius">@Elerius</a>: the background tiles are in fact the same which you see as default map on osm.org, right. But waymarkedtrails.org overlays the hiking routes (which have been extracted from OSM data, of course and as <a href="http://hiking.waymarkedtrails.org/en/help/about">mentioned on the site</a> and in the copyright map header). This is the power of the open OSM data - everybody can build maps and services based on the raw data to enhance some specific view. Having only one map which shows everything in a way best for hikers, boat drivers, HGV drivers, … would be impossible.</p>
<p>Yes, you are doing it right. Compare with <span>other</span> hiking routes, e.g. <span>this</span> one (randomly selected by me).</p>
<p>Cycle maps likely will not render hiking routes as that is out of scope for them. If you just like the OpenCycleMap as background with your hiking routes, check <a href="http://www.gpsies.com/createTrack.do">gpsies.com</a>, select the OpenCycleMap as background and select the "waymarked trails" as overlay.</p>
</div>
<div id="comment-45255-info" class="comment-info">
<span class="comment-age">(15 Sep '15, 19:39)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-45244" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45244-form-container" class="comment-form-container">
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

