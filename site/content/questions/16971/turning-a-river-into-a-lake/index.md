+++
type = "question"
title = "Turning a river into a lake"
description = '''A local river was dammed up in 1924, forming a man-made lake. The river no longer exists in this location as it is now at the bottom of the lake. For some reason, the river and lots of tributaries that haven&#x27;t existed in 88 years was in OSM. When viewing the map, it showed a river (and tributaries) ...'''
date = "2012-10-17T19:32:00Z"
lastmod = "2012-10-17T20:26:00Z"
weight = 16971
keywords = [ "river", "shoreline", "lake" ]
aliases = [ "/questions/16971" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Turning a river into a lake](/questions/16971/turning-a-river-into-a-lake)

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
<span id="post-16971-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16971-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-16971-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A local river was dammed up in 1924, forming a man-made lake. The river no longer exists in this location as it is now at the bottom of the lake. For some reason, the river and lots of tributaries that haven't existed in 88 years was in OSM. When viewing the map, it showed a river (and tributaries) flowing down the middle of this big lake, which is ridiculous. I've already removed all the way-out-of-date river ways from Potlatch2 so it doesn't display in the lake anymore. But I now see that while the large man-made lake shows up, no name is displayed anywhere.</p>
<p>How to handle this?</p>
<p>When I click on the lake shore line, a mile or so at a time will highlight. But that's just a line (a way?), not a closed shape. Let me back up a bit and explain that the lake shows up as blue on the OSM map but I can't find anything in Potlatch2 that would designate this as water in any way. Those lines that are the shore, show up as "not recognised". I could assign them as coastline but I'm assuming coastline is only for an ocean? Either way, since these separate ways (lines) are not connected into a closed shape, Lake is not even an option for me to choose (unless I force it in with the advanced details). So do I need to join all the miles and miles of lakeshore so that I can then create one big lake? And again, why is this showing up as blue on the map when in Potlatch2 it's just an undesignated shape between various lines?</p>
<p>If you need to look at the specific situation it is here: <a href="https://www.openstreetmap.org/?lat=35.09975&amp;lon=-81.03627&amp;zoom=15&amp;layers=M">https://www.openstreetmap.org/?lat=35.09975&amp;lon=-81.03627&amp;zoom=15&amp;layers=M</a> But I'm not asking anybody else to fix it - I just want to know a) what's going on here and b) how to fix it myself.</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-river" rel="tag" title="see questions tagged &#39;river&#39;">river</span> <span class="post-tag tag-link-shoreline" rel="tag" title="see questions tagged &#39;shoreline&#39;">shoreline</span> <span class="post-tag tag-link-lake" rel="tag" title="see questions tagged &#39;lake&#39;">lake</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Oct '12, 19:32</strong></p>
<img src="https://secure.gravatar.com/avatar/228a09e620f374c61a25e546d76bc6a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gopanthers&#39;s gravatar image" />
<p><span>gopanthers</span><br />
<span class="score" title="366 reputation points">366</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gopanthers has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16971" class="comments-container">
&#10;</div>
<div id="comment-tools-16971" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16971-form-container" class="comment-form-container">
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

<span id="16975"></span>

<div id="answer-container-16975" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16975-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16975-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-16975-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to read up on how relations work. Checkout: <a href="https://wiki.openstreetmap.org/wiki/Relation">https://wiki.openstreetmap.org/wiki/Relation</a></p>
<p>With your specific case, each of the segments along the shoreline are polygons that are members of a multipolygon relation. Using Potlatch2, click on one of the shoreline segments then click 'Advanced' at the bottom-left. You'll see the relation box containing 'multipolygon lake'. Double click on that and you'll get a popup window which allows you to view and edit the relation.</p>
<p>Regarding the missing name of the lake, my guess is that the relation is broken somehow which is stopping it from rendering on the main map. This could be because the segments don't form a closed circuit. Unfortunately that's the limit of Potlatch2. You will have to start playing with the more advanced JOSM tool to fix that one.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Oct '12, 20:06</strong></p>
<img src="https://secure.gravatar.com/avatar/7408fce5260e98922355385680be0179?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="porjo&#39;s gravatar image" />
<p><span>porjo</span><br />
<span class="score" title="183 reputation points">183</span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="porjo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Oct '12, 20:08</strong> </span></p>
</div>
</div>
<div id="comments-container-16975" class="comments-container">
<span id="16977"></span>
<div id="comment-16977" class="comment">
<div id="post-16977-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The relation is <a href="https://www.openstreetmap.org/browse/relation/299167">https://www.openstreetmap.org/browse/relation/299167</a> which also shows the source (NHD). The relation looks OK in JOSM. It might be that due to the shape of the lake it might be trying to place the label outside the water area, but that's only a guess. I thought I found the label for a minute, but it was the same feature from the gnis import <a href="https://www.openstreetmap.org/browse/node/357090944">https://www.openstreetmap.org/browse/node/357090944</a> - perhaps this is an example of why sometimes imports are frowned on. Ah! This might be it? <a href="http://osm.org/go/ZSlzTSF9i--?m">http://osm.org/go/ZSlzTSF9i--?m</a></p>
</div>
<div id="comment-16977-info" class="comment-info">
<span class="comment-age">(17 Oct '12, 20:26)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
</div>
<div id="comment-tools-16975" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16975-form-container" class="comment-form-container">
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

