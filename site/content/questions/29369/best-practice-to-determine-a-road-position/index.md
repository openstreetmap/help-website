+++
type = "question"
title = "Best practice to determine a road position"
description = '''While doing some routing related edits (marking only straight turns), I have noticed that some roads do not seem to be well placed in regards with other elements (other roads, buildings).  Currently an example is at Lugano where one road (Viale Carlo Cattaneo) seems to be moved north, by several met...'''
date = "2013-12-27T10:44:00Z"
lastmod = "2013-12-27T13:48:00Z"
weight = 29369
keywords = [ "roads", "position", "bestpractice" ]
aliases = [ "/questions/29369" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Best practice to determine a road position](/questions/29369/best-practice-to-determine-a-road-position)

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
<span id="post-29369-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29369-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-29369-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>While doing some routing related edits (marking only straight turns), I have noticed that some roads do not seem to be well placed in regards with other elements (other roads, buildings). Currently an example is at <a href="http://www.openstreetmap.org/#map=19/46.00564/8.95549">Lugano</a> where one road (Viale Carlo Cattaneo) seems to be moved north, by several meters, and now intersections are not correct and it goes through buildings.</p>
<p>I can open a note/bug and let someone deal with it, but I would be curious how you would deal with such a case.</p>
<p>I know that satellite imagery has an offset (so it can't always be used). I also know that a GPS will have some error (so even if I would "go and check" I can't guarantee it is perfect). What I have tried is to download the GPX traces in JOSM. By looking at that road, there is only one trace following more or less the current road, while there are many others south of the current position (where I think it is correct). I have checked also the history and there is no useful comment for the changeset that moved the nodes.</p>
<p>Is there anything more that I can do? In the future (and for this) would you recommend that I fix it or that I open a note?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-roads" rel="tag" title="see questions tagged &#39;roads&#39;">roads</span> <span class="post-tag tag-link-position" rel="tag" title="see questions tagged &#39;position&#39;">position</span> <span class="post-tag tag-link-bestpractice" rel="tag" title="see questions tagged &#39;bestpractice&#39;">bestpractice</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Dec '13, 10:44</strong></p>
<img src="https://secure.gravatar.com/avatar/9a40eb6c01263ddc795f5ce62b043d13?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vlad-Mihai%20Sima&#39;s gravatar image" />
<p><span>Vlad-Mihai Sima</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vlad-Mihai Sima has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-29369" class="comments-container">
&#10;</div>
<div id="comment-tools-29369" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29369-form-container" class="comment-form-container">
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

<span id="29370"></span>

<div id="answer-container-29370" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29370-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29370-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-29370-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Vlad-Mihai Sima has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If there are several GPX traces I will move the Sat image to agree with the majority. This can be done in most editors (research then ask if not sure how to do this). The roads and ways can then been dragged to agree. Once you start a re-adjustment deciding where to stop can be problem but if nobody starts nothing will get improved. You have some experience so have a try. Good Luck<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Dec '13, 11:18</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span> </br></p>
</div>
</div>
<div id="comments-container-29370" class="comments-container">
<span id="29371"></span>
<div id="comment-29371" class="comment">
<div id="post-29371-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Adjustments in potlatch2 <a href="https://help.openstreetmap.org/questions/1686/adjusting-aerial-backgrounds-in-potlatch-2">https://help.openstreetmap.org/questions/1686/adjusting-aerial-backgrounds-in-potlatch-2</a></p>
</div>
<div id="comment-29371-info" class="comment-info">
<span class="comment-age">(27 Dec '13, 11:23)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="29372"></span>
<div id="comment-29372" class="comment">
<div id="post-29372-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>another related q <a href="https://help.openstreetmap.org/questions/17661/aligning-roads-to-proper-location">https://help.openstreetmap.org/questions/17661/aligning-roads-to-proper-location</a></p>
</div>
<div id="comment-29372-info" class="comment-info">
<span class="comment-age">(27 Dec '13, 11:25)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-29370" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29370-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29374"></span>

<div id="answer-container-29374" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29374-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29374-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-29374-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In addition to fixing the problem (as Andy suggests) I'd also contact the user who moved the road** to a location that doesn't match either the underlying GPS traces or the Bing imagery. The immediately previous location of the traffic signals can be seen <a href="http://www.openstreetmap.org/?mlat=46.00559&amp;mlon=8.95553&amp;zoom=18#map=18/46.00559/8.95553">here</a>, and looks to be more correct. The user in question has made relatively few edits, although the first was a long time ago. It's far more likely to be a simple mistake than any kind of "vandalism"; they may have only looked at their own traces (or none at all). I'd explain the problem and say that you've moved the road down to a location that best fits the available evidence.<br />
</p>
<p>We were all inexperienced users once, and it's practice and help from the rest of the community that turns inexperienced mappers into experienced ones.</p>
<p>** The node history is probably the easiest way to see this.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Dec '13, 13:48</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span> </br></p>
</div>
</div>
<div id="comments-container-29374" class="comments-container">
&#10;</div>
<div id="comment-tools-29374" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29374-form-container" class="comment-form-container">
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

