+++
type = "question"
title = "drawing over traces"
description = '''when I draw a line over a trace or bing image I&#x27;m guessing that using too many segments wiil use up memory and slow down map on osm system and on a gps/pda/ smart phone. what is best advice from an expert note I&#x27;ve edited my question(02/02/11) to make it clearer '''
date = "2011-01-14T18:51:00Z"
lastmod = "2012-08-27T01:05:00Z"
weight = 2197
keywords = [ "nodes", "spacing", "drawing", "way", "memory" ]
aliases = [ "/questions/2197" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [drawing over traces](/questions/2197/drawing-over-traces)

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
<span id="post-2197-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2197-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-2197-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>when I draw a line over a trace or bing image I'm guessing that using too many segments wiil use up memory and slow down map on osm system and on a gps/pda/ smart phone. what is best advice from an expert note I've edited my question(02/02/11) to make it clearer</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-spacing" rel="tag" title="see questions tagged &#39;spacing&#39;">spacing</span> <span class="post-tag tag-link-drawing" rel="tag" title="see questions tagged &#39;drawing&#39;">drawing</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span> <span class="post-tag tag-link-memory" rel="tag" title="see questions tagged &#39;memory&#39;">memory</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Jan '11, 18:51</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> retagged <strong>26 Aug '12, 09:18</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/1fb9da36bbe8817c461df33d395ee413?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gerdami&#39;s gravatar image" />
<p><span>gerdami</span><br />
<span class="score" title="696 reputation points">696</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="46 badges"><span class="bronze">●</span><span class="badgecount">46</span></span></p>
</div>
</div>
<div id="comments-container-2197" class="comments-container">
&#10;</div>
<div id="comment-tools-2197" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2197-form-container" class="comment-form-container">
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

<span id="2201"></span>

<div id="answer-container-2201" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2201-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2201-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-2201-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="andy mackey has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is some advice about this on these pages, with example pictures: <a href="http://wiki.openstreetmap.org/wiki/Editing_Standards_and_Conventions#Accuracy">Editing Standards and conventions</a> and <a href="http://wiki.openstreetmap.org/wiki/Good_practice">Good practice</a></p>
<p>Basically, you should try to add enough nodes to make the curves look reasonably smooth. This means if you have a tight curve, the nodes will have to be closer together than they would on a wider curve. So you should avoid having close to right angles between nodes (unless there actually is a right angle on the road/path).</p>
<p>There is no fixed rules about how many nodes to use, you have to use some judgement for this. I think you should just try to make it fairly close to what is on the ground. I don't think you have to worry about the memory used unless you are adding hundreds of nodes for a short road.</p>
<p>Also remember GPS traces may be inaccurate, so make sure you are not drawing curves that are not actually there. Its helpful to average out several traces, as well as using aerial imagery where available.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jan '11, 19:26</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-2201" class="comments-container">
<span id="15537"></span>
<div id="comment-15537" class="comment">
<div id="post-15537-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Note that Vclaw gave this answer before Bing was available to OSM.</p>
</div>
<div id="comment-15537-info" class="comment-info">
<span class="comment-age">(27 Aug '12, 01:05)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-2201" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2201-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="15517"></span>

<div id="answer-container-15517" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15517-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15517-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-15517-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>May I add a plea for people not to follow Bing imagery to the exclusion of everything else. The georeferencing of the imagery is not quite exact, as can be shown by comparing the position of a mapped feature against the imagery at two different zoom levels. Certainly one GPS trace can sometimes be inaccurate, but often the average of many traces (not necessarily all your own) can be very accurate indeed.</p>
<p>Please note that I am not criticising Bing. I am more than ready to accept that photogrammetry is difficult.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Aug '12, 12:02</strong></p>
<img src="https://secure.gravatar.com/avatar/c81fd17cde8b2747629b78bdef81a202?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Madryn&#39;s gravatar image" />
<p><span>Madryn</span><br />
<span class="score" title="2241 reputation points"><span>2.2k</span></span><span title="36 badges"><span class="badge1">●</span><span class="badgecount">36</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Madryn has 5 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Aug '12, 12:36</strong> </span></p>
</div>
</div>
<div id="comments-container-15517" class="comments-container">
<span id="15536"></span>
<div id="comment-15536" class="comment">
<div id="post-15536-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When I asked this question Bing wasn't available for use in OSM. Now Bing is available it will give you the shape of roads BUT I would agree it should be checked for alignment with a SEVERAL GPX traces before doing any drawing from it. In Potlach2 you can drag the image into alignment by holding down the spacebar and left mouse button.</p>
</div>
<div id="comment-15536-info" class="comment-info">
<span class="comment-age">(27 Aug '12, 01:00)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-15517" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15517-form-container" class="comment-form-container">
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

