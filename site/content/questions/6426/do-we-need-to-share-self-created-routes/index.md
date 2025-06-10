+++
type = "question"
title = "Do we need to share self-created routes?"
description = '''We are doing a mobile navigation app with the following features:  based on locally stored (offline) OSM-maps live routing based on GPS data predefined routes possibility for the user to create routes and navigate on them  The self-defined routes are created by ourselves independently from OSM data....'''
date = "2011-07-19T11:27:00Z"
lastmod = "2011-07-19T12:30:00Z"
weight = 6426
keywords = [ "route", "legal" ]
aliases = [ "/questions/6426" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Do we need to share self-created routes?](/questions/6426/do-we-need-to-share-self-created-routes)

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
<span id="post-6426-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6426-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-6426-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We are doing a mobile navigation app with the following features:</p>
<ul>
<li>based on locally stored (offline) OSM-maps</li>
<li>live routing based on GPS data</li>
<li>predefined routes</li>
<li>possibility for the user to create routes and navigate on them</li>
</ul>
<p>The self-defined routes are created by ourselves independently from OSM data. Do we need to share this route data if it's kept in separate files and drawn as overlay?</p>
<p>Is it relevant if the route data consists only of geo-coordinates or if we also pre-process it before distribution to link to OSM data (in order to make the app faster and development easier)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-legal" rel="tag" title="see questions tagged &#39;legal&#39;">legal</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jul '11, 11:27</strong></p>
<img src="https://secure.gravatar.com/avatar/4f49e8480ae1b687c02ca0b7f4de12c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="didi_X3&#39;s gravatar image" />
<p><span>didi_X3</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="didi_X3 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jul '11, 11:53</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></p>
</div>
</div>
<div id="comments-container-6426" class="comments-container">
&#10;</div>
<div id="comment-tools-6426" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6426-form-container" class="comment-form-container">
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

<span id="6427"></span>

<div id="answer-container-6427" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6427-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6427-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-6427-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I Am Not A Lawyer, but:</p>
<p>The crucial question is: Are you adding to or modifying the OpenStreetMap data in some way? If not, then there's actually nothing to share, since all you're doing is using the existing data. Only if you're combining the OSM data with another source (perhaps a database of GPS traces, showing streets that aren't in OSM) to produce your routing mesh do you trigger the share-alike provisions of the licence.</p>
<p>Also bear in mind that the main OSM database only stores data that can be verified by independent mappers in some way, so your routes probably aren't suitable for inclusion anyway.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jul '11, 11:35</strong></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonathan Bennett has 21 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-6427" class="comments-container">
&#10;</div>
<div id="comment-tools-6427" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6427-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="6430"></span>

<div id="answer-container-6430" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6430-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6430-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-6430-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you are creating the routes without any OSM data then the routes does not have to be licenced under OSM terms. Even when displaying the routes on top of OSM data it is still a seperate dataset.</p>
<p>In addition it seems that the data is only for private use. Copyright laws states that you can use and modify data for private use. That means that you can use any data source as long as you only use it in private and don't distribute it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jul '11, 12:30</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-6430" class="comments-container">
&#10;</div>
<div id="comment-tools-6430" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6430-form-container" class="comment-form-container">
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

