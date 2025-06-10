+++
type = "question"
title = "How to tag map location markers or signs"
description = '''I&#x27;m mapping some local nordic trails following the guidelines for Piste Maps but I can&#x27;t find conclusive info on how to mark certain trail signs. They&#x27;re large numeric signs that are used as reference points for paper maps. I realize that most folks using OSM data will be using a GPS device so they&#x27;...'''
date = "2020-11-16T19:09:00Z"
lastmod = "2020-11-17T19:55:00Z"
weight = 77574
keywords = [ "rendering", "information", "piste", "signs" ]
aliases = [ "/questions/77574" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to tag map location markers or signs](/questions/77574/how-to-tag-map-location-markers-or-signs)

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
<span id="post-77574-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77574-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77574-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm mapping some local nordic trails following the guidelines for <a href="https://wiki.openstreetmap.org/wiki/Piste_Maps">Piste Maps</a> but I can't find conclusive info on how to mark certain trail signs. They're large numeric signs that are used as reference points for paper maps.</p>
<p>I realize that most folks using OSM data will be using a GPS device so they're somewhat redundant but they do offer clear waypoints if you're traveling the path.</p>
<p>Here's a couple examples:</p>
<p><img src="https://help.openstreetmap.org/upfiles/2020-11-15_16-16-scweitzer-screencap_5iElWH7.png" alt="Schweitzer resort nordic trails" /></p>
<p><img src="https://help.openstreetmap.org/upfiles/2020-11-15_16-18-salt-creek-summit_LMWkWN0.png" alt="Salt creek summit nordic trails" /></p>
<p>Do you think they'd work better as:</p>
<p><code>information=trail_blaze name=1</code></p>
<p>Which seems a little understated. There are numerous blue diamond blazes along all these routes.</p>
<p><code>information=route_marker name=1</code></p>
<p>This seems a little clearer.</p>
<p><code>information=guidepost name=1</code></p>
<p>This seems to be designated for more elaborate signage with detailed information on it.</p>
<p><strong>Secondarily</strong>: would it be possible to get these to render on the maps? I looked at the details on <a href="https://hiking.waymarkedtrails.org/help/rendering/osmc">Waymarked Trails</a> about rendering OSMC symbols along a route. This seems popular in Europe but not so much in the states. This rendering convention would provide an easy way to render numeric indicators on the map if a node were tagged with it. e.g.</p>
<p><code>information=route_marker name=3 osmc:symbol=waycolor:blue:none:3:white</code></p>
<p>I'm not sure how to start the proposal process for something like that. Maybe I can email the owner of OpenSnowMap who seems to be doing a lot of the piste rendering work.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-information" rel="tag" title="see questions tagged &#39;information&#39;">information</span> <span class="post-tag tag-link-piste" rel="tag" title="see questions tagged &#39;piste&#39;">piste</span> <span class="post-tag tag-link-signs" rel="tag" title="see questions tagged &#39;signs&#39;">signs</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Nov '20, 19:09</strong></p>
<img src="https://secure.gravatar.com/avatar/2aaf1c277958d5834a5228268ae37f8a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="funwhilelost&#39;s gravatar image" />
<p><span>funwhilelost</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="funwhilelost has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-77574" class="comments-container">
&#10;</div>
<div id="comment-tools-77574" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77574-form-container" class="comment-form-container">
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

<span id="77576"></span>

<div id="answer-container-77576" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77576-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77576-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-77576-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="funwhilelost has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<h3 id="to-your-first-part">To your first part:</h3>
<p>Generally speaking for numbered/lettered points or routes, the <code>ref</code> tag is usually considered more appropriate than <code>name</code>. If the sign contains the reference for the junction, then the junction node should carry the ref tagged regardless of whether you decide to independently map the sign (as for roads carrying the <code>name=*</code> rather than the signpost). Some Norwegian mappers <a href="https://overpass-turbo.eu/s/10e7">seem</a> to be adding <code>ref</code>s to nodes that are part of skiing routes but as some are marked as <code>hiking=yes</code> but not <code>ski=yes</code> these may have other purposes. This tagging doesn't appear to have spread much outside the region.</p>
<p>Named road junctions are common in some parts of the world, so it may be possible to co-opt that <a href="https://wiki.openstreetmap.org/wiki/Named_spots_instead_of_street_names">tagging</a> here too. The system you describe reminds me of a Dutch/Belgian cycle network <a href="https://wiki.openstreetmap.org/wiki/Cycle_Node_Network_Tagging">variant</a> that has had dedicated tagging for quite a while now. As this type of tagging doesn't seem to be documented for ski routes it may be worth putting together a similar proposal if they're fairly common (or at least document what you decide on).</p>
<p>The guidepost tag is normally used for posts with multiple signs with arrows pointing in several directions at an intersection. From your description it sounds like each junction in a route will have a single unique reference so this doesn't sound like the right tag unless that sign also identifies which branch is which.</p>
<p>For what it's worth <a href="http://www.opensnowmap.org/">OpenSnowMap</a> also seems to <a href="http://www.opensnowmap.org/iframes/how-to-eng.html%5D">recommend</a> the use of <a href="https://wiki.openstreetmap.org/wiki/Key:osmc:symbol">OSMC</a> symbols although that seems to be for the route as a whole.</p>
<h3 id="to-your-second-part">To your second part:</h3>
<p>The WikiProject Piste Maps <a href="https://wiki.openstreetmap.org/wiki/WikiProject_Piste_Maps">page</a> on the wik suggest <a href="http://www.opensnowmap.org/">OpenSnowMap</a> as a rendered slippy map and also links to <a href="https://openskimap.org/">OpenSkimap</a>. I know OsmAnd also has a Ski Map plugin (<a href="https://osmand.net/help-online/map-legend#ski">legend</a>), but I have never had cause to use either. All three of these projects are open source so if you establish some tagging and ask nicely on their GitHubs they might add this to their render.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Nov '20, 00:44</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</img>
</div>
</div>
<div id="comments-container-77576" class="comments-container">
<span id="77580"></span>
<div id="comment-77580" class="comment">
<div id="post-77580-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Absolutely stellar answer. Thank you.</p>
</div>
<div id="comment-77580-info" class="comment-info">
<span class="comment-age">(17 Nov '20, 19:55)</span> <span class="comment-user userinfo">funwhilelost</span>
</div>
</div>
</div>
<div id="comment-tools-77576" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77576-form-container" class="comment-form-container">
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

