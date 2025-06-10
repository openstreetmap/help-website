+++
type = "question"
title = "adding elevation data to existing routes - conflation"
description = '''I would like to add elevation data to existing routes in OSM. The data is quite detailed--I&#x27;ll be adding a new node for each 20cm change in elevation. What would be the best way to do this? Should I try to add new nodes to existing routes? If I add an entire route, will it be properly conflated with...'''
date = "2011-12-29T15:16:00Z"
lastmod = "2012-01-07T03:06:00Z"
weight = 9681
keywords = [ "route", "elevation", "conflate" ]
aliases = [ "/questions/9681" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [adding elevation data to existing routes - conflation](/questions/9681/adding-elevation-data-to-existing-routes-conflation)

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
<span id="post-9681-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9681-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-9681-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to add elevation data to existing routes in OSM. The data is quite detailed--I'll be adding a new node for each 20cm change in elevation. What would be the best way to do this? Should I try to add new nodes to existing routes? If I add an entire route, will it be properly conflated with existing data?</p>
<p>Thanks,</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-elevation" rel="tag" title="see questions tagged &#39;elevation&#39;">elevation</span> <span class="post-tag tag-link-conflate" rel="tag" title="see questions tagged &#39;conflate&#39;">conflate</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Dec '11, 15:16</strong></p>
<img src="https://secure.gravatar.com/avatar/eeac8dea6b1172adb2a029817f0178b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mike80439&#39;s gravatar image" />
<p><span>mike80439</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mike80439 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9681" class="comments-container">
<span id="9832"></span>
<div id="comment-9832" class="comment">
<div id="post-9832-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think you need to supply more information. so we can answer this better. e.g. what kind of data, and why do you want to do it?</p>
</div>
<div id="comment-9832-info" class="comment-info">
<span class="comment-age">(07 Jan '12, 01:01)</span> <span class="comment-user userinfo">emj</span>
</div>
</div>
</div>
<div id="comment-tools-9681" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9681-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="9682"></span>

<div id="answer-container-9682" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9682-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9682-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-9682-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please don't. We do not collect elevation data in OpenStreetMap, for a variety of reasons.</p>
<p>One of these reasons is that elevation data is inherently raster data - with measurements occuring at certain intervals, and with reference to a fixed latitude/longitude grid. If you were to attach elevation information to individual nodes of a geometry in OSM, then nobody could move that geometry about without also altering your elevation data. Our editors don't support that.</p>
<p>The proper way to deal with elevation is to keep a separate database with elevation data, and then reference a route from OSM with matching elevation data from this second source. This is routinely done with SRTM elevation data but there's no reason why it cannot be done with other sources of elevation information. OpenStreetMap is not suitable as an elevation database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Dec '11, 15:33</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-9682" class="comments-container">
<span id="9687"></span>
<div id="comment-9687" class="comment">
<div id="post-9687-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>May I respectfully disagree.</p>
<p>While F. Ramm is perhaps the most active user here, and me the least, I truly believe there ARE needs for elevation data (keys?), and the argument according to which "moving a geometry will alter elevation" is definitely light to me. We don't displace geometries everyday everywhere, we rather bring minute corrections. And potentially "our editors" could be made to just kill an elevation if the point is moved without reconfirming it: "editors are not OSM" ;-)</p>
<p>I'd suggest proposing this feature (duly prepared) in <a href="http://wiki.openstreetmap.org/wiki/Proposed_features">http://wiki.openstreetmap.org/wiki/Proposed_features</a></p>
</div>
<div id="comment-9687-info" class="comment-info">
<span class="comment-age">(29 Dec '11, 18:28)</span> <span class="comment-user userinfo">Herve5</span>
</div>
</div>
<span id="9688"></span>
<div id="comment-9688" class="comment">
<div id="post-9688-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Herve5, I'm not saying that there are non needs for elevation data. It is certainly useful - just OSM is not the right medium, at least not for capturing DEM type of data. There's of course nothing to say against spot heights for mountain tops or passes, or specifying the height of a building or a tower; but trying to capture the altitude profile of a route by adding tags to its supporting nodes is just wrong on so many levels.</p>
</div>
<div id="comment-9688-info" class="comment-info">
<span class="comment-age">(29 Dec '11, 18:32)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="9732"></span>
<div id="comment-9732" class="comment">
<div id="post-9732-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Take a look at the cyclemap: <a href="http://www.openstreetmap.org/?lat=53.4172&amp;lon=-1.9053&amp;zoom=13&amp;layers=C">http://www.openstreetmap.org/?lat=53.4172&amp;lon=-1.9053&amp;zoom=13&amp;layers=C</a> The elevation data is not stored in OSM - it is better to store it elsewhere and superimpose it as shown here. This is also used on GPS devices like this too. To maintain data in 3D (with elevation) adds a huge amount of work that is not needed. GPS receivers have large vertical error.</p>
</div>
<div id="comment-9732-info" class="comment-info">
<span class="comment-age">(01 Jan '12, 20:16)</span> <span class="comment-user userinfo">ChrisH</span>
</div>
</div>
<span id="9733"></span>
<div id="comment-9733" class="comment">
<div id="post-9733-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks ChrisH. I recognize "&amp;layers=C" indeed already shows elevations, although at the cost of almost everything else (buildings, streams...)</p>
<p>Hervé</p>
</div>
<div id="comment-9733-info" class="comment-info">
<span class="comment-age">(01 Jan '12, 21:15)</span> <span class="comment-user userinfo">Herve5</span>
</div>
</div>
<span id="9734"></span>
<div id="comment-9734" class="comment">
<div id="post-9734-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>That, like all of the maps on the OSM site, are just examples of what is possible. My point is that the elevation can be added to <em>any</em> map render without holding the elevation data in OSM as you suggest we need.</p>
</div>
<div id="comment-9734-info" class="comment-info">
<span class="comment-age">(01 Jan '12, 21:53)</span> <span class="comment-user userinfo">ChrisH</span>
</div>
</div>
<span id="9834"></span>
<div id="comment-9834" class="comment not_top_scorer">
<div id="post-9834-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There is working code to combine altitude data from a separate database (eg SRTM) with a route from OSM here: <a href="http://wiki.openstreetmap.org/wiki/Route_altitude_profiles_SRTM">http://wiki.openstreetmap.org/wiki/Route_altitude_profiles_SRTM</a> (this was a Google Summer of Code project years ago). I believe this had at one point been integrated into <a href="http://yournavigation.org">yournavigation.org</a> but I cannot find it on their site now. Also, folks at <a href="http://openseamap.org">openseamap.org</a> are working on something that will allow them to crowd-source the measuring of sea depths; if that turns out to work well it could conceivably be used as the basis for a crowd-sourced DEM as well.</p>
</div>
<div id="comment-9834-info" class="comment-info">
<span class="comment-age">(07 Jan '12, 03:06)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-9682" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-9682-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9830"></span>

<div id="answer-container-9830" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9830-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9830-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9830-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Work on <a href="http://www.opendem.info/">opendem.info</a>, but from reading what you want to do I would recommend:</p>
<ol>
<li>publish and link to the dataset that gives you these elevation data.</li>
<li>make tools available to extract height profiles for ways in osm.</li>
<li>document it, and write an article so other people can do it.</li>
</ol>
<p>Bringing elevation into the core of OSM is a possibility but because it is not compatible with the current data model, it will require modifications to the way OSM works at the moment. This is considerably more work than simply importing a batch of elevation tags which would likely be removed again.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jan '12, 00:56</strong></p>
<img src="https://secure.gravatar.com/avatar/dd3858f5f89f5a6b738f9dbe59824440?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emj&#39;s gravatar image" />
<p><span>emj</span><br />
<span class="score" title="2024 reputation points"><span>2.0k</span></span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emj has 11 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Jan '12, 02:58</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-9830" class="comments-container">
&#10;</div>
<div id="comment-tools-9830" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9830-form-container" class="comment-form-container">
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

