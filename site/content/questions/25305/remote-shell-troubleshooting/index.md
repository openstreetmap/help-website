+++
type = "question"
title = "Remote shell troubleshooting"
description = '''Hello, everybody. Please, if this is not the right place, tell me where I should send this question. A TWAIN driver installed in a workstation uses remote shell (RSH) to connect to a multifunction printer in other subnet in order to scan through the network. A Checkpoint firewall routes packets betw...'''
date = "2013-09-27T02:53:00Z"
lastmod = "2013-10-02T23:55:00Z"
weight = 25305
keywords = [ "twain", "remoteshell" ]
aliases = [ "/questions/25305" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Remote shell troubleshooting](/questions/25305/remote-shell-troubleshooting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25305-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25305-score" class="post-score" title="current number of votes">0</div><span id="post-25305-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, everybody.</p><p>Please, if this is not the right place, tell me where I should send this question.</p><p>A TWAIN driver installed in a workstation uses remote shell (RSH) to connect to a multifunction printer in other subnet in order to scan through the network. A Checkpoint firewall routes packets between both networks and the right ACLs have been configured.</p><p>The first command sent by the workstation instructs the MFP to redirect standard error (stderr) console to port 1022. After exchanging usernames, then the next TCP stream appears:</p><pre><code>No. Time           Source      Destination Protocol Length Info

  6 *REF*          MFP_Printer Scanning_WS TCP      74     1023 &gt; 1022 [SYN] Seq=0 Win=16384 Len=0 MSS=1460 WS=1 TSval=0 TSecr=0

  7 0.000070000    Scanning_WS MFP_Printer TCP      74     1022 &gt; 1023 [SYN, ACK] Seq=0 Ack=1 Win=8192 Len=0 MSS=1460 WS=256 TSval=175963 TSecr=0

  8 0.000778000    MFP_Printer Scanning_WS TCP      66     1023 &gt; 1022 [ACK] Seq=1 Ack=1 Win=17520 Len=0 TSval=0 TSecr=175963

 13 0.005591000    Scanning_WS MFP_Printer TCP      68     1022 &gt; 1023 [PSH, ACK] Seq=1 Ack=1 Win=66560 Len=2 TSval=175963 TSecr=0

 15 0.310455000    Scanning_WS MFP_Printer TCP      68     [TCP Retransmission] 1022 &gt; 1023 [PSH, ACK] Seq=1 Ack=1 Win=66560 Len=2 TSval=175994 TSecr=0

 16 0.918846000    Scanning_WS MFP_Printer TCP      68     [TCP Retransmission] 1022 &gt; 1023 [PSH, ACK] Seq=1 Ack=1 Win=66560 Len=2 TSval=176055 TSecr=0

 17 2.135649000    Scanning_WS MFP_Printer TCP      68     [TCP Retransmission] 1022 &gt; 1023 [PSH, ACK] Seq=1 Ack=1 Win=66560 Len=2 TSval=176176 TSecr=0

 18 4.538069000    Scanning_WS MFP_Printer TCP      68     [TCP Retransmission] 1022 &gt; 1023 [PSH, ACK] Seq=1 Ack=1 Win=66560 Len=2 TSval=176417 TSecr=0

 19 9.358490000    Scanning_WS MFP_Printer TCP      68     [TCP Retransmission] 1022 &gt; 1023 [PSH, ACK] Seq=1 Ack=1 Win=66560 Len=2 TSval=176899 TSecr=0
 20 18.968060000   Scanning_WS MFP_Printer TCP      54     1022 &gt; 1023 [RST, ACK] Seq=3 Ack=1 Win=0 Len=0

 21 18.968948000   MFP_Printer Scanning_WS TCP      66     [TCP Dup ACK 8#1] 1023 &gt; 1022 [ACK] Seq=1 Ack=1 Win=17520 Len=0 TSval=38 TSecr=175963

 22 18.968985000   Scanning_WS MFP_Printer TCP      54     1022 &gt; 1023 [RST] Seq=1 Win=0 Len=0</code></pre><p>As you can see, TCP connection is created by MFP_Printer. After syncing, I would expect that frame 13 should be MFP_Printer transmitting data to Scanning_WS, but it is not, it's just the opposite.</p><p>The firewall (the IPS, I guess) is dropping this packet, reporting "Violated unidirectional connection". TCP Retransmissions work as expected until the connection is eventually reset.</p><p>So the questions are:</p><p>After correct TCP three-way handshake, the peer which sent the TCP SYN should be the peer transmiting data. Is it right?</p><p>Is this remote shell behaviour a non-standard behaviour?</p><p>Is it a wrong design related to the driver or to the linix running in the MFP?</p><p>I need to understand what's happening in order to provide some solution, so any information will be greatly appreciated.</p><p>Regards.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-twain" rel="tag" title="see questions tagged &#39;twain&#39;">twain</span> <span class="post-tag tag-link-remoteshell" rel="tag" title="see questions tagged &#39;remoteshell&#39;">remoteshell</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Sep '13, 02:53</strong></p><img src="https://secure.gravatar.com/avatar/24d0053e1e34abf5ca1e5fdca76c94c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="selecnor&#39;s gravatar image" /><p><span>selecnor</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="selecnor has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Sep '13, 14:41</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-25305" class="comments-container"></div><div id="comment-tools-25305" class="comment-tools"></div><div class="clear"></div><div id="comment-25305-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25425"></span>

<div id="answer-container-25425" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25425-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25425-score" class="post-score" title="current number of votes">0</div><span id="post-25425-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not sure how the RSH protocol should look, but I suspect that the twain driver is not using the remote shell protocol, or at least not a compliant version of it. So if you instruct your checkpoint firewall (or the IDS) to interpret the data as RSH, then you might run into a violation.</p><p>Can you disable the protocol inspection and just let the traffic through based on the TCP ports.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '13, 15:02</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-25425" class="comments-container"><span id="25577"></span><div id="comment-25577" class="comment"><div id="post-25577-score" class="comment-score"></div><div class="comment-text"><p>Hello, SYN-bit.</p><p>Thank you for your answer. Disabling the IPS for the related IP addresses was my first advice for the CheckPoint's administrator; I'm not really sure about his/her skills and if this was done. It's out of my scope.</p><p>Anycase, I was just curious and wanted to offer more information. Does somebody know where can I find documentation about the behaviour of Remote Shell from the TCP connections point of view?</p><p>Regards.</p></div><div id="comment-25577-info" class="comment-info"><span class="comment-age">(02 Oct '13, 23:55)</span> <span class="comment-user userinfo">selecnor</span></div></div></div><div id="comment-tools-25425" class="comment-tools"></div><div class="clear"></div><div id="comment-25425-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

