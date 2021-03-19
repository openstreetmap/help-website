+++
type = "question"
title = "cookie stealing in https"
description = '''I am able to see cookies in http connection. I would like to know if the same is possible in https connection. Stealing cookies in http connection is quite useless and vague.Instead it would be quite useful if the same is visible for http(s) connection. Is there any way to view cookies in https conn...'''
date = "2014-08-13T05:10:00Z"
lastmod = "2014-08-13T05:39:00Z"
weight = 35453
keywords = [ "cookies", "https" ]
aliases = [ "/questions/35453" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [cookie stealing in https](/questions/35453/cookie-stealing-in-https)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35453-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35453-score" class="post-score" title="current number of votes">0</div><span id="post-35453-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am able to see cookies in http connection. I would like to know if the same is possible in https connection. Stealing cookies in http connection is quite useless and vague.Instead it would be quite useful if the same is visible for http(s) connection. Is there any way to view cookies in https connection and steal the session is from it</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-cookies" rel="tag" title="see questions tagged &#39;cookies&#39;">cookies</span> <span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Aug '14, 05:10</strong></p><img src="https://secure.gravatar.com/avatar/54a87865c7482d3576309e7dc746fd51?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tanu&#39;s gravatar image" /><p><span>tanu</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tanu has no accepted answers">0%</span></p></div></div><div id="comments-container-35453" class="comments-container"><span id="35456"></span><div id="comment-35456" class="comment"><div id="post-35456-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Stealing cookies in http connection <strong>is quite useless</strong></p></blockquote><p>I don't agree with that. If I'm able to get your session cookie, transmitted via HTTP, I could be able to impersonate your session to the server (depends on some security measures within the web application).</p><p>That's way better than 'useless' to me ;-))</p></div><div id="comment-35456-info" class="comment-info"><span class="comment-age">(13 Aug '14, 05:39)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-35453" class="comment-tools"></div><div class="clear"></div><div id="comment-35453-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35454"></span>

<div id="answer-container-35454" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35454-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35454-score" class="post-score" title="current number of votes">0</div><span id="post-35454-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In general, no as that's the point of using an encrypted transport layer (SSL\TLS), all the transported data (i.e. http) is encapsulated by the encryption.</p><p>However, there are known methods of defeating SSL\TLS, e.g. <a href="http://en.wikipedia.org/wiki/Man-in-the-middle_attack">MITM</a> attacks so using one of those will allow the plain text HTTP to be recovered and the cookies viewed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '14, 05:15</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Aug '14, 05:15</strong> </span></p></div></div><div id="comments-container-35454" class="comments-container"></div><div id="comment-tools-35454" class="comment-tools"></div><div class="clear"></div><div id="comment-35454-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

