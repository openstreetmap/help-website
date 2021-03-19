+++
type = "question"
title = "traffic to closed ports"
description = '''A dumb question to understand how Wireshark works: if I monitor my inbound traffic and someone send me a packet directed to a closed port, will I see this packet in wireshark?'''
date = "2015-10-29T10:32:00Z"
lastmod = "2015-10-29T10:36:00Z"
weight = 47072
keywords = [ "inbound", "closed-port", "port", "monitor" ]
aliases = [ "/questions/47072" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [traffic to closed ports](/questions/47072/traffic-to-closed-ports)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47072-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>A dumb question to understand how Wireshark works: if I monitor my inbound traffic and someone send me a packet directed to a closed port, will I see this packet in wireshark?</p></div><div id="question-tags" class="tags-container tags">inbound closed-port port monitor</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Oct '15, 10:32</strong></p><img src="https://secure.gravatar.com/avatar/065a787c1564a0f77c10c927f7f080b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rok&#39;s gravatar image" /><p>rok<br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rok has no accepted answers">0%</span></p></div></div><div id="comments-container-47072" class="comments-container"></div><div id="comment-tools-47072" class="comment-tools"></div><div class="clear"></div><div id="comment-47072-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47073"></span>

<div id="answer-container-47073" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47073-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, unless you have a local firewall running that blocks the packet before Wireshark can record it. But without, a closed port will result in an reset packet, which you should see.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Oct '15, 10:36</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-47073" class="comments-container"><span id="47074"></span><div id="comment-47074" class="comment"><div id="post-47074-score" class="comment-score"></div><div class="comment-text"><p>could you tell me more about the reset packet? Is it the reply I send once I receive a packet directed to my closed port? I mean, if you send me a tcp packet directed to my ip:port where port is closed.. I will see it normally in wireshark, and you'll get a reset packet as response.. am I right? Thank you</p></div><div id="comment-47074-info" class="comment-info"><span class="comment-age">(29 Oct '15, 10:41)</span> rok</div></div><span id="47076"></span><div id="comment-47076" class="comment"><div id="post-47076-score" class="comment-score">1</div><div class="comment-text"><p>Yes, if a packet arrives for a closed port your TCP stack will reply with an reset packet. You should see both in Wireshark.</p></div><div id="comment-47076-info" class="comment-info"><span class="comment-age">(29 Oct '15, 10:43)</span> Jasper ♦♦</div></div></div><div id="comment-tools-47073" class="comment-tools"></div><div class="clear"></div><div id="comment-47073-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

