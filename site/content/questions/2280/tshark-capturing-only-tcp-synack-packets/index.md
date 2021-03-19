+++
type = "question"
title = "Tshark capturing only TCP SYN/ACK packets"
description = '''Hi, Problem Statement: Tshark captured packet dump contains only TCP SYN / ACK packets. I am using tshark to capture tcp packets flowing towards the HTTP server and Database server. The machine on which tshark is installed is a Win 2K3 Server machine. The machine is having 3 NICs. Command Used: tsha...'''
date = "2011-02-10T20:45:00Z"
lastmod = "2011-02-11T09:54:00Z"
weight = 2280
keywords = [ "tshark" ]
aliases = [ "/questions/2280" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark capturing only TCP SYN/ACK packets](/questions/2280/tshark-capturing-only-tcp-synack-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2280-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p><strong>Problem Statement:</strong> Tshark captured packet dump contains only TCP SYN / ACK packets.</p><p>I am using tshark to capture tcp packets flowing towards the HTTP server and Database server. The machine on which tshark is installed is a <strong>Win 2K3 Server</strong> machine. The machine is having 3 NICs.</p><p><strong>Command Used:</strong> tshark -bfilesize10240 -p -f "tcp and (host 10.64.70.80 and host 10.64.70.81)" -w netpackets.pcap -i "3"</p><p>Thanks, Sreeni</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '11, 20:45</strong></p><img src="https://secure.gravatar.com/avatar/30141052a4a9d856b643341218d7fc4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sreeni&#39;s gravatar image" /><p>sreeni<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sreeni has no accepted answers">0%</span></p></div></div><div id="comments-container-2280" class="comments-container"></div><div id="comment-tools-2280" class="comment-tools"></div><div class="clear"></div><div id="comment-2280-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2282"></span>

<div id="answer-container-2282" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2282-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I suppose you're capturing on the HTTP/Database server - if not, you need to clarify how your setup looks like.</p><p>Maybe the server is using one of the other NICs to transfer all the frames you don't see. I'd try to run a Wireshark instance on each of them at the same time to see if that is the case. If not, you have a weird capture problem where something isn't working like it should.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '11, 08:47</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-2282" class="comments-container"></div><div id="comment-tools-2282" class="comment-tools"></div><div class="clear"></div><div id="comment-2282-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2285"></span>

<div id="answer-container-2285" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2285-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>We ran into this issue several years ago on Windows 2003 with Broadcom NIC (Intel NIC had no issue). Need to make registry change, then reboot:</p><p>My ComputerHKEY_LOCAL_MACHINESYSTEMCurrentControlSetServicesTcpipParameters</p><p>Change from 1 to 0 for:</p><p>EnableRSS EnableTCPA EnableTCPChimney</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '11, 09:54</strong></p><img src="https://secure.gravatar.com/avatar/f24e48940d8b97fd56789ed422038a0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CKC&#39;s gravatar image" /><p>CKC<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CKC has no accepted answers">0%</span></p></div></div><div id="comments-container-2285" class="comments-container"></div><div id="comment-tools-2285" class="comment-tools"></div><div class="clear"></div><div id="comment-2285-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

