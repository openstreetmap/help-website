+++
type = "question"
title = "Decode SSL Decimal fields in tshark output"
description = '''Hi All, I am trying to list all supported ciphersuites during the SSL client hello by running the capture thru tshark. The query is fine, but the values coverted to decimal. Is there a way tshark can convert them to ascii so that I can see the TLS versions and ciphersuite names instead? Here is my c...'''
date = "2014-11-01T20:57:00Z"
lastmod = "2014-11-02T04:31:00Z"
weight = 37528
keywords = [ "ciphersuite", "ssl", "tshark" ]
aliases = [ "/questions/37528" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decode SSL Decimal fields in tshark output](/questions/37528/decode-ssl-decimal-fields-in-tshark-output)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37528-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37528-score" class="post-score" title="current number of votes">0</div><span id="post-37528-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All, I am trying to list all supported ciphersuites during the SSL client hello by running the capture thru tshark. The query is fine, but the values coverted to decimal. Is there a way tshark can convert them to ascii so that I can see the TLS versions and ciphersuite names instead? Here is my command:</p><p>tshark -r SSLCapture.cap -V -2R ssl.handshake.type==1 -T fields -e ssl.handshake.version -e ssl.handshake.ciphersuite Output:: 769 47,53,5,10,49171,49172,49161,49162,50,56,19,4</p><p>769 = 0x0301 which is TLS 1.0 so can I display TLSv1 in tshark?</p><p>5 = 0x0005 which is TLS_RSA_WITH_RC4_128_SHA, and so forth.....</p><p>Thanks in advance for your help!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ciphersuite" rel="tag" title="see questions tagged &#39;ciphersuite&#39;">ciphersuite</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Nov '14, 20:57</strong></p><img src="https://secure.gravatar.com/avatar/f86f7ca5d84e2cc32500a7e4d4daa3b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="StriclyFlava&#39;s gravatar image" /><p><span>StriclyFlava</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="StriclyFlava has no accepted answers">0%</span></p></div></div><div id="comments-container-37528" class="comments-container"></div><div id="comment-tools-37528" class="comment-tools"></div><div class="clear"></div><div id="comment-37528-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37536"></span>

<div id="answer-container-37536" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37536-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37536-score" class="post-score" title="current number of votes">0</div><span id="post-37536-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use thsark in the following way</p><blockquote><p>tshark -nr ssl_example.pcap -Y "ssl.handshake.ciphersuites" -Vx &gt; ssl.output.txt</p></blockquote><p>Sample output:</p><pre><code>Secure Sockets Layer
    SSL Record Layer: Handshake Protocol: Client Hello
        Content Type: Handshake (22)
        Version: TLS 1.0 (0x0301)
        Length: 512
        Handshake Protocol: Client Hello
            Handshake Type: Client Hello (1)
            Length: 508
            Version: TLS 1.2 (0x0303)
            Random
                GMT Unix Time: Jun 28, 2097 09:17:21.000000000 W. Europe Daylight Time
                Random Bytes: 577f9fb99f0e042633046e9b969fd957b903edb4bbb77449...
            Session ID Length: 32
            Session ID: 888489fa25a177efb30c21cc89b6e447ae680357a0b762b6...
            Cipher Suites Length: 32
            Cipher Suites (16 suites)
                Cipher Suite: TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 (0xc02b)
                Cipher Suite: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (0xc02f)
                Cipher Suite: TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA (0xc00a)
                Cipher Suite: TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA (0xc009)
                Cipher Suite: TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA (0xc013)
                Cipher Suite: TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (0xc014)</code></pre><p>Then use a script (perl/python/whatever) to extract the information you need, like:</p><pre><code>   Version: TLS 1.0 (0x0301)</code></pre><p>or</p><pre><code>   Cipher Suite: TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 (0xc02b)
   Cipher Suite: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (0xc02f)
   Cipher Suite: TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA (0xc00a)</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '14, 04:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-37536" class="comments-container"></div><div id="comment-tools-37536" class="comment-tools"></div><div class="clear"></div><div id="comment-37536-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

