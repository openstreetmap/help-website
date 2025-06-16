+++
type = "question"
title = "iD editor - simple version to allow parish clerks to map allotments and cemeteries"
description = '''Hi good people. Our customers are over 65 years old, so lack tech skills. But I want to get them to contribute their cemeteries and allotments data (UK) to OSM via iD editor. I need a really simple version of iD, which I can customise, then embed into our web apps with our custom look a feel. Is it ...'''
date = "2021-12-17T10:29:00Z"
lastmod = "2021-12-18T15:19:00Z"
weight = 82865
keywords = [ "ideditor" ]
aliases = [ "/questions/82865" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [iD editor - simple version to allow parish clerks to map allotments and cemeteries](/questions/82865/id-editor-simple-version-to-allow-parish-clerks-to-map-allotments-and-cemeteries)

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
<span id="post-82865-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82865-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-82865-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi good people.</p>
<p>Our customers are over 65 years old, so lack tech skills. But I want to get them to contribute their cemeteries and allotments data (UK) to OSM via iD editor. I need a really simple version of iD, which I can customise, then embed into our web apps with our custom look a feel.</p>
<p>Is it standard practice to fork the iD app to do this? Then to keep our fork updated we have to merge all changes from the official release?</p>
<p>Background</p>
<p>I work at scribe.ac, we build apps to help clerks administer parish and town councils (local government) in the UK. We are building an app to help them manage allotments and cemeteries, which includes mapping their plots. I really want to contribute this data directly back to OSM, since we have over 750 customers (growing 100% YoY).</p>
<p>Any help is appreciated!</p>
<p>John Fagan</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Dec '21, 10:29</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffb2031e7774ad39f2fa2cb128bf3cb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johnbfagan&#39;s gravatar image" />
<p><span>johnbfagan</span><br />
<span class="score" title="111 reputation points">111</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johnbfagan has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82865" class="comments-container">
<span id="82873"></span>
<div id="comment-82873" class="comment">
<div id="post-82873-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Duplicate or follow-up of <a href="/questions/82864/id-editor-contributors-from-single-account">https://help.openstreetmap.org/questions/82864/id-editor-contributors-from-single-account</a></p>
</div>
<div id="comment-82873-info" class="comment-info">
<span class="comment-age">(18 Dec '21, 15:19)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-82865" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82865-form-container" class="comment-form-container">
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

<span id="82871"></span>

<div id="answer-container-82871" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82871-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82871-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-82871-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="johnbfagan has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="https://github.com/openstreetmap/iD/blob/develop/API.md">iD API</a> allows one to call the editor with only some presets enabled. I don't know if these options are too generic for your purposes (e.g., all landuse features), in which case this (along with very specific validations) may be appropriate areas to focus on if a fork is required.</p>
<p>Tagging presets are maintained in the <a href="https://github.com/openstreetmap/id-tagging-schema">iD Tagging Presets</a> repo which is probably a much less thing to maintain as a fork.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Dec '21, 22:55</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-82871" class="comments-container">
&#10;</div>
<div id="comment-tools-82871" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82871-form-container" class="comment-form-container">
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

