+++
type = "question"
title = "Capture filter - tcpdump man page - syntax error?"
description = '''I have found a capture filter in the tcpdump man page (and replicated in several other places) that does not make sense. The filter is: tcp[tcpflags] &amp;amp; (tcp-syn|tcp-fin) != 0 and not src and dst 192.168 Unless I misunderstand - the last part (and not src and dst net) is incorrect. The &quot;not&quot; woul...'''
date = "2013-09-07T12:02:00Z"
lastmod = "2013-09-07T13:07:00Z"
weight = 24448
keywords = [ "capture-filter" ]
aliases = [ "/questions/24448" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture filter - tcpdump man page - syntax error?](/questions/24448/capture-filter-tcpdump-man-page-syntax-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24448-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have found a capture filter in the tcpdump man page (and replicated in several other places) that does not make sense. The filter is:</p><p>tcp[tcpflags] &amp; (tcp-syn|tcp-fin) != 0 and not src and dst 192.168</p><p>Unless I misunderstand - the last part (and not src and dst net) is incorrect. The "not" would only negate src - dst would not be negated.</p><p>Isn't this how that filter would actually have to be entered?</p><p>tcp[tcpflags] &amp; (tcp-syn|tcp-fin) != 0 and not (src or dst net 192.168)</p><p>I've searched the net for over an hour and can't find the explanation - any help at all would be very much appreciated.</p></div><div id="question-tags" class="tags-container tags">capture-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Sep '13, 12:02</strong></p><img src="https://secure.gravatar.com/avatar/eb859ad26d92eb0902b45ba20a167917?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kpalmgren&#39;s gravatar image" /><p>kpalmgren<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kpalmgren has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Sep '13, 12:42</p></div></div><div id="comments-container-24448" class="comments-container"></div><div id="comment-tools-24448" class="comment-tools"></div><div class="clear"></div><div id="comment-24448-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24450"></span>

<div id="answer-container-24450" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24450-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Isn't this how that filter would actually have to be entered?<br />
tcp[tcpflags] &amp; (tcp-syn|tcp-fin) != 0 and not (src or dst net 192.168)</p></blockquote><p>If you print the BPF code for both of these statements, you'll see, that they are the same, meaning the filter is identical.</p><blockquote><p>tcpdump 'tcp[tcpflags] &amp; (tcp-syn|tcp-fin) != 0 and not src and dst net 192.168' -d<br />
tcpdump 'tcp[tcpflags] &amp; (tcp-syn|tcp-fin) != 0 and not (src and dst net 192.168)' -d</p></blockquote><pre><code>(000) ldh      [12]
(001) jeq      #0x800           jt 2    jf 16
(002) ldb      [23]
(003) jeq      #0x6             jt 4    jf 16
(004) ldh      [20]
(005) jset     #0x1fff          jt 16   jf 6
(006) ldxb     4*([14]&amp;0xf)
(007) ldb      [x + 27]
(008) jset     #0x3             jt 9    jf 16
(009) ld       [26]
(010) and      #0xffff0000
(011) jeq      #0xc0a80000      jt 12   jf 15
(012) ld       [30]
(013) and      #0xffff0000
(014) jeq      #0xc0a80000      jt 16   jf 15
(015) ret      #65535
(016) ret      #0</code></pre><p>Without further checking, I would say, that's due to the precedence of the <strong>not</strong> operator. See man page of <a href="http://www.manpagez.com/man/7/pcap-filter/">pcap-filter(7)</a>.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '13, 13:07</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Sep '13, 13:13</p></div></div><div id="comments-container-24450" class="comments-container"></div><div id="comment-tools-24450" class="comment-tools"></div><div class="clear"></div><div id="comment-24450-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

