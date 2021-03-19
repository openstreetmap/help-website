+++
type = "question"
title = "wireshark ICMPV6"
description = '''I find these ICMPV6 router solicitation, router adverts and then the following pops up can I know what are these ? '''
date = "2017-04-22T23:07:00Z"
lastmod = "2017-04-23T09:12:00Z"
weight = 60978
keywords = [ "router", "solicitation", "wireshark" ]
aliases = [ "/questions/60978" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark ICMPV6](/questions/60978/wireshark-icmpv6)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60978-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I find these <img src="https://osqa-ask.wireshark.org/upfiles/Capture1_FdviFNW.PNG" alt="alt text" />ICMPV6 router solicitation, router adverts and <img src="https://osqa-ask.wireshark.org/upfiles/Capture2_qwDI2Tt.PNG" alt="alt text" />then the following pops up can I know what are these ?</p></div><div id="question-tags" class="tags-container tags">router solicitation wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '17, 23:07</strong></p><img src="https://secure.gravatar.com/avatar/4debf4d644c7320e639547bd1b13c1b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="w_keyboard&#39;s gravatar image" /><p>w_keyboard<br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="w_keyboard has no accepted answers">0%</span></p></img></div></div><div id="comments-container-60978" class="comments-container"></div><div id="comment-tools-60978" class="comment-tools"></div><div class="clear"></div><div id="comment-60978-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60987"></span>

<div id="answer-container-60987" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60987-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's just normal IPv6 behavior - the router solicitation is a request for information from a router to find out what network is available. If an advertisement arrives it means that there is an IPv6 enabled router, providing that information. Usually a computer will then create a IPv6 address and start registering to various multicast group (e.g. there is no ARP available for IPv6, so instead you need ICMPv6 multicast to find layer 2 addresses).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '17, 09:12</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></img></div></div><div id="comments-container-60987" class="comments-container"></div><div id="comment-tools-60987" class="comment-tools"></div><div class="clear"></div><div id="comment-60987-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

