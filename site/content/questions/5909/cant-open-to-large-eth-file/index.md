+++
type = "question"
title = "can&#x27;t open to large .eth file"
description = '''Hello, have a to big (*.eth) file (7gb) and can&#x27;t open that with wireshark. how can i reduce it and make smaler files thereout. (like you can do ist with editcap and .pcap files, for example: editcap -c 10000 .........) Or can i convert the .eth file in an .pcap file? Hallo, habe eine zu große .eth ...'''
date = "2011-08-28T16:29:00Z"
lastmod = "2011-08-30T04:48:00Z"
weight = 5909
keywords = [ "editcap" ]
aliases = [ "/questions/5909" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [can't open to large .eth file](/questions/5909/cant-open-to-large-eth-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5909-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>have a to big (*.eth) file (7gb) and can't open that with wireshark. how can i reduce it and make smaler files thereout. (like you can do ist with editcap and .pcap files, for example: editcap -c 10000 .........)</p><p>Or can i convert the <em>.eth file in an</em> .pcap file?</p><p>Hallo,</p><p>habe eine zu große .eth Datei die mit wireshark nicht zu öffnen ist. (7gb) Da während der Aufnahme Daten geladen wurden. Wie kann ich die Datei verkleinern/splitten damit ich sie wieder öffnen kann. Mit editcap hab ich es versucht aber anscheinend kann der nur pcap dateine verarbeiten.</p><p>Kann man evtl. die eth datei in eine pcap datei umwandeln?</p></div><div id="question-tags" class="tags-container tags">editcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Aug '11, 16:29</strong></p><img src="https://secure.gravatar.com/avatar/e1ad487a049ec97db8bda42d6b23fb07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tkwire&#39;s gravatar image" /><p>tkwire<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tkwire has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Aug '11, 12:23</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-5909" class="comments-container"><span id="5911"></span><div id="comment-5911" class="comment"><div id="post-5911-score" class="comment-score"></div><div class="comment-text"><p>What program did you record the file with? The extension doesn't really mean much when it comes to trace files.</p></div><div id="comment-5911-info" class="comment-info"><span class="comment-age">(29 Aug '11, 01:01)</span> Jasper ♦♦</div></div><span id="5915"></span><div id="comment-5915" class="comment"><div id="post-5915-score" class="comment-score"></div><div class="comment-text"><p>...which can be determined by using:</p><pre><code>capinfos -Et &lt;filename&gt;</code></pre></div><div id="comment-5915-info" class="comment-info"><span class="comment-age">(29 Aug '11, 06:54)</span> Jaap ♦</div></div><span id="5950"></span><div id="comment-5950" class="comment"><div id="post-5950-score" class="comment-score"></div><div class="comment-text"><p>it was made with my router (fritz box) own capturesoftware. i just have to login to the router and to klick on the start button for the capture. regular i can open the files but this file is to big.</p><pre><code>If i want open the file with wireshark i can get informations: 
filename: fritzbox-vcc_28.08.11_1044.eth 
format(file type): Modified tcpdump - libpcap 
Size: 8097448066 bytes 
Packets: more than 247300 packets (preview timeout) 
First Packet: 2011-08-28 10:44:55 
Elapsed: unknown End time: Sun Aug 28 20:50:51 2011</code></pre><p>sorry for my worse english</p></div><div id="comment-5950-info" class="comment-info"><span class="comment-age">(30 Aug '11, 03:25)</span> tkwire</div></div><span id="5953"></span><div id="comment-5953" class="comment"><div id="post-5953-score" class="comment-score"></div><div class="comment-text"><p>it looks like the Fritz Box is writing pcap formated files then, which means that editcap should be able to cut them into smaller files. The question is why editcap doesn't work though, but this is hard to tell without having the tracefile.</p></div><div id="comment-5953-info" class="comment-info"><span class="comment-age">(30 Aug '11, 04:40)</span> Jasper ♦♦</div></div></div><div id="comment-tools-5909" class="comment-tools"></div><div class="clear"></div><div id="comment-5909-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5954"></span>

<div id="answer-container-5954" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5954-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Since the file is in libpcap format, all the Wireshark tools, including editcap are able to <strong>read</strong> the file. However the file is bigger than 2GB, which was a limit in earlier versions of wireshark (and accompanying tools). There has been some work on this limit. Could you try version 1.6.1 of editcap?</p><p>If version 1.6.1 of editcap does not work either, could you post the error-message you get?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '11, 04:48</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5954" class="comments-container"><span id="5959"></span><div id="comment-5959" class="comment"><div id="post-5959-score" class="comment-score"></div><div class="comment-text"><p>version 1.6.1</p><p>i don't know what i did wrong the first time, but now i did the same to get the error message and now it run without problems.</p><p>editcap -c 2000000 "filename".eth "filename".pcap and editcap -c 2000000 "filename".eth "filename".eth</p><p>both lines are running</p><p>a lots of thank for all who tryed to help me special for SYNBit;Jasper;Jaap</p></div><div id="comment-5959-info" class="comment-info"><span class="comment-age">(30 Aug '11, 08:44)</span> tkwire</div></div><span id="5961"></span><div id="comment-5961" class="comment"><div id="post-5961-score" class="comment-score"></div><div class="comment-text"><p>(I converted your "answer" to a "comment", please see the FAQ for details)</p></div><div id="comment-5961-info" class="comment-info"><span class="comment-age">(30 Aug '11, 09:22)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-5954" class="comment-tools"></div><div class="clear"></div><div id="comment-5954-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

