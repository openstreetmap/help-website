+++
type = "question"
title = "How to capture incoming TCP traffic on Win 10"
description = '''Hi. I&#x27;m using a very simple C# console program to send TCP data to a Win 10 tablet that has a cellular connection (using TcpClient). The data is going to a specific IP of that tablet and port 8080. Using another C# console program on the tablet (which uses TcpListener), I&#x27;m able to see the packet, b...'''
date = "2016-11-07T08:03:00Z"
lastmod = "2016-11-07T13:56:00Z"
weight = 57064
keywords = [ "windows", "incoming", "tcp", "wireshark" ]
aliases = [ "/questions/57064" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to capture incoming TCP traffic on Win 10](/questions/57064/how-to-capture-incoming-tcp-traffic-on-win-10)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57064-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. I'm using a very simple C# console program to send TCP data to a Win 10 tablet that has a <strong>cellular</strong> connection (using TcpClient). The data is going to a specific IP of that tablet and port 8080. Using another C# console program on the tablet (which uses TcpListener), I'm able to see the packet, but with WireShark, I don't see anything. How do I set up WireShark (latest version) to capture the incoming <strong>cellular</strong> traffic on port 8080 on Windows 10 x64?</p><p><strong>Update 1:</strong> If I plug in my Ethernet cable, I see traffic in WireShark. But if I'm on the cellular connection of the tablet, no traffic. Nothing. What am I doing wrong?</p><p><strong>Update 2:</strong> List of interfaces when WireShark comes up:</p><ul><li>Intel Ethernet Connection</li><li>Microsoft Local Area Connection 2</li><li>Microsoft Wi-Fi</li><li>Microsoft Bluetooth</li><li>Microsoft Local Area Connection 12</li></ul><p>None of the above have any activity displayed (see image below); only when I plug in the cable do I see activity on the Intel Ethernet Connection.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/unnamed.png" alt="alt text" /></p><p><strong>Update 3:</strong> Here's the list of interfaces after installing npcap. Also note the activity on connection 12 (which previously showed no activity):</p><p><img src="https://osqa-ask.wireshark.org/upfiles/unnamed_(1).png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">windows incoming tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '16, 08:03</strong></p><img src="https://secure.gravatar.com/avatar/346a725f57d0caffe1ba2655135d2b88?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wireShark95&#39;s gravatar image" /><p>wireShark95<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wireShark95 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 08 Nov '16, 10:14</p></div></div><div id="comments-container-57064" class="comments-container"><span id="57068"></span><div id="comment-57068" class="comment"><div id="post-57068-score" class="comment-score"></div><div class="comment-text"><p>Can you confirm the ports being used?</p><p>You state that "the data is going to a specific IP of that tablet and port 8080", but then you want to "capture incoming traffic on port 8080" on the PC.</p><p>Can you draw a simple diagram of the setup?</p></div><div id="comment-57068-info" class="comment-info"><span class="comment-age">(07 Nov '16, 08:51)</span> grahamb ♦</div></div><span id="57070"></span><div id="comment-57070" class="comment"><div id="post-57070-score" class="comment-score"></div><div class="comment-text"><p>Thanks, @grahamb, for your reply. I might have been inartful in my description: The tablet PC is receiving TCP data on port 8080 and I need to see that incoming information via WireShark. In fact, if it's possible to see any incoming traffic via WireShark, that would be good. Right now I'm seeing nothing -- not even outgoing data.</p></div><div id="comment-57070-info" class="comment-info"><span class="comment-age">(07 Nov '16, 09:35)</span> wireShark95</div></div><span id="57077"></span><div id="comment-57077" class="comment"><div id="post-57077-score" class="comment-score">1</div><div class="comment-text"><p>So where are you running Wireshark, on the tablet?</p><p>If so, what interfaces are listed on the tablet when you start Wireshark?</p></div><div id="comment-57077-info" class="comment-info"><span class="comment-age">(07 Nov '16, 10:04)</span> grahamb ♦</div></div><span id="57085"></span><div id="comment-57085" class="comment"><div id="post-57085-score" class="comment-score"></div><div class="comment-text"><p>@grahamb, yes, running WS on tablet. Please see update to the question above for list of interfaces.</p></div><div id="comment-57085-info" class="comment-info"><span class="comment-age">(07 Nov '16, 11:01)</span> wireShark95</div></div></div><div id="comment-tools-57064" class="comment-tools"></div><div class="clear"></div><div id="comment-57064-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57100"></span>

<div id="answer-container-57100" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57100-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Is this an interface which cannot be seen by WinPcap? Maybe <a href="https://nmap.org/npcap/">npcap</a> is able to. You may want to try that, being aware it's still under development.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '16, 13:56</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></img></div></div><div id="comments-container-57100" class="comments-container"><span id="57151"></span><div id="comment-57151" class="comment"><div id="post-57151-score" class="comment-score"></div><div class="comment-text"><p>Thanks, @Jaap. That was it! I installed npcap and Wireshark started seeing the cellular data. Do you mind throwing that into an answer below and I'll accept it?</p></div><div id="comment-57151-info" class="comment-info"><span class="comment-age">(08 Nov '16, 05:42)</span> wireShark95</div></div><span id="57153"></span><div id="comment-57153" class="comment"><div id="post-57153-score" class="comment-score"></div><div class="comment-text"><p>Out of interest, does the list of interfaces differ when using npcap?</p></div><div id="comment-57153-info" class="comment-info"><span class="comment-age">(08 Nov '16, 06:02)</span> grahamb ♦</div></div><span id="57181"></span><div id="comment-57181" class="comment"><div id="post-57181-score" class="comment-score"></div><div class="comment-text"><p>@grahamb, please see Update 3 to the question above for the new list of interfaces.</p></div><div id="comment-57181-info" class="comment-info"><span class="comment-age">(08 Nov '16, 10:15)</span> wireShark95</div></div></div><div id="comment-tools-57100" class="comment-tools"></div><div class="clear"></div><div id="comment-57100-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

