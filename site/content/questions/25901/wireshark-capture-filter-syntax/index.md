+++
type = "question"
title = "wireshark capture filter syntax"
description = '''HI, I am trying to set a capture filter to capture only DHCP packets and also a display filter for the same.  I know we can use -f option with tshark for capture filter and normally DHCP packets come on port 67 or port 68. I apply the same capture filter in wireshark GUI and it captures fine.  But w...'''
date = "2013-10-10T23:07:00Z"
lastmod = "2013-10-26T09:56:00Z"
weight = 25901
keywords = [ "capture", "capture-filter" ]
aliases = [ "/questions/25901" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark capture filter syntax](/questions/25901/wireshark-capture-filter-syntax)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25901-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>HI,</p><p>I am trying to set a capture filter to capture only DHCP packets and also a display filter for the same.</p><p>I know we can use -f option with tshark for capture filter and normally DHCP packets come on port 67 or port 68. I apply the same capture filter in wireshark GUI and it captures fine.</p><p>But when i try through Command Prompt its gives wrong syntax errors command: tshark -i 2 -f "port 67 or port 68" -R "bootp" -w capture.pcap</p><p>please help I am trying for a long time</p></div><div id="question-tags" class="tags-container tags">capture capture-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Oct '13, 23:07</strong></p><img src="https://secure.gravatar.com/avatar/503fc9de325c128612cbf9da0f4941d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Koushik%20Ganesh%20M&#39;s gravatar image" /><p>Koushik Gane...<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Koushik Ganesh M has no accepted answers">0%</span></p></div></div><div id="comments-container-25901" class="comments-container"></div><div id="comment-tools-25901" class="comment-tools"></div><div class="clear"></div><div id="comment-25901-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="25913"></span>

<div id="answer-container-25913" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25913-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>What version are you running, on what OS, and what exactly is the error. On the version I have currently (I'm a bit lazy and haven't updated for a while from 1.9.2 development version), I get the following error.</p><p>./tshark.exe -n -i 3 -f "port 67 or port 68" -R "bootp" -w capture.pcap tshark: Read filters aren't supported when capturing and saving the captured packets.</p><p>This error isn't so much a syntax issue in that you can't use BOTH capture and read (the equivalent of Wireshark display filters) at the same time if you are saving the file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '13, 02:59</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p>martyvis<br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-25913" class="comments-container"><span id="26418"></span><div id="comment-26418" class="comment"><div id="post-26418-score" class="comment-score"></div><div class="comment-text"><p>I am running on windows 7 OS and the wireshark version is - Version 1.2.8 (SVN Rev 32676)</p><p>even trying with the normal capture filter syntax which is like: tshark -i 2 -f "port 67 or port 68" -w capture.pcap</p><p>does not work !! is the qoutes correctly given. do i need to change anything in the command ?</p></div><div id="comment-26418-info" class="comment-info"><span class="comment-age">(25 Oct '13, 18:59)</span> Gourab Majumdar</div></div><span id="26427"></span><div id="comment-26427" class="comment"><div id="post-26427-score" class="comment-score"></div><div class="comment-text"><p>When you write, <em>"does not work!!"</em>, what exactly do you mean? The command fails or you fail to capture DHCP traffic?</p><p>Perhaps you could provide answers to:</p><ul><li>Are you sure you've specified the correct interface number? You can use <code>tshark.exe -D</code> to verify.</li><li>What is the exact output when you run that command, <code>tshark -i 2 -f "port 67 or port 68" -w capture.pcap</code>?</li></ul></div><div id="comment-26427-info" class="comment-info"><span class="comment-age">(26 Oct '13, 11:58)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-25913" class="comment-tools"></div><div class="clear"></div><div id="comment-25913-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26422"></span>

<div id="answer-container-26422" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26422-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>tshark -i 5 -2 -R "http" -w test.pcap</p><p>tshark: Read filters aren't supported when capturing and saving the captured packets.</p><p>and</p><p>tshark -i 5 -Y "http" -w test.pcap</p><p>tshark: Display filters aren't supported when capturing and saving the captured packets.</p><p>Are both expected behaviors. This is "Bug 2234" as explained at:</p><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=2234">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=2234</a></p><p>You can capture to a file, then use a capture filter with tshark and direct your output to a new file using tshark.</p><p>I also just successfully used the following (using v1.10.2)</p><p>dumpcap -i 5 -w - | tshark -r - -Y "http" -w file.pcap</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '13, 09:56</strong></p><img src="https://secure.gravatar.com/avatar/eb859ad26d92eb0902b45ba20a167917?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kpalmgren&#39;s gravatar image" /><p>kpalmgren<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kpalmgren has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Oct '13, 10:10</p></div></div><div id="comments-container-26422" class="comments-container"></div><div id="comment-tools-26422" class="comment-tools"></div><div class="clear"></div><div id="comment-26422-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

