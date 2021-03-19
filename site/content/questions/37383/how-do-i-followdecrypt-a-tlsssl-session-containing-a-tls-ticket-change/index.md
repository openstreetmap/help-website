+++
type = "question"
title = "How do I follow/decrypt a TLS/SSL session containing a TLS ticket change?"
description = '''I&#x27;m attempting to analyze a TLS capture containing numerous TCP sessions. It seems that I do have the correct certificate configured, considering that Wireshark is successfully decrypting at least some sessions not containing TLS session ticket replacements (&quot;TLSv1: New Session Ticket, Change Cipher...'''
date = "2014-10-27T20:07:00Z"
lastmod = "2014-10-28T02:40:00Z"
weight = 37383
keywords = [ "tls", "follow", "ticket", "decrypt", "ssl" ]
aliases = [ "/questions/37383" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I follow/decrypt a TLS/SSL session containing a TLS ticket change?](/questions/37383/how-do-i-followdecrypt-a-tlsssl-session-containing-a-tls-ticket-change)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37383-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm attempting to analyze a TLS capture containing numerous TCP sessions. It seems that I do have the correct certificate configured, considering that Wireshark is successfully decrypting at least some sessions not containing TLS session ticket replacements ("TLSv1: New Session Ticket, Change Cipher Spec, Finished"). I haven't yet figured out how to follow a TLS session containing a session ticket replacement. I've tried Wireshark v1.10.6 (Linux) and v1.12.1 (Linux and Windows 7).</p><p>I have the my pem configured under Edit -&gt; Preferences -&gt; Protocols -&gt; SSL -&gt; RSA keys list. I've used editcap to remove duplicate packets. I've tried using a custom compiled version containing every option that might be relevant.</p><p>Bug 5963 indicates that this capability is at least present in Wireshark 1.6.x for Windows 7. Is this capability not in Wireshark v1.10.6 or v1.12.1 for Linux? If so, how do I enable this feature? If not, are there other tools that are (ssldump doesn't seem to have that ability)?</p><p>Thank you in advance for any help any of you can provide,</p><p>Andrew</p></div><div id="question-tags" class="tags-container tags">tls follow ticket decrypt ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Oct '14, 20:07</strong></p><img src="https://secure.gravatar.com/avatar/31af5241ef49dbee9adf58435f39a161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andrew%20Immerman&#39;s gravatar image" /><p>Andrew Immerman<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andrew Immerman has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Oct '14, 20:41</p></div></div><div id="comments-container-37383" class="comments-container"></div><div id="comment-tools-37383" class="comment-tools"></div><div class="clear"></div><div id="comment-37383-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37388"></span>

<div id="answer-container-37388" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37388-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I did a brief test with 1.12.1 on Win7, with the capture file attached to <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5963">bug 5963</a>. While using the file <strong>tls_session_ticket_enabled.pcap</strong> with the included keying material, I can see in the SSL debug file, that Wireshark is able to decrypt the session. Using "Follow SSL Stream" on TCP stream 4, which is using a session ticket, shows the decrypted data. So, decrypting the data works, but there seems to be a problem to view the decrypted data as HTTP in the GUI. Whether that's a bug or not: I don't know. Please update the bug with your findings and possibly a link to your question.</p><p>Output of "Follow SSL Stream"</p><pre><code>GET /gb/images/b_8d5afc09.png HTTP/1.1
Host: ssl.gstatic.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1
Accept: image/png,image/*;q=0.8,*/*;q=0.5
Accept-Language: en-gb,en;q=0.5
Accept-Encoding: gzip, deflate
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
Connection: keep-alive
Referer: https://www.google.com/

HTTP/1.1 200 OK
Content-Type: image/png
Last-Modified: Wed, 28 Sep 2011 03:00:23 GMT</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '14, 02:40</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-37388" class="comments-container"></div><div id="comment-tools-37388" class="comment-tools"></div><div class="clear"></div><div id="comment-37388-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

