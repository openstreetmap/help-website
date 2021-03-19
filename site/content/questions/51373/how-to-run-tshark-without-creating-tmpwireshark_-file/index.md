+++
type = "question"
title = "How to run tshark without creating /tmp/wireshark_* file?"
description = '''Hi! I&#x27;m using tshark for capturing probe requests for some statistic calculates on raspberry pi. Device has so small memory card and after ~20hours tshark overflow the memory. I found only way to restart tshark every 1 hour for example. I no need to create tmp file. I start the tshark by &#x27;spawn&#x27; met...'''
date = "2016-04-02T08:09:00Z"
lastmod = "2016-04-02T15:56:00Z"
weight = 51373
keywords = [ "temp", "tshark", "capturing", "memory" ]
aliases = [ "/questions/51373" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to run tshark without creating /tmp/wireshark\_\* file?](/questions/51373/how-to-run-tshark-without-creating-tmpwireshark_-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51373-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi! I'm using tshark for capturing probe requests for some statistic calculates on raspberry pi. Device has so small memory card and after ~20hours tshark overflow the memory.</p><p>I found only way to restart tshark every 1 hour for example.</p><p>I no need to create tmp file. I start the tshark by 'spawn' method using NodeJS and capturing stdout of it in nodejs process for sending to backend.</p><p>here is the command which runs tshark with needed filters and fields:</p><pre><code> tshark -l -i wlan1 -Y &#39;wlan.fc.type_subtype eq 4&#39; -T fields -e wlan.sa -e wlan.sa_resolved -e radiotap.dbm_antsignal -e frame.time -e wlan_mgt.ssid</code></pre><p>When tshark runs it will create the file in /tmp/wireshark_pcapng_wlan1_* .</p><p>How I can run it <strong>without</strong> creating this temp file? tshark version - 1.12.1.</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">temp tshark capturing memory</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Apr '16, 08:09</strong></p><img src="https://secure.gravatar.com/avatar/44a5f2527c1fd16d1a6ba30474313ece?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="freedev&#39;s gravatar image" /><p>freedev<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="freedev has one accepted answer">100%</span></p></div></div><div id="comments-container-51373" class="comments-container"></div><div id="comment-tools-51373" class="comment-tools"></div><div class="clear"></div><div id="comment-51373-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="51379"></span>

<div id="answer-container-51379" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51379-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The problem was solved! Here is the solution.</p><p>Firstly we cannot control output file using display filters. I need to capture probe requests only. I read that I can use for it pcap-filter and then I can control of output file and him size.</p><p><a href="http://www.tcpdump.org/manpages/pcap-filter.7.html">http://www.tcpdump.org/manpages/pcap-filter.7.html</a> here I read about pcap-filter and syntax of it and change my tshark launch command to this:</p><pre><code>tshark -l -i wlx000f6008facf -f &#39;type mgt subtype probe-req&#39; -T fields -e wlan.sa -e wlan.sa_resolved -e radiotap.dbm_antsignal -e frame.time -e wlan_mgt.ssid -b filesize:2 -w /tmp/probe-req.tmp</code></pre><p>And file cannot has more than 2 kb size.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '16, 15:56</strong></p><img src="https://secure.gravatar.com/avatar/44a5f2527c1fd16d1a6ba30474313ece?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="freedev&#39;s gravatar image" /><p>freedev<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="freedev has one accepted answer">100%</span></p></div></div><div id="comments-container-51379" class="comments-container"><span id="51380"></span><div id="comment-51380" class="comment"><div id="post-51380-score" class="comment-score"></div><div class="comment-text"><p>That still creates a temporary file, it just happens to be called /tmp/probe-req.tmp and is limited in size. That's <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=2743">bug 2743</a>.</p></div><div id="comment-51380-info" class="comment-info"><span class="comment-age">(02 Apr '16, 16:40)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-51379" class="comment-tools"></div><div class="clear"></div><div id="comment-51379-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="51374"></span>

<div id="answer-container-51374" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51374-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please read this article <a href="https://blog.packet-foo.com/2014/07/wireshark-file-storage/">https://blog.packet-foo.com/2014/07/wireshark-file-storage/</a><br />
Maybe you could try setting the temp path temporarily to /dev/null</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '16, 08:34</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span> </br></p></div></div><div id="comments-container-51374" class="comments-container"><span id="51375"></span><div id="comment-51375" class="comment"><div id="post-51375-score" class="comment-score"></div><div class="comment-text"><p>Oh yea.. very nice case. Will check this possibility. Thanks for response</p></div><div id="comment-51375-info" class="comment-info"><span class="comment-age">(02 Apr '16, 08:50)</span> freedev</div></div></div><div id="comment-tools-51374" class="comment-tools"></div><div class="clear"></div><div id="comment-51374-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

