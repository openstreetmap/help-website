+++
type = "question"
title = "How to prune the .osm data?"
description = '''Hi all: I&#x27;m a newbie trying to do some analysis with the .osm data. My first task is to parse the xml into efficient data struture for later search algorithm. But noticably, there is pretty much noise in the raw data.(e.g. one road may have several &amp;lt;way&amp;gt; tags, some nodes in &amp;lt;way&amp;gt;&amp;lt;nd&amp;g...'''
date = "2011-10-17T02:18:00Z"
lastmod = "2014-10-08T13:08:00Z"
weight = 8476
keywords = [ ".osm", "pruning" ]
aliases = [ "/questions/8476" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to prune the .osm data?](/questions/8476/how-to-prune-the-osm-data)

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
<span id="post-8476-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8476-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8476-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all:</p>
<p>I'm a newbie trying to do some analysis with the .osm data.</p>
<p>My first task is to parse the xml into efficient data struture for later search algorithm.</p>
<p>But noticably, there is pretty much noise in the raw data.(e.g. one road may have several &lt;way&gt; tags, some nodes in &lt;way&gt;&lt;nd&gt; are redundant)</p>
<p>Just wondering if there is a standard way to prune the raw .osm data instead of hacking by myself?</p>
<p>Thanks for your help Best E</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-.osm" rel="tag" title="see questions tagged &#39;.osm&#39;">.osm</span> <span class="post-tag tag-link-pruning" rel="tag" title="see questions tagged &#39;pruning&#39;">pruning</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Oct '11, 02:18</strong></p>
<img src="https://secure.gravatar.com/avatar/a24fb83b1a0f9b1915be072d2c42762d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eminemya&#39;s gravatar image" />
<p><span>eminemya</span><br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eminemya has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Oct '14, 00:36</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-8476" class="comments-container">
&#10;</div>
<div id="comment-tools-8476" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8476-form-container" class="comment-form-container">
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

<span id="8478"></span>

<div id="answer-container-8478" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8478-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8478-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8478-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The "pruning" of data is highly specialised to the algorithm you are running, and most algorithms are capable of handeling "noise" in the data. Hence there are no standard way of "pruning" the data to fit any algoritm.</p>
<p>I would suggest you merge the ways based on the name/ref either on import or after you have applied the search algorithm. The later may be perfered if you want to update the date structure.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Oct '11, 07:29</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-8478" class="comments-container">
<span id="8482"></span>
<div id="comment-8482" class="comment">
<div id="post-8482-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your advice :)</p>
</div>
<div id="comment-8482-info" class="comment-info">
<span class="comment-age">(17 Oct '11, 14:23)</span> <span class="comment-user userinfo">eminemya</span>
</div>
</div>
</div>
<div id="comment-tools-8478" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8478-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="37423"></span>

<div id="answer-container-37423" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37423-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37423-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37423-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could use GPSBabel to do some auto pruning or you could view and prune with GPSprune. <a href="http://activityworkshop.net/software/gpsprune/">http://activityworkshop.net/software/gpsprune/</a> <a href="https://wiki.openstreetmap.org/wiki/GPSBabel">https://wiki.openstreetmap.org/wiki/GPSBabel</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Oct '14, 13:08</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
</div>
<div id="comments-container-37423" class="comments-container">
&#10;</div>
<div id="comment-tools-37423" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37423-form-container" class="comment-form-container">
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

