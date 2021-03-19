+++
type = "question"
title = "Connection reset on iOS/mac osx"
description = '''We have a weird problem that can only be reproduced with iOS and Mac OSX.  The problem occurs when the clients are redirected in a SSL-session which is done from a custom filter in a TMG. Looking at the logs in wireshark we get from the server FIN, ACK and then right after RST, ACK. The last ACK is ...'''
date = "2014-12-01T04:48:00Z"
lastmod = "2014-12-01T04:48:00Z"
weight = 38252
keywords = [ "macosx", "ios", "rst+ack" ]
aliases = [ "/questions/38252" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Connection reset on iOS/mac osx](/questions/38252/connection-reset-on-iosmac-osx)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38252-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38252-score" class="post-score" title="current number of votes">0</div><span id="post-38252-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have a weird problem that can only be reproduced with iOS and Mac OSX. The problem occurs when the clients are redirected in a SSL-session which is done from a custom filter in a TMG. Looking at the logs in wireshark we get from the server FIN, ACK and then right after RST, ACK. The last ACK is for a sequence number I cannot find.</p><p>The weird thing is that we can only reproduce it with iOS and Mac OSX(and it happens every time). It works fine with windows, ubuntu, windows phone and so on. Has anyone seen these kind of problems with iOS/mac os?</p><pre><code>No.     Time           Source             Destination       Protocol Length Info
  1 0.000000000    client-ip          server-ip         TCP      78     50847→443 [SYN] Seq=0 Win=65535 Len=0 MSS=1460 WS=32 TSval=490636520 TSecr=0 SACK_PERM=1
  2 0.009105000    server-ip          client-ip         TCP      74     443→50847 [SYN, ACK] Seq=0 Ack=1 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1 TSval=103007363 TSecr=490636520
  3 0.009225000    client-ip          server-ip         TCP      66     50847→443 [ACK] Seq=1 Ack=1 Win=131744 Len=0 TSval=490636529 TSecr=103007363
  4 0.010158000    client-ip          server-ip         TLSv1    303    Client Hello
  5 0.030827000    server-ip          client-ip         TLSv1    211    Server Hello, Change Cipher Spec, Encrypted Handshake Message
  6 0.030912000    client-ip          server-ip         TCP      66     50847→443 [ACK] Seq=238 Ack=146 Win=131616 Len=0 TSval=490636550 TSecr=103007365
  7 0.031190000    client-ip          server-ip         TLSv1    72     Change Cipher Spec
  8 0.031195000    client-ip          server-ip         TLSv1    119    Encrypted Handshake Message
  9 0.032129000    client-ip          server-ip         TLSv1    519    Application Data
 10 0.049597000    server-ip          client-ip         TCP      66     443→50847 [ACK] Seq=146 Ack=297 Win=131584 Len=0 TSval=103007367 TSecr=490636550
 11 0.049773000    server-ip          client-ip         TLSv1    343    Application Data
 12 0.049857000    client-ip          server-ip         TCP      66     50847→443 [ACK] Seq=750 Ack=423 Win=131328 Len=0 TSval=490636568 TSecr=103007367
 13 0.053849000    client-ip          server-ip         TLSv1    620    Application Data, Application Data
 14 0.056073000    server-ip          client-ip         TCP      66     443→50847 [FIN, ACK] Seq=423 Ack=750 Win=131072 Len=0 TSval=103007368 TSecr=490636568
 15 0.065695000    server-ip          client-ip         TCP      60     443→50847 [RST, ACK] Seq=424 Ack=1304 Win=0 Len=0
 16 0.295689000    client-ip          server-ip         TLSv1    620    [TCP Window Full] [TCP Retransmission] Application Data, Application Data
 17 0.572773000    client-ip          server-ip         TLSv1    620    [TCP Window Full] [TCP Retransmission] Application Data, Application Data
 18 0.924984000    client-ip          server-ip         TLSv1    620    [TCP Window Full] [TCP Retransmission] Application Data, Application Data
 19 1.430060000    client-ip          server-ip         TLSv1    620    [TCP Window Full] [TCP Retransmission] Application Data, Application Data
 20 2.239149000    client-ip          server-ip         TLSv1    620    [TCP Window Full] [TCP Retransmission] Application Data, Application Data
 21 3.400246000    client-ip          server-ip         TLSv1    620    [TCP Window Full] [TCP Retransmission] Application Data, Application Data
 22 5.521333000    client-ip          server-ip         TLSv1    620    [TCP Window Full] [TCP Retransmission] Application Data, Application Data
 23 7.642410000    client-ip          server-ip         TLSv1    620    [TCP Window Full] [TCP Retransmission] Application Data, Application Data
 24 9.763488000    client-ip          server-ip         TLSv1    620    [TCP Window Full] [TCP Retransmission] Application Data, Application Data
 25 11.884578000   client-ip          server-ip         TLSv1    620    [TCP Window Full] [TCP Retransmission] Application Data, Application Data
 26 14.005664000   client-ip          server-ip         TLSv1    620    [TCP Window Full] [TCP Retransmission] Application Data, Application Data
 27 16.126750000   client-ip          server-ip         TLSv1    620    [TCP Window Full] [TCP Retransmission] Application Data, Application Data
 28 18.247842000   client-ip          server-ip         TCP      54     50847→443 [RST, ACK] Seq=1304 Ack=423 Win=131328 Len=0</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-macosx" rel="tag" title="see questions tagged &#39;macosx&#39;">macosx</span> <span class="post-tag tag-link-ios" rel="tag" title="see questions tagged &#39;ios&#39;">ios</span> <span class="post-tag tag-link-rst+ack" rel="tag" title="see questions tagged &#39;rst+ack&#39;">rst+ack</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Dec '14, 04:48</strong></p><img src="https://secure.gravatar.com/avatar/66a1da34704d18984e99b76edfa3a9ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JanBanan&#39;s gravatar image" /><p><span>JanBanan</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JanBanan has no accepted answers">0%</span></p></div></div><div id="comments-container-38252" class="comments-container"></div><div id="comment-tools-38252" class="comment-tools"></div><div class="clear"></div><div id="comment-38252-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

