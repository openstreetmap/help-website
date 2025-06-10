+++
type = "question"
title = "Is there an OSM-based router on the web that can be used to replicate a car navigation issue attributed to OSM?"
description = '''A Tesla driver reports the following issue:  When I tried to Navigate to Dave &amp;amp; Busters which is directly under I805, it declared &quot;you have reached your destination&quot; on I805, some 100ft up above the actual destination.  His route was   from CA 92128 to Dave &amp;amp; Busters 2931 Camino Del Rio N, S...'''
date = "2018-05-25T00:50:00Z"
lastmod = "2018-05-25T01:39:00Z"
weight = 63721
keywords = [ "tesla", "navigation", "valhalla", "mapbox" ]
aliases = [ "/questions/63721" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Is there an OSM-based router on the web that can be used to replicate a car navigation issue attributed to OSM?](/questions/63721/is-there-an-osm-based-router-on-the-web-that-can-be-used-to-replicate-a-car-navigation-issue-attributed-to-osm)

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
<span id="post-63721-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63721-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-63721-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A Tesla driver reports the following issue:</p>
<blockquote>
<p>When I tried to Navigate to Dave &amp; Busters which is directly under I805, it declared "you have reached your destination" on I805, some 100ft up above the actual destination.</p>
</blockquote>
<p>His route was</p>
<blockquote>
<p>from CA 92128 to Dave &amp; Busters 2931 Camino Del Rio N, San Diego, CA 92108</p>
</blockquote>
<p>Tesla is rumored to be using OSM (via MapBox and Valhalla) for in-car routing since April 2018.</p>
<p>Where can I go (other than into a Tesla) to simulate this route knowing that it will be based on OSM/MapBox/Valhalla?</p>
<p>I tried <a href="https://www.tesla.com/trips,">https://www.tesla.com/trips,</a> but it is apparently based on Google, and the routing was precise. The Dave &amp; Busters the user wanted to go to is mapped on Google. It is not mapped on OSM.</p>
<p>I am trying to construct (and demonstarte) a scenario, of which OSM is part, where a POI does not exist, yet it is somehow found (from an external POI database? by address? street number extrapolation?) and is mapped to the GPS coordinates but without regard for the elevation.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tesla" rel="tag" title="see questions tagged &#39;tesla&#39;">tesla</span> <span class="post-tag tag-link-navigation" rel="tag" title="see questions tagged &#39;navigation&#39;">navigation</span> <span class="post-tag tag-link-valhalla" rel="tag" title="see questions tagged &#39;valhalla&#39;">valhalla</span> <span class="post-tag tag-link-mapbox" rel="tag" title="see questions tagged &#39;mapbox&#39;">mapbox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 May '18, 00:50</strong></p>
<img src="https://secure.gravatar.com/avatar/c23c2891306229bb036de7ce63bb8c9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ponzu&#39;s gravatar image" />
<p><span>ponzu</span><br />
<span class="score" title="2104 reputation points"><span>2.1k</span></span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ponzu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63721" class="comments-container">
&#10;</div>
<div id="comment-tools-63721" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63721-form-container" class="comment-form-container">
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

<span id="63722"></span>

<div id="answer-container-63722" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63722-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63722-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-63722-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ponzu has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can click the doubled arrow button on the upper left of <a href="https://www.openstreetmap.org/">https://www.openstreetmap.org/</a> to experiment with routers using OSM data. I don't know of a public Valhalla instance.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 May '18, 01:08</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-63722" class="comments-container">
<span id="63725"></span>
<div id="comment-63725" class="comment">
<div id="post-63725-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, can't reproduce the issue navigating by endpoint address, because, naturally, it leads to the correct street. You answered my original question, but the real question for me is, how can the described issue be possible? Since the POI he wanted is not on OSM, it had to come from a third party. I doubt most POIs have altitude coordinate. If the lat and lon placed it under the freeway, then the nav software, whether using OSM or not, would be tempted to navigate to the largest nearest road, i.e., the freeway. Does that sound about right? I don't see how OSM can be blamed -- or for that matter, used to fix the issue. Other than by adding the POI. And that's IF Tesla is really using OSM, which is a big "if".</p>
</div>
<div id="comment-63725-info" class="comment-info">
<span class="comment-age">(25 May '18, 01:39)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
</div>
<div id="comment-tools-63722" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63722-form-container" class="comment-form-container">
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

