+++
type = "question"
title = "Struggling to decrypt SSL"
description = '''I&#x27;ve spent most of the day ripping my hair out trying to get SSL traffic to decrypt... Here is the capture i&#x27;ve taken which should just be a simple hit to IIS splash screen. https://dl.dropboxusercontent.com/u/8208314/Wireshark/Capture.pcapng The private key to the certificate is here:  https://dl.d...'''
date = "2015-07-01T08:39:00Z"
lastmod = "2015-07-09T07:38:00Z"
weight = 43788
keywords = [ "ssl", "decrypt" ]
aliases = [ "/questions/43788" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Struggling to decrypt SSL](/questions/43788/struggling-to-decrypt-ssl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43788-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43788-score" class="post-score" title="current number of votes">1</div><span id="post-43788-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've spent most of the day ripping my hair out trying to get SSL traffic to decrypt...</p><p>Here is the capture i've taken which should just be a simple hit to IIS splash screen. <a href="https://dl.dropboxusercontent.com/u/8208314/Wireshark/Capture.pcapng">https://dl.dropboxusercontent.com/u/8208314/Wireshark/Capture.pcapng</a></p><p>The private key to the certificate is here: <a href="https://dl.dropboxusercontent.com/u/8208314/Wireshark/privatekey.pem">https://dl.dropboxusercontent.com/u/8208314/Wireshark/privatekey.pem</a></p><p><strong>I've checked the private key matches the certificate. The modulus has been compared.</strong> I can decrypt snake oil example.</p><p>My debug log is here: <a href="https://dl.dropboxusercontent.com/u/8208314/Wireshark/debug.txt">https://dl.dropboxusercontent.com/u/8208314/Wireshark/debug.txt</a></p><p>I've removed from IIS all the cipher suites for Diffie-Hellman and ECDH so am at a loss why this won't decrypt.</p><p>The debug log is just saying there is no enough material to generate the key... what else does it need?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-decrypt" rel="tag" title="see questions tagged &#39;decrypt&#39;">decrypt</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jul '15, 08:39</strong></p><img src="https://secure.gravatar.com/avatar/0fd9254e876670b245a27af6492caa9f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ingybing&#39;s gravatar image" /><p><span>ingybing</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ingybing has no accepted answers">0%</span></p></div></div><div id="comments-container-43788" class="comments-container"></div><div id="comment-tools-43788" class="comment-tools"></div><div class="clear"></div><div id="comment-43788-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43789"></span>

<div id="answer-container-43789" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43789-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43789-score" class="post-score" title="current number of votes">0</div><span id="post-43789-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your SSL capture uses SSL session resumption and skips the ServerKeyExchange. Therefore the encrypted key is not transmitted over the wire and you cannot decrypt the traffic even if you have the private key.</p><p>See the client request:</p><pre><code>Frame 5: 204 bytes on wire (1632 bits), 204 bytes captured (1632 bits) on interface 0
...
Secure Sockets Layer
    SSL Record Layer: Handshake Protocol: Client Hello
        Content Type: Handshake (22)
        Version: TLS 1.0 (0x0301)
        Length: 145
        Handshake Protocol: Client Hello
            Handshake Type: Client Hello (1)
            Length: 141
            Version: TLS 1.0 (0x0301)
            Random
                GMT Unix Time: Jul  1, 2015 17:04:25.000000000 CEST
                Random Bytes: ea0ea305800f28c796df322c46728872f74e6464fe1fbc96...
            Session ID Length: 32
            Session ID: ed1100003c6c96e97979417c6bacf88ae7b637abcb5df1c1...
            ...</code></pre><p>and the server response:</p><pre><code>Frame 6: 199 bytes on wire (1592 bits), 199 bytes captured (1592 bits) on interface 0
...
Secure Sockets Layer
    TLSv1 Record Layer: Handshake Protocol: Server Hello
        Content Type: Handshake (22)
        Version: TLS 1.0 (0x0301)
        Length: 81
        Handshake Protocol: Server Hello
            Handshake Type: Server Hello (2)
            Length: 77
            Version: TLS 1.0 (0x0301)
            Random
                GMT Unix Time: Jul  1, 2015 17:04:25.000000000 CEST
                Random Bytes: b20d047492d020cb99ba0d233760e46ddc1dca41478a6732...
            Session ID Length: 32
            Session ID: ed1100003c6c96e97979417c6bacf88ae7b637abcb5df1c1...
            Cipher Suite: TLS_RSA_WITH_AES_256_CBC_SHA (0x0035)
            ...</code></pre><p>and the full communication (note: missing ClientKeyExchange):</p><pre><code>  5  11.039305  10.64.99.12 -&gt; 10.64.104.135 SSL 204 Client Hello
  6  11.039592 10.64.104.135 -&gt; 10.64.99.12  TLSv1 199 Server Hello, Change Cipher Spec, Encrypted Handshake Message
  7  11.041144  10.64.99.12 -&gt; 10.64.104.135 TLSv1 438 Change Cipher Spec, Encrypted Handshake Message, Application Data
  8  11.042308 10.64.104.135 -&gt; 10.64.99.12  TLSv1 1072 Application Data, Application Data
 10  11.338115  10.64.99.12 -&gt; 10.64.104.135 SSL 60 Continuation Data</code></pre><p>See <a href="https://tools.ietf.org/html/rfc5246#page-37">this figure from RFC 5246</a> for a flow diagram for the abbreviated handshake due to the use of session resumption (be sure to read the preceding text as well for a background).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jul '15, 08:46</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Jul '15, 08:52</strong> </span></p></div></div><div id="comments-container-43789" class="comments-container"><span id="43793"></span><div id="comment-43793" class="comment"><div id="post-43793-score" class="comment-score"></div><div class="comment-text"><p>Ok i think i understand... so i reset iis, closed my client ran another trace: <a href="https://dl.dropboxusercontent.com/u/8208314/Wireshark/capture2.pcapng">https://dl.dropboxusercontent.com/u/8208314/Wireshark/capture2.pcapng</a> and it's still not sending the serverkeyexchange during the server hello even through the client hello had no session id... so that ones no resuming an existing session is it? Shouldn't that be sending the server key exchange now? Is it due to the cypher why its not?</p></div><div id="comment-43793-info" class="comment-info"><span class="comment-age">(01 Jul '15, 09:27)</span> <span class="comment-user userinfo">ingybing</span></div></div><span id="43801"></span><div id="comment-43801" class="comment"><div id="post-43801-score" class="comment-score"></div><div class="comment-text"><p>Also the snakeoil example doesn't have a server key exchange... i'm confused.....</p></div><div id="comment-43801-info" class="comment-info"><span class="comment-age">(01 Jul '15, 13:45)</span> <span class="comment-user userinfo">ingybing</span></div></div><span id="43876"></span><div id="comment-43876" class="comment"><div id="post-43876-score" class="comment-score"></div><div class="comment-text"><p><span>@ingybing</span> FYI, I have been working on this issue for the past days. The problem is within the parameters from your RSA private key. It upsets the crypto library (libgcrypt). I am now trying to find out the cause and a solution.</p></div><div id="comment-43876-info" class="comment-info"><span class="comment-age">(05 Jul '15, 08:36)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div><span id="44010"></span><div id="comment-44010" class="comment"><div id="post-44010-score" class="comment-score"></div><div class="comment-text"><p><span>@ingybing</span> It took some time to understand the cryptography behind it, but the fix such that your traffic is recognized can be found at: <a href="https://code.wireshark.org/review/9573">https://code.wireshark.org/review/9573</a></p></div><div id="comment-44010-info" class="comment-info"><span class="comment-age">(09 Jul '15, 07:38)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div></div><div id="comment-tools-43789" class="comment-tools"></div><div class="clear"></div><div id="comment-43789-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

