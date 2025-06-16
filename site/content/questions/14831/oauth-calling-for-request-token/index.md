+++
type = "question"
title = "Oauth calling for Request Token"
description = '''Hi, I&#x27;m interested in creating an Oauth 1.0 client for Openstreetmaps. I wanted to make my own client without using libraries.  In OSM I saw that callback url is optional and have to set when registering application. But according to normal protocol we have to insert callback as a parameter. In this...'''
date = "2012-08-04T17:21:00Z"
lastmod = "2012-12-14T15:54:00Z"
weight = 14831
keywords = [ "oauth", "token", "client", "request" ]
aliases = [ "/questions/14831" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Oauth calling for Request Token](/questions/14831/oauth-calling-for-request-token)

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
<span id="post-14831-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14831-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-14831-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'm interested in creating an Oauth 1.0 client for Openstreetmaps. I wanted to make my own client without using libraries. In OSM I saw that callback url is optional and have to set when registering application. But according to normal protocol we have to insert callback as a parameter. In this case I'm confused about <strong>what should be included in parameter list that send to Request Token URL</strong> ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-oauth" rel="tag" title="see questions tagged &#39;oauth&#39;">oauth</span> <span class="post-tag tag-link-token" rel="tag" title="see questions tagged &#39;token&#39;">token</span> <span class="post-tag tag-link-client" rel="tag" title="see questions tagged &#39;client&#39;">client</span> <span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Aug '12, 17:21</strong></p>
<img src="https://secure.gravatar.com/avatar/658670034a8466e9db4fb65067d310f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="buddhima&#39;s gravatar image" />
<p><span>buddhima</span><br />
<span class="score" title="116 reputation points">116</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="buddhima has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Aug '12, 12:17</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-14831" class="comments-container">
<span id="14926"></span>
<div id="comment-14926" class="comment">
<div id="post-14926-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi,</p>
<p>Can someone answer this question please? because it is very essential for my project.</p>
<p>common way of requesting is :</p>
<p>oauthRequest('requestTokenURL', 'POST', $parameters)</p>
<p>This $parameters variable only consists of 'callback' url.</p>
<p>I want to know what should I provide at there instead of 'callback' url?</p>
<p>Will it cause any problem if I send it as an empty variable?</p>
<p>Thank you!</p>
</div>
<div id="comment-14926-info" class="comment-info">
<span class="comment-age">(09 Aug '12, 16:43)</span> <span class="comment-user userinfo">buddhima</span>
</div>
</div>
<span id="14931"></span>
<div id="comment-14931" class="comment">
<div id="post-14931-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you cannot get any answer here, try to ask at <a href="http://forum.osm.org">http://forum.osm.org</a> or at one of the <a href="https://wiki.openstreetmap.org/wiki/Mailing_lists">https://wiki.openstreetmap.org/wiki/Mailing_lists</a></p>
</div>
<div id="comment-14931-info" class="comment-info">
<span class="comment-age">(09 Aug '12, 17:25)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-14831" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14831-form-container" class="comment-form-container">
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

<span id="18458"></span>

<div id="answer-container-18458" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18458-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18458-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18458-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, Problem solved! Must mentioned callback url in OSM web site. No use of sending it in requests.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Dec '12, 15:54</strong></p>
<img src="https://secure.gravatar.com/avatar/658670034a8466e9db4fb65067d310f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="buddhima&#39;s gravatar image" />
<p><span>buddhima</span><br />
<span class="score" title="116 reputation points">116</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="buddhima has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18458" class="comments-container">
&#10;</div>
<div id="comment-tools-18458" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18458-form-container" class="comment-form-container">
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

