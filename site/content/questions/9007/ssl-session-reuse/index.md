+++
type = "question"
title = "SSL Session ReUse"
description = '''Does anyone know how SSL Servers maintains its SSL Session ID Table so it know that a SSL Session ID that is being reused is still valid? What I&#x27;m trying to determine is if it keeps track of the session id and the client ip or is it something else that the server uses to keep track of the sessions. ...'''
date = "2012-02-14T14:45:00Z"
lastmod = "2012-03-20T19:03:00Z"
weight = 9007
keywords = [ "ssl" ]
aliases = [ "/questions/9007" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [SSL Session ReUse](/questions/9007/ssl-session-reuse)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9007-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9007-score" class="post-score" title="current number of votes">0</div><span id="post-9007-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Does anyone know how SSL Servers maintains its SSL Session ID Table so it know that a SSL Session ID that is being reused is still valid? What I'm trying to determine is if it keeps track of the session id and the client ip or is it something else that the server uses to keep track of the sessions.</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Feb '12, 14:45</strong></p><img src="https://secure.gravatar.com/avatar/98ec75d031a962cf9b8cd542330f511d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="seyerekim&#39;s gravatar image" /><p><span>seyerekim</span><br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="seyerekim has no accepted answers">0%</span></p></div></div><div id="comments-container-9007" class="comments-container"></div><div id="comment-tools-9007" class="comment-tools"></div><div class="clear"></div><div id="comment-9007-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9013"></span>

<div id="answer-container-9013" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9013-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9013-score" class="post-score" title="current number of votes">0</div><span id="post-9013-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>AFAIK the SSL SessionID is used (without client IP address) as both Client and Server need to cache the keying material for the particular session to be able to re-use it. Both the client and the server have a (individual) lifetime on the session (so an absolute timeout instead of an idle timeout). The SSL SessionID is used to fetch the keying material from cache to prevent the full SSL handshake (which is CPU intensive).</p><p>In TLS there is a mechanism called <a href="http://www.ietf.org/rfc/rfc5077">TLS session Tickets</a> to remove the need for a session cache on the server. The server will encrypt the keying material in a session ticket and send it to the client. The client caches it and will send it back to the server when setting up a new session.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '12, 03:09</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-9013" class="comments-container"></div><div id="comment-tools-9013" class="comment-tools"></div><div class="clear"></div><div id="comment-9013-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9669"></span>

<div id="answer-container-9669" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9669-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9669-score" class="post-score" title="current number of votes">0</div><span id="post-9669-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Many server-side implementations will associate the SessionID with a particular source IP address as a security measure and will reject any attempt to reuse that Session from a different source. Also the typical server will time out the Session cache after a period of time (~5 minutes).</p><p>The answer to your question will depend on just what framework was used to build the server AND what additional parameters or controls the server application itself may impose.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '12, 19:03</strong></p><img src="https://secure.gravatar.com/avatar/b64129b7a3bf2a9f1760fbdee1b3b74c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="inetdog&#39;s gravatar image" /><p><span>inetdog</span><br />
<span class="score" title="167 reputation points">167</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="inetdog has 3 accepted answers">14%</span> </br></p></div></div><div id="comments-container-9669" class="comments-container"></div><div id="comment-tools-9669" class="comment-tools"></div><div class="clear"></div><div id="comment-9669-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

