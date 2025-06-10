+++
type = "question"
title = "iD background imagery brightness"
description = '''I&#x27;m struggling to find a way to change the background imagery in iD to be bright enough to use. I&#x27;m currently editing here. In iD the (Bing) imagery is too dark to see what&#x27;s going on. For comparison, in P2 it&#x27;s not - it&#x27;s possible to make out e.g. field boundaries clearly. In order to try and make ...'''
date = "2015-06-13T17:17:00Z"
lastmod = "2015-06-15T17:59:00Z"
weight = 43557
keywords = [ "ideditor" ]
aliases = [ "/questions/43557" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [iD background imagery brightness](/questions/43557/id-background-imagery-brightness)

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
<span id="post-43557-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43557-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43557-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm struggling to find a way to change the background imagery in iD to be bright enough to use. I'm currently editing <a href="http://www.openstreetmap.org/#map=16/53.0435/-1.0588">here</a>. In <a href="http://www.openstreetmap.org/edit?editor=id#map=16/53.0435/-1.0588">iD</a> the (Bing) imagery is too dark to see what's going on. For comparison, in <a href="http://www.openstreetmap.org/edit?editor=potlatch2#map=16/53.0435/-1.0588">P2</a> it's not - it's possible to make out e.g. field boundaries clearly.</p>
<p>In order to try and make the imagery visible I've turned up the screen brightness as far as I can, and tried each of the boxes at the top of the "background imagery" list (from reading the documentation I think that they're supposed to be "100% brightness" through "25% brightness" though that text doesn't display properly on a small screen). However the result is still too dark to use in iD when what is presumably the same imagery looks just fine in P2.</p>
<p>It's possible that this is just a bug (not necessarily in iD) but I'm asking here in case I'm missing something obvious.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jun '15, 17:17</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-43557" class="comments-container">
<span id="43566"></span>
<div id="comment-43566" class="comment">
<div id="post-43566-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Might be slightly off-topic, but after two years using Potlatch2, I discovered that the background imagery is pale because by default it is "softened". When you go to Background, you can uncheck this button and suddenly it looks like the iD background. In same cases, that makes the picture much more legible.</p>
</div>
<div id="comment-43566-info" class="comment-info">
<span class="comment-age">(15 Jun '15, 08:37)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
</div>
<div id="comment-tools-43557" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43557-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="43573"></span>

<div id="answer-container-43573" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43573-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43573-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43573-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think the answer is what joost schouppe said above. P2 softens the imagery, and iD is just displaying the raw imagery.</p>
<p>I'm considering adding some background image processing to iD (see <a href="https://github.com/openstreetmap/iD/issues/2211">#2211</a>) but it's not implemented yet.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jun '15, 15:47</strong></p>
<img src="https://secure.gravatar.com/avatar/5372740989fdca18458f194a285fcb3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bhousel&#39;s gravatar image" />
<p><span>bhousel</span><br />
<span class="score" title="2089 reputation points"><span>2.1k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bhousel has 13 accepted answers">38%</span></p>
</div>
</div>
<div id="comments-container-43573" class="comments-container">
<span id="43578"></span>
<div id="comment-43578" class="comment">
<div id="post-43578-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks - I'll look forward to it.</p>
</div>
<div id="comment-43578-info" class="comment-info">
<span class="comment-age">(15 Jun '15, 17:59)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-43573" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43573-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43558"></span>

<div id="answer-container-43558" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43558-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43558-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43558-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The brightness worked for me. Here is a poor photo of my Tesco Hudl which shows that it seems to work ok. Not an answer but may help with your problem solving.<img src="http://help.openstreetmap.org/upfiles/SDC17618.JPG" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jun '15, 19:06</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</img>
</div>
</div>
<div id="comments-container-43558" class="comments-container">
&#10;</div>
<div id="comment-tools-43558" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43558-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43576"></span>

<div id="answer-container-43576" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43576-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43576-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43576-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For some weird reason Ive yet to figure the answer to, iD shows the imagery as dimmed unless you manually adjust the brightness (as shown above)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jun '15, 17:52</strong></p>
<img src="https://secure.gravatar.com/avatar/9f0faef4659de616c82f448ff3f4e8e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaCor&#39;s gravatar image" />
<p><span>DaCor</span><br />
<span class="score" title="1339 reputation points"><span>1.3k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaCor has one accepted answer">2%</span></p>
</div>
</div>
<div id="comments-container-43576" class="comments-container">
&#10;</div>
<div id="comment-tools-43576" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43576-form-container" class="comment-form-container">
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

