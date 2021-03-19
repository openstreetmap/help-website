+++
type = "question"
title = "[closed] RDP sessions getting intermittent TCP RST+ACK&#x27;s"
description = '''Hey guys I&#x27;ve got a question. I&#x27;ve installed a server 2012 R2 hyper-v with a few VM&#x27;s in them. One of them is a TS. My client is having issues with the TS because every now and then they get a popup from RDP that the connection is interrupted and that it will retry to setup the connection. This is v...'''
date = "2015-03-10T08:22:00Z"
lastmod = "2015-03-10T08:22:00Z"
weight = 40426
keywords = [ "rdp", "rst+ack", "packetloss" ]
aliases = [ "/questions/40426" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] RDP sessions getting intermittent TCP RST+ACK's](/questions/40426/rdp-sessions-getting-intermittent-tcp-rstacks)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40426-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey guys I've got a question.</p><p>I've installed a server 2012 R2 hyper-v with a few VM's in them. One of them is a TS. My client is having issues with the TS because every now and then they get a popup from RDP that the connection is interrupted and that it will retry to setup the connection. This is visible for less then a second, but is very disruptive when working.</p><p>I've been doing some captures on the Hypervisor itself and am seeing a lot of RST, ACKs when the interruptions appear. The stream can be going for some time but they all end the same.</p><pre><code>212651  2287.339664000  10.0.0.25   10.0.0.110  TPKT    155 Continuation
212693  2287.540852000  10.0.0.110  10.0.0.25   TCP 60  61059→3389 [ACK] Seq=76446 Ack=237599 Win=64768 Len=0
213075  2288.339741000  10.0.0.25   10.0.0.110  TPKT    155 Continuation
213292  2288.652196000  10.0.0.25   10.0.0.110  TPKT    155 [TCP Retransmission] Continuation
213319  2289.261509000  10.0.0.25   10.0.0.110  TPKT    155 [TCP Retransmission] Continuation
213334  2289.339681000  10.0.0.25   10.0.0.110  TPKT    155 Continuation
213437  2290.339736000  10.0.0.25   10.0.0.110  TPKT    155 Continuation
213444  2290.464660000  10.0.0.25   10.0.0.110  TPKT    357 [TCP Retransmission] Continuation
213631  2291.339771000  10.0.0.25   10.0.0.110  TPKT    155 Continuation
213709  2292.355402000  10.0.0.25   10.0.0.110  TPKT    155 Continuation
213735  2292.870883000  10.0.0.25   10.0.0.110  TPKT    559 [TCP Retransmission] Continuation
213828  2293.355672000  10.0.0.25   10.0.0.110  TPKT    155 Continuation
214009  2294.355357000  10.0.0.25   10.0.0.110  TPKT    155 Continuation
214204  2295.370990000  10.0.0.25   10.0.0.110  TPKT    155 Continuation
214206  2295.371172000  10.0.0.110  10.0.0.25   TCP 66  [TCP Dup ACK 212693#1] 61059→3389 [ACK] Seq=76446 Ack=237599 Win=64768 Len=0 SLE=238306 SRE=238407
214230  2295.465630000  10.0.0.110  10.0.0.25   TCP 60  61059→3389 [RST, ACK] Seq=76446 Ack=237599 Win=0 Len=0
214265  2295.538954000  10.0.0.110  10.0.0.25   TCP 66  61214→3389 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1
214268  2295.539242000  10.0.0.25   10.0.0.110  TCP 66  3389→61214 [SYN, ACK] Seq=0 Ack=1 Win=64000 Len=0 MSS=1460 WS=1 SACK_PERM=1
214270  2295.539754000  10.0.0.110  10.0.0.25   TCP 60  61214→3389 [ACK] Seq=1 Ack=1 Win=65536 Len=0</code></pre><p>As you can see the connection is happily resumed after the reset.</p><p>Any idea what could be causing these resets? The capture is performed on the NIC that handles all VM traffic. The client I've been using to test is connected to the same switch as the Hyper-V server. The Hyper-V isn't using any teaming on the virtual nic.</p></div><div id="question-tags" class="tags-container tags">rdp rst+ack packetloss</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Mar '15, 08:22</strong></p><img src="https://secure.gravatar.com/avatar/f4ea5ee54323f153bdb5e0378e37f0c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fraeco&#39;s gravatar image" /><p>Fraeco<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fraeco has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>closed 26 Mar '15, 02:46</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-40426" class="comments-container"><span id="40860"></span><div id="comment-40860" class="comment"><div id="post-40860-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>I have same problem but with physical machines (no hyperv). The problem appear when the connection pass by a NetASQ Firewall. Have you any solution ?</p></div><div id="comment-40860-info" class="comment-info"><span class="comment-age">(25 Mar '15, 15:01)</span> jboitel</div></div></div><div id="comment-tools-40426" class="comment-tools"></div><div class="clear"></div><div id="comment-40426-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by Jaap 26 Mar '15, 02:46

</div>

</div>

</div>

