+++
type = "question"
title = "Relation between packet number and time"
description = '''Packet 1 2 3 4 5 time .00001 .00002 .00005 .00006 .00004'''
date = "2015-05-26T12:59:00Z"
lastmod = "2015-05-26T13:57:00Z"
weight = 42669
keywords = [ "sequence" ]
aliases = [ "/questions/42669" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Relation between packet number and time](/questions/42669/relation-between-packet-number-and-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42669-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Packet 1 2 3 4 5 time .00001 .00002 .00005 .00006 .00004</p></div><div id="question-tags" class="tags-container tags">sequence</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 May '15, 12:59</strong></p><img src="https://secure.gravatar.com/avatar/640f31c3684eea11e2848f86425d506f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stobbe99&#39;s gravatar image" /><p>stobbe99<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stobbe99 has no accepted answers">0%</span></p></div></div><div id="comments-container-42669" class="comments-container"><span id="42670"></span><div id="comment-42670" class="comment"><div id="post-42670-score" class="comment-score"></div><div class="comment-text"><p>Is this the out sink sequence between number and time an issue?</p></div><div id="comment-42670-info" class="comment-info"><span class="comment-age">(26 May '15, 13:01)</span> stobbe99</div></div></div><div id="comment-tools-42669" class="comment-tools"></div><div class="clear"></div><div id="comment-42669-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42674"></span>

<div id="answer-container-42674" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42674-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is this the out sink sequence between number and time an issue?</p></blockquote><p>It (most certainly) means one of the following things:</p><ul><li>you have captured on several interfaces in parallel</li><li>you have merged several pcap files into one file</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 May '15, 13:57</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-42674" class="comments-container"><span id="42677"></span><div id="comment-42677" class="comment"><div id="post-42677-score" class="comment-score"></div><div class="comment-text"><p>Kurt,</p><p>And when I see this on one interface? I really see packets with a higher sequence number arriving before some packets with a lower sequence number.</p><p>KR Henk</p></div><div id="comment-42677-info" class="comment-info"><span class="comment-age">(26 May '15, 14:11)</span> stobbe99</div></div><span id="42678"></span><div id="comment-42678" class="comment"><div id="post-42678-score" class="comment-score"></div><div class="comment-text"><p>The OS delivering packets to the packet capture mechanism out of order? I've seen that happen on multiprocessor/multicore Linux systems, for example; it may be that the packet that arrives on the host first (and gets an earlier time stamp) ends up arriving at the PF_PACKET socket after another packet that arrived later on the host.</p></div><div id="comment-42678-info" class="comment-info"><span class="comment-age">(26 May '15, 14:52)</span> Guy Harris ♦♦</div></div><span id="42687"></span><div id="comment-42687" class="comment"><div id="post-42687-score" class="comment-score"></div><div class="comment-text"><p>Guy,</p><p>Yes it is a multicore linux system, is this a problem for wireshark?</p><p>KR Henk</p></div><div id="comment-42687-info" class="comment-info"><span class="comment-age">(26 May '15, 19:56)</span> stobbe99</div></div><span id="42689"></span><div id="comment-42689" class="comment"><div id="post-42689-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Yes it is a multicore linux system, is this a problem for wireshark?</p></blockquote><p>If by that do you mean "is this a problem for programs that capture packets using PF_PACKET sockets, such as programs using libpcap, one of which is dumpcap, the program that Wireshark uses to capture packets" :-), the answer is "yes", but the answer also means "trying another program, such as tcpdump, which <em>also</em> uses libpcap, won't help".</p><p>It might be possible to make libpcap work around that "feature" of Linux, but that would take some work.</p></div><div id="comment-42689-info" class="comment-info"><span class="comment-age">(26 May '15, 22:05)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-42674" class="comment-tools"></div><div class="clear"></div><div id="comment-42674-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

