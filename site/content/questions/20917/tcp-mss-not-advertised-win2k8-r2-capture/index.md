+++
type = "question"
title = "TCP MSS not advertised Win2k8 r2 Capture"
description = '''Hello. I am running Windows 2008 r2 and have noticed that some of our machines do not advertise the MSS value in the TCP header information. This is odd. Anyone know what may be causing this problem? It is causing internet connectivity problems.'''
date = "2013-05-02T12:35:00Z"
lastmod = "2013-05-30T18:21:00Z"
weight = 20917
keywords = [ "windows", "mss", "tcp" ]
aliases = [ "/questions/20917" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TCP MSS not advertised Win2k8 r2 Capture](/questions/20917/tcp-mss-not-advertised-win2k8-r2-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20917-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello. I am running Windows 2008 r2 and have noticed that some of our machines do not advertise the MSS value in the TCP header information. This is odd. Anyone know what may be causing this problem? It is causing internet connectivity problems.</p></div><div id="question-tags" class="tags-container tags">windows mss tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 May '13, 12:35</strong></p><img src="https://secure.gravatar.com/avatar/892f0bf9e1f4c1e5f667243ce86037f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rogermitan&#39;s gravatar image" /><p>rogermitan<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rogermitan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 May '13, 02:03</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-20917" class="comments-container"></div><div id="comment-tools-20917" class="comment-tools"></div><div class="clear"></div><div id="comment-20917-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20919"></span>

<div id="answer-container-20919" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20919-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please read <a href="http://tools.ietf.org/html/rfc6691">RFC 6691</a>. It is about some 'confusion' how to calculate the MSS value.</p><p>In that document you'll find a reference to <a href="http://tools.ietf.org/html/rfc793">RFC 793</a>, which states:</p><pre><code>      Maximum Segment Size Option Data:  16 bits

         If this option is present, then it communicates the maximum
         receive segment size at the TCP which sends this segment.  This
         field must only be sent in the initial connection request
         (i.e., in segments with the SYN control bit set).  If this
         option is not used, any segment size is allowed.
</code></pre><p>Furthermore: <a href="http://tools.ietf.org/html/rfc1122">RFC 1122</a></p><pre><code>      If an MSS option is not received at connection setup, TCP MUST
      assume a default send MSS of 536 (576-40) [TCP:4].</code></pre><p><strong>Conclusion:</strong> It is possible to omit the MSS value. Why and when Windows 2008 R2 does that is beyond my knowledge. It could be a bug related to this problem (although this one is quite different).</p><blockquote><p><code>http://support.microsoft.com/default.aspx?scid=kb;EN-US;2762983</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '13, 18:04</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 May '13, 18:05</p></div></div><div id="comments-container-20919" class="comments-container"><span id="20985"></span><div id="comment-20985" class="comment"><div id="post-20985-score" class="comment-score"></div><div class="comment-text"><p>Thank you.</p></div><div id="comment-20985-info" class="comment-info"><span class="comment-age">(06 May '13, 05:50)</span> rogermitan</div></div><span id="20995"></span><div id="comment-20995" class="comment"><div id="post-20995-score" class="comment-score"></div><div class="comment-text"><p>If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-20995-info" class="comment-info"><span class="comment-age">(06 May '13, 15:57)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-20919" class="comment-tools"></div><div class="clear"></div><div id="comment-20919-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21628"></span>

<div id="answer-container-21628" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21628-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hello,</p><p>I had the same issue, then in the registry I found:</p><p>EnablePMTUDiscovery</p><p>Key: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters</p><p>Value Type: REG_DWORD - Boolean</p><p>Valid Range: 0,1 (False, True)</p><p>Default: 1 (True)</p><p>Description: If you set this parameter to 1 (True), TCP tries to discover the Maximum Transmission Unit (MTU or largest packet size) over the path to a remote host. By discovering the Path MTU and limiting TCP segments to this size, TCP can eliminate fragmentation at routers along the path that connect networks with different MTUs. Fragmentation adversely affects TCP throughput and causes network congestion. If you set this parameter to 0, an MTU of 576 bytes is used for all connections that are not to computers on the local subnet.</p><p>This was set to "0" on this server. Changing this to "1" fixed this issue.</p><p>Jens</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 May '13, 18:21</strong></p><img src="https://secure.gravatar.com/avatar/a53409151520cf3a863a788f20aeb0cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harsem&#39;s gravatar image" /><p>Harsem<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harsem has no accepted answers">0%</span></p></div></div><div id="comments-container-21628" class="comments-container"></div><div id="comment-tools-21628" class="comment-tools"></div><div class="clear"></div><div id="comment-21628-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

