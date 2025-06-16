+++
type = "question"
title = "this site can&#x27;t be reached error while trying to export a map"
description = '''I am trying to export a map but get a site can&#x27;t be reached error: http://api.openstreetmap.org/api/0.6/map?bbox=-87.9952,43.0188,-87.8604,43.0778 This site can’t be reached The webpage at http://api.openstreetmap.org/api/0.6/map?bbox=-87.9952,43.0188,-87.8604,43.0778 might be temporarily down or it...'''
date = "2016-06-04T08:38:00Z"
lastmod = "2016-12-23T19:34:00Z"
weight = 50006
keywords = [ "export" ]
aliases = [ "/questions/50006" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [this site can't be reached error while trying to export a map](/questions/50006/this-site-cant-be-reached-error-while-trying-to-export-a-map)

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
<span id="post-50006-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50006-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50006-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to export a map but get a site can't be reached error: <a href="http://api.openstreetmap.org/api/0.6/map?bbox=-87.9952,43.0188,-87.8604,43.0778">http://api.openstreetmap.org/api/0.6/map?bbox=-87.9952,43.0188,-87.8604,43.0778</a></p>
<p>This site can’t be reached</p>
<p>The webpage at <a href="http://api.openstreetmap.org/api/0.6/map?bbox=-87.9952,43.0188,-87.8604,43.0778">http://api.openstreetmap.org/api/0.6/map?bbox=-87.9952,43.0188,-87.8604,43.0778</a> might be temporarily down or it may have moved permanently to a new web address. ERR_INVALID_RESPONSE</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jun '16, 08:38</strong></p>
<img src="https://secure.gravatar.com/avatar/ffb3c85bb5a859d18e7bcf2d016ffc63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="erikwanta&#39;s gravatar image" />
<p><span>erikwanta</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="erikwanta has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50006" class="comments-container">
<span id="50317"></span>
<div id="comment-50317" class="comment">
<div id="post-50317-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could you explain what you are actually trying to do?</p>
<p>"a map" could mean one of many things, and unless you explain what you're trying to do no-one will be able to help much.</p>
</div>
<div id="comment-50317-info" class="comment-info">
<span class="comment-age">(19 Jun '16, 16:54)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-50006" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50006-form-container" class="comment-form-container">
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

<span id="50008"></span>

<div id="answer-container-50008" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50008-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50008-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50008-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You will not get a map there, just raw OSM data in XML format. This API is intended to be called by editor programs only. Therefore it supports only comparatively small areas to be exported.</p>
<p>And why an error? Likely the server was too busy to process your request <em>or</em> your requested area is too large. Also see <a href="/questions/21192/error-export-load-average-on-the-server-is-too-high-at-the-moment">https://help.openstreetmap.org/questions/21192/error-export-load-average-on-the-server-is-too-high-at-the-moment</a> .</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jun '16, 09:56</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Dec '16, 19:10</strong> </span></p>
</div>
</div>
<div id="comments-container-50008" class="comments-container">
&#10;</div>
<div id="comment-tools-50008" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50008-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53679"></span>

<div id="answer-container-53679" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53679-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53679-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53679-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>hi, i'm having the same problem for central Paris but i also tried down town Manhattan and same thing. did anyone figure it out? thanks</p>
<p>my bad, just shrunk the are and its working now</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Dec '16, 01:07</strong></p>
<img src="https://secure.gravatar.com/avatar/6d6d4ce305195784a449e9d482a273d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="steveh2112&#39;s gravatar image" />
<p><span>steveh2112</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="steveh2112 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Dec '16, 01:15</strong> </span></p>
</div>
</div>
<div id="comments-container-53679" class="comments-container">
<span id="53680"></span>
<div id="comment-53680" class="comment">
<div id="post-53680-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>what is "just shrunk the are"? Do yo mean "just shrunk the area"? Yes, like I said in my answer, the area may be too large. Thanks for your update!</p>
</div>
<div id="comment-53680-info" class="comment-info">
<span class="comment-age">(23 Dec '16, 01:18)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="53687"></span>
<div id="comment-53687" class="comment">
<div id="post-53687-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>When you export data, the text on the screen says "If the above export fails, please consider using one of the sources listed below".</p>
<p>I suggest that you consider using one of those sources.</p>
</div>
<div id="comment-53687-info" class="comment-info">
<span class="comment-age">(23 Dec '16, 19:34)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-53679" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53679-form-container" class="comment-form-container">
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

