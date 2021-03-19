+++
type = "question"
title = "How to get IP of the server i&#x27;m connecting to"
description = '''Hello everyone. I&#x27;d like to know the IP of a TCP server I&#x27;m connecting to. For example, while I play a game and I&#x27;m connecting to a server, I wanna know the IP of that server. People tells me that Wireshark CAN do this, since it sniffs your network traffic. So, how to capture the IP of the TCP serve...'''
date = "2015-11-02T03:16:00Z"
lastmod = "2015-11-02T09:18:00Z"
weight = 47142
keywords = [ "ip", "server" ]
aliases = [ "/questions/47142" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to get IP of the server i'm connecting to](/questions/47142/how-to-get-ip-of-the-server-im-connecting-to)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47142-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone.</p><p>I'd like to know the IP of a TCP server I'm connecting to. For example, while I play a game and I'm connecting to a server, I wanna know the IP of that server.</p><p>People tells me that Wireshark CAN do this, since it sniffs your network traffic.</p><p>So, how to capture the IP of the TCP server I'm connecting to?</p><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags">ip server</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Nov '15, 03:16</strong></p><img src="https://secure.gravatar.com/avatar/7c0f7c2a6d76c78ec4fedc08c7ba9daa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtur&#39;s gravatar image" /><p>mtur<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtur has no accepted answers">0%</span></p></div></div><div id="comments-container-47142" class="comments-container"></div><div id="comment-tools-47142" class="comment-tools"></div><div class="clear"></div><div id="comment-47142-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47161"></span>

<div id="answer-container-47161" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47161-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><ol><li>Download and install Wireshark on the PC that will connect to the server.</li><li>Open Wireshark and start a capture.</li><li>On the same PC running Wireshark, start the TCP connection.</li><li>Wait for the connection to the server to be established and some data is transferred.</li><li>Stop the capture on Wireshark.</li><li>Enter the following display filter in wireshark: tcp</li></ol><p>This will list all the TCP streams that was captured.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '15, 09:18</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-47161" class="comments-container"><span id="47163"></span><div id="comment-47163" class="comment"><div id="post-47163-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply. I wanted to know if there's a way to determine which is the right one in the great list that shows up on the screen!</p></div><div id="comment-47163-info" class="comment-info"><span class="comment-age">(02 Nov '15, 09:26)</span> mtur</div></div><span id="47165"></span><div id="comment-47165" class="comment"><div id="post-47165-score" class="comment-score"></div><div class="comment-text"><p>If you know the TCP port that is being used for the connection, then you can use the display filter tcp.port==xx where xx is the port number. For example, web traffic use port 80 and port 8080, so the filter would be:</p><p>tcp.port==80 || tcp.port==8080</p><p>If you know the IP address of the TCP server, then you could use the display fitler: ip.addr==x.x.x.x</p><p>If you want more help, then you have to provide more details on the TCP connection you want to investigate and preferably leave a capture file on cloudshark or Google drive, etc.</p></div><div id="comment-47165-info" class="comment-info"><span class="comment-age">(02 Nov '15, 10:17)</span> Amato_C</div></div></div><div id="comment-tools-47161" class="comment-tools"></div><div class="clear"></div><div id="comment-47161-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

