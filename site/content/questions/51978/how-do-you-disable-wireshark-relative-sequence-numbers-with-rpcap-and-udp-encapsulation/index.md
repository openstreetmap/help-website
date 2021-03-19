+++
type = "question"
title = "How do you disable wireshark relative sequence numbers with RPCAP and UDP encapsulation?"
description = '''We have recently developed a remote packet capture tool in the form of an SFP that can be plugged into a switch, router or NID. It is capable of bi-directional capture of traffic with 5 tuple filters at line rate. It then adds meta data such as hardware based timestamp, sequence number and length an...'''
date = "2016-04-26T16:46:00Z"
lastmod = "2016-04-27T23:03:00Z"
weight = 51978
keywords = [ "capture", "rpcap", "remote", "sfp", "packet" ]
aliases = [ "/questions/51978" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do you disable wireshark relative sequence numbers with RPCAP and UDP encapsulation?](/questions/51978/how-do-you-disable-wireshark-relative-sequence-numbers-with-rpcap-and-udp-encapsulation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51978-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have recently developed a remote packet capture tool in the form of an SFP that can be plugged into a switch, router or NID. It is capable of bi-directional capture of traffic with 5 tuple filters at line rate. It then adds meta data such as hardware based timestamp, sequence number and length and optionally truncates packets before forwarding as UDP to wireshark using RPCAP protocol.</p><p>Wireshark replaces the original sequence numbers with its own. I see there is a feature with TCP encapsulation to disable Wireshark relative sequence numbers and use the original ones. Is there something equivalent with UDP encapsulation?</p></div><div id="question-tags" class="tags-container tags">capture rpcap remote sfp packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Apr '16, 16:46</strong></p><img src="https://secure.gravatar.com/avatar/6726e1b73f345ac3b9585915ed7a443c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Eitan&#39;s gravatar image" /><p>Eitan<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Eitan has no accepted answers">0%</span></p></div></div><div id="comments-container-51978" class="comments-container"><span id="51995"></span><div id="comment-51995" class="comment"><div id="post-51995-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by <em>sequence numbers</em> with reference to UDP?</p></div><div id="comment-51995-info" class="comment-info"><span class="comment-age">(27 Apr '16, 02:39)</span> grahamb ♦</div></div></div><div id="comment-tools-51978" class="comment-tools"></div><div class="clear"></div><div id="comment-51978-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="52022"></span>

<div id="answer-container-52022" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52022-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>For RPCAP-over-TCP, the sequence numbers are TCP sequence numbers, and the TCP dissector can either display them as the raw sequence numbers in the packet or as sequence numbers relative to the initial sequence number.</p><p>For RPCAP-over-UDP, the sequence numbers are <em>RPCAP</em> sequence numbers, as UDP has no sequence numbers. If you're dissecting the RPCAP protocol, they're <em>always</em> displayed as the raw sequence number.</p><p>However, if by "Wireshark's relative sequence number" you're referring to the <em>packet number column</em>:</p><p>If you're dissecting a local capture that includes RPCAP packets, the <em>packet number column</em> will, as is <em>always</em> the case in Wireshark, be the ordinal number of the packet as seen by Wireshark; not all packets in such a capture are necessarily RPCAP packets, so it makes no sense to use the RPCAP sequence number. You could add the RPCAP sequence number as a custom column. If your sequence number is separate from RPCAP-over-UDP's sequence number, and you want to display <em>that</em> as a column, you could add <em>that</em> as a custom column.</p><p>If you have a <em>remote</em> capture taken using RPCAP, the RPCAP sequence number has been discarded, and there's no way to display it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '16, 11:28</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-52022" class="comments-container"></div><div id="comment-tools-52022" class="comment-tools"></div><div class="clear"></div><div id="comment-52022-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="52029"></span>

<div id="answer-container-52029" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52029-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks Guy,</p><p>Appreciate the explanation. Also learnt today from our system engineering that they found the following work around to see the RPCAP sequence number:<br />
1. Open 1st Wireshark capture on the local PC port<br />
2. Open a 2nd Wireshark and capture from remote smart SFP<br />
3. Look in 1st Wireshark with display filter set to “rpcap and udp”, look for field “rpcap frame number” (this will display the RPCAP packets with the RPCAP encapsulation)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '16, 23:03</strong></p><img src="https://secure.gravatar.com/avatar/6726e1b73f345ac3b9585915ed7a443c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Eitan&#39;s gravatar image" /><p>Eitan<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Eitan has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-52029" class="comments-container"></div><div id="comment-tools-52029" class="comment-tools"></div><div class="clear"></div><div id="comment-52029-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

