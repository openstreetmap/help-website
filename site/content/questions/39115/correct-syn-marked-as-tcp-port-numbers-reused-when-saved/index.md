+++
type = "question"
title = "Correct SYN marked as &quot;TCP port numbers reused&quot; when saved"
description = '''Hi there, I captured a correct sequence with wireshark V1.12.3 starting with a SYN: 22 23.886574000s 192.168.0.160 192.168.0.2 50000 TCP 60 1027→50000 [SYN] Seq=0 Win=1446 Len=0 MSS=1446 Everything is fine. But when I save this File an reopen it, so the same line is being displayed as: 22 23.8865740...'''
date = "2015-01-14T00:04:00Z"
lastmod = "2015-01-14T01:47:00Z"
weight = 39115
keywords = [ "reused", "saved" ]
aliases = [ "/questions/39115" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Correct SYN marked as "TCP port numbers reused" when saved](/questions/39115/correct-syn-marked-as-tcp-port-numbers-reused-when-saved)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39115-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there, I captured a correct sequence with wireshark V1.12.3 starting with a SYN:</p><p>22 23.886574000s 192.168.0.160 192.168.0.2 50000 TCP 60 1027→50000 [SYN] Seq=0 Win=1446 Len=0 MSS=1446 Everything is fine. But when I save this File an reopen it, so the same line is being displayed as:</p><p>22 23.886574000s 192.168.0.160 192.168.0.2 50000 TCP 60 [TCP Port numbers reused] 1027→50000 [SYN] Seq=4294967260 Win=1446 Len=0 MSS=1446</p><p>with an other sequence number and the Frame is marked as possible erroneous (TCP Port numbers reused).<br />
What can be the cause of this and how to avoid it? Regards Steffen</p></div><div id="question-tags" class="tags-container tags">reused saved</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jan '15, 00:04</strong></p><img src="https://secure.gravatar.com/avatar/669b508299066ce6bd2c5b37b2043256?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ClownFerdinand&#39;s gravatar image" /><p>ClownFerdinand<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ClownFerdinand has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-39115" class="comments-container"></div><div id="comment-tools-39115" class="comment-tools"></div><div class="clear"></div><div id="comment-39115-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="39122"></span>

<div id="answer-container-39122" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39122-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I can reproduce the issue when opening the capture file in Wireshark 1.12.1. The ISN is 0 (absolute value), so it seems the TCP dissector can not properly handle the case of an ISN of 0. Could you file this as a bug on bugs.wireshark.org (referring to this question)?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jan '15, 01:47</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-39122" class="comments-container"><span id="39123"></span><div id="comment-39123" class="comment"><div id="post-39123-score" class="comment-score"></div><div class="comment-text"><p>Thanks. The corresponding bug-number is: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10854">Bug 10854</a></p></div><div id="comment-39123-info" class="comment-info"><span class="comment-age">(14 Jan '15, 01:58)</span> ClownFerdinand</div></div></div><div id="comment-tools-39122" class="comment-tools"></div><div class="clear"></div><div id="comment-39122-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39116"></span>

<div id="answer-container-39116" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39116-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>[TCP Port number reused] is diagnosed when you have a SYN packet with the same IP:Port combination for client and server as a previous conversation. The new SYN has a different sequence number, otherwise it would be considered a retransmission of the previous SYN.</p><p>See packet-tcp.c:</p><pre><code>    /* If this is a SYN packet, then check if its seq-nr is different
     * from the base_seq of the retrieved conversation. If this is the
     * case, create a new conversation with the same addresses and ports
     * and set the TA_PORTS_REUSED flag. If the seq-nr is the same as
     * the base_seq, then do nothing so it will be marked as a retrans-
     * mission later.
     */</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jan '15, 00:13</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-39116" class="comments-container"><span id="39117"></span><div id="comment-39117" class="comment"><div id="post-39117-score" class="comment-score"></div><div class="comment-text"><p>This is not the problem. The second line is not a second SYN. Its is the same SYN as in the first line. 1. I captured the sequence: --&gt; copy to first line 2. I save the sequence in a file 3. I opened the file saved in step 2 --&gt; copy to second line</p></div><div id="comment-39117-info" class="comment-info"><span class="comment-age">(14 Jan '15, 00:21)</span> ClownFerdinand</div></div><span id="39118"></span><div id="comment-39118" class="comment"><div id="post-39118-score" class="comment-score"></div><div class="comment-text"><p>Okay, looks like there are two problems. Wireshark should not save/load anything different than it was captured, and second, it should not mark something as port number reused if it isn't.</p><p>Can you provide a sample capture? Upload to <a href="http://www.cloudshark.org">http://www.cloudshark.org</a> and post the link if you can.</p></div><div id="comment-39118-info" class="comment-info"><span class="comment-age">(14 Jan '15, 00:24)</span> Jasper ♦♦</div></div><span id="39121"></span><div id="comment-39121" class="comment"><div id="post-39121-score" class="comment-score"></div><div class="comment-text"><p>Here you are: <a href="https://www.cloudshark.org/captures/28171169d695">SYN-Capture</a></p><p>On this page, the explanation of the frame is o.k. No "TCP Port numbers reused" issue. But open this file in the wireshark V1.12.3. Than the issue will happen.</p><p>Thanx in advance</p><p>Steffen</p></div><div id="comment-39121-info" class="comment-info"><span class="comment-age">(14 Jan '15, 01:19)</span> ClownFerdinand</div></div></div><div id="comment-tools-39116" class="comment-tools"></div><div class="clear"></div><div id="comment-39116-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

