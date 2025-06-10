+++
type = "question"
title = "how Openstreetmap validate the input? Does any tool do the validation before uploading the data?"
description = '''how Openstreetmap validate the input that are providing by different users? Is there any tool that will do the validation before uploading the data on server?'''
date = "2014-01-21T21:34:00Z"
lastmod = "2014-01-22T00:07:00Z"
weight = 30044
keywords = [ "validation", "quality" ]
aliases = [ "/questions/30044" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how Openstreetmap validate the input? Does any tool do the validation before uploading the data?](/questions/30044/how-openstreetmap-validate-the-input-does-any-tool-do-the-validation-before-uploading-the-data)

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
<span id="post-30044-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30044-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-30044-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>how Openstreetmap validate the input that are providing by different users? Is there any tool that will do the validation before uploading the data on server?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-validation" rel="tag" title="see questions tagged &#39;validation&#39;">validation</span> <span class="post-tag tag-link-quality" rel="tag" title="see questions tagged &#39;quality&#39;">quality</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jan '14, 21:34</strong></p>
<img src="https://secure.gravatar.com/avatar/72546801e2c8e9cd01ca084730b9dc10?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fsrehman&#39;s gravatar image" />
<p><span>fsrehman</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fsrehman has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jan '14, 00:26</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-30044" class="comments-container">
&#10;</div>
<div id="comment-tools-30044" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30044-form-container" class="comment-form-container">
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

<span id="30046"></span>

<div id="answer-container-30046" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30046-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30046-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-30046-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are a fe ways to answer this questions :</p>
<ul>
<li>The editors do a fair bit of validation before upload. <a href="http://wiki.openstreetmap.org/wiki/JOSM/Validator">JOSM's validator</a> in particular is quite powerfull.</li>
<li>The editors also try hard to prevent bad edits in the first place (like <a href="http://wiki.openstreetmap.org/wiki/ID">iD</a>'s polygon tool avoids creating an unclosed building way).</li>
<li>The <a href="http://wiki.openstreetmap.org/wiki/API_v0.6">api</a> doesn't do any validation beyond making sure the request is well-formed, and stores the result directly (old versions of the data are kept).</li>
<li>There are many <a href="http://wiki.openstreetmap.org/wiki/QA">Quality Assurance tools</a> to check the data once it is uploaded.</li>
<li>Many mappers <a href="https://help.openstreetmap.org/questions/20805/how-can-i-set-up-automatic-notification-whenever-data-that-ive-added-to-osm-is-changed?page=1&amp;focusedAnswerId=20809#20809">keep an eye on their favorite areas</a> to fix problems as they occur.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jan '14, 22:43</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-30046" class="comments-container">
&#10;</div>
<div id="comment-tools-30046" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30046-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="30050"></span>

<div id="answer-container-30050" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30050-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30050-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-30050-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>See <span>previous questions tagged "quality"</span>. E.g. <a href="/questions/20312/">data-verification-process</a>! The answers there answer your question (although not really focussing on the "before" aspect).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jan '14, 00:07</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-30050" class="comments-container">
&#10;</div>
<div id="comment-tools-30050" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30050-form-container" class="comment-form-container">
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

