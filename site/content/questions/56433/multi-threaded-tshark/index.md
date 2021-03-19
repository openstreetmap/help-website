+++
type = "question"
title = "Multi-threaded Tshark"
description = '''Hi everyone,  As I know, tshark is a single threaded application so that it cannot use multiple cores to increase speed. I&#x27;m currently working with its source code and have some questions:  How fast does wireshark can dissect data (maximum bytes/s) Why don&#x27;t tshark use multi-threading? Is it possibl...'''
date = "2016-10-17T00:11:00Z"
lastmod = "2016-10-17T06:25:00Z"
weight = 56433
keywords = [ "multi-thread" ]
aliases = [ "/questions/56433" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Multi-threaded Tshark](/questions/56433/multi-threaded-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56433-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone, As I know, tshark is a single threaded application so that it cannot use multiple cores to increase speed. I'm currently working with its source code and have some questions:</p><ol><li>How fast does wireshark can dissect data (maximum bytes/s)</li><li>Why don't tshark use multi-threading?</li><li>Is it possible to change the source code in order to multi thread tshark?</li><li>if NOT, is it possible to write a new application in which:<ul><li>winpcap/libcap is used for capturing data</li><li>tapping data is store in a queue</li><li>multi-threading is used for getting data from queue and then decode each packet by using dissectors</li></ul></li></ol><p>Please help if you have any idea for these question. Thank you very much.</p></div><div id="question-tags" class="tags-container tags">multi-thread</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Oct '16, 00:11</strong></p><img src="https://secure.gravatar.com/avatar/824a7342f59ff90e6040505b38626416?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hoangsonk49&#39;s gravatar image" /><p>hoangsonk49<br />
<span class="score" title="81 reputation points">81</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hoangsonk49 has 2 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Oct '16, 00:40</p></div></div><div id="comments-container-56433" class="comments-container"><span id="56435"></span><div id="comment-56435" class="comment"><div id="post-56435-score" class="comment-score">1</div><div class="comment-text"><p>The main problem with multi-threading is that some packet dissection relays on the information from previous frames so these packets need to be dissected in order to have the right results.</p></div><div id="comment-56435-info" class="comment-info"><span class="comment-age">(17 Oct '16, 01:27)</span> Anders ♦</div></div><span id="56437"></span><div id="comment-56437" class="comment"><div id="post-56437-score" class="comment-score"></div><div class="comment-text"><p>Thank Anders for the answer of question 2 and 3. How about the others? Please help if you have any idea. Thank you.</p></div><div id="comment-56437-info" class="comment-info"><span class="comment-age">(17 Oct '16, 02:09)</span> hoangsonk49</div></div></div><div id="comment-tools-56433" class="comment-tools"></div><div class="clear"></div><div id="comment-56433-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="56440"></span>

<div id="answer-container-56440" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56440-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>First thing, the thing you are talking about is actually the dissection engine. This engine is shared between tshark and wireshark, so there's no difference there. The additional analysis features differ, these are part of the programs.</p><p>Packet dissection is (by nature) a sequential task. Information from packet N is used to determine characteristics of packet N+1. That aspect makes packet dissection not very suitable for multithreading. The first dissection run is indeed done sequentially. In Wireshark, when clicking a packet the packet is redissected (for details) using this information. But that is only that packet, so not that much work.</p><p>This basically covers 2, 3 and 4. As for 1 this depends on how many CPU cycles you can trow at it, and memory and I/O bandwidth, and the extensiveness of packet dissection being done. So it's really hard to give numbers on this.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '16, 03:01</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Oct '16, 03:08</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-56440" class="comments-container"><span id="56480"></span><div id="comment-56480" class="comment"><div id="post-56480-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your answer, Jaap</p></div><div id="comment-56480-info" class="comment-info"><span class="comment-age">(17 Oct '16, 18:16)</span> hoangsonk49</div></div></div><div id="comment-tools-56440" class="comment-tools"></div><div class="clear"></div><div id="comment-56440-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="56464"></span>

<div id="answer-container-56464" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56464-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>A few more thoughts (in addition to what Jaap and Anders said)...</p><p>Yes, analyzing packets is by nature fairly sequential. But it should be possible to parallelize it to some extent. For example, it should be possible to send processing of packets for a given TCP session off to a separate thread (e.g., look at source and destination IPs and ports and put that message on a queue for a thread dedicated to that session). Assuming you've got multiple sessions you'll use multiple threads.</p><p>BUT you couldn't do this with Wireshark's source code--at least not in its current state. There are way too many global variables and other thread-unsafeness in the dissectors. There has been a little bit of general work to eliminate this kind of thing but I think it's mostly done on principle with only a slight eye towards eventual thread-safeness.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '16, 06:25</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-56464" class="comments-container"><span id="56481"></span><div id="comment-56481" class="comment"><div id="post-56481-score" class="comment-score"></div><div class="comment-text"><p>Thank you Jeff :)</p></div><div id="comment-56481-info" class="comment-info"><span class="comment-age">(17 Oct '16, 18:16)</span> hoangsonk49</div></div></div><div id="comment-tools-56464" class="comment-tools"></div><div class="clear"></div><div id="comment-56464-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

