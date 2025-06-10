+++
type = "question"
title = "Best programmatic solution to push changesets from local PostGIS OSM replicant"
description = '''I&#x27;m setting up a server to replicate a small subset of the OSM database (amenities in the United Kingdom tagged as &quot;place of worship&quot;) which will be stored on a cartoDB instance (PostGIS database) and updated on an hourly basis. From what I can tell current best practice for this is to use osmosis t...'''
date = "2017-01-11T18:08:00Z"
lastmod = "2017-01-11T19:20:00Z"
weight = 53986
keywords = [ "osmosis", "postgis", "poi" ]
aliases = [ "/questions/53986" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Best programmatic solution to push changesets from local PostGIS OSM replicant](/questions/53986/best-programmatic-solution-to-push-changesets-from-local-postgis-osm-replicant)

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
<span id="post-53986-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53986-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53986-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm setting up a server to replicate a small subset of the OSM database (amenities in the United Kingdom tagged as "place of worship") which will be stored on a cartoDB instance (PostGIS database) and updated on an hourly basis. From what I can tell current best practice for this is to use osmosis to filter out a subset of the planet.osm databse. This all seems straight-forward and well documented, and this brings me to my question. The current data in OSM is pretty messy and incomplete, and I have already generated a nearly complete set of data. So I'd like to merge in a bulk changeset on these POIs (around 25,000 points) to OSM and then continue to push smaller changesets as metadata is updated on the local server periodically as well. Can someone recommend the best practice for push rather than pull interaction with OSM?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jan '17, 18:08</strong></p>
<img src="https://secure.gravatar.com/avatar/802a09b11098c939c866273db5352db9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kidwellj&#39;s gravatar image" />
<p><span>kidwellj</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kidwellj has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53986" class="comments-container">
&#10;</div>
<div id="comment-tools-53986" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53986-form-container" class="comment-form-container">
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

<span id="53987"></span>

<div id="answer-container-53987" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53987-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53987-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53987-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kidwellj has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>JOSM has the option of reading shape files and converting them to OSM data, and there's also a number of shp2osm-style programs around, but none of these techniques actually allows updating existing objects. Doing so will require, among other things, conflict resolution for cases where the object has been edited in the mean time. You might want to check out the codebase of "POSM" here <a href="https://github.com/AmericanRedCross/posm">https://github.com/AmericanRedCross/posm</a> which has the aim of allowing offline edits and loading them into OSM later; perhaps there's something you can re-use.</p>
<p>Having said that: You write that you have "generated" a nearly complete set of data. If this involves (a) the automatic conversion/use of third-party data sources and/or (b) the query-based or rule-based editing of OSM objects (e.g. search+replace operations on names, geometric operations like merging tags from nodes to ways or vice versa, removal of duplicates, etc.etc.), then you must follow the appropriate policies for imports and/or mechanical edits. The most important point of both these policies is that you must discuss your import/edit with the community before you act, and you must explain what rules you've applied to what data. If you simply stuff the results of some computation into OSM then your edits will be reverted. The same is true if you plan to continually apply automatic edits - seek community agreement before you act. The reason we have these policies is that a lot can go wrong, even if people think they know what they're doing.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jan '17, 18:56</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-53987" class="comments-container">
<span id="53989"></span>
<div id="comment-53989" class="comment">
<div id="post-53989-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for pointing this out. I've been reading the policy (<a href="http://wiki.openstreetmap.org/wiki/Import/Guidelines)">http://wiki.openstreetmap.org/wiki/Import/Guidelines)</a> in-depth and plan definitely to work through the human/consensus aspect before flipping the switch. I've already begun conversations regarding tagging etc. and plan to get input and consensus along the way, with a wiki page for the import process in draft. Just out of curiosity, have you worked with osmsync (<a href="http://wiki.openstreetmap.org/wiki/Osmsync)?">http://wiki.openstreetmap.org/wiki/Osmsync)?</a> And hadn't thought of POSM. I'll add that to my list!</p>
</div>
<div id="comment-53989-info" class="comment-info">
<span class="comment-age">(11 Jan '17, 19:20)</span> <span class="comment-user userinfo">kidwellj</span>
</div>
</div>
</div>
<div id="comment-tools-53987" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53987-form-container" class="comment-form-container">
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

