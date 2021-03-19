+++
type = "question"
title = "Too many FIN_WAIT_2 and Client&#x27;s delayed tls encrypted alert followed by server&#x27;s fin with Keep-Alive On"
description = '''Hi. We are using Apache 2.4 and Keep Alive is set to On. We have too many Fin_Wait_2. Captured packets are like as following. ---begin of session--- p1. session open p2. tls handshakes p3. application data p4. no packets during 5 seconds p5. server&#x27;s fin p6. client&#x27;s ack p7. no packets during 19~79 ...'''
date = "2017-04-15T00:51:00Z"
lastmod = "2017-04-15T00:51:00Z"
weight = 60836
keywords = [ "delyed", "alert", "fin_wait_2", "keep-alive", "encrypted" ]
aliases = [ "/questions/60836" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Too many FIN\_WAIT\_2 and Client's delayed tls encrypted alert followed by server's fin with Keep-Alive On](/questions/60836/too-many-fin_wait_2-and-clients-delayed-tls-encrypted-alert-followed-by-servers-fin-with-keep-alive-on)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60836-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi.</p><p>We are using Apache 2.4 and Keep Alive is set to On.</p><p>We have too many Fin_Wait_2.</p><p>Captured packets are like as following.</p><p>---begin of session---</p><p>p1. session open</p><p>p2. tls handshakes</p><p>p3. application data</p><p>p4. no packets during 5 seconds</p><p>p5. server's fin</p><p>p6. client's ack</p><p>p7. no packets during 19~79 seconds</p><p>p8. client's "Encrypted Alert" and TCP RESET(session close)</p><p>---end of session---</p><p>p7 is not shown when Keep-Alive is set to Off. (There is not any delay with keep-alive off.)</p><p>I need your idea about</p><ol><li>p7(state of FinWait2)?</li><li>Client's delayed "Encrypted Alert"(p8)?</li></ol><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">delyed alert fin_wait_2 keep-alive encrypted</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Apr '17, 00:51</strong></p><img src="https://secure.gravatar.com/avatar/8f2085dfc9368a6cc1ea0bbdaa9d9e3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="impask&#39;s gravatar image" /><p>impask<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="impask has no accepted answers">0%</span></p></div></div><div id="comments-container-60836" class="comments-container"><span id="60837"></span><div id="comment-60837" class="comment"><div id="post-60837-score" class="comment-score"></div><div class="comment-text"><p>keep alive time-out is 5 seconds</p></div><div id="comment-60837-info" class="comment-info"><span class="comment-age">(15 Apr '17, 00:59)</span> impask</div></div></div><div id="comment-tools-60836" class="comment-tools"></div><div class="clear"></div><div id="comment-60836-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

