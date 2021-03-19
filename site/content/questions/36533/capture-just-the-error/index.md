+++
type = "question"
title = "Capture just the error"
description = '''Hello There, When I run a backup program, I see TCP connection getting re-established once in few days. System error code is 10053 and 10054. Capturing all the wireshark traces for these days might be a huge task. Can I run wireshark and set filter to capture packets only while TCP Reconnection occu...'''
date = "2014-09-23T10:51:00Z"
lastmod = "2014-10-10T07:52:00Z"
weight = 36533
keywords = [ "reconnection", "re-establish", "tcp", "wireshark" ]
aliases = [ "/questions/36533" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture just the error](/questions/36533/capture-just-the-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36533-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello There,</p><p>When I run a backup program, I see TCP connection getting re-established once in few days. System error code is 10053 and 10054. Capturing all the wireshark traces for these days might be a huge task. Can I run wireshark and set filter to capture packets only while TCP Reconnection occurs?<br />
</p><p>I know it is not that easy as I think because we need to capture packets before reconnection too to analyze the traces in detail.</p><p>So, in this scenario, what is the best practice to capture the traces? Should I run wireshark and monitor it until the next TCP reconnection occurs?</p><p>Any help with an example will be much helpful.</p><p>Thanks Santhosh</p></div><div id="question-tags" class="tags-container tags">reconnection re-establish tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Sep '14, 10:51</strong></p><img src="https://secure.gravatar.com/avatar/32fb9474264e66dac4c295002ac0a2dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Santhosh%20Pallikara&#39;s gravatar image" /><p>Santhosh Pal...<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Santhosh Pallikara has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-36533" class="comments-container"><span id="36594"></span><div id="comment-36594" class="comment"><div id="post-36594-score" class="comment-score"></div><div class="comment-text"><p>Perhaps you can clarify exactly what you mean by "TCP Reconnnection". I'm not sure what you mean by that. Do you mean the TCP connection is broken, and a new one is established? If that's the case, there's quite a few ways you could handle this. The first one that comes to my mind is filter on packets where the SYN flag or the RST flag is set.</p><p>In situations where the problem is more likely related to the SYN/ACK/RST stuff, and not in the actual TCP data, you don't need to capture the entire packet. You only need to capture the L2-L4 headers, which can make your trace significantly smaller - helpful in situations with long-running traces. By default, my Linux tcpdump uses a snaplen of 64 bytes which is enough to capture the TCP header and below. You can adjust this parameter in Wireshark using the Edit Interfaces dialog box. dumpcap also has the -s switch.</p><p>There are other techniques to limit the size/number of your traces if you're concerned about size, such has rolling buffers and limiting the number of files. In Wireshark, these can be configured in the Capture Options dialog box.</p></div><div id="comment-36594-info" class="comment-info"><span class="comment-age">(25 Sep '14, 05:58)</span> smp</div></div><span id="36608"></span><div id="comment-36608" class="comment"><div id="post-36608-score" class="comment-score"></div><div class="comment-text"><p>While running a backup, I get a message stating the TCP connetion has reestablished. I wanted to know why it got reestablished. Can you guide me on what flag I could use?</p></div><div id="comment-36608-info" class="comment-info"><span class="comment-age">(25 Sep '14, 11:00)</span> Santhosh Pal...</div></div></div><div id="comment-tools-36533" class="comment-tools"></div><div class="clear"></div><div id="comment-36533-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36960"></span>

<div id="answer-container-36960" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36960-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think your best bet is to run <a href="https://www.wireshark.org/docs/man-pages/dumpcap.html"><code>dumpcap</code></a> instead of Wireshark. If you need to capture for lengthy periods of time, consider using a ring buffer, limiting the size of each file by size and/or by time.</p><p>But yes, you should run <code>dumpcap</code> and monitor it until the next TCP reconnection occurs.</p><p>If you're running on Windows, you might want to take a look at a batch file I posted on the <a href="https://www.wireshark.org/lists/wireshark-users/201405/msg00030.html">wireshark-users</a> mailing list which, when used in combination with <code>mailsend</code>, can even send you an e-mail notification of when a particular capture event of interest occurs. The idea is that you wouldn't have to manually monitor the capturing to figure out when the event occurs, but instead you could be immediately notified whenever it does occur. It's possible to implement your own custom hooks as well. If you do decide to try it, just be sure to read the 2 follow-ups <a href="https://www.wireshark.org/lists/wireshark-users/201405/msg00031.html">here</a> and <a href="https://www.wireshark.org/lists/wireshark-users/201405/msg00032.html">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Oct '14, 07:52</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-36960" class="comments-container"></div><div id="comment-tools-36960" class="comment-tools"></div><div class="clear"></div><div id="comment-36960-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

