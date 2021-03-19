+++
type = "question"
title = "TCP PREVIOUS SEGMENT LOST #REALLY RARE CASE#"
description = '''Hi everybody! Currently I&#x27;m in troubleshooting a web communication problem and I say web because a user tries to web browser unsuccessfully an HP multifuntional administration page that it is located in a remote branch that is connected to the main office using an ISP MPLS where the user is. Here co...'''
date = "2012-05-19T15:40:00Z"
lastmod = "2012-05-20T11:00:00Z"
weight = 11146
keywords = [ "packet", "segment", "lost", "tcp", "previous" ]
aliases = [ "/questions/11146" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [TCP PREVIOUS SEGMENT LOST \#REALLY RARE CASE\#](/questions/11146/tcp-previous-segment-lost-really-rare-case)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11146-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everybody!</p><p>Currently I'm in troubleshooting a web communication problem and I say web because a user tries to web browser unsuccessfully an HP multifuntional administration page that it is located in a remote branch that is connected to the main office using an ISP MPLS where the user is. Here comes the rare part, trying to web brower the HP multifuntional administration page locally it works! either in the same network segment or in a different network segment through local routing.</p><p>We already verify network layer connectivity and is fine, I mean, point to point communication is settup a ping from user pc to the HP multifuntional device is successful and a telnet using port 80 from user pc to the HP multifuntional device IP address shows that is open port 80.</p><p>The matter here is when graphic data is requested from a external place of that branch does not work. We have two web services whitin that branch and neither one works from outside.</p><p>We have another branch in the same scenario but it works this is the cause I suspect from the ISP MPLS to the affected branch they may be are filtering something but...</p><p>What you say???</p><p>Next the complete comunication from when user web browser an HP multifuntional administration page in the branch where it actually works <img src="https://osqa-ask.wireshark.org/upfiles/1_2.png" alt="alt text" /></p><p>Now the problematic case <img src="https://osqa-ask.wireshark.org/upfiles/2_3.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">packet segment lost tcp previous</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 May '12, 15:40</strong></p><img src="https://secure.gravatar.com/avatar/fdc605f538d1908942d00975e8f6a575?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MarkNet&#39;s gravatar image" /><p>MarkNet<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MarkNet has no accepted answers">0%</span></p></img></div></div><div id="comments-container-11146" class="comments-container"><span id="11147"></span><div id="comment-11147" class="comment"><div id="post-11147-score" class="comment-score"></div><div class="comment-text"><p>Could you please upload the tracefiles to <a href="http://www.cloudshark.org">http://www.cloudshark.org</a> and paste the two links here? It's not very convenient to do network analysis in a picture viewer instead of Wireshark ;-)</p></div><div id="comment-11147-info" class="comment-info"><span class="comment-age">(19 May '12, 15:57)</span> SYN-bit ♦♦</div></div><span id="11157"></span><div id="comment-11157" class="comment"><div id="post-11157-score" class="comment-score"></div><div class="comment-text"><p>link for not working communication capture <a href="http://www.cloudshark.org/captures/97f3001c88b1">http://www.cloudshark.org/captures/97f3001c88b1</a></p><p>link for working communication capture <a href="http://www.cloudshark.org/captures/c3c0b1767dd7">http://www.cloudshark.org/captures/c3c0b1767dd7</a></p></div><div id="comment-11157-info" class="comment-info"><span class="comment-age">(20 May '12, 10:04)</span> MarkNet</div></div></div><div id="comment-tools-11146" class="comment-tools"></div><div class="clear"></div><div id="comment-11146-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11160"></span>

<div id="answer-container-11160" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11160-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>All the fully-sized segments are missing?! This just looks to me like just another MTU problem and not some really rare case. I'd guess firewall blocks ICMP fragmentation needed but CF bit set messages so they don't appear in the trace.</p><p>Check your MTU at the links and compare with advertised MSS, if that doesn't solve your problem please comment again.</p><p>cheers</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '12, 11:00</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></img></div></div><div id="comments-container-11160" class="comments-container"><span id="11161"></span><div id="comment-11161" class="comment"><div id="post-11161-score" class="comment-score"></div><div class="comment-text"><p>I agree, it looks like an MTU based problem...</p></div><div id="comment-11161-info" class="comment-info"><span class="comment-age">(20 May '12, 11:24)</span> Jasper ♦♦</div></div><span id="11163"></span><div id="comment-11163" class="comment"><div id="post-11163-score" class="comment-score"></div><div class="comment-text"><p>Fine, thanks for your replay on this guys i'll validate it.</p></div><div id="comment-11163-info" class="comment-info"><span class="comment-age">(20 May '12, 11:50)</span> MarkNet</div></div><span id="11194"></span><div id="comment-11194" class="comment"><div id="post-11194-score" class="comment-score"></div><div class="comment-text"><p>yeap, MTU problem :) I just validated the correct MTU to use using different packet sizes in a ping from main office to the branch office once determined I used it on the wan interface of the remote branch where the problem was.</p><p>But just two more questions, since I'm a novice using wireshark how did it look to you another MTU problem?? what did you look at in the capture file??</p><p>Thanks a lot for your help guys!! cheers</p></div><div id="comment-11194-info" class="comment-info"><span class="comment-age">(21 May '12, 21:01)</span> MarkNet</div></div><span id="11197"></span><div id="comment-11197" class="comment"><div id="post-11197-score" class="comment-score">1</div><div class="comment-text"><p>Four signs for me:</p><ol><li>the difference of the MSS announced by the client (1260) and the server (1460). However this is a weak sign.</li><li>the largest packet has a size of 654 bytes, so all the large packets (up to the possible MSS) were missing.</li><li>the SEQ number of the packet 13 with a delta of 2741 bytes to the previous frame (that's why wireshark marked it with "previous segment lost). 4.) the behaviour of the same server software in the working example, with packtes up to 1314 bytes length (these are missing in the non working sample)</li></ol><p>Regards<br />
Kurt</p></div><div id="comment-11197-info" class="comment-info"><span class="comment-age">(21 May '12, 23:07)</span> Kurt Knochner ♦</div></div><span id="11226"></span><div id="comment-11226" class="comment"><div id="post-11226-score" class="comment-score"></div><div class="comment-text"><p>Alright, very thanks Kurt!!</p><p>Regards, Mark</p></div><div id="comment-11226-info" class="comment-info"><span class="comment-age">(22 May '12, 15:03)</span> MarkNet</div></div><span id="11228"></span><div id="comment-11228" class="comment not_top_scorer"><div id="post-11228-score" class="comment-score"></div><div class="comment-text"><p>For me - and probably @Landi - it was mostly @Kurt's number 2. It is a common pattern that when you compare traces that work and do not work you'll see the working one with packets has full size segments while the nonworking doesn't.</p><p>Oh, and I have to admit that after 10 years of doing network analysis there is a fair amount of "gut feeling" involved :-D ...which still needs to be verified each time, of course ;-)</p></div><div id="comment-11228-info" class="comment-info"><span class="comment-age">(22 May '12, 17:16)</span> Jasper ♦♦</div></div></div><div id="comment-tools-11160" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-11160-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

