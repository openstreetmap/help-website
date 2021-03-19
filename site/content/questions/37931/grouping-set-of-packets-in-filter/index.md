+++
type = "question"
title = "Grouping set of packets in filter"
description = '''Just started using wireshark, and I am trying to follow server / client TCP flow.. We are running ATM business where i just want to make sure TCP flow is as expected from socket. For example, if I want to group these message with custom color what should be done: Client to Server request (PSH MSG)--...'''
date = "2014-11-17T22:41:00Z"
lastmod = "2014-11-17T22:41:00Z"
weight = 37931
keywords = [ "capture-filter", "tcp", "display-filter" ]
aliases = [ "/questions/37931" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Grouping set of packets in filter](/questions/37931/grouping-set-of-packets-in-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37931-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Just started using wireshark, and I am trying to follow server / client TCP flow..</p><p>We are running ATM business where i just want to make sure TCP flow is as expected from socket.</p><p>For example, if I want to group these message with custom color what should be done:</p><pre><code>Client to Server request (PSH MSG)----
                                    ||
---       Server to Client (PSH ACK)
||
SERVER to RESPOND (PSH MSG) ------
                                    ||
    Server to Client (PSH ACK)-----</code></pre><p>For the above flow I have manually HIGHIGHTED a set of packet. Need guidance in handling these type of filters with wireshark.</p><pre><code>1398    37977.393994    172.11.105.5    172.250.10.10   TCP 41831 &gt; 13824 [PSH, ACK] Seq=3792 Ack=5868 Win=2003 Len=119 TSV=84371804 TSER=720051399
1399    37977.518972    172.250.10.10   172.11.105.5    TCP 13824 &gt; 41831 [ACK] Seq=5868 Ack=3911 Win=17680 Len=0 TSV=720058937 TSER=84371804
1400    37977.882262    172.250.10.10   172.11.105.5    TCP 13824 &gt; 41831 [PSH, ACK] Seq=5868 Ack=3911 Win=17680 Len=251 TSV=720058973 TSER=84371804
1401    37977.882354    172.11.105.5    172.250.10.10   TCP 41831 &gt; 13824 [ACK] Seq=3911 Ack=6119 Win=2003 Len=0 TSV=84371926 TSER=720058973</code></pre><p>Sample highlighted image:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/packet.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">capture-filter tcp display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Nov '14, 22:41</strong></p><img src="https://secure.gravatar.com/avatar/6ad04bff031b8e9268cd4e2e2930d182?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ragav&#39;s gravatar image" /><p>Ragav<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ragav has no accepted answers">0%</span></p></img></div></div><div id="comments-container-37931" class="comments-container"></div><div id="comment-tools-37931" class="comment-tools"></div><div class="clear"></div><div id="comment-37931-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

