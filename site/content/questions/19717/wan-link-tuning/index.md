+++
type = "question"
title = "WAN Link Tuning"
description = '''Im currently looking at the necessary TCP settings I could use to increase the throughput of a WAN link. The current download speed is 1.78Mbps and a ping is showing a 300ms RTT. So far the following settings I was thinking of deploying were SACK and Nagle. However Im not sure what the Window Scale ...'''
date = "2013-03-21T09:47:00Z"
lastmod = "2013-03-21T10:41:00Z"
weight = 19717
keywords = [ "wan" ]
aliases = [ "/questions/19717" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [WAN Link Tuning](/questions/19717/wan-link-tuning)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19717-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Im currently looking at the necessary TCP settings I could use to increase the throughput of a WAN link. The current download speed is 1.78Mbps and a ping is showing a 300ms RTT.</p><p>So far the following settings I was thinking of deploying were SACK and Nagle. However Im not sure what the Window Scale should be set to (or if used at all). Im also thinking of lowering the MTU based on the PMTU to avoid any fragmentation, but still waiting on confirmation on the PMTU.</p><p>Does anyone have any thoughts on the above or if there is anything Im missing.</p><p>Thanks.....</p></div><div id="question-tags" class="tags-container tags">wan</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Mar '13, 09:47</strong></p><img src="https://secure.gravatar.com/avatar/22baebd906c29ccfcb5b2aeb350b22fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bart80&#39;s gravatar image" /><p>bart80<br />
<span class="score" title="11 reputation points">11</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bart80 has no accepted answers">0%</span></p></div></div><div id="comments-container-19717" class="comments-container"></div><div id="comment-tools-19717" class="comment-tools"></div><div class="clear"></div><div id="comment-19717-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19718"></span>

<div id="answer-container-19718" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19718-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>SACK is always good to have, Nagle can help with utilization if you don't need shortest possible latency. Scaling only needs to be enabled if the optimum window size for that WAN link is larger than 64k. You can calculate the optimum window size by multiplying the RTT in seconds times the slowest connection speed in bytes that happens on the link. For example, a RTT of 300ms and a 10MBit link would get you 0,3s x 1,250,000 byte = 375.000 byte window size. In that case you'd need to enable window scaling to be able to get to that window size.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '13, 10:41</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Mar '13, 09:44</p></div></div><div id="comments-container-19718" class="comments-container"><span id="20009"></span><div id="comment-20009" class="comment"><div id="post-20009-score" class="comment-score"></div><div class="comment-text"><p>Just a quick update , that based on making these updates I managed to get 3 times the speec that we were previously getting,</p><p>Thanks...</p></div><div id="comment-20009-info" class="comment-info"><span class="comment-age">(02 Apr '13, 02:01)</span> bart80</div></div></div><div id="comment-tools-19718" class="comment-tools"></div><div class="clear"></div><div id="comment-19718-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

