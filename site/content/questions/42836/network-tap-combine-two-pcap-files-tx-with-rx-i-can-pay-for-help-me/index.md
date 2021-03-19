+++
type = "question"
title = "Network tap, combine two pcap files Tx with Rx. i can pay for help me"
description = '''Well i have a question. im using a mini pc with two ports and a network tap. then i connect to create a file by each interface. this files was capturing a Rx and Tx individual. router -------- Mini PC and network tap, Rx to eth0 and Tx to eth1 capturare and save on pcap file each hour ------------ P...'''
date = "2015-06-02T21:22:00Z"
lastmod = "2015-06-03T05:31:00Z"
weight = 42836
keywords = [ "sniffing", "tap", "network", "capturing" ]
aliases = [ "/questions/42836" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Network tap, combine two pcap files Tx with Rx. i can pay for help me](/questions/42836/network-tap-combine-two-pcap-files-tx-with-rx-i-can-pay-for-help-me)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42836-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Well i have a question.</p><p>im using a mini pc with two ports and a network tap. then i connect to create a file by each interface. this files was capturing a Rx and Tx individual.</p><p>router -------- Mini PC and network tap, Rx to eth0 and Tx to eth1 capturare and save on pcap file each hour ------------ PC</p><p>there is any software to combine theses two file in one.</p><p>i will thank you a lot.</p><p><img src="http://s1.pos/timg.org/5s4jnsxtb/plan.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">sniffing tap network capturing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jun '15, 21:22</strong></p><img src="https://secure.gravatar.com/avatar/a7efdaf6079e24cd2813662f99e0cf05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Juan%20Carlos%20Garcia&#39;s gravatar image" /><p>Juan Carlos ...<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Juan Carlos Garcia has no accepted answers">0%</span></p></img></div></div><div id="comments-container-42836" class="comments-container"></div><div id="comment-tools-42836" class="comment-tools"></div><div class="clear"></div><div id="comment-42836-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="42837"></span>

<div id="answer-container-42837" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42837-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use wireshark's "mergecap" utility, or in Wireshark's GUI go to File -&gt; Merge, load the second file into the first, and save it as a new combined file. In both cases you have options, but the default (suggested in this case) is a chronological merge on packet timestamps.</p><p>Edit: If you're doing this each hour, I definitely suggest a "mergecap" command line statement scripted to run when the hourly capture files are finished.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '15, 21:51</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Jun '15, 21:53</p></div></div><div id="comments-container-42837" class="comments-container"><span id="42842"></span><div id="comment-42842" class="comment"><div id="post-42842-score" class="comment-score"></div><div class="comment-text"><p>thanks a lot Quadratic</p></div><div id="comment-42842-info" class="comment-info"><span class="comment-age">(03 Jun '15, 07:18)</span> Juan Carlos ...</div></div></div><div id="comment-tools-42837" class="comment-tools"></div><div class="clear"></div><div id="comment-42837-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42841"></span>

<div id="answer-container-42841" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42841-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Uhm, better yet, why don't you capture into a single file on both cards at the same time? Wireshark/dumpcap support capturing from multiple NICs since version 1.8., so there's no need to merge afterwards.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jun '15, 05:31</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-42841" class="comments-container"><span id="42843"></span><div id="comment-42843" class="comment"><div id="post-42843-score" class="comment-score"></div><div class="comment-text"><p>thanks jasper</p></div><div id="comment-42843-info" class="comment-info"><span class="comment-age">(03 Jun '15, 07:18)</span> Juan Carlos ...</div></div></div><div id="comment-tools-42841" class="comment-tools"></div><div class="clear"></div><div id="comment-42841-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

