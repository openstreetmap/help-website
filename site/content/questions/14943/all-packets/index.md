+++
type = "question"
title = "all packets"
description = '''are there packets wireshark will not capture? I am trying to watch a link between my router and a destination server but I do not see the traffic. I seem to see quite a bit of traffic but not to the server the router is supposed to be sending to.'''
date = "2012-10-11T17:55:00Z"
lastmod = "2012-10-17T10:50:00Z"
weight = 14943
keywords = [ "packets" ]
aliases = [ "/questions/14943" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [all packets](/questions/14943/all-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14943-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>are there packets wireshark will not capture? I am trying to watch a link between my router and a destination server but I do not see the traffic. I seem to see quite a bit of traffic but not to the server the router is supposed to be sending to.</p></div><div id="question-tags" class="tags-container tags">packets</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '12, 17:55</strong></p><img src="https://secure.gravatar.com/avatar/0fb63e8bfffe6bddd3ea24968f415345?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wrcooke&#39;s gravatar image" /><p>wrcooke<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wrcooke has no accepted answers">0%</span></p></div></div><div id="comments-container-14943" class="comments-container"><span id="14947"></span><div id="comment-14947" class="comment"><div id="post-14947-score" class="comment-score"></div><div class="comment-text"><p>You've got to be a little more specific than this...</p></div><div id="comment-14947-info" class="comment-info"><span class="comment-age">(11 Oct '12, 23:13)</span> Jaap ♦</div></div><span id="14957"></span><div id="comment-14957" class="comment"><div id="post-14957-score" class="comment-score"></div><div class="comment-text"><p>I wish I could be vastly more specific but I see the app running on the router talking to a server but wireshark does not see that conversation. This is why I ask if there are packet types wireshark cannot capture.</p></div><div id="comment-14957-info" class="comment-info"><span class="comment-age">(12 Oct '12, 03:55)</span> wrcooke</div></div><span id="14958"></span><div id="comment-14958" class="comment"><div id="post-14958-score" class="comment-score"></div><div class="comment-text"><p>Do you mean you don't see any packets on wireshark? Are you capturing on correct interface? And what is this app you're talking about?</p></div><div id="comment-14958-info" class="comment-info"><span class="comment-age">(12 Oct '12, 04:03)</span> rakki</div></div><span id="14959"></span><div id="comment-14959" class="comment"><div id="post-14959-score" class="comment-score"></div><div class="comment-text"><p>This is most likely a problem related to how the capture setup is done, so you should tell us how you are capturing the data. If you're just attached to the router, and the server has it's own line, you'll not see much of their communication since it is switched.</p></div><div id="comment-14959-info" class="comment-info"><span class="comment-age">(12 Oct '12, 04:28)</span> Jasper ♦♦</div></div><span id="15040"></span><div id="comment-15040" class="comment"><div id="post-15040-score" class="comment-score"></div><div class="comment-text"><p>I might be wrong about this, so someone please correct me if I am, but since Wireshark capture naturally runs above the kernel it can't capture packets that don't appear at higher levels. This may be due to driver or something that maybe filters or redirects the packets. Could this possibly be the problem in your case?</p></div><div id="comment-15040-info" class="comment-info"><span class="comment-age">(16 Oct '12, 22:30)</span> SidR</div></div></div><div id="comment-tools-14943" class="comment-tools"></div><div class="clear"></div><div id="comment-14943-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15062"></span>

<div id="answer-container-15062" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15062-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>but since Wireshark capture naturally runs above the kernel it can't capture packets that don't appear at higher levels.</p></blockquote><p>Wireshark itself runs "above" the kernel (in userspace), but it has a direct "link" to the kernel via libpcap/winpcap (dumpcap) and thus it will get all packets from the kernel, no matter which protocol level. However, there might be "interfering" software installed on the capturing device, that filters packets before they are handed over to libpcap/winpcap.</p><blockquote><p><code>http://wiki.wireshark.org/CaptureSetup/InterferingSoftware</code><br />
</p></blockquote><p>According to the description of the OP, I think the Capture Setup is not correct.</p><blockquote><p><code>http://wiki.wireshark.org/CaptureSetup/Ethernet</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '12, 10:50</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-15062" class="comments-container"></div><div id="comment-tools-15062" class="comment-tools"></div><div class="clear"></div><div id="comment-15062-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

