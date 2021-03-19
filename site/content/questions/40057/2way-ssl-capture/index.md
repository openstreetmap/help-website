+++
type = "question"
title = "2way SSL Capture?"
description = '''We have a 2way SSL service running. Today we came across an issue that raised a question about a 2way SSL packet capture. In the Certificate exchange we noticed the Client sent a SSL Cert Length 0 (null) which we interpreted as the Client Certificate was not being presented. To our surprise we achie...'''
date = "2015-02-24T19:56:00Z"
lastmod = "2015-02-27T02:49:00Z"
weight = 40057
keywords = [ "ssl", "2way" ]
aliases = [ "/questions/40057" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [2way SSL Capture?](/questions/40057/2way-ssl-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40057-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40057-score" class="post-score" title="current number of votes">0</div><span id="post-40057-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have a 2way SSL service running. Today we came across an issue that raised a question about a 2way SSL packet capture. In the Certificate exchange we noticed the Client sent a SSL Cert Length 0 (null) which we interpreted as the Client Certificate was not being presented. To our surprise we achieved the same effect when the RootCA's or Intermediate CA's did not match. With all that being said, is there an indicator in the packet to differentiate between the 2 issues?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-2way" rel="tag" title="see questions tagged &#39;2way&#39;">2way</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Feb '15, 19:56</strong></p><img src="https://secure.gravatar.com/avatar/1b7a5adb09e617735ec56ae98e775d13?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KickAss&#39;s gravatar image" /><p><span>KickAss</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KickAss has no accepted answers">0%</span></p></div></div><div id="comments-container-40057" class="comments-container"></div><div id="comment-tools-40057" class="comment-tools"></div><div class="clear"></div><div id="comment-40057-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40065"></span>

<div id="answer-container-40065" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40065-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40065-score" class="post-score" title="current number of votes">0</div><span id="post-40065-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When the client sends a "Certificate" handshake message with cert length 0, it means it did not have a suitable Client Certificate to send to the server. It all depends on the SSL client being used what this means. In case of a browser, it means there either were no client certificates available or the user did not select one to send to the server if there were.</p><p>Can you elaborate on "To our surprise we achieved the same effect when the RootCA's or Intermediate CA's did not match."? What do you mean by "same effect"? A "Certificate" handshake message with cert length 0 perhaps? And there are several places on the client and server where CA's are configured, so which ones are you talking about exactly in this sentence?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Feb '15, 01:39</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-40065" class="comments-container"><span id="40072"></span><div id="comment-40072" class="comment"><div id="post-40072-score" class="comment-score"></div><div class="comment-text"><p>Being that we are troubleshooting on the server side only. The captures revealed that the client certificate length was null zero, which led us to believe that the client did not have the client certificate installed. However, upon further review the client did have the cert installed but had different RootCA's. From my understanding that behavior is normal from a client when CA's don't match.</p><p>So back to my original question, since the client had different RootCA's than what the server side had. Is there a way to indicate that in a packet capture? To me they look identical to one another but maybe I'm missing something?</p></div><div id="comment-40072-info" class="comment-info"><span class="comment-age">(25 Feb '15, 09:08)</span> <span class="comment-user userinfo">KickAss</span></div></div><span id="40122"></span><div id="comment-40122" class="comment"><div id="post-40122-score" class="comment-score"></div><div class="comment-text"><p>The "Certificate" handshake of the client will not be different. However, I would expect an "Alert" message from the client when it can not match the "Certficate" message from the server to any of it's trusted RootCA's. Could you post the handshake messages of the case where the client did not have the right RootCA installed?</p><p>If you can supply a capture file (on <a href="https://appliance.cloudshark.org/upload/">Cloudshark</a> for instance), that would be great. You can anonimize the file with <a href="https://www.tracewrangler.com/">TraceWrangler</a> if you need to remove the ip addresses and/or the TCP payload of the packets.</p></div><div id="comment-40122-info" class="comment-info"><span class="comment-age">(27 Feb '15, 02:49)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-40065" class="comment-tools"></div><div class="clear"></div><div id="comment-40065-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

