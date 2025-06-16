+++
type = "question"
title = "Mapping philosophy"
description = '''I have had a cordial disagreeement with another mapper about the proper philosophy for tagging ways. When I encounter a fire road I tag it as a footway if there is a barrier that physically prevents vehicles from accessing it legally. The reason I do this is because I use OSM data extensively for ve...'''
date = "2012-05-29T21:23:00Z"
lastmod = "2012-05-30T08:45:00Z"
weight = 13090
keywords = [ "track", "tagging_ways", "fire_trails" ]
aliases = [ "/questions/13090" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Mapping philosophy](/questions/13090/mapping-philosophy)

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
<span id="post-13090-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13090-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13090-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have had a cordial disagreeement with another mapper about the proper philosophy for tagging ways. When I encounter a fire road I tag it as a footway if there is a barrier that physically prevents vehicles from accessing it legally. The reason I do this is because I use OSM data extensively for vehicle navigation and would not want to be directed onto a way that I could not use. The disagreeing mapper stated that I should tag it as a track if it is large enough to admit a vehicle, even if such navigation is prohibited and/or requires 4 wheel drive to access. Which is the generally accepted philosophy?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-track" rel="tag" title="see questions tagged &#39;track&#39;">track</span> <span class="post-tag tag-link-tagging_ways" rel="tag" title="see questions tagged &#39;tagging_ways&#39;">tagging_ways</span> <span class="post-tag tag-link-fire_trails" rel="tag" title="see questions tagged &#39;fire_trails&#39;">fire_trails</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 May '12, 21:23</strong></p>
<img src="https://secure.gravatar.com/avatar/fb0c3e65757bcd0489176eaba53bcc12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ras_oscar&#39;s gravatar image" />
<p><span>ras_oscar</span><br />
<span class="score" title="101 reputation points">101</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ras_oscar has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13090" class="comments-container">
<span id="13115"></span>
<div id="comment-13115" class="comment">
<div id="post-13115-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Related question: <a href="/questions/4817/how-to-tag-a-fire-department-controlled-gate">How to tag a fire department-controlled gate?</a></p>
<p>You probably want to use access=no , emergency=yes .</p>
</div>
<div id="comment-13115-info" class="comment-info">
<span class="comment-age">(30 May '12, 08:45)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
</div>
<div id="comment-tools-13090" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13090-form-container" class="comment-form-container">
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

<span id="13098"></span>

<div id="answer-container-13098" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13098-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13098-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-13098-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If it is something that I would normally map as a track, then I would map it as a track, add the barriers and add <a href="https://wiki.openstreetmap.org/wiki/Access">access</a> tags - maybe something like "access=no,foot=yes".</p>
<p>If your vehicle navigator still directs you into roads with access=no or access=private then your navigator is broken, but that should not be fixed by trying to map things as something else.</p>
<p>This sound like a variant of the golden rule "Don't map for the renderer".</p>
<p>One may also think about the case that someone could actually write a navigator for fire vehicles. If you have tagged your tracks as footways in order to fit your own needs in your broken navigator, then the navigator in the fire vehicle may get into problems navigating the fire roads.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 May '12, 22:46</strong></p>
<img src="https://secure.gravatar.com/avatar/c2a980da3fdfa1ee2659ad70d1e21f31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gnurk&#39;s gravatar image" />
<p><span>gnurk</span><br />
<span class="score" title="6114 reputation points"><span>6.1k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="silver">●</span><span class="badgecount">60</span></span><span title="96 badges"><span class="bronze">●</span><span class="badgecount">96</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gnurk has 18 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-13098" class="comments-container">
&#10;</div>
<div id="comment-tools-13098" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13098-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13099"></span>

<div id="answer-container-13099" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13099-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13099-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-13099-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In general, we'd like OSM data to closely depict the reality on the ground, for various, even "unexpected", uses.</p>
<p>We know for sure that emergency services in some parts of the world are already using OSM data - perhaps not relying on OSM exclusively but at least using it as an auxiliary source of information. So even if conventional vehicles aren't allowed, it would be better to tag the way so that a potential emergency services routing system could use it (e.g. by applying one of the <code>access</code> tags).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 May '12, 22:50</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-13099" class="comments-container">
<span id="13106"></span>
<div id="comment-13106" class="comment">
<div id="post-13106-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>ok. I understand. However, if I tag it as track and put barriers at the ends(which most closeley represents the ground truth) how would I differentiate between barriers can open for emergency vehicles with the proper key, as opposed to an immobile barrier such as a guard rail or large rocks? I have encountered both.</p>
</div>
<div id="comment-13106-info" class="comment-info">
<span class="comment-age">(30 May '12, 00:28)</span> <span class="comment-user userinfo">ras_oscar</span>
</div>
</div>
<span id="13108"></span>
<div id="comment-13108" class="comment">
<div id="post-13108-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You have a lot of barriers to chose from at <a href="https://wiki.openstreetmap.org/wiki/Key:barrier">https://wiki.openstreetmap.org/wiki/Key:barrier</a> and most of them implies access=no. But if you look at for example <a href="https://wiki.openstreetmap.org/wiki/Tag:barrier%3Dgate">https://wiki.openstreetmap.org/wiki/Tag:barrier%3Dgate</a> or <a href="https://wiki.openstreetmap.org/wiki/Tag:barrier%3Dlift_gate">https://wiki.openstreetmap.org/wiki/Tag:barrier%3Dlift_gate</a> you will see that the combination with the access tag is considered useful. So you could tag your locked barrier with something like "barrier=gate,access=private,foot=yes,bicycle=no" and the blocks maybe are something like "barrier=block,foot=yes,bicycle=yes".</p>
</div>
<div id="comment-13108-info" class="comment-info">
<span class="comment-age">(30 May '12, 00:48)</span> <span class="comment-user userinfo">gnurk</span>
</div>
</div>
</div>
<div id="comment-tools-13099" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13099-form-container" class="comment-form-container">
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

