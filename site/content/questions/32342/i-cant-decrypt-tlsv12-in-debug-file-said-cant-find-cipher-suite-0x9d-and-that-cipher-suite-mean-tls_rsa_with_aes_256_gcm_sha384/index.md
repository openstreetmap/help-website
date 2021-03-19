+++
type = "question"
title = "i cant decrypt TLSv1.2, in debug file said can&#x27;t find cipher suite 0x9D, and  that cipher suite mean TLS_RSA_WITH_AES_256_GCM_SHA384"
description = '''i wanna decrypt cipher suite 0x9D ( TLS_RSA_WITH_AES_256_GCM_SHA384 ) but when i search tutorial, thats said i need to add cipher suite for that method,  but, i still doesnt understand how to add it, and use patch, i am still begineer, so i need step by step how to patch it,  i am using wireshark fo...'''
date = "2014-05-01T06:57:00Z"
lastmod = "2014-05-01T07:12:00Z"
weight = 32342
keywords = [ "tls", "tlsv1.2" ]
aliases = [ "/questions/32342" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [i cant decrypt TLSv1.2, in debug file said can't find cipher suite 0x9D, and that cipher suite mean TLS\_RSA\_WITH\_AES\_256\_GCM\_SHA384](/questions/32342/i-cant-decrypt-tlsv12-in-debug-file-said-cant-find-cipher-suite-0x9d-and-that-cipher-suite-mean-tls_rsa_with_aes_256_gcm_sha384)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32342-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32342-score" class="post-score" title="current number of votes">0</div><span id="post-32342-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i wanna decrypt cipher suite 0x9D ( TLS_RSA_WITH_AES_256_GCM_SHA384 )</p><p>but when i search tutorial, thats said i need to add cipher suite for that method,</p><p>but, i still doesnt understand how to add it, and use patch,</p><p>i am still begineer, so i need step by step how to patch it,</p><p>i am using wireshark for windows version 1.10.7.</p><p>anyone can help me with my problem?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tls" rel="tag" title="see questions tagged &#39;tls&#39;">tls</span> <span class="post-tag tag-link-tlsv1.2" rel="tag" title="see questions tagged &#39;tlsv1.2&#39;">tlsv1.2</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 May '14, 06:57</strong></p><img src="https://secure.gravatar.com/avatar/c77a3b07f418cd7bf1b71e3349fcb191?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="justian123456789&#39;s gravatar image" /><p><span>justian12345...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="justian123456789 has no accepted answers">0%</span></p></div></div><div id="comments-container-32342" class="comments-container"></div><div id="comment-tools-32342" class="comment-tools"></div><div class="clear"></div><div id="comment-32342-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32343"></span>

<div id="answer-container-32343" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32343-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32343-score" class="post-score" title="current number of votes">1</div><span id="post-32343-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You need the latest development release (1.11.x) for that cipher.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 May '14, 06:59</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 May '14, 07:03</strong> </span></p></div></div><div id="comments-container-32343" class="comments-container"><span id="32344"></span><div id="comment-32344" class="comment"><div id="post-32344-score" class="comment-score"></div><div class="comment-text"><p>so i need to use development release of wireshark kurt?</p><p>okay, i will try it, and i will give the report later.</p><p>thanks for ur answer kurt.</p></div><div id="comment-32344-info" class="comment-info"><span class="comment-age">(01 May '14, 07:01)</span> <span class="comment-user userinfo">justian12345...</span></div></div><span id="32345"></span><div id="comment-32345" class="comment"><div id="post-32345-score" class="comment-score"></div><div class="comment-text"><p>thanks kurt, finally i can decrypt that.</p></div><div id="comment-32345-info" class="comment-info"><span class="comment-age">(01 May '14, 07:07)</span> <span class="comment-user userinfo">justian12345...</span></div></div><span id="32347"></span><div id="comment-32347" class="comment"><div id="post-32347-score" class="comment-score"></div><div class="comment-text"><p>Good.</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-32347-info" class="comment-info"><span class="comment-age">(01 May '14, 07:12)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-32343" class="comment-tools"></div><div class="clear"></div><div id="comment-32343-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

