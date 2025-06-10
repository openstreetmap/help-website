+++
type = "question"
title = "Guidelines for selecting a road network according to a mode of transport"
description = '''Dear all, I&#x27;m developing an R package named osmextract to import OSM data using OSM extracts that are stored by external providers (such as Geofabrik).  I&#x27;m trying to code a new function that can be used to import a set of ways representing a spatial network according to a specific mode of transport...'''
date = "2021-07-09T09:34:00Z"
lastmod = "2021-07-13T08:42:00Z"
weight = 80893
keywords = [ "walking", "cycling", "network", "driving" ]
aliases = [ "/questions/80893" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Guidelines for selecting a road network according to a mode of transport](/questions/80893/guidelines-for-selecting-a-road-network-according-to-a-mode-of-transport)

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
<span id="post-80893-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80893-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80893-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear all, I'm developing an <a href="https://www.r-project.org/">R</a> package named <a href="https://github.com/ropensci/osmextract">osmextract</a> to import OSM data using OSM extracts that are stored by external providers (such as <a href="https://www.geofabrik.de/">Geofabrik</a>).</p>
<p>I'm trying to code a new function that can be used to import a set of <em>ways</em> representing a spatial network according to a specific mode of transport (i.e. <em>walking</em>, <em>cycling</em>, or <em>driving</em>) and I was wondering if there are official guidelines on how to select those roads. For example, if I'd like to import a set of ways according to a cycling mode of transport, I would exclude <em>highway = motorway</em> or <em>highway = footway</em>, but I was wondering if there are official and standardised guidelines.</p>
<p>Thanks for your help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-walking" rel="tag" title="see questions tagged &#39;walking&#39;">walking</span> <span class="post-tag tag-link-cycling" rel="tag" title="see questions tagged &#39;cycling&#39;">cycling</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span> <span class="post-tag tag-link-driving" rel="tag" title="see questions tagged &#39;driving&#39;">driving</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jul '21, 09:34</strong></p>
<img src="https://secure.gravatar.com/avatar/fbb9e8e1458481e288aeba64a5639a6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="agila5&#39;s gravatar image" />
<p><span>agila5</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="agila5 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80893" class="comments-container">
&#10;</div>
<div id="comment-tools-80893" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80893-form-container" class="comment-form-container">
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

<span id="80897"></span>

<div id="answer-container-80897" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80897-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80897-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-80897-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="agila5 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi.</p>
<p>You probably want to read this <a href="https://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Access_restrictions">page</a> and others in the same category.</p>
<p>The gist of it is that the type of road does not necessarily define what kind of vehicules may pass, the access tags do.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jul '21, 11:03</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-80897" class="comments-container">
<span id="80941"></span>
<div id="comment-80941" class="comment">
<div id="post-80941-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much.</p>
</div>
<div id="comment-80941-info" class="comment-info">
<span class="comment-age">(13 Jul '21, 08:42)</span> <span class="comment-user userinfo">agila5</span>
</div>
</div>
</div>
<div id="comment-tools-80897" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80897-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="80902"></span>

<div id="answer-container-80902" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80902-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80902-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80902-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In addition to what H_mlet shared you should probably also have a look around what other routing engines assume. Some things are not so obvious. For example cyclists could still use footways/stairs if they push the bike. Or you might want to disregard the tagged access restriction if an official bike/walking route is following a path. Or you want to make the routabilitiy dependent on the surface.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jul '21, 14:36</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-80902" class="comments-container">
&#10;</div>
<div id="comment-tools-80902" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80902-form-container" class="comment-form-container">
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

