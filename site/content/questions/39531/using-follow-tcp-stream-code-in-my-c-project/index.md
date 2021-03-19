+++
type = "question"
title = "using “follow tcp stream” code in my c project"
description = '''I want to assemble all tcp sessions from real time and save payload to file. Is there such a c library wireshark &#x27;follow tcp stream&#x27;? (I tried using the libnids. However, the TCP sequence order is not correct.) wireshark a-&amp;gt;b-&amp;gt;c-&amp;gt;d-&amp;gt;e libnids or tcpflow : a-&amp;gt;c-&amp;gt;b-&amp;gt;d-&amp;gt;e ???'''
date = "2015-01-31T22:01:00Z"
lastmod = "2016-07-23T12:29:00Z"
weight = 39531
keywords = [ "libnids", "pcap", "stream", "tcp" ]
aliases = [ "/questions/39531" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [using “follow tcp stream” code in my c project](/questions/39531/using-follow-tcp-stream-code-in-my-c-project)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39531-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to assemble all tcp sessions from real time and save payload to file.</p><p>Is there such a c library wireshark 'follow tcp stream'?</p><p>(I tried using the libnids. However, the TCP sequence order is not correct.)</p><p>wireshark a-&gt;b-&gt;c-&gt;d-&gt;e</p><p>libnids or tcpflow : a-&gt;c-&gt;b-&gt;d-&gt;e ???</p></div><div id="question-tags" class="tags-container tags">libnids pcap stream tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jan '15, 22:01</strong></p><img src="https://secure.gravatar.com/avatar/ddb64b7d8a3aa59695f9add9665e3533?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="goesang&#39;s gravatar image" /><p>goesang<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="goesang has no accepted answers">0%</span></p></div></div><div id="comments-container-39531" class="comments-container"></div><div id="comment-tools-39531" class="comment-tools"></div><div class="clear"></div><div id="comment-39531-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="39756"></span>

<div id="answer-container-39756" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39756-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there such a c library wireshark 'follow tcp stream'?</p></blockquote><p>no, there isn't. "Follow TCP Stream" is tightly integrated into the code and not available as a separate library.</p><blockquote><p>I want to assemble all tcp sessions <strong>from real time</strong> and save payload to file.</p></blockquote><p>Furthermore, if you are trying to do this in real time, Wireshark/tshark is (probably) the wrong tool for you, as it was not designed to work that way.</p><p>See my answer to a similar question and the links therein.</p><blockquote><p><a href="https://ask.wireshark.org/questions/26224/plain-text-automatic-save">https://ask.wireshark.org/questions/26224/plain-text-automatic-save</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '15, 03:10</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-39756" class="comments-container"></div><div id="comment-tools-39756" class="comment-tools"></div><div class="clear"></div><div id="comment-39756-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="54255"></span>

<div id="answer-container-54255" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54255-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I can recommend you <a href="https://github.com/seladb/PcapPlusPlus">PcapPlusPlus</a> which is a C++ library that can do exactly that. Please take a look at the <a href="https://github.com/seladb/PcapPlusPlus/tree/master/Examples/TcpReassembly">TcpReassembly</a> example that does what you ask which is reassemble TCP data from packets being captured from live traffic or from pcap file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '16, 12:29</strong></p><img src="https://secure.gravatar.com/avatar/0b6fc0687623a56d9f42c88153062754?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="seladb&#39;s gravatar image" /><p>seladb<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="seladb has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Jun '17, 14:51</p></div></div><div id="comments-container-54255" class="comments-container"></div><div id="comment-tools-54255" class="comment-tools"></div><div class="clear"></div><div id="comment-54255-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

