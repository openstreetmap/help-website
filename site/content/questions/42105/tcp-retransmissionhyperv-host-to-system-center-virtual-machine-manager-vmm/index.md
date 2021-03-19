+++
type = "question"
title = "[TCP retransmission]hyperV host to system center Virtual Machine Manager VMM"
description = '''Question: We are getting a lot of Expert(error notifications) about TCP Retransmissions, Reassembly error; New Fragment overlaps old data.(retransmission?). The offending packets are happening between a hyperV node and the VMM. Should we be concerned or is this is false positive.  both servers are p...'''
date = "2015-05-05T13:21:00Z"
lastmod = "2015-05-08T04:06:00Z"
weight = 42105
keywords = [ "retransmission", "reassembly", "hyperv", "microsoft", "error" ]
aliases = [ "/questions/42105" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [\[TCP retransmission\]hyperV host to system center Virtual Machine Manager VMM](/questions/42105/tcp-retransmissionhyperv-host-to-system-center-virtual-machine-manager-vmm)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42105-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Question: We are getting a lot of Expert(error notifications) about TCP Retransmissions, Reassembly error; New Fragment overlaps old data.(retransmission?).</p><p>The offending packets are happening between a hyperV node and the VMM. Should we be concerned or is this is false positive.</p><p>both servers are plugged in to the same switch, the hyper V node has a dedicated port and virtual network created for our server lan. The vmm is just a server that sits on the same vlan natively.</p><p>Summary...</p><pre><code>3035    0.983810000 172.31.1.89 172.31.1.78 TCP 318 Note    [TCP Retransmission] 52503→5985 [PSH, ACK] Seq=2407 Ack=2911 Win=4100 Len=264
3036    0.983863000 172.31.1.89 172.31.1.78 TCP 1514        [TCP segment of a reassembled PDU]
3037    0.983864000 172.31.1.89 172.31.1.78 TCP 1514    Note    [TCP Retransmission] [TCP segment of a reassembled PDU]
3038    0.983865000 172.31.1.89 172.31.1.78 HTTP    736 Error   POST /wsman HTTP/1.1 [Malformed Packet]
3039    0.983866000 172.31.1.89 172.31.1.78 TCP 736 Error   [TCP Retransmission] 52503→5985 [PSH, ACK] Seq=4131 Ack=2911 Win=4100 Len=682[Reassembly error, protocol TCP: New fragment overlaps old data (retransmission?)]</code></pre></div><div id="question-tags" class="tags-container tags">retransmission reassembly hyperv microsoft error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 May '15, 13:21</strong></p><img src="https://secure.gravatar.com/avatar/e91f091a9af05e5f7680e618506c48e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quorrum&#39;s gravatar image" /><p>Quorrum<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quorrum has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 May '15, 14:03</p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-42105" class="comments-container"><span id="42106"></span><div id="comment-42106" class="comment"><div id="post-42106-score" class="comment-score"></div><div class="comment-text"><p>also check the switch ports and there are no errors.</p></div><div id="comment-42106-info" class="comment-info"><span class="comment-age">(05 May '15, 13:22)</span> Quorrum</div></div><span id="42108"></span><div id="comment-42108" class="comment"><div id="post-42108-score" class="comment-score"></div><div class="comment-text"><p>sounds more like false positives... but maybe you can upload a capture file at <a href="http://www.cloudshark.org">http://www.cloudshark.org</a> and post the link here? It's easier to check a trace than some ASCII dump.</p></div><div id="comment-42108-info" class="comment-info"><span class="comment-age">(05 May '15, 14:05)</span> Jasper ♦♦</div></div><span id="42134"></span><div id="comment-42134" class="comment"><div id="post-42134-score" class="comment-score"></div><div class="comment-text"><p>here is a chopped, cap. Any help with this is appreciated. <a href="https://www.cloudshark.org/captures/64c49f52f75e">https://www.cloudshark.org/captures/64c49f52f75e</a></p></div><div id="comment-42134-info" class="comment-info"><span class="comment-age">(06 May '15, 08:17)</span> Quorrum</div></div><span id="42135"></span><div id="comment-42135" class="comment"><div id="post-42135-score" class="comment-score"></div><div class="comment-text"><p>my issues are the dup ACk's and ReTransmissions. These seem like waste of band... Should i be worried about these.</p></div><div id="comment-42135-info" class="comment-info"><span class="comment-age">(06 May '15, 08:19)</span> Quorrum</div></div></div><div id="comment-tools-42105" class="comment-tools"></div><div class="clear"></div><div id="comment-42105-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="42194"></span>

<div id="answer-container-42194" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42194-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>we are chalking these up to false positives and microsoft doing some thing as usual that they are not supposed to be doing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '15, 13:08</strong></p><img src="https://secure.gravatar.com/avatar/e91f091a9af05e5f7680e618506c48e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quorrum&#39;s gravatar image" /><p>Quorrum<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quorrum has one accepted answer">100%</span></p></div></div><div id="comments-container-42194" class="comments-container"></div><div id="comment-tools-42194" class="comment-tools"></div><div class="clear"></div><div id="comment-42194-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42206"></span>

<div id="answer-container-42206" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42206-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, since every frame is seen twice, did you by any chance capture on a span-port with the source being a vlan? Then it is a capturing artefact as every frame with first enter the vlan and then exit the vlan. When capturing on a vlan, better use "rx only" instead of "both".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 May '15, 04:06</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-42206" class="comments-container"><span id="42221"></span><div id="comment-42221" class="comment"><div id="post-42221-score" class="comment-score"></div><div class="comment-text"><p>monitor session 1 source vlan 100 monitor session 1 destination interface Gi9/18 monitor session 1 filter packet-type good rx</p><p>only isnt an option.</p><p>ad.m.1(config)#monitor session 1 filter packet-type good rx ? &lt;cr&gt;</p></div><div id="comment-42221-info" class="comment-info"><span class="comment-age">(08 May '15, 10:20)</span> Quorrum</div></div><span id="42222"></span><div id="comment-42222" class="comment"><div id="post-42222-score" class="comment-score"></div><div class="comment-text"><p>good idea i was under the assumption that is was only. i will look in to that.</p></div><div id="comment-42222-info" class="comment-info"><span class="comment-age">(08 May '15, 10:21)</span> Quorrum</div></div><span id="42224"></span><div id="comment-42224" class="comment"><div id="post-42224-score" class="comment-score"></div><div class="comment-text"><p>I don't have a cisco switch at hand, but it should be something like:</p><pre><code>monitor session 1 source vlan 100 rx
monitor session 1 destination interface Gi9/18</code></pre></div><div id="comment-42224-info" class="comment-info"><span class="comment-age">(08 May '15, 10:39)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-42206" class="comment-tools"></div><div class="clear"></div><div id="comment-42206-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

