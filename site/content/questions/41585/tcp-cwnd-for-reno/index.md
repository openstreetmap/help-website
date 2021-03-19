+++
type = "question"
title = "TCP-CWND for RENO"
description = '''TCP Reno based CWND In linux if we are working on TCP-RENO (in-place of cubic), cwnd will increase till packet drops occur I will get sawtooth graph for cwnd vs time........... Am I right?? RTT based CWND If cwnd is computed based on currently updated RTT along with Previous RTT values packet drop w...'''
date = "2015-04-19T23:59:00Z"
lastmod = "2015-04-20T02:07:00Z"
weight = 41585
keywords = [ "reno", "for", "tcp-cwnd" ]
aliases = [ "/questions/41585" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP-CWND for RENO](/questions/41585/tcp-cwnd-for-reno)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41585-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><strong>TCP Reno based CWND</strong></p><p>In linux if we are working on TCP-RENO (in-place of cubic), cwnd will increase till packet drops occur I will get sawtooth graph for cwnd vs time........... Am I right??</p><p><strong>RTT based CWND</strong></p><p>If cwnd is computed based on currently updated RTT along with Previous RTT values packet drop will not occur</p><p>I will get straight horizontal line graph for cwnd vs time</p><p>Am I right??</p></div><div id="question-tags" class="tags-container tags">reno for tcp-cwnd</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '15, 23:59</strong></p><img src="https://secure.gravatar.com/avatar/ce1843f92a1c18db26bc79b3afa9bd50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srinu_bel&#39;s gravatar image" /><p>srinu_bel<br />
<span class="score" title="20 reputation points">20</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srinu_bel has no accepted answers">0%</span></p></div></div><div id="comments-container-41585" class="comments-container"></div><div id="comment-tools-41585" class="comment-tools"></div><div class="clear"></div><div id="comment-41585-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41590"></span>

<div id="answer-container-41590" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41590-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, you're wrong. You can get packet drop even if you consider Previous RTT, because packet drop can always occur for various reasons.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '15, 02:07</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-41590" class="comments-container"></div><div id="comment-tools-41590" class="comment-tools"></div><div class="clear"></div><div id="comment-41590-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

