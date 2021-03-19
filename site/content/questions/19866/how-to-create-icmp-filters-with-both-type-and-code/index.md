+++
type = "question"
title = "How to create ICMP filters with both type and code ?"
description = '''ICMP filter filtering only Destination Unreachable(type) - icmp[0] == 3 . ICMP filter filtering Destination Unreachable(type),Destination host unreachable(code) - icmp[0:2] == ? Regards Dinged'''
date = "2013-03-27T06:14:00Z"
lastmod = "2013-03-27T09:35:00Z"
weight = 19866
keywords = [ "capture-filter", "icmp" ]
aliases = [ "/questions/19866" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to create ICMP filters with both type and code ?](/questions/19866/how-to-create-icmp-filters-with-both-type-and-code)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19866-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>ICMP filter filtering only Destination Unreachable(type) - icmp[0] == 3 .</p><p>ICMP filter filtering Destination Unreachable(type),Destination host unreachable(code) - icmp[0:2] == ?</p><p>Regards Dinged</p></div><div id="question-tags" class="tags-container tags">capture-filter icmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Mar '13, 06:14</strong></p><img src="https://secure.gravatar.com/avatar/9b52984d9786885d47fe81e43d8591ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dinged&#39;s gravatar image" /><p>Dinged<br />
<span class="score" title="36 reputation points">36</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dinged has no accepted answers">0%</span></p></div></div><div id="comments-container-19866" class="comments-container"></div><div id="comment-tools-19866" class="comment-tools"></div><div class="clear"></div><div id="comment-19866-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19875"></span>

<div id="answer-container-19875" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19875-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>The capture filter you are probably thinking of is:</p><pre><code>icmp[0:2]==0x0301</code></pre><p>But to be more descriptive, you could use something like this instead:</p><pre><code>icmp[icmptype]==icmp-unreach and icmp[icmpcode]==1</code></pre><p>Note that the compiled BPF code isn't exactly the same though. It seems that the first format is slightly more efficient, taking 2 fewer instructions.</p><p>Compare <code>icmp[0:2]==0x0301</code>:</p><pre><code>(000) ldh      [12]
(001) jeq      #0x800           jt 2    jf 10
(002) ldb      [23]
(003) jeq      #0x1             jt 4    jf 10
(004) ldh      [20]
(005) jset     #0x1fff          jt 10   jf 6
(006) ldxb     4*([14]&amp;0xf)
(007) ldh      [x + 14]
(008) jeq      #0x301           jt 9    jf 10
(009) ret      #65535
(010) ret      #0</code></pre><p>to <code>icmp[icmptype]==icmp-unreach and icmp[icmpcode]==1</code>:</p><pre><code>(000) ldh      [12]
(001) jeq      #0x800           jt 2    jf 12
(002) ldb      [23]
(003) jeq      #0x1             jt 4    jf 12
(004) ldh      [20]
(005) jset     #0x1fff          jt 12   jf 6
(006) ldxb     4*([14]&amp;0xf)
(007) ldb      [x + 14]
(008) jeq      #0x3             jt 9    jf 12
(009) ldb      [x + 15]
(010) jeq      #0x1             jt 11   jf 12
(011) ret      #65535
(012) ret      #0</code></pre><p>Refer to the <a href="http://www.manpagez.com/man/7/pcap-filter/">pcap-filter</a> man page for more information.</p><p>(If instead you're looking for a Wireshark display filter, then refer to pfuender's answer.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '13, 09:35</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Mar '13, 20:56</p></div></div><div id="comments-container-19875" class="comments-container"><span id="19891"></span><div id="comment-19891" class="comment"><div id="post-19891-score" class="comment-score"></div><div class="comment-text"><p>Great detailed answer. I am wondering how does the hex value 0x0301 come about ? 03 = type 3, 01 = code 1 ?</p></div><div id="comment-19891-info" class="comment-info"><span class="comment-age">(27 Mar '13, 20:15)</span> Dinged</div></div><span id="19893"></span><div id="comment-19893" class="comment"><div id="post-19893-score" class="comment-score">1</div><div class="comment-text"><p>The 1st byte of an ICMP packet is the type, and type 3 is the "Destination Unreachable" message. The 2nd byte of the ICMP packet is the code, and code 1 of a "Destination Unreachable" message is "host unreachable". For more details refer to <a href="http://tools.ietf.org/html/rfc792">RFC 792</a> or to your favorite on-line help for ICMP, such as <a href="http://www.inacon.de/ph/data/ICMP/Header_fields/ICMP-Messag-Field-Code_OS_RFC-792-IANA.htm">Inacon's help for the ICMP code field</a> or even <a href="http://en.wikipedia.org/wiki/Internet_Control_Message_Protocol#Destination_unreachable">wikipedia's article on ICMP</a>.</p></div><div id="comment-19893-info" class="comment-info"><span class="comment-age">(27 Mar '13, 21:02)</span> cmaynard ♦♦</div></div><span id="19906"></span><div id="comment-19906" class="comment"><div id="post-19906-score" class="comment-score"></div><div class="comment-text"><p>Oh, after reading Inacon's guide, then did I know that the type and code values are actually hex values. Thanks for the link to this great resource.</p></div><div id="comment-19906-info" class="comment-info"><span class="comment-age">(28 Mar '13, 07:33)</span> Dinged</div></div></div><div id="comment-tools-19875" class="comment-tools"></div><div class="clear"></div><div id="comment-19875-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19868"></span>

<div id="answer-container-19868" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19868-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can combine several filters using '&amp;&amp;', so you can use the two filters as you've requested. Here's an example to only show ICMP 'Host Unreachable' messages:</p><pre><code>(icmp.type==3) &amp;&amp; (icmp.code==1)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '13, 07:12</strong></p><img src="https://secure.gravatar.com/avatar/7141e1bec61c168ead9f00d304b75859?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pfuender&#39;s gravatar image" /><p>pfuender<br />
<span class="score" title="56 reputation points">56</span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pfuender has no accepted answers">0%</span></p></div></div><div id="comments-container-19868" class="comments-container"><span id="19892"></span><div id="comment-19892" class="comment"><div id="post-19892-score" class="comment-score"></div><div class="comment-text"><p>Sorry for not being clear in the question, I am looking for a capture filter. But nevertheless, good to know. :D</p></div><div id="comment-19892-info" class="comment-info"><span class="comment-age">(27 Mar '13, 20:15)</span> Dinged</div></div></div><div id="comment-tools-19868" class="comment-tools"></div><div class="clear"></div><div id="comment-19868-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

