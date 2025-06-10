+++
type = "question"
title = "Suddenly throwing CORS Error on Open Street Map API calls"
description = '''Hi all, We have implemented Open Street Map and It works great though. We are facing some challenges while accessing Open Street Map API from our endpoint. The error is as follows: CORS Error  Access to XMLHttpRequest at &#x27;https://nominatim.openstreetmap.org/search?format=json&amp;amp;q=vvvvv&amp;amp;limit=4...'''
date = "2023-08-02T08:28:00Z"
lastmod = "2023-08-02T12:42:00Z"
weight = 87587
keywords = [ "cors" ]
aliases = [ "/questions/87587" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Suddenly throwing CORS Error on Open Street Map API calls](/questions/87587/suddenly-throwing-cors-error-on-open-street-map-api-calls)

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
<span id="post-87587-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87587-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87587-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>We have implemented Open Street Map and It works great though. We are facing some challenges while accessing Open Street Map API from our endpoint.</p>
<p>The error is as follows: CORS Error Access to XMLHttpRequest at 'https://nominatim.openstreetmap.org/search?format=json&amp;q=vvvvv&amp;limit=4' from origin 'http://localhost:4200' has been blocked by CORS policy: Request header field authorization is not allowed by Access-Control-Allow-Headers in preflight response.</p>
<p>How can we fix this issue urgently ?</p>
<p>Any help will be appreciated</p>
<p>Thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-cors" rel="tag" title="see questions tagged &#39;cors&#39;">cors</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Aug '23, 08:28</strong></p>
<img src="https://secure.gravatar.com/avatar/83c132d2e5648bde98c1474b2acab48a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SSD241993&#39;s gravatar image" />
<p><span>SSD241993</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SSD241993 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Aug '23, 08:28</strong> </span></p>
</div>
</div>
<div id="comments-container-87587" class="comments-container">
&#10;</div>
<div id="comment-tools-87587" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87587-form-container" class="comment-form-container">
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

<span id="87589"></span>

<div id="answer-container-87589" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87589-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87589-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-87589-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>While SomeoneElse pointed out the technical problem you should be aware that the nominatim.openstreetmap.org URL you currently use points to a demo service run by volunteers that can be down anytime and should not be used in production, esp. if something is "urgently".</p>
<p>If you need a reliable service than you should look out for providers offering geocoding apis as a service or install nominatim yourself.</p>
<p>Let's at least hope that you have read and adhere the usage policy that can be found here: <a href="https://operations.osmfoundation.org/policies/nominatim/">https://operations.osmfoundation.org/policies/nominatim/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Aug '23, 12:42</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-87589" class="comments-container">
&#10;</div>
<div id="comment-tools-87589" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87589-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87588"></span>

<div id="answer-container-87588" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87588-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87588-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87588-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Likely <a href="https://community.openstreetmap.org/t/cors-issue-while-using-search-api/101942/3">this</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Aug '23, 09:58</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Aug '23, 09:58</strong> </span></p>
</div>
</div>
<div id="comments-container-87588" class="comments-container">
&#10;</div>
<div id="comment-tools-87588" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87588-form-container" class="comment-form-container">
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

