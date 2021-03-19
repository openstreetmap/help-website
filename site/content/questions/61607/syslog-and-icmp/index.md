+++
type = "question"
title = "Syslog and ICMP"
description = '''What is the capture filter for getting both Syslog and ICMP Captures?'''
date = "2017-05-24T09:51:00Z"
lastmod = "2017-05-24T13:47:00Z"
weight = 61607
keywords = [ "and", "syslog", "icmp" ]
aliases = [ "/questions/61607" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Syslog and ICMP](/questions/61607/syslog-and-icmp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61607-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What is the capture filter for getting both Syslog and ICMP Captures?</p></div><div id="question-tags" class="tags-container tags">and syslog icmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 May '17, 09:51</strong></p><img src="https://secure.gravatar.com/avatar/6569b989bf5cfedd50dd1489c3dd2b9c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="praveen453&#39;s gravatar image" /><p>praveen453<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="praveen453 has no accepted answers">0%</span></p></div></div><div id="comments-container-61607" class="comments-container"></div><div id="comment-tools-61607" class="comment-tools"></div><div class="clear"></div><div id="comment-61607-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61609"></span>

<div id="answer-container-61609" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61609-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming that Syslog is transported over UDP port 514:</p><p><code>udp port 514 or icmp</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 May '17, 13:47</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-61609" class="comments-container"><span id="61614"></span><div id="comment-61614" class="comment"><div id="post-61614-score" class="comment-score"></div><div class="comment-text"><p>No, I tried above command before but it is giving only syslog capture but not both as the function is "or", i used below command udp dst port 514 or icmp</p></div><div id="comment-61614-info" class="comment-info"><span class="comment-age">(24 May '17, 23:10)</span> praveen453</div></div><span id="61624"></span><div id="comment-61624" class="comment"><div id="post-61624-score" class="comment-score"></div><div class="comment-text"><p>Well, this is the BPF (for Ethernet) if you're interested:</p><pre><code>(000) ldh      [12]
(001) jeq      #0x86dd          jt 2    jf 6
(002) ldb      [20]
(003) jeq      #0x11            jt 4    jf 16
(004) ldh      [56]
(005) jeq      #0x202           jt 15   jf 16
(006) jeq      #0x800           jt 7    jf 16
(007) ldb      [23]
(008) jeq      #0x11            jt 9    jf 14
(009) ldh      [20]
(010) jset     #0x1fff          jt 16   jf 11
(011) ldxb     4*([14]&amp;0xf)
(012) ldh      [x + 16]
(013) jeq      #0x202           jt 15   jf 16
(014) jeq      #0x1             jt 15   jf 16
(015) ret      #262144
(016) ret      #0</code></pre><p>Maybe, when looking at the frame, you can figure out why it's not working for you. If VLAN is involved prefix the filter with the vlan keyword.</p></div><div id="comment-61624-info" class="comment-info"><span class="comment-age">(25 May '17, 07:56)</span> Jaap ♦</div></div></div><div id="comment-tools-61609" class="comment-tools"></div><div class="clear"></div><div id="comment-61609-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

