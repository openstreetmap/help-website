+++
type = "question"
title = "Why isnt tshark responding to my command?"
description = '''Hello, I am trying to conduct OS fingerprint using tshark. I have created a capture, saved it to the desktop and named it testshark.pcap, here is the command that I am typing: C:&#92;Program Files&#92;Wireshark&amp;gt;tshark -r &quot;C:&#92;Users&#92;User 1&#92;Desktop&#92;testtshark tcp.flags.syn eq 1&quot; - T fields -e ip.src -e ip.t...'''
date = "2016-04-07T23:46:00Z"
lastmod = "2016-04-07T23:52:00Z"
weight = 51499
keywords = [ "tshark" ]
aliases = [ "/questions/51499" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why isnt tshark responding to my command?](/questions/51499/why-isnt-tshark-responding-to-my-command)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51499-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am trying to conduct OS fingerprint using tshark. I have created a capture, saved it to the desktop and named it <strong>testshark.pcap</strong>, here is the command that I am typing:</p><p>C:\Program Files\Wireshark&gt;<strong>tshark -r "C:\Users\User 1\Desktop\testtshark tcp.flags.syn eq 1" - T fields -e ip.src -e ip.ttl -e tcp.window_size</strong></p><p>and this is the error I am receiving: <strong>tshark: "-T" was unexpected in this context.</strong></p><p>I have recently updated to Wireshark 2.0.2 and I am using a Windows 7 box. I have successfully done this in the past with an older version of wireshark, can someone please help?</p><p>Lee G</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Apr '16, 23:46</strong></p><img src="https://secure.gravatar.com/avatar/dd9fd7fa314331a6847f1f0795eeb4b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lee_G&#39;s gravatar image" /><p>Lee_G<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lee_G has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>wikified 11 Apr '16, 05:35</p></div></div><div id="comments-container-51499" class="comments-container"></div><div id="comment-tools-51499" class="comment-tools"></div><div class="clear"></div><div id="comment-51499-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51500"></span>

<div id="answer-container-51500" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51500-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should try this <code>C:\Program Files\Wireshark&gt;tshark -r "C:\Users\User 1\Desktop\testtshark" -Y "tcp.flags.syn eq 1" - T fields -e ip.src -e ip.ttl -e tcp.window_size</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Apr '16, 23:52</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div></div><div id="comments-container-51500" class="comments-container"><span id="51501"></span><div id="comment-51501" class="comment"><div id="post-51501-score" class="comment-score"></div><div class="comment-text"><p>As in, you borked the command line, which happens. One more detail: you may need to add ".pcap' to the filename as well.</p></div><div id="comment-51501-info" class="comment-info"><span class="comment-age">(08 Apr '16, 01:10)</span> Jaap ♦</div></div><span id="51502"></span><div id="comment-51502" class="comment"><div id="post-51502-score" class="comment-score"></div><div class="comment-text"><p>What I can also see is the blank space between <code>-</code> and <code>T</code> which is likely to cause another issue.</p></div><div id="comment-51502-info" class="comment-info"><span class="comment-age">(08 Apr '16, 01:51)</span> sindy</div></div><span id="51550"></span><div id="comment-51550" class="comment"><div id="post-51550-score" class="comment-score"></div><div class="comment-text"><p>Christian, your recommendation worked, you were right my syntax was flawed, Kudos to you sir! BTW, love your website, very informative.</p></div><div id="comment-51550-info" class="comment-info"><span class="comment-age">(11 Apr '16, 05:41)</span> Lee_G</div></div></div><div id="comment-tools-51500" class="comment-tools"></div><div class="clear"></div><div id="comment-51500-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

