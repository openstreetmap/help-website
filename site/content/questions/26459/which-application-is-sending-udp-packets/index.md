+++
type = "question"
title = "Which application is sending UDP packets"
description = '''How to know which application is sending udp data packet using wire shark?please help. i want to track which application is sending or receiving udp data packets in my pc, i tried filtering udp packets, but i am not able to track the root application .please give me a solution for this.'''
date = "2013-10-28T02:44:00Z"
lastmod = "2013-10-28T08:55:00Z"
weight = 26459
keywords = [ "udp", "pid" ]
aliases = [ "/questions/26459" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Which application is sending UDP packets](/questions/26459/which-application-is-sending-udp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26459-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to know which application is sending udp data packet using wire shark?please help. i want to track which application is sending or receiving udp data packets in my pc, i tried filtering udp packets, but i am not able to track the root application .please give me a solution for this.</p></div><div id="question-tags" class="tags-container tags">udp pid</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Oct '13, 02:44</strong></p><img src="https://secure.gravatar.com/avatar/a4a870837f401c5d0af370f8fc1b949d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shafaquatbari&#39;s gravatar image" /><p>shafaquatbari<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shafaquatbari has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted to question 28 Oct '13, 03:05</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-26459" class="comments-container"></div><div id="comment-tools-26459" class="comment-tools"></div><div class="clear"></div><div id="comment-26459-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="26473"></span>

<div id="answer-container-26473" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26473-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, it's a multi-step process. Here's one way.<br />
</p><p>At the same time that you are capturing the Wireshark trace, also capture the output from netstat (more on that in a minute) on the host that's using the UDP connection you are interested in.<br />
</p><p>Filter the Wireshark trace to find the UDP packets of interest. Look at the port number being used in those UDP packets. Find that port number in the netstat output. You might see something like 143.169.14.133:51126 (where 51126 is the port number in this case), and then note the PID (Process ID) given on the same line.</p><p>The PID will identify the running application that is using UDP to communicate. You can find the application based on the PID on the Processes tab in Windows Task Manager.</p><p>The parameters used on netstat will vary depending on the host operating system. For Windows, something like "netstat -a -o -p UDP &gt; netstat.out" should do the trick.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '13, 08:49</strong></p><img src="https://secure.gravatar.com/avatar/b260fb38b621169269b5030f1ed6b766?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="griff&#39;s gravatar image" /><p>griff<br />
<span class="score" title="361 reputation points">361</span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="griff has 2 accepted answers">10%</span> </br></br></p></div></div><div id="comments-container-26473" class="comments-container"></div><div id="comment-tools-26473" class="comment-tools"></div><div class="clear"></div><div id="comment-26473-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26476"></span>

<div id="answer-container-26476" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26476-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If the pc is running windows you can try using Message Analyser from Microsoft as that captures the sending process along with the network traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '13, 08:55</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-26476" class="comments-container"></div><div id="comment-tools-26476" class="comment-tools"></div><div class="clear"></div><div id="comment-26476-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

