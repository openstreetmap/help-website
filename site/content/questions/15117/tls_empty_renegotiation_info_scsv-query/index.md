+++
type = "question"
title = "TLS_EMPTY_RENEGOTIATION_INFO_SCSV query"
description = '''I used wireshark to capture a SSL handshake and when I inspected the Client Hello packet and went to the Cipher Suites heading and I saw the following cipher:  Cipher Suite: TLS EMPTY RENEGOTIATION INFO SCSV (0x00ff)  (There should be an underscore where those spaces are) I only see that when I insp...'''
date = "2012-10-20T09:56:00Z"
lastmod = "2012-10-23T01:46:00Z"
weight = 15117
keywords = [ "ssl", "handshake", "cipher", "wireshark" ]
aliases = [ "/questions/15117" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [TLS\_EMPTY\_RENEGOTIATION\_INFO\_SCSV query](/questions/15117/tls_empty_renegotiation_info_scsv-query)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15117-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I used wireshark to capture a SSL handshake and when I inspected the Client Hello packet and went to the Cipher Suites heading and I saw the following cipher:</p><blockquote><p>Cipher Suite: TLS EMPTY RENEGOTIATION INFO SCSV (0x00ff)</p></blockquote><p>(There should be an underscore where those spaces are)</p><p>I only see that when I inspect a SSL handshake if FireFox initiates the handshake, but if I used Chrome or Internet Explorer I don't see that. Why is that? I did google the cipher suite, but I didn't understand most of it. From what I could understand it was added with FireFox 8 and it has something to do with java.</p></div><div id="question-tags" class="tags-container tags">ssl handshake cipher wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Oct '12, 09:56</strong></p><img src="https://secure.gravatar.com/avatar/d2230b03035fa99dc2d895a14f26be03?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Howlin1&#39;s gravatar image" /><p>Howlin1<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Howlin1 has no accepted answers">0%</span></p></div></div><div id="comments-container-15117" class="comments-container"></div><div id="comment-tools-15117" class="comment-tools"></div><div class="clear"></div><div id="comment-15117-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15180"></span>

<div id="answer-container-15180" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15180-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>This message is part of the TLS Secure Renegotiation protocol which was introduced to defeat a vulnerability in the original TLS session renegotiation protocol discovered 2009 and only fully handled by most server and client TLS implementations this year. The state of the TLS renegotiation process used by a particular client will depend in part on the underlying cryptographic provider (the latest Java and OpenSSL versions support the new process) and the options which have been set by the application which requests the cryptographic operation.</p><p>TLS clients which do not support the new secure renegotiation protocol will be refused by any properly patched TLS server if they submit an original style TLS renegotation request. (The most common use, AFAIK, of TLS renegotiation has been to allow an HTTPS server to request client certificate authentication after the original TLS handshake has been completed. This is used, for example, when the server considers some URL paths to require stronger client authentication than others, but cannot make that determination until after the initial HTTPS Request has been examined.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Oct '12, 01:46</strong></p><img src="https://secure.gravatar.com/avatar/b64129b7a3bf2a9f1760fbdee1b3b74c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="inetdog&#39;s gravatar image" /><p>inetdog<br />
<span class="score" title="167 reputation points">167</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="inetdog has 3 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Oct '12, 11:16</p></div></div><div id="comments-container-15180" class="comments-container"><span id="15228"></span><div id="comment-15228" class="comment"><div id="post-15228-score" class="comment-score"></div><div class="comment-text"><p>Ah okay, thanks :)</p></div><div id="comment-15228-info" class="comment-info"><span class="comment-age">(24 Oct '12, 08:33)</span> Howlin1</div></div></div><div id="comment-tools-15180" class="comment-tools"></div><div class="clear"></div><div id="comment-15180-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

