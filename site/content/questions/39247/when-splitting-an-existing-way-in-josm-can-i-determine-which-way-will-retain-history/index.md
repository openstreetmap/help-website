+++
type = "question"
title = "When splitting an existing way in JOSM, can I determine which way will retain history?"
description = '''I&#x27;m splitting a way that&#x27;s A====B====C====D=====E This way&#x27;s first version was A===B===C  (in the example, A, B,C,D, and E are nodes).  If I split the way at node D, can I choose whether I want DE to have the original way&#x27;s history or ABC?  If so, how?'''
date = "2014-12-12T19:27:00Z"
lastmod = "2016-10-13T20:06:00Z"
weight = 39247
keywords = [ "ways", "josm", "split", "history" ]
aliases = [ "/questions/39247" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [When splitting an existing way in JOSM, can I determine which way will retain history?](/questions/39247/when-splitting-an-existing-way-in-josm-can-i-determine-which-way-will-retain-history)

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
<span id="post-39247-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39247-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-39247-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm splitting a way that's <code>A====B====C====D=====E</code></p>
<p>This way's first version was <code>A===B===C</code> (in the example, A, B,C,D, and E are nodes).</p>
<p>If I split the way at node D, can I choose whether I want DE to have the original way's history or ABC?</p>
<p>If so, how?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-split" rel="tag" title="see questions tagged &#39;split&#39;">split</span> <span class="post-tag tag-link-history" rel="tag" title="see questions tagged &#39;history&#39;">history</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Dec '14, 19:27</strong></p>
<img src="https://secure.gravatar.com/avatar/3f2a3925f19f9684808db864d290682c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skorasaurus&#39;s gravatar image" />
<p><span>skorasaurus</span><br />
<span class="score" title="1398 reputation points"><span>1.4k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skorasaurus has 3 accepted answers">12%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Aug '15, 23:56</strong> </span></p>
</div>
</div>
<div id="comments-container-39247" class="comments-container">
&#10;</div>
<div id="comment-tools-39247" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39247-form-container" class="comment-form-container">
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

<span id="52542"></span>

<div id="answer-container-52542" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52542-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52542-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-52542-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>(Since the JOSM version which was <a href="https://josm.openstreetmap.de/wiki/Changelog/2015#stable-release-15.10">released on 2015-10-30</a>:) JOSM reuses the id (and hence the way's history) of the existing way for the longest (node count) split segment and allows expert users to choose another segment. Also see the <a href="https://josm.openstreetmap.de/wiki/Help/Action/SplitWay#Usingoldobjectid">relevant section in the documentation of the "split way" function</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Oct '16, 20:06</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Oct '16, 22:16</strong> </span></p>
</div>
</div>
<div id="comments-container-52542" class="comments-container">
&#10;</div>
<div id="comment-tools-52542" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52542-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="39248"></span>

<div id="answer-container-39248" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39248-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39248-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-39248-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, Never thought of this before but it's the first section of the way that retains the history. So if you want the other half to retain the history then reverse the way before splitting it.</p>
<p>Bernard</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Dec '14, 20:05</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-39248" class="comments-container">
<span id="39249"></span>
<div id="comment-39249" class="comment">
<div id="post-39249-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>RPR is the key sequence (first select the node, and if needed the way, of course) I often use for this purpose. This keeps the history at the part I want and does not change the way directions needlessly.</p>
<p>In fact a tool for this would be nice.</p>
</div>
<div id="comment-39249-info" class="comment-info">
<span class="comment-age">(12 Dec '14, 21:24)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="39250"></span>
<div id="comment-39250" class="comment">
<div id="post-39250-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also I would automatically add a tag like meta:history:split_off_from=$oldwayID to the new (ID: 0) ways (which could be automatically removed in subsequent object versions like it is done for created_by tags). Anybody thought of this before? :-)</p>
</div>
<div id="comment-39250-info" class="comment-info">
<span class="comment-age">(12 Dec '14, 21:29)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="39254"></span>
<div id="comment-39254" class="comment">
<div id="post-39254-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not a bad idea. But it gets a little more complicated when splitting the way again or merging it with another way. Likewise it would be useful to keep such a reference when replacing a point feature with an area feature.</p>
</div>
<div id="comment-39254-info" class="comment-info">
<span class="comment-age">(13 Dec '14, 08:36)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="39255"></span>
<div id="comment-39255" class="comment">
<div id="post-39255-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Splitting ways and (not) keeping history was a hot topic during ODbL license change. Tracking a way's history across splits was also discussed back then in much detail (while I don't happen to remember any specifics). Simon probably can chime in here.</p>
</div>
<div id="comment-39255-info" class="comment-info">
<span class="comment-age">(13 Dec '14, 09:22)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="41050"></span>
<div id="comment-41050" class="comment">
<div id="post-41050-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><strong><a href="https://help.openstreetmap.org/users/158/scai">@scai</a></strong>:</p>
<p>Use "replace geometry" from utilsplugin2 when converting nodes to areas.</p>
</div>
<div id="comment-41050-info" class="comment-info">
<span class="comment-age">(16 Feb '15, 15:07)</span> <span class="comment-user userinfo">skyper</span>
</div>
</div>
</div>
<div id="comment-tools-39248" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39248-form-container" class="comment-form-container">
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

