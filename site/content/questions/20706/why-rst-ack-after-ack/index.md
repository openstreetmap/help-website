+++
type = "question"
title = "Why RST, ACK after ACK"
description = '''Hi, Why would you normally see RST, ACK packets apparently in the middle of a transaction? https://www.cloudshark.org/captures/3b405a6ad37b Thanks'''
date = "2013-04-22T07:08:00Z"
lastmod = "2013-04-22T07:23:00Z"
weight = 20706
keywords = [ "reset", "ack", "after", "tcp", "wireshark" ]
aliases = [ "/questions/20706" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why RST, ACK after ACK](/questions/20706/why-rst-ack-after-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20706-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Why would you normally see RST, ACK packets apparently in the middle of a transaction?</p><p><a href="https://www.cloudshark.org/captures/3b405a6ad37b">https://www.cloudshark.org/captures/3b405a6ad37b</a></p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">reset ack after tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '13, 07:08</strong></p><img src="https://secure.gravatar.com/avatar/6fa0b64284fc9384c9a79a92e4986a3b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mikecl&#39;s gravatar image" /><p>Mikecl<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mikecl has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Apr '13, 07:26</p></div></div><div id="comments-container-20706" class="comments-container"><span id="20707"></span><div id="comment-20707" class="comment"><div id="post-20707-score" class="comment-score"></div><div class="comment-text"><p>the link to cloudshark.org does not work.</p><p>UPDATE: I fixed the link</p></div><div id="comment-20707-info" class="comment-info"><span class="comment-age">(22 Apr '13, 07:12)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-20706" class="comment-tools"></div><div class="clear"></div><div id="comment-20706-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20710"></span>

<div id="answer-container-20710" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20710-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The RESET (Frame #699) of the client is an answer to the FIN of the server (Frame #697). The whole communication is a SSL/TLS session via port 8080 and apparently windows clients do close a SSL connection with a RESET instead of answering the FIN. See also this question:</p><blockquote><p><a href="http://ask.wireshark.org/questions/5533/rst-ack-immediately-after-sending-data">http://ask.wireshark.org/questions/5533/rst-ack-immediately-after-sending-data</a></p></blockquote><p>Based on the TTL and the window size of the SYN packet, I believe your client is a Windows XP system. I just (re-) verified that behavior with a Windows XP system and IE.</p><p>So, that's nothing to worry about, as you cannot change it anyways ;-))</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '13, 07:23</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Apr '13, 07:26</p></div></div><div id="comments-container-20710" class="comments-container"><span id="20711"></span><div id="comment-20711" class="comment"><div id="post-20711-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt,</p><p>Not quite clear what you mean, the Application People say that the Client sending the RESET is causing a problem, on the actual client as far as we know we are not closing the connection. This happens to multiple clients. Should I be able to see something different with Windows7</p></div><div id="comment-20711-info" class="comment-info"><span class="comment-age">(22 Apr '13, 07:33)</span> Mikecl</div></div><span id="20716"></span><div id="comment-20716" class="comment"><div id="post-20716-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Not quite clear what you mean,</p></blockquote><p>I mean, that there is nothing to do for you, as that's default behavior of some windows clients.</p><blockquote><p>the Application People say that the Client sending the RESET is causing a problem,</p></blockquote><p>What kind of problem?</p><blockquote><p>Should I be able to see something different with Windows7</p></blockquote><p>maybe. I did not check.</p></div><div id="comment-20716-info" class="comment-info"><span class="comment-age">(22 Apr '13, 12:31)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-20710" class="comment-tools"></div><div class="clear"></div><div id="comment-20710-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

