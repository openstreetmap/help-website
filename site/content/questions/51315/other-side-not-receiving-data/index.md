+++
type = "question"
title = "Other side not receiving data"
description = '''Hi, I&#x27;m having an issue with TCP communication between two computers. Computer1 at address 192.168.254.39 is supposed to initiate a connection to Computer2 192.168.254.37 on port 6010, and send a short message, 400-800 ASCII characters approximately. Computer2 is then supposed to process that messag...'''
date = "2016-03-31T11:06:00Z"
lastmod = "2016-03-31T12:13:00Z"
weight = 51315
keywords = [ "packets", "syn" ]
aliases = [ "/questions/51315" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Other side not receiving data](/questions/51315/other-side-not-receiving-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51315-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm having an issue with TCP communication between two computers. Computer1 at address 192.168.254.39 is supposed to initiate a connection to Computer2 192.168.254.37 on port 6010, and send a short message, 400-800 ASCII characters approximately. Computer2 is then supposed to process that message and respond with a short message of its own, approx 150-300 characters. Computer1 should then close the connection.</p><p>What's happening here is that Computer1 connects, Computer2 receives the connection and accepts it, Computer1 sends the message, but Computer2 does not seem to receive it (I haven't put WireShark on Computer2 yet so not exactly sure what's coming in there). Looking at the communication, is there anything odd here?</p><p><img src="http://i67.tinypic.com/70gn50.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">packets syn</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Mar '16, 11:06</strong></p><img src="https://secure.gravatar.com/avatar/9c23251f8184b2e649c14a863ae54601?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sarah%20B&#39;s gravatar image" /><p>Sarah B<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sarah B has no accepted answers">0%</span></p></img></div></div><div id="comments-container-51315" class="comments-container"><span id="51317"></span><div id="comment-51317" class="comment"><div id="post-51317-score" class="comment-score"></div><div class="comment-text"><p>Could you Provide us thaw capture file at a public accessible place like Dropbox? You can use a tool like tracewrangler to anomyze the trace</p></div><div id="comment-51317-info" class="comment-info"><span class="comment-age">(31 Mar '16, 12:11)</span> Christian_R</div></div></div><div id="comment-tools-51315" class="comment-tools"></div><div class="clear"></div><div id="comment-51315-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51318"></span>

<div id="answer-container-51318" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51318-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's very difficult to troubleshoot from a screen shot. Instead, post a capture file (assuming it doesn't contain confidential information) somewhere publicly accessible, like <a href="http://www.cloudshark.org">Cloudshark</a>, or Google Drive, or Dropbox and then edit your question to include a link to the file.</p><p>Computer 2 does receive the data, it just doesn't respond with an application-layer message. Computer 1 sends 421 bytes of data in packet 812 and Computer B acknowledges that data in packet 818. Computer 1 sends 736 bytes of data in packet 892 and Computer B acknowledges that data in packet 908.</p><p>Computer B receives both data packets, but never sends any data back. Computer A waits about 2.8 seconds and then closes the connection.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Mar '16, 12:13</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-51318" class="comments-container"><span id="51321"></span><div id="comment-51321" class="comment"><div id="post-51321-score" class="comment-score"></div><div class="comment-text"><p>Thank you. I'm using WireShark 2.0.2. In which format should I save the capture file?</p></div><div id="comment-51321-info" class="comment-info"><span class="comment-age">(31 Mar '16, 12:20)</span> Sarah B</div></div><span id="51322"></span><div id="comment-51322" class="comment"><div id="post-51322-score" class="comment-score"></div><div class="comment-text"><p>Also, yes, the messages sent by Computer A do have confidential information and I will need to edit it. So saving to a file that will allow simple editing helps.</p></div><div id="comment-51322-info" class="comment-info"><span class="comment-age">(31 Mar '16, 12:26)</span> Sarah B</div></div><span id="51323"></span><div id="comment-51323" class="comment"><div id="post-51323-score" class="comment-score"></div><div class="comment-text"><p>Either .pcap or .pcapng. .pcapng is Wireshark's default format.</p><p>You can use TraceWrangler, available from www.tracewrangler.com, to remove the payload.</p></div><div id="comment-51323-info" class="comment-info"><span class="comment-age">(31 Mar '16, 12:28)</span> Jim Aragon</div></div><span id="51325"></span><div id="comment-51325" class="comment"><div id="post-51325-score" class="comment-score"></div><div class="comment-text"><p>While having an actual trace file is better, in this case, we're probably already seeing everything that's relevant. Again, Computer 2 DOES receive the data. However, Computer 2 does not respond with its own application-layer message. All we can see is that it doesn't send anything. Wireshark shows us what's happening on the network, but not why it's happening. You're going to have to investigate Computer 2 to see why it doesn't respond. Network packets are not going to explain why.</p></div><div id="comment-51325-info" class="comment-info"><span class="comment-age">(31 Mar '16, 14:34)</span> Jim Aragon</div></div></div><div id="comment-tools-51318" class="comment-tools"></div><div class="clear"></div><div id="comment-51318-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

