+++
type = "question"
title = "llmnr packets data flow"
description = '''what the reason of llmnr packets flow in non ad-hoc network?significant number llmnr protocol packets in one capture can be vulnaribility or victim?'''
date = "2016-12-13T22:29:00Z"
lastmod = "2016-12-14T08:47:00Z"
weight = 58065
keywords = [ "netflow", "data" ]
aliases = [ "/questions/58065" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [llmnr packets data flow](/questions/58065/llmnr-packets-data-flow)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58065-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>what the reason of llmnr packets flow in non ad-hoc network?significant number llmnr protocol packets in one capture can be vulnaribility or victim?</p></div><div id="question-tags" class="tags-container tags">netflow data</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Dec '16, 22:29</strong></p><img src="https://secure.gravatar.com/avatar/5bb19a01c4e56b8f9fbb907b717a5f6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="acropo&#39;s gravatar image" /><p>acropo<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="acropo has no accepted answers">0%</span></p></div></div><div id="comments-container-58065" class="comments-container"></div><div id="comment-tools-58065" class="comment-tools"></div><div class="clear"></div><div id="comment-58065-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58084"></span>

<div id="answer-container-58084" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58084-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>LLMNR is the link layer multicast name resolution. This protocol is protocol is used by Windows systems as fallback if they could not translate a hostname to an IP address through DNS.</p><p>The presence of LLMNR packet shows, that certain hostnames could not be translated.</p><p>LLMNR is nothing bad, if your host does not have a DNS server configured, or if your DNS server(s) are momentarily not available. For ad-hoc networks, that is the usual behavior.</p><p>LLMNR might reveal the presence of a rootkit if your hosts are frequently asking for random hostnames. This could be caused by Domain Name Generator (DGA) embedded in the malware.</p><p>Please note, that certain browsers try to translate random host names to find out, if the Internet is only available through some captive portal (hotel network etc.)</p><p>You can turn off LLMNR through a group policy in your name resolution policy.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '16, 08:47</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-58084" class="comments-container"></div><div id="comment-tools-58084" class="comment-tools"></div><div class="clear"></div><div id="comment-58084-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

