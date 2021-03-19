+++
type = "question"
title = "Using the gsm_rlcmac dissector"
description = '''Hi, im trying to use the gsm_rlcmac dissector, but if i run wireshark, select a packet and the &quot;decode as...&quot; option, i cant find it in the list. If i type gsm_rlcmac on the filter place, it turns green, so the dissector is up and running. I also tried to make my own dissector, that calls the gsm_rl...'''
date = "2014-08-29T08:55:00Z"
lastmod = "2014-08-29T09:34:00Z"
weight = 35877
keywords = [ "dissector", "gsm_rlcmac" ]
aliases = [ "/questions/35877" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Using the gsm\_rlcmac dissector](/questions/35877/using-the-gsm_rlcmac-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35877-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, im trying to use the gsm_rlcmac dissector, but if i run wireshark, select a packet and the "decode as..." option, i cant find it in the list. If i type gsm_rlcmac on the filter place, it turns green, so the dissector is up and running. I also tried to make my own dissector, that calls the gsm_rlcmac, but it wont work, the</p><p><code>find_dissector("gsm_rlcmac")</code></p><p>returns NULL.</p><p>What am i doing wrong? Thanks in advance</p></div><div id="question-tags" class="tags-container tags">dissector gsm_rlcmac</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Aug '14, 08:55</strong></p><img src="https://secure.gravatar.com/avatar/3f60a30a327fa363a0166009000c466d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ingcpt&#39;s gravatar image" /><p>ingcpt<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ingcpt has no accepted answers">0%</span></p></div></div><div id="comments-container-35877" class="comments-container"></div><div id="comment-tools-35877" class="comment-tools"></div><div class="clear"></div><div id="comment-35877-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35879"></span>

<div id="answer-container-35879" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35879-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The <code>gsm_rlcmac</code> registers twice, as <code>gsm_rlcmac_ul</code> and <code>gsm_rlcmac_dl</code>, try using one of those in the find_dissector call.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Aug '14, 09:34</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-35879" class="comments-container"><span id="35889"></span><div id="comment-35889" class="comment"><div id="post-35889-score" class="comment-score"></div><div class="comment-text"><p>I.e., there are <em>separate</em> dissectors for the uplink and downlink, so either you have to choose one of the dissectors or, if this is some protocol that encapsulates GSM RLC MAC messages, that protocol needs to have some extra field indicating whether the traffic is uplink or downlink traffic, in which case that protocol needs a new dissector that looks at that field and calls the uplink or downlink dissector.</p></div><div id="comment-35889-info" class="comment-info"><span class="comment-age">(30 Aug '14, 14:43)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-35879" class="comment-tools"></div><div class="clear"></div><div id="comment-35879-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

