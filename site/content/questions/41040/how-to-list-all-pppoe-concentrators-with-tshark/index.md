+++
type = "question"
title = "How to list all pppoe concentrators with tshark ?"
description = '''How to list all pppoe concentrators with tshark ?'''
date = "2015-03-30T19:01:00Z"
lastmod = "2015-03-31T10:48:00Z"
weight = 41040
keywords = [ "concentrators", "pppoe", "tshark" ]
aliases = [ "/questions/41040" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to list all pppoe concentrators with tshark ?](/questions/41040/how-to-list-all-pppoe-concentrators-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41040-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to list all pppoe concentrators with tshark ?</p></div><div id="question-tags" class="tags-container tags">concentrators pppoe tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Mar '15, 19:01</strong></p><img src="https://secure.gravatar.com/avatar/f1abd9a126fb53c9e9bf96036e7fd394?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="coopermine&#39;s gravatar image" /><p>coopermine<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="coopermine has no accepted answers">0%</span></p></div></div><div id="comments-container-41040" class="comments-container"><span id="41049"></span><div id="comment-41049" class="comment"><div id="post-41049-score" class="comment-score">1</div><div class="comment-text"><p>can you please add more details what you are looking for?</p></div><div id="comment-41049-info" class="comment-info"><span class="comment-age">(31 Mar '15, 03:31)</span> Kurt Knochner ♦</div></div><span id="41064"></span><div id="comment-41064" class="comment"><div id="post-41064-score" class="comment-score"></div><div class="comment-text"><p>I need to find out the name of concetradores pppoe that are active my network. like - &gt; <a href="http://pppoem.com/">http://pppoem.com/</a></p></div><div id="comment-41064-info" class="comment-info"><span class="comment-age">(31 Mar '15, 09:48)</span> coopermine</div></div></div><div id="comment-tools-41040" class="comment-tools"></div><div class="clear"></div><div id="comment-41040-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41065"></span>

<div id="answer-container-41065" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41065-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I need to find out the name of concetradores pppoe that are active my network. like -</p></blockquote><p>O.K. then please try this:</p><blockquote><p>tshark -ni eth0 -Y "pppoe.code == 0x07" -T fields -e pppoed.tags.ac_name</p></blockquote><p>If you are on Windows, please replace <strong>eth0</strong> with the interface index of your LAN interface.</p><p>Hint: This will only print the AC names. If you need any other field, please add them with additional -e options.</p><blockquote><p><a href="https://www.wireshark.org/docs/dfref/p/pppoed.html">https://www.wireshark.org/docs/dfref/p/pppoed.html</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Mar '15, 10:48</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-41065" class="comments-container"><span id="41067"></span><div id="comment-41067" class="comment"><div id="post-41067-score" class="comment-score"></div><div class="comment-text"><p>Great answer !!! Thank U.</p><p>Well now listen to all PADO packets coming in my interface.</p><p>I have two more questions.</p><p>1 - I get a PADO when my interface sends a PADI . How can I send PADI for the broadcast?</p><p>2 - How can I receive all PADO network packets without filter only my interface? ( packets sent to other interfaces on the same network ?</p><p>Excuse my English. I appreciate your help.</p></div><div id="comment-41067-info" class="comment-info"><span class="comment-age">(31 Mar '15, 11:31)</span> coopermine</div></div><span id="41068"></span><div id="comment-41068" class="comment"><div id="post-41068-score" class="comment-score"></div><div class="comment-text"><p>1: --&gt; <strong>scapy:</strong> <a href="http://www.secdev.org/projects/scapy/">http://www.secdev.org/projects/scapy/</a> <strong>Tutorial:</strong> <a href="http://www.secdev.org/projects/scapy/doc/usage.html#interactive-tutorial">http://www.secdev.org/projects/scapy/doc/usage.html#interactive-tutorial</a><br />
2: --&gt; as the PADO is unicast, the only option I see is: switch mirror port or hub (see: <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">https://wiki.wireshark.org/CaptureSetup/Ethernet</a> )</p></div><div id="comment-41068-info" class="comment-info"><span class="comment-age">(31 Mar '15, 13:43)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-41065" class="comment-tools"></div><div class="clear"></div><div id="comment-41065-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

