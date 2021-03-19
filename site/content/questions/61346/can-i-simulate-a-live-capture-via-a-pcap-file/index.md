+++
type = "question"
title = "Can I &quot;simulate a live capture&quot; via a .pcap file?"
description = '''Hi there, I&#x27;m looking to record some videos from the Wireshark interface and for that purpose I would like to simulate a scenario where I&#x27;m live capturing the data while recording the screen. For practical reasons, however, it would be ideal if I could &quot;play&quot; a pcap file so that it appears as if the...'''
date = "2017-05-10T14:23:00Z"
lastmod = "2017-05-13T10:39:00Z"
weight = 61346
keywords = [ "capture", "replay", "pcap", "wireshark", "player" ]
aliases = [ "/questions/61346" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Can I "simulate a live capture" via a .pcap file?](/questions/61346/can-i-simulate-a-live-capture-via-a-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61346-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>I'm looking to record some videos from the Wireshark interface and for that purpose I would like to simulate a scenario where I'm live capturing the data while recording the screen. For practical reasons, however, it would be ideal if I could "play" a pcap file so that it appears as if the data is coming in message-by-message (as in live capture) at the original speed of the incoming transmissions.</p><p>Is this possible in Wireshark or via some plugin?</p><p>Thank you, Martin</p></div><div id="question-tags" class="tags-container tags">capture replay pcap wireshark player</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 May '17, 14:23</strong></p><img src="https://secure.gravatar.com/avatar/bb505f6832bb10125678c300fff66aae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mfcss&#39;s gravatar image" /><p>mfcss<br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mfcss has no accepted answers">0%</span></p></div></div><div id="comments-container-61346" class="comments-container"></div><div id="comment-tools-61346" class="comment-tools"></div><div class="clear"></div><div id="comment-61346-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="61348"></span>

<div id="answer-container-61348" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61348-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think there are tools that can take a capture file and replay it, using the packet time stamps to determine when to send the packets, so that, for example, if two packets in the file have time stamps 1 second apart, the packets will be sent 1 second apart.</p><p>That may not be what you want, however, as it causes actual network traffic to occur.</p><p>In theory, a program could be written that reads a capture file and writes the records from the capture file to the standard output, with the delays between packet records being determined by the packet time stamps; you could then start Wireshark up, capturing from a pipe, and have the program write to the pipe. That would look a little different, when starting up, from a live capture, but it'd look very similar to a live capture as the packets come in. I don't know of such a tool, however.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 May '17, 21:39</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-61348" class="comments-container"></div><div id="comment-tools-61348" class="comment-tools"></div><div class="clear"></div><div id="comment-61348-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="61384"></span>

<div id="answer-container-61384" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61384-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe you can use 'tcpreplay'?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '17, 10:39</strong></p><img src="https://secure.gravatar.com/avatar/1bd7aa9ec4636e9d234ddfb63bb15f85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="r00t070&#39;s gravatar image" /><p>r00t070<br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="r00t070 has no accepted answers">0%</span></p></div></div><div id="comments-container-61384" class="comments-container"></div><div id="comment-tools-61384" class="comment-tools"></div><div class="clear"></div><div id="comment-61384-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

