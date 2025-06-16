+++
type = "question"
title = "Navigation System Guidance"
description = '''Hi all, I&#x27;m creating an indoor navigation to help staff/student around, and to locate me, I shall be using QR Code to find where the person is. This is for my thesis, and I just came across JOSM recently and was intrigued should I use JOSM over my intention of developing this application. Here are s...'''
date = "2015-02-12T21:34:00Z"
lastmod = "2015-02-13T12:30:00Z"
weight = 40983
keywords = [ "josm" ]
aliases = [ "/questions/40983" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Navigation System Guidance](/questions/40983/navigation-system-guidance)

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
<span id="post-40983-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40983-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40983-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all, I'm creating an indoor navigation to help staff/student around, and to locate me, I shall be using QR Code to find where the person is. This is for my thesis, and I just came across JOSM recently and was intrigued should I use JOSM over my intention of developing this application.</p>
<p>Here are some info in what I intend to do without using JOSM.</p>
<ol>
<li>I intend to create my application using Eclipse or Android Studio.</li>
<li>Use A* algorithm which will find the shortest nodes to find the location - I learnt this in school and thought it would be a good idea to use this.</li>
<li>Design the UI under Eclipse or Android Studio</li>
<li>Create the floor plan and save it as PNG</li>
<li>Code and implement</li>
<li>Testing</li>
<li>Finish</li>
</ol>
<p>I was thinking should follow my method of making the application or use JOSM?</p>
<p>Any idea to help me conclude on what i should go for would be appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Feb '15, 21:34</strong></p>
<img src="https://secure.gravatar.com/avatar/ade7383bf4223cacbc42cf917e5526a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ZerkaMaximus&#39;s gravatar image" />
<p><span>ZerkaMaximus</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ZerkaMaximus has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Feb '15, 21:34</strong> </span></p>
</div>
</div>
<div id="comments-container-40983" class="comments-container">
&#10;</div>
<div id="comment-tools-40983" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40983-form-container" class="comment-form-container">
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

<span id="40991"></span>

<div id="answer-container-40991" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40991-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40991-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-40991-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are aware that JOSM is mainly an offline editor for OSM data?</p>
<p>So you want to use its sourcecode as a frame for your app? You can try it by stripping off all features you don't need. You can edit the map paint style by JOSM via <a href="https://wiki.openstreetmap.org/wiki/MapCSS">MapCSS</a>.</p>
<p>See also <a href="https://wiki.openstreetmap.org/wiki/Routing">Routing</a> in general to find opensource projects.</p>
<p>But why not trying other Java opensource software like listed in the OSM wiki at <a href="https://wiki.openstreetmap.org/wiki/Category:Java">Category:Java</a> ...?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Feb '15, 12:30</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-40991" class="comments-container">
&#10;</div>
<div id="comment-tools-40991" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40991-form-container" class="comment-form-container">
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

