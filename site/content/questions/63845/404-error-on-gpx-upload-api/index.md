+++
type = "question"
title = "404 error on GPX upload API"
description = '''I develop iOS App by Objective-C that have function to upload GPX file as GPS trace. When I used this app at May 4th, this app worked well. But now, the GPX upload function in this app shows 404 error by calling &quot;POST /api/0.6/gpx/create&quot; of OSM API. ( I noticed the error May 20th.) In this period, ...'''
date = "2018-05-29T14:53:00Z"
lastmod = "2018-05-30T13:21:00Z"
weight = 63845
keywords = [ "api", "gpx", "upload", "error" ]
aliases = [ "/questions/63845" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [404 error on GPX upload API](/questions/63845/404-error-on-gpx-upload-api)

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
<span id="post-63845-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63845-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63845-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I develop iOS App by Objective-C that have function to upload GPX file as GPS trace.</p>
<p>When I used this app at May 4th, this app worked well. But now, the GPX upload function in this app shows 404 error by calling "POST /api/0.6/gpx/create" of OSM API. ( I noticed the error May 20th.) In this period, I didn’t change any source of program.</p>
<p>Did something change on server and API in this period, or nothing? Or please let me know the solution of the error if you know.</p>
<p>Device : iPhone SE, iPhone 6s and iPad OS version : iOS 11.3.1(latest) and 11.1</p>
<p>The function to upload GPX file is used NSURLSession and NSMutableURLRequest(Apple’s standard SDK) to call “POST /api/0.6/gpx/create” of OSM API. I re-compiled this app by latest Xcode but 404 error was still occurred.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-upload" rel="tag" title="see questions tagged &#39;upload&#39;">upload</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 May '18, 14:53</strong></p>
<img src="https://secure.gravatar.com/avatar/0401120bcd8972c4763705473b02c38c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ao_zeal&#39;s gravatar image" />
<p><span>ao_zeal</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ao_zeal has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63845" class="comments-container">
&#10;</div>
<div id="comment-tools-63845" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63845-form-container" class="comment-form-container">
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

<span id="63846"></span>

<div id="answer-container-63846" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63846-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63846-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-63846-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ao_zeal has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Are you using http: or https: ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 May '18, 15:01</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-63846" class="comments-container">
<span id="63869"></span>
<div id="comment-63869" class="comment">
<div id="post-63869-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I use http to access API.</p>
</div>
<div id="comment-63869-info" class="comment-info">
<span class="comment-age">(30 May '18, 13:08)</span> <span class="comment-user userinfo">ao_zeal</span>
</div>
</div>
<span id="63870"></span>
<div id="comment-63870" class="comment">
<div id="post-63870-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>My app did well to change http to https!! Thanks so much!</p>
</div>
<div id="comment-63870-info" class="comment-info">
<span class="comment-age">(30 May '18, 13:21)</span> <span class="comment-user userinfo">ao_zeal</span>
</div>
</div>
</div>
<div id="comment-tools-63846" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63846-form-container" class="comment-form-container">
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

