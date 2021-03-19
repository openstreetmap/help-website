+++
type = "question"
title = "Getting Encrypt Alert from Client after Application Data exchange"
description = '''I am getting a Encryption alert from the client after the server and client have exchanged application data. The Error codes do not seem consistent between the Alert Description Types. Why would the client send an alert after several application packets have passed successfully? Thank you in advance...'''
date = "2013-01-16T15:58:00Z"
lastmod = "2013-01-17T07:43:00Z"
weight = 17727
keywords = [ "from", "tsclient", "encrypt", "alert" ]
aliases = [ "/questions/17727" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Getting Encrypt Alert from Client after Application Data exchange](/questions/17727/getting-encrypt-alert-from-client-after-application-data-exchange)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17727-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17727-score" class="post-score" title="current number of votes">0</div><span id="post-17727-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am getting a Encryption alert from the client after the server and client have exchanged application data. The Error codes do not seem consistent between the Alert Description Types. Why would the client send an alert after several application packets have passed successfully? Thank you in advance. Dan</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-from" rel="tag" title="see questions tagged &#39;from&#39;">from</span> <span class="post-tag tag-link-tsclient" rel="tag" title="see questions tagged &#39;tsclient&#39;">tsclient</span> <span class="post-tag tag-link-encrypt" rel="tag" title="see questions tagged &#39;encrypt&#39;">encrypt</span> <span class="post-tag tag-link-alert" rel="tag" title="see questions tagged &#39;alert&#39;">alert</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jan '13, 15:58</strong></p><img src="https://secure.gravatar.com/avatar/77360afb27bb03577d8f760316049cae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DanS&#39;s gravatar image" /><p><span>DanS</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DanS has no accepted answers">0%</span></p></div></div><div id="comments-container-17727" class="comments-container"></div><div id="comment-tools-17727" class="comment-tools"></div><div class="clear"></div><div id="comment-17727-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17750"></span>

<div id="answer-container-17750" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17750-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17750-score" class="post-score" title="current number of votes">1</div><span id="post-17750-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming the traffic is https, what is the order in which you see "application data". This can most easily be seen when using a filter <code>"tcp.len&gt;0"</code>. Do you application data from the client, then application data from the server and then the EncryptedAlert from the client (without the server first sending an EncryptedAlert or TCP-FIN? Is there a delay between the last Application data packet and the EncryptedAlert?</p><p>The connection is kept open on the application level (http). So you need to look into the KeepAlive settings of the embedded server or the http settings on the client to make the session last longer. Also SSL session caching can reduce the workload on the embedded server, if it supports it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jan '13, 07:43</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-17750" class="comments-container"></div><div id="comment-tools-17750" class="comment-tools"></div><div class="clear"></div><div id="comment-17750-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17728"></span>

<div id="answer-container-17728" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17728-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17728-score" class="post-score" title="current number of votes">0</div><span id="post-17728-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It is probably not an error. You will see alerts as a notification that the encrypted session is going to be terminated after the data exchange was complete, which is perfectly normal. IIRC it is designed like this to make it harder for attackers to spoof session termination packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jan '13, 16:02</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-17728" class="comments-container"><span id="17747"></span><div id="comment-17747" class="comment"><div id="post-17747-score" class="comment-score"></div><div class="comment-text"><p>Thank you Jasper. We have an embedded server and the handshake is hurting our performance for the web session. Is there a way to keep the connection open? I haven't found a linger option in SSL. There is one for the socket connection which we have set, but it doesn't help if SSL is shutting the connection down. Thanks again. Dan</p></div><div id="comment-17747-info" class="comment-info"><span class="comment-age">(17 Jan '13, 07:06)</span> <span class="comment-user userinfo">DanS</span></div></div><span id="17748"></span><div id="comment-17748" class="comment"><div id="post-17748-score" class="comment-score"></div><div class="comment-text"><p>Is there a way to keep an SSL connection open?</p></div><div id="comment-17748-info" class="comment-info"><span class="comment-age">(17 Jan '13, 07:08)</span> <span class="comment-user userinfo">DanS</span></div></div></div><div id="comment-tools-17728" class="comment-tools"></div><div class="clear"></div><div id="comment-17728-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

