+++
type = "question"
title = "TCP transmission deviates from receive window - any legitimate reason"
description = '''I have observed a TCP connection where the client keeps sending data despite the sequence number exceeding the highest ack number + window size received from the peer. Shortly thereafter the peer terminates the connection, and I am trying to figure out why. Is there any legitimate reason to transmit...'''
date = "2015-08-16T10:30:00Z"
lastmod = "2015-08-16T13:42:00Z"
weight = 45146
keywords = [ "window", "xp", "tcp" ]
aliases = [ "/questions/45146" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP transmission deviates from receive window - any legitimate reason](/questions/45146/tcp-transmission-deviates-from-receive-window-any-legitimate-reason)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45146-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have observed a TCP connection where the client keeps sending data despite the sequence number exceeding the highest ack number + window size received from the peer. Shortly thereafter the peer terminates the connection, and I am trying to figure out why. Is there any legitimate reason to transmit the data even though it falls outside the peer's receive window?</p><p>For instance there is an ACK=24220 with Win=65392 and the transmitter responds with a segment with SEQ=93364, which is clearly outside the window. Am I fundamentally misunderstanding how the TCP window is supposed to work?</p><p>The full capture of this particular stream can be found at <a href="https://drive.google.com/file/d/0B17tiJAzTan8Q1VvRm1lcWwtRG8/view?usp=sharing">https://drive.google.com/file/d/0B17tiJAzTan8Q1VvRm1lcWwtRG8/view?usp=sharing</a></p><p>Some more context: the application in question is Picasa's google album upload on Windows XP, which uses the InternetWriteFile API.</p></div><div id="question-tags" class="tags-container tags">window xp tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Aug '15, 10:30</strong></p><img src="https://secure.gravatar.com/avatar/d4e80ef39aa7ca369745a79c6c647a0f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Evgeny&#39;s gravatar image" /><p>Evgeny<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Evgeny has no accepted answers">0%</span></p></div></div><div id="comments-container-45146" class="comments-container"></div><div id="comment-tools-45146" class="comment-tools"></div><div class="clear"></div><div id="comment-45146-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45147"></span>

<div id="answer-container-45147" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45147-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't know why the sender keeps sending data even after the receive window fills. (Something about the way the XP TCP stack works ?)</p><p>I do note, however, that the rate at which the receiver acks the data seems pretty low and that repeated duplicate acks are being received.</p><p>Maybe the connection is being throttled or something...</p><p>Can you try the upload with a more modern version of Windows ?</p><p>The TCP graph of the session is shown below. (Statistics ! Tcp StreamGraph ! Time-Sequence Graph (tcptrace)</p><p>The top line shows the available window (shown as the maximum sequence number of the window); the next shows the send sequence numbers and the bottom line shows the ack sequence numbers for the upload sender to receiver direction.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture_tAGc20b.PNG" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Aug '15, 13:42</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 16 Aug '15, 13:43</p></div></div><div id="comments-container-45147" class="comments-container"><span id="45148"></span><div id="comment-45148" class="comment"><div id="post-45148-score" class="comment-score"></div><div class="comment-text"><p>The other strange issue is that the "Don't Fragment" flag isn't set, which it should be... this doesn't look like a "normal" capture at all :-)</p></div><div id="comment-45148-info" class="comment-info"><span class="comment-age">(16 Aug '15, 14:06)</span> Jasper ♦♦</div></div><span id="45149"></span><div id="comment-45149" class="comment"><div id="post-45149-score" class="comment-score"></div><div class="comment-text"><p>Windows 10 on a different PC on the same WiFi network does not have this problem. This does seem like something specific to XPs stack, however I haven't found any documented bug.</p></div><div id="comment-45149-info" class="comment-info"><span class="comment-age">(16 Aug '15, 14:11)</span> Evgeny</div></div><span id="45150"></span><div id="comment-45150" class="comment"><div id="post-45150-score" class="comment-score"></div><div class="comment-text"><p>... and the server does not support Selective Acknowledgements.</p><p>According to Jaspers finding:</p><p>I found something for Win2000 systems:</p><pre><code>However, if MTU detection is disabled (that is, the value of EnablePMTUDiscovery is 0), the system uses a fixed MTU of 576 bytes. If you change the default value of the MTU entry, you override either setting as it pertains to the interface represented by this subkey.</code></pre><p>This can be found here: <a href="https://technet.microsoft.com/en-us/library/cc938197.aspx">https://technet.microsoft.com/en-us/library/cc938197.aspx</a></p><p>But it seems to be valid for XP, too. Because the largest SegementSize from the Client is 536 in the trace.</p><p>Could you provide the Win10 trace, too?</p></div><div id="comment-45150-info" class="comment-info"><span class="comment-age">(16 Aug '15, 15:01)</span> Christian_R</div></div></div><div id="comment-tools-45147" class="comment-tools"></div><div class="clear"></div><div id="comment-45147-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

