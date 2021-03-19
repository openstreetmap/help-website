+++
type = "question"
title = "Header Checksum error (incorrect, should be ....)"
description = '''Hi there, It has been a while that I&#x27;m experiencing some problems on my network, as I&#x27;m not the network admin and I&#x27;ve got from them the info that everything is OK on the network side I&#x27;ll need your help to investigate what&#x27;s going on.  I&#x27;ve started the capture and most of the packets had the Checks...'''
date = "2012-08-13T04:09:00Z"
lastmod = "2012-08-13T04:31:00Z"
weight = 13577
keywords = [ "checksum", "wireshark" ]
aliases = [ "/questions/13577" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Header Checksum error (incorrect, should be ....)](/questions/13577/header-checksum-error-incorrect-should-be)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13577-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>It has been a while that I'm experiencing some problems on my network, as I'm not the network admin and I've got from them the info that everything is OK on the network side I'll need your help to investigate what's going on.</p><p>I've started the capture and most of the packets had the Checksum error, I've deactivated this filter as per some other post recommendation to see what is left and I can see a couple of packets, when i go to detail window expand the Internet Protocal and the Header, it shows a red highlight on the Header and then on Bad:True, also says Header checksum: 0x0000 [incorrect, should be 0x822f], this 0x822f is replaced by many other numbers for the other packets.</p><p>Can you help me on this troubleshoot? I can post the capture if necessary.</p><p>Regards, WRIBEIRO</p></div><div id="question-tags" class="tags-container tags">checksum wireshark</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Aug '12, 04:09</strong></p><img src="https://secure.gravatar.com/avatar/8ea5bd54ac085478e4a331d9a2904750?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WRIBEIRO&#39;s gravatar image" /><p>WRIBEIRO<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WRIBEIRO has no accepted answers">0%</span></p></div></div><div id="comments-container-13577" class="comments-container"></div><div id="comment-tools-13577" class="comment-tools"></div><div class="clear"></div><div id="comment-13577-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="13579"></span>

<div id="answer-container-13579" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13579-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please check if the packets with checksum errors are packets your machine is sending out to the network. If they are, and none of the incoming packets have errors, you can ignore these CRC error messages - they're a result of you capturing your own traffic locally with network card optimizations enabled.</p><p>Especially the 0x0000 is a typical value for a placeholder when the NIC does the checksum calculation later (after Wireshark captured the packet already).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '12, 04:22</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-13579" class="comments-container"><span id="13584"></span><div id="comment-13584" class="comment"><div id="post-13584-score" class="comment-score"></div><div class="comment-text"><p>There you go, when I sort if from my machine the error comes up, when i sort from my "destination" it goes away. Less one problem. Now i need to find out why, it's so slow. I have a bunch of TPKT - Continuation coming from my server. And also a lot of TCP segment of a reassembled PDU, any clue on that?</p></div><div id="comment-13584-info" class="comment-info"><span class="comment-age">(13 Aug '12, 06:06)</span> WRIBEIRO</div></div><span id="13589"></span><div id="comment-13589" class="comment"><div id="post-13589-score" class="comment-score"></div><div class="comment-text"><p>"Segment of a reassembled PDU" is not an error, it is a message that Wireshark considers the packet being a part of a larger payload. You can disable the packet reassembly in the TCP protocol preferences by unchecking "Allow subdisector to reassemble TCP streams".</p><p>Continuation messages are a similar thing - Wireshark tells you that the packet contains more parts of a payload.</p><p>If you try to figure out why communication is slow you should check delta times between requests and answers, the throughput achieved (see Statistics/Conversations/TCP) and filter for problems using tcp.analysis.flags</p></div><div id="comment-13589-info" class="comment-info"><span class="comment-age">(13 Aug '12, 08:21)</span> Jasper ♦♦</div></div></div><div id="comment-tools-13579" class="comment-tools"></div><div class="clear"></div><div id="comment-13579-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13580"></span>

<div id="answer-container-13580" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13580-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>As Jasper says, the errors are often caused by the network driver calculating the checksum after Wireshark has captured it. You can turn off the display of these errant errors by:</p><p>For IP checksums right click on the IP part of the frame in the packet details pane (the tree) and go into Protocol Preferences and uncheck "Validate the IPv4 checksum if possible". You may also want to check "Support packet-capture from IP TSO-enabled hardware".</p><p>For TCP checksums, right click on the TCP part of the frame, and again in Protocol Preferences uncheck "Validate the TCP checksum if possible".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '12, 04:31</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-13580" class="comments-container"><span id="13585"></span><div id="comment-13585" class="comment"><div id="post-13585-score" class="comment-score"></div><div class="comment-text"><p>Hi Grahamb,</p><p>Thanks for the info, useful indeed. After your trick the black and red just went off. I've posted another problem, I meant the second phase of this problem above, on Jasper block, any clue on that? Thanks</p></div><div id="comment-13585-info" class="comment-info"><span class="comment-age">(13 Aug '12, 06:08)</span> WRIBEIRO</div></div><span id="13586"></span><div id="comment-13586" class="comment"><div id="post-13586-score" class="comment-score"></div><div class="comment-text"><p>You should really open another question for that (after searching for a similar one first) rather than trying to change this question to your next problem.</p></div><div id="comment-13586-info" class="comment-info"><span class="comment-age">(13 Aug '12, 06:42)</span> grahamb ♦</div></div></div><div id="comment-tools-13580" class="comment-tools"></div><div class="clear"></div><div id="comment-13580-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

