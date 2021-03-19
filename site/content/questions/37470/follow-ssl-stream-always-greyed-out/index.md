+++
type = "question"
title = "Follow SSL Stream always greyed out."
description = '''No matter what I tried, the Follow SSL Stream is always greyed out, even though I can see and recognize some trace elements under Follow TCP Stream, e.g. parts of the certificate sent from client to server. I have server key. I am running on a CentOS box, and wireshark -v gives me the following: wir...'''
date = "2014-10-30T10:37:00Z"
lastmod = "2014-10-31T06:41:00Z"
weight = 37470
keywords = [ "follow_ssl_stream", "ssl_decrypt" ]
aliases = [ "/questions/37470" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Follow SSL Stream always greyed out.](/questions/37470/follow-ssl-stream-always-greyed-out)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37470-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37470-score" class="post-score" title="current number of votes">0</div><span id="post-37470-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>No matter what I tried, the Follow SSL Stream is always greyed out, even though I can see and recognize some trace elements under Follow TCP Stream, e.g. parts of the certificate sent from client to server. I have server key.</p><h1 id="i-am-running-on-a-centos-box-and-wireshark--v-gives-me-the-following">I am running on a CentOS box, and wireshark -v gives me the following:</h1><p>wireshark 1.10.8 (Git Rev Unknown from unknown)</p><p>Copyright 1998-2014 Gerald Combs <span><span class="__cf_email__" data-cfemail="3d5a584f5c51597d4a544f584e555c4f5613524f5a">[email protected]</span></span> and contributors. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p><p>Compiled (64-bit) with GTK+ 2.20.1, with Cairo 1.8.8, with Pango 1.28.1, with GLib 2.26.1, with libpcap, with libz 1.2.3, without POSIX capabilities, without libnl, without SMI, without c-ares, without ADNS, without Lua, without Python, with GnuTLS 2.8.5, with Gcrypt 1.4.5, with MIT Kerberos, without GeoIP, without PortAudio, with AirPcap.</p><p>Running on Linux 2.6.32-431.29.2.el6.x86_64, with locale en_US.UTF-8, with libpcap version 1.4.0, with libz 1.2.3, GnuTLS 2.8.5, Gcrypt 1.4.5, without AirPcap. Intel(R) Pentium(R) CPU 2127U @ 1.90GHz</p><p>Built using gcc 4.4.7 20120313 (Red Hat 4.4.7-4).</p><h1 id="my-ssl-debug-log-has-following">My SSL debug log has following:</h1><p>Wireshark SSL debug log</p><p>ssl_association_remove removing TCP 0 - http handle 0x1180450 Private key imported: KeyID 49:0f:97:17:a5:1d:a4:4d:a9:d7:a4:d3:58:5e:0f:e4:... ssl_load_key: swapping p and q parameters and recomputing u ssl_init IPv4 addr '127.0.0.1' (127.0.0.1) port '0' filename '/home/cemil/keytests/44DCCDD7.pem' password(only for p12 file) '' ssl_init private key file /home/cemil/keytests/44DCCDD7.pem successfully loaded. association_add TCP port 0 protocol http handle 0x1180450</p><p>So, it looks like key file is OK.</p><p>To ensure that I have the complete trace, I started wireshark capture before I started my server and browser (both on same machine).</p><p>BTW, I also tried port 443, but I read somewhere that port 0 can be used as a wildcard.</p><p>I can see what looks like the encrypted dialog in the captured logs, but the Follow SSL Stream is always greyed out, hence I cannot see the decrypted traffic.</p><p>What am I doing wrong?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-follow_ssl_stream" rel="tag" title="see questions tagged &#39;follow_ssl_stream&#39;">follow_ssl_stream</span> <span class="post-tag tag-link-ssl_decrypt" rel="tag" title="see questions tagged &#39;ssl_decrypt&#39;">ssl_decrypt</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Oct '14, 10:37</strong></p><img src="https://secure.gravatar.com/avatar/8ff0dedad0c32b08f2f65114c9dade91?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CemilB&#39;s gravatar image" /><p><span>CemilB</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CemilB has no accepted answers">0%</span></p></div></div><div id="comments-container-37470" class="comments-container"><span id="37493"></span><div id="comment-37493" class="comment"><div id="post-37493-score" class="comment-score"></div><div class="comment-text"><blockquote><p>hence I cannot see the decrypted traffic.</p></blockquote><p>can you see the decrypted traffic in the debug log (search for GET or POST)?</p></div><div id="comment-37493-info" class="comment-info"><span class="comment-age">(31 Oct '14, 01:42)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-37470" class="comment-tools"></div><div class="clear"></div><div id="comment-37470-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37500"></span>

<div id="answer-container-37500" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37500-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37500-score" class="post-score" title="current number of votes">0</div><span id="post-37500-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What I could see so far, the "Follow SSL Stream" option is <strong>only greyed</strong> out if you selected a frame in the TCP stream that is not shown as SSL or TLS in the protocol column, like (SYN, SYN-ACK, ACKs). For all other frames (marked as SSL/TLS), the option is <strong>not greyed</strong> out, even if Wireshark failed to decrypt the session. In the later case, you will see no result, but the option is still there.</p><p>So, did you really click on a SSL/TLS frame, before you tried to use "Follow SSL Stream"?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Oct '14, 03:27</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Oct '14, 03:39</strong> </span></p></div></div><div id="comments-container-37500" class="comments-container"><span id="37507"></span><div id="comment-37507" class="comment"><div id="post-37507-score" class="comment-score"></div><div class="comment-text"><p>Thanks, Kurt. Eventually, I could see the "Follow SSL Stream", when I used the correct port address, which was 9031. While I am past that problem, I still have a related questions: I read somewhere that I could use "0" as a wild port address (I assume that all ports are assumed to be SSL on selected interface). So, that must be incorrect. Can you confirm and set record straight?</p><p>Also, I read somewhere else that one could use start_tls for protocol? Is that correct?</p><p>Thanks, again.</p></div><div id="comment-37507-info" class="comment-info"><span class="comment-age">(31 Oct '14, 06:41)</span> <span class="comment-user userinfo">CemilB</span></div></div></div><div id="comment-tools-37500" class="comment-tools"></div><div class="clear"></div><div id="comment-37500-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

