+++
type = "question"
title = "Is there a way to fix a mis-ordered polyline?"
description = '''I&#x27;ve extracted a number of streets out of OpenStreetMap. I&#x27;ve found that some streets are great to work with, and others cannot be displayed in a polyline format because their coordinates are out of order. Here&#x27;s an example of a good street:  The line (on the left, obviously) matches the coordinates...'''
date = "2015-10-31T00:25:00Z"
lastmod = "2015-10-31T20:28:00Z"
weight = 46261
keywords = [ "nodes", "polyline", "order" ]
aliases = [ "/questions/46261" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Is there a way to fix a mis-ordered polyline?](/questions/46261/is-there-a-way-to-fix-a-mis-ordered-polyline)

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
<span id="post-46261-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46261-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46261-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've extracted a number of streets out of OpenStreetMap. I've found that some streets are great to work with, and others cannot be displayed in a polyline format because their coordinates are out of order.</p>
<p>Here's an example of a good street: <img src="http://i.imgur.com/bGnWG6S.jpg" alt="good street" /></p>
<p>The line (on the left, obviously) matches the coordinates (on the right), and looks the way you'd expect it to.</p>
<p>Here's an example of a bad street: <img src="http://i.imgur.com/OGwqOlG.jpg" alt="bad street" /></p>
<p>The coordinates (on the bottom left) seem just fine, but once I try to make a polyline out of them (top right) things go crazy.</p>
<p>I think it's because the coordinates (the node entries, from OpenStreetMap) are out of order.</p>
<p>Is this a common issue? Is there a way to correct it?</p>
<p>(The imgur link for the image set is <a href="http://imgur.com/a/dvD3M">http://imgur.com/a/dvD3M</a> - I'm not sure if the individual image links used above will ever change.)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-polyline" rel="tag" title="see questions tagged &#39;polyline&#39;">polyline</span> <span class="post-tag tag-link-order" rel="tag" title="see questions tagged &#39;order&#39;">order</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Oct '15, 00:25</strong></p>
<img src="https://secure.gravatar.com/avatar/0ada7b97d85873855231744286452af4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesChevalier&#39;s gravatar image" />
<p><span>JamesChevalier</span><br />
<span class="score" title="151 reputation points">151</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesChevalier has one accepted answer">25%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Oct '15, 00:34</strong> </span></p>
</div>
</div>
<div id="comments-container-46261" class="comments-container">
&#10;</div>
<div id="comment-tools-46261" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46261-form-container" class="comment-form-container">
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

<span id="46264"></span>

<div id="answer-container-46264" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46264-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46264-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-46264-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JamesChevalier has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As user_5359 suggests, nodes are only ordered within each Openstreetmap way. Your lower image contains multiple ways starting with</p>
<p><a href="https://www.openstreetmap.org/way/8766694">https://www.openstreetmap.org/way/8766694</a> in the north, then</p>
<p><a href="https://www.openstreetmap.org/way/8767452">https://www.openstreetmap.org/way/8767452</a></p>
<p><a href="https://www.openstreetmap.org/way/101458166">https://www.openstreetmap.org/way/101458166</a></p>
<p><a href="https://www.openstreetmap.org/way/101458163">https://www.openstreetmap.org/way/101458163</a></p>
<p><a href="https://www.openstreetmap.org/way/8768186">https://www.openstreetmap.org/way/8768186</a></p>
<p>after which it gets a bit more complicated as there are dual carriageway sections with one way in each direction (both of which join to that last way I mentioned).</p>
<p><a href="https://www.openstreetmap.org/way/8767828">https://www.openstreetmap.org/way/8767828</a></p>
<p><a href="https://www.openstreetmap.org/way/33824767">https://www.openstreetmap.org/way/33824767</a></p>
<p>If you are trying to draw a route you will need to select the ways that are needed depending on direction of travel, in the correct order, and depending which way the way nodes are ordered you may need to reverse the list for individual ways. In the above example if you were heading north from the one way section you might also want to exclude the section of way 8768186 that you wouldn't travel on when you turn left onto it (most routers pre-process the data I believe).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Oct '15, 07:50</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Oct '15, 07:50</strong> </span></p>
</div>
</div>
<div id="comments-container-46264" class="comments-container">
<span id="46275"></span>
<div id="comment-46275" class="comment">
<div id="post-46275-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That's the problem! I imported all the individual ways into my database as one one single street object. That works perfectly for my underlying use case, but really jams things up when I try to display them on a map. I kept the OSM ID for each node ... I wonder if there's a way for me to piece together the separate sections with that data ...</p>
</div>
<div id="comment-46275-info" class="comment-info">
<span class="comment-age">(31 Oct '15, 20:10)</span> <span class="comment-user userinfo">JamesChevalier</span>
</div>
</div>
<span id="46276"></span>
<div id="comment-46276" class="comment">
<div id="post-46276-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You really have to reassemble street objects from OSM ways: you cant just treat them as a multilinestring. They need to be manipulated as a graph (which is what most routing software does).</p>
</div>
<div id="comment-46276-info" class="comment-info">
<span class="comment-age">(31 Oct '15, 20:28)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-46264" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46264-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="46263"></span>

<div id="answer-container-46263" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46263-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46263-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-46263-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Is that really just one OSM way? The nodes are sorted only within an OSM way. Can you tell us the OSM Way ID, please?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Oct '15, 04:16</strong></p>
<img src="https://secure.gravatar.com/avatar/2608aa8e00ed6db4f5d8090f8983fbb8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="user_5359&#39;s gravatar image" />
<p><span>user_5359</span><br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="user_5359 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-46263" class="comments-container">
&#10;</div>
<div id="comment-tools-46263" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46263-form-container" class="comment-form-container">
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

