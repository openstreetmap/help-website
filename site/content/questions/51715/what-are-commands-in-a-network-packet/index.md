+++
type = "question"
title = "What are commands in a network packet?"
description = '''I need to analyse a network packet in wireshark. I have a packet with several flags like seq,win,ack,etc., Are these considered as commands? Basically i need to Comment on each command and response between the client and the server.  '''
date = "2016-04-16T03:07:00Z"
lastmod = "2016-04-17T08:15:00Z"
weight = 51715
keywords = [ "wireshark" ]
aliases = [ "/questions/51715" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What are commands in a network packet?](/questions/51715/what-are-commands-in-a-network-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51715-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to analyse a network packet in wireshark. I have a packet with several flags like seq,win,ack,etc., Are these considered as commands? Basically i need to Comment on each command and response between the client and the server.<br />
</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '16, 03:07</strong></p><img src="https://secure.gravatar.com/avatar/7f649b8d1d78c9fd74961d4c8f84e853?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sujitha&#39;s gravatar image" /><p>Sujitha<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sujitha has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-51715" class="comments-container"></div><div id="comment-tools-51715" class="comment-tools"></div><div class="clear"></div><div id="comment-51715-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51729"></span>

<div id="answer-container-51729" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51729-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark attempts to "decode" a packet, to show what network protocols were in use (eg: IPv4, TCP, HTTP). It attempts to present them into a human-readable format out of the packet's raw binary for analysis.</p><p>For your question, how are you defining the word "command"? A "command" between a "client" and a "server" is something that must be put in the context of the protocol or application in question. For example, I could say that "GET" or "PUT" are commands in the HTTP protocol, and I could use Wireshark to search on HTTP and pull up examples of such commands.</p><p>Where you are asking about flags and sequence numbers it looks like you are asking about TCP specifically? If so, Wireshark will decode the fields but won't tell you what a flag does. An understanding of how a protocol works is paramount to analyzing it, but it's homework that needs to be done before using that tool. In TCP's case: <a href="https://tools.ietf.org/html/rfc793">https://tools.ietf.org/html/rfc793</a></p><p>Aside from the RFC, if you just google "TCP flag definitions" there are plenty of example descriptions of them online, assuming that it is TCP flags you are specifically asking about.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Apr '16, 08:15</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-51729" class="comments-container"></div><div id="comment-tools-51729" class="comment-tools"></div><div class="clear"></div><div id="comment-51729-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

