+++
type = "question"
title = "Getting strange SSL record size"
description = '''Hi, We have a software where Client is used to copy file over to and from a server. The communication happens over SSL layer. I am analyzing an issue where file copying is &quot;very&quot; slow using our client-server software when compared with some other tools. What I have observed is that, the packets capt...'''
date = "2014-12-26T12:02:00Z"
lastmod = "2014-12-27T07:30:00Z"
weight = 38718
keywords = [ "ssl", "wireshark" ]
aliases = [ "/questions/38718" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Getting strange SSL record size](/questions/38718/getting-strange-ssl-record-size)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38718-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>We have a software where Client is used to copy file over to and from a server. The communication happens over SSL layer. I am analyzing an issue where file copying is "very" slow using our client-server software when compared with some other tools.</p><p>What I have observed is that, the packets captured follow a pattern. First there will be a packet with a payload data of 16384 bytes (reassembled from 12 assembled TCP segments) and the next one be a packet with payload data of 71 bytes only. And this pattern repeats itself. I am worried about the packet with 71 bytes, is it causing some delay?</p><p>The following is the screenshot of a reassembled packet of 16384 bytes. <img src="https://osqa-ask.wireshark.org/upfiles/packet-16384.png" alt="First Packet" /></p><p>The following is the screenshot of next packet of 71 bytes. <img src="https://osqa-ask.wireshark.org/upfiles/packet-71.png" alt="Second Packet" /></p><p>This pattern of 16384 byte SSL record(?) and 71 byte SSL record(?) keeps on repeating itself till the whole file is uploaded. Could this be slowing down the file transfer? Moreover, why could this thing be happening? Any pointers?</p><p>Sorry if this is something very simple that I can't understand, I am very new to this thing. Thanks for taking time to go through this message.</p></div><div id="question-tags" class="tags-container tags">ssl wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Dec '14, 12:02</strong></p><img src="https://secure.gravatar.com/avatar/679d9d8af4df169fddb0ffc1ea1984a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="prabhatpuroshottam&#39;s gravatar image" /><p>prabhatpuros...<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="prabhatpuroshottam has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 26 Dec '14, 12:07</p></div></div><div id="comments-container-38718" class="comments-container"></div><div id="comment-tools-38718" class="comment-tools"></div><div class="clear"></div><div id="comment-38718-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38732"></span>

<div id="answer-container-38732" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38732-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>First of all: It's hard to do troubleshooting based on screenshot, where most of the interesting parts are missing!! Would it be possible to upload an anonymized capture file (see tracewrangler.com) somewhere (google drive, dropbox, cloudshark.org) and to post the link here??</p><p>Anyway, here are some wild guesses based on the information you provided in the text and the screenshots.</p><ol><li><p>The time stamps of all frames, including frame 76588 with 71 bytes, are within a few milliseconds, if the blackened pieces all belong to the same session! So, I don't believe that the frame with 71 bytes is <strong>causing</strong> the problem.</p></li><li><p>You mentioned 16384 bytes followed by 71 bytes. The first one is 16 Kbyte and sounds like the default size of a buffer, either on client or the server, either application or TCP/IP stack.</p></li><li><p>As there is no information about the rest of the transmission (ACKs, lost frames, timing), it's impossible to give any real explanation, especially as you did not specify what exactly <strong>"slow"</strong> means in your context.</p></li></ol><p>So, here are some ideas:</p><p>Idea #1: Try to find the value of 16 Kbyte in your code or the config of your TCP/IP stack (send/receive buffer) and increase that value. Maybe that will increase throughput.</p><p>Idea #2: Compare a capture file created with your application to one created with another client. How do they differ?</p><p>Idea #3: draw the following I/O graphs and post them here.</p><ul><li>Statistics -&gt; TCP Stream Graph -&gt; Window Scaling Graph<br />
</li><li>Statistics -&gt; TCP Stream Graph -&gt; Time-Squence Graph (tcptrace)</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Dec '14, 07:30</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></img></div></div><div id="comments-container-38732" class="comments-container"></div><div id="comment-tools-38732" class="comment-tools"></div><div class="clear"></div><div id="comment-38732-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

