+++
type = "question"
title = "Should long roads, trails, paths be broken into segments so the label will appear multiple times along the path?"
description = '''I&#x27;m new to this so bear with me. Last night I fixed up a bunch of junctions to improve routing when using sites like bikeroutetoaster. Along the way I found some multi-use paths and trails that were segmented. In particular, the Mesa Trail in Boulder, CO is around 7 miles long and it was broken into...'''
date = "2011-05-17T17:29:00Z"
lastmod = "2011-05-17T18:35:00Z"
weight = 5249
keywords = [ "path", "labels", "long" ]
aliases = [ "/questions/5249" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Should long roads, trails, paths be broken into segments so the label will appear multiple times along the path?](/questions/5249/should-long-roads-trails-paths-be-broken-into-segments-so-the-label-will-appear-multiple-times-along-the-path)

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
<span id="post-5249-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5249-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-5249-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm new to this so bear with me.</p>
<p>Last night I fixed up a bunch of junctions to improve routing when using sites like bikeroutetoaster. Along the way I found some multi-use paths and trails that were segmented. In particular, the Mesa Trail in Boulder, CO is around 7 miles long and it was broken into multiple pieces. I joined the pieces back together into one 7-mile long trail, thinking that was the right thing to do. But now I wonder if that will limit the placement of labels and make it less clear which trail segments are actually the Mesa Trail (there are numerous side trails and connectors). Should I go back and split the trail at major junctions so it gets rendered with better labels?</p>
<p>For example, on the <a href="http://osm.org/go/T2JZIfSP--">southern section of the trail</a>, there is no "Mesa Trail" label between its junction with the Shanahan South Fork trail and the trailhead on Eldorado Springs Drive.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-path" rel="tag" title="see questions tagged &#39;path&#39;">path</span> <span class="post-tag tag-link-labels" rel="tag" title="see questions tagged &#39;labels&#39;">labels</span> <span class="post-tag tag-link-long" rel="tag" title="see questions tagged &#39;long&#39;">long</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 May '11, 17:29</strong></p>
<img src="https://secure.gravatar.com/avatar/43b0b1c21e5dbb5c170c2d6aa3eda055?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wallnut&#39;s gravatar image" />
<p><span>wallnut</span><br />
<span class="score" title="81 reputation points">81</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wallnut has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 May '11, 17:32</strong> </span></p>
</div>
</div>
<div id="comments-container-5249" class="comments-container">
&#10;</div>
<div id="comment-tools-5249" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5249-form-container" class="comment-form-container">
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

<span id="5251"></span>

<div id="answer-container-5251" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5251-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5251-score" class="post-score" title="current number of votes">
12
</div>
<span id="post-5251-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wallnut has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Different rendering systems have different behaviour when it comes to repeating the label down the length of a road, and they <em>will</em> repeat the label on long ways (or at least all good rendering software will do this) Unfortunately you can also influence behaviour by splitting a road into separate ways, in a manner which is otherwise unnecessary. <strong>You should not do this</strong>. It's bad practice.</p>
<p>We say "<a href="http://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">tagging for the renderer</a>" is bad, but that applies equally to other mapping decisions regarding the arrangement of ways and nodes. That doesn't mean you shouldn't give consideration to renderers, routing systems, and other uses, when entering data. It just means you shouldn't contort things to try to trick a renderer into behaving properly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 May '11, 17:59</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-5251" class="comments-container">
<span id="5254"></span>
<div id="comment-5254" class="comment">
<div id="post-5254-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the answer &amp; the link. I'll leave it alone.</p>
</div>
<div id="comment-5254-info" class="comment-info">
<span class="comment-age">(17 May '11, 18:32)</span> <span class="comment-user userinfo">wallnut</span>
</div>
</div>
</div>
<div id="comment-tools-5251" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5251-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5253"></span>

<div id="answer-container-5253" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5253-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5253-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-5253-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As Harry already has mentioned with other words, "Don't map for the renderers", and the number of labels may not depend on the number of segments in a road anyway. For example if you look at <a href="http://www.openstreetmap.org/">http://www.openstreetmap.org/</a> Osmarender tends to put one single or just a few names on a complicated road, while Mapnik puts more names one it, but both are using the same OSM database. (You switch map at the "+" in the upper right corner.)</p>
<p>A valid reason for breaking one road into multiple segments is that there are different speed limits, lighting, surface etc etc along the road. Another reason may be that a part of the road is used as a border for something, and they share the same segment.</p>
<p>There may also be other reasons to split a way into segments. See <a href="http://wiki.openstreetmap.org/wiki/FAQ#I_want_to_create_a_very_long_way_-_how_do_I_download_OSM_data_for_such_a_big_area.3F">I want to create a very long way - how do I download OSM data for such a big area?</a> in the FAQ.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 May '11, 18:20</strong></p>
<img src="https://secure.gravatar.com/avatar/c2a980da3fdfa1ee2659ad70d1e21f31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gnurk&#39;s gravatar image" />
<p><span>gnurk</span><br />
<span class="score" title="6114 reputation points"><span>6.1k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="silver">●</span><span class="badgecount">60</span></span><span title="96 badges"><span class="bronze">●</span><span class="badgecount">96</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gnurk has 18 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-5253" class="comments-container">
<span id="5255"></span>
<div id="comment-5255" class="comment">
<div id="post-5255-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks - that's a good list of exceptions. In this case I don't think any of them apply so I'll leave it as one big trail.</p>
</div>
<div id="comment-5255-info" class="comment-info">
<span class="comment-age">(17 May '11, 18:35)</span> <span class="comment-user userinfo">wallnut</span>
</div>
</div>
</div>
<div id="comment-tools-5253" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5253-form-container" class="comment-form-container">
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

