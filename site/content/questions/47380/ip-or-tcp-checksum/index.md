+++
type = "question"
title = "IP or TCP checksum"
description = '''When two hosts exchange packets through a few LANs, if there are corruptions in packets, it&#x27;s going to be likely caught by the ethernet frame CRC and dropped by either router/switch/PC NIC. Wonder if this is a correct assumption.'''
date = "2015-11-08T05:44:00Z"
lastmod = "2015-11-08T06:52:00Z"
weight = 47380
keywords = [ "network" ]
aliases = [ "/questions/47380" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [IP or TCP checksum](/questions/47380/ip-or-tcp-checksum)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47380-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When two hosts exchange packets through a few LANs, if there are corruptions in packets, it's going to be likely caught by the ethernet frame CRC and dropped by either router/switch/PC NIC. Wonder if this is a correct assumption.</p></div><div id="question-tags" class="tags-container tags">network</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '15, 05:44</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p>pktUser1001<br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-47380" class="comments-container"></div><div id="comment-tools-47380" class="comment-tools"></div><div class="clear"></div><div id="comment-47380-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47382"></span>

<div id="answer-container-47382" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47382-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, the assumption is correct, even though the FCS may still match for corrupted packets on very rare occasions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '15, 06:52</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-47382" class="comments-container"><span id="47384"></span><div id="comment-47384" class="comment"><div id="post-47384-score" class="comment-score"></div><div class="comment-text"><p>Agree. FCS and IP/TCP header checksum use different algorithm. So that's possible. Thanks.</p></div><div id="comment-47384-info" class="comment-info"><span class="comment-age">(08 Nov '15, 06:56)</span> pktUser1001</div></div><span id="47389"></span><div id="comment-47389" class="comment"><div id="post-47389-score" class="comment-score"></div><div class="comment-text"><p>Recently we experienced a faulty network device that was corrupting packets internally but sending valid Ethernet frames containing that corrupted data, so I don't think this is necessarily a correct assumption. Statistically speaking, it's probably safe to say that in most cases the FCS will catch the bad frames, but in cases like this, it won't.</p></div><div id="comment-47389-info" class="comment-info"><span class="comment-age">(08 Nov '15, 07:45)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-47382" class="comment-tools"></div><div class="clear"></div><div id="comment-47382-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

