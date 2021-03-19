+++
type = "question"
title = "I am seeing lots of retransmission between two nodes in same subnet."
description = '''Dear Team, I am new to TCP analysis, i am seeing lots of retransmission , i am unable to understand how come there are so many retransmission if they are in same sub nett.Other node is Application side and i suspect while submitting packet on SMPP (using TCP as transport layer ) there window size is...'''
date = "2012-08-01T09:58:00Z"
lastmod = "2012-08-01T10:31:00Z"
weight = 13275
keywords = [ "smpp", "window", "retrasmission", "tcp" ]
aliases = [ "/questions/13275" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [I am seeing lots of retransmission between two nodes in same subnet.](/questions/13275/i-am-seeing-lots-of-retransmission-between-two-nodes-in-same-subnet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13275-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear Team,</p><p>I am new to TCP analysis, i am seeing lots of retransmission , i am unable to understand how come there are so many retransmission if they are in same sub nett.Other node is Application side and i suspect while submitting packet on SMPP (using TCP as transport layer ) there window size is giving 46, is the same reason we are seeing retransmission ? I am confused please help.</p><p>Link for trace file is:</p><blockquote><p><a href="https://docs.google.com/open?id=0B5duHt-843JlRWdJY3lFWFFIck0">https://docs.google.com/open?id=0B5duHt-843JlRWdJY3lFWFFIck0</a><br />
<a href="http://www.cloudshark.org/captures/80ad5769ba77">http://www.cloudshark.org/captures/80ad5769ba77</a><br />
</p></blockquote><h2 id="thanks-in-advance...">Thanks in Advance...</h2><p>With Regards Avinash Jha</p></div><div id="question-tags" class="tags-container tags">smpp window retrasmission tcp</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Aug '12, 09:58</strong></p><img src="https://secure.gravatar.com/avatar/ea81afbd71dc63ea6a6506203bc83c3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="creative&#39;s gravatar image" /><p>creative<br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="creative has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Aug '12, 10:17</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-13275" class="comments-container"></div><div id="comment-tools-13275" class="comment-tools"></div><div class="clear"></div><div id="comment-13275-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="13280"></span>

<div id="answer-container-13280" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13280-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't know how your capture setup looked like when you recorded this, but your trace has lots of duplicate packets which are showing up as false positives (retransmissions, duplicate acks). You need to deduplicate your trace before analyzing it.</p><p>See my answer to a similar case here: <a href="http://ask.wireshark.org/questions/10369/too-many-lost-segments-dup-acks-and-retransmission">http://ask.wireshark.org/questions/10369/too-many-lost-segments-dup-acks-and-retransmission</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '12, 10:27</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-13280" class="comments-container"></div><div id="comment-tools-13280" class="comment-tools"></div><div class="clear"></div><div id="comment-13280-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13282"></span>

<div id="answer-container-13282" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13282-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your system 10.10.6.6 just sends every single packet twice. Wireshark just shows that as <strong>DUP ACK</strong> and as <strong>Retransmission</strong>. One possible reason is a problem while capturing the packets. Maybe your sniffer on 10.10.6.6 (what did you use?) just captured (or wrote) every packet twice. To verify, capture at the other side as well and compare the capture files.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '12, 10:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-13282" class="comments-container"></div><div id="comment-tools-13282" class="comment-tools"></div><div class="clear"></div><div id="comment-13282-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

