+++
type = "question"
title = "Wireshark named pipes disconnect"
description = '''I have managed to make a program that feeds packets to Wireshark through a named pipe. It can detect that Wireshark has stopped/restarted the capture, because writing fails. It can then reopen the pipe, so Wireshark can receive packets when it starts capturing again. What I want is the same, but for...'''
date = "2013-10-29T10:49:00Z"
lastmod = "2013-10-31T04:16:00Z"
weight = 26523
keywords = [ "pipe", "windows", "capture" ]
aliases = [ "/questions/26523" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark named pipes disconnect](/questions/26523/wireshark-named-pipes-disconnect)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26523-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have managed to make a program that feeds packets to Wireshark through a named pipe. It can detect that Wireshark has stopped/restarted the capture, because writing fails. It can then reopen the pipe, so Wireshark can receive packets when it starts capturing again.</p><p>What I want is the same, but for when my application restarts. My question is:</p><p>What does Wireshark do when a named pipe is closed from the server side. Does (can) it recognize this, and is there any way to make Wireshark receive packets on the same pipe, from a new instance of the feeding program, without restarting the capture? I basically want the same functionality with pipes as with network interfaces.</p><p>This is on Windows 7.</p></div><div id="question-tags" class="tags-container tags">pipe windows capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Oct '13, 10:49</strong></p><img src="https://secure.gravatar.com/avatar/d3a401b158e956a431d34c5e71109063?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="oyv&#39;s gravatar image" /><p>oyv<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="oyv has no accepted answers">0%</span></p></div></div><div id="comments-container-26523" class="comments-container"></div><div id="comment-tools-26523" class="comment-tools"></div><div class="clear"></div><div id="comment-26523-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26577"></span>

<div id="answer-container-26577" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26577-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>What does Wireshark do when a named pipe is closed from the server side.</p></blockquote><p>It <strong>stops capturing</strong>.</p><blockquote><p>is there any way to make Wireshark receive packets on the same pipe, from a new instance of the feeding program,</p></blockquote><p>The only way to tell the <strong>running instance</strong> of Wireshark to start capturing again, is by clicking on the appropriate button/menus in the GUI. By doing so, you will either loose the old capture data or you'll have to save them to a file. The GUI will ask you what to do after you requested a capture restart.</p><p>Tested on Linux, but it's the same on Windows:</p><blockquote><p>mkfifo /tmp/pcap_data<br />
tcpdump -ni eth0 -w /tmp/pcap_data &amp;<br />
wireshark -ni /tmp/pcap_data -k &amp;<br />
killall tcpdump<br />
</p></blockquote><p>At this point, Wireshark stops capturing and you need to click in the GUI if you want to restart it.</p><p>So, to answer your question:</p><blockquote><p>and <strong>is there any way</strong> to make <strong>Wireshark receive packets on the same pipe</strong>, from a new instance of the feeding program, <strong>without restarting the capture</strong>?</p></blockquote><p>No. You must restart the capture manually.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Oct '13, 04:16</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-26577" class="comments-container"></div><div id="comment-tools-26577" class="comment-tools"></div><div class="clear"></div><div id="comment-26577-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

