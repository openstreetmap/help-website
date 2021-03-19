+++
type = "question"
title = "Client sends RST after FIN,ACK"
description = '''While doing a file transfer using secure file transfer protocol, I am seeing the behaviour as given in the below image.  Instead accepting packets from server, it simply sends a RST. Found a similar case. https://stackoverflow.com/questions/12320998/client-sends-rst-to-server-after-fin-ack-during-ss...'''
date = "2017-06-08T09:30:00Z"
lastmod = "2017-06-08T09:30:00Z"
weight = 61871
keywords = [ "packet-capture", "packet" ]
aliases = [ "/questions/61871" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Client sends RST after FIN,ACK](/questions/61871/client-sends-rst-after-finack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61871-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>While doing a file transfer using secure file transfer protocol, I am seeing the behaviour as given in the below image.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture_9625rCN.PNG" alt="wireshark output" /></p><p>Instead accepting packets from server, it simply sends a RST. Found a similar case. <a href="https://stackoverflow.com/questions/12320998/client-sends-rst-to-server-after-fin-ack-during-ssl-handshake">https://stackoverflow.com/questions/12320998/client-sends-rst-to-server-after-fin-ack-during-ssl-handshake</a></p><p>But wasn't helpful Please help.</p><p>Regards, Joemon</p></div><div id="question-tags" class="tags-container tags">packet-capture packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '17, 09:30</strong></p><img src="https://secure.gravatar.com/avatar/51e532424651c10f13e3af124aea4640?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="user_shark&#39;s gravatar image" /><p>user_shark<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="user_shark has no accepted answers">0%</span></p></img></div></div><div id="comments-container-61871" class="comments-container"><span id="61874"></span><div id="comment-61874" class="comment"><div id="post-61874-score" class="comment-score"></div><div class="comment-text"><p>Can you share us a trace: <a href="https://blog.packet-foo.com/2016/11/the-wireshark-qa-trace-file-sharing-tutorial/">https://blog.packet-foo.com/2016/11/the-wireshark-qa-trace-file-sharing-tutorial/</a></p></div><div id="comment-61874-info" class="comment-info"><span class="comment-age">(08 Jun '17, 11:48)</span> Christian_R</div></div><span id="61886"></span><div id="comment-61886" class="comment"><div id="post-61886-score" class="comment-score"></div><div class="comment-text"><p>Hi Christian, Please find the trace at the below link <a href="https://drive.google.com/open?id=0ByHA0TOU8EmCdWlyRHJ5YlExSjQ">https://drive.google.com/open?id=0ByHA0TOU8EmCdWlyRHJ5YlExSjQ</a></p></div><div id="comment-61886-info" class="comment-info"><span class="comment-age">(08 Jun '17, 22:14)</span> user_shark</div></div><span id="61923"></span><div id="comment-61923" class="comment"><div id="post-61923-score" class="comment-score"></div><div class="comment-text"><p>What exactly is your problem? That RST itsself is not really bad at that moement. Some systems send an RST to avoid TIME_WAIT2. But it also can be sent due to the Encrypted alert.</p><p>If you have problems with unfinished file transfers, encrypted alert seems to be your problem. Some other side findings can be seen in your trace... Duplicate IP and Spanning Tree Topology Changes.</p></div><div id="comment-61923-info" class="comment-info"><span class="comment-age">(09 Jun '17, 14:15)</span> Christian_R</div></div><span id="61943"></span><div id="comment-61943" class="comment"><div id="post-61943-score" class="comment-score"></div><div class="comment-text"><p>Yes Christian, the problem is with unfinished file transfer. Also can you explain on how is this encrypted alert different from the previous alerts. As you can see for the same connection, the client has accepted many such encrypted alerts sent previously by the server.</p></div><div id="comment-61943-info" class="comment-info"><span class="comment-age">(11 Jun '17, 21:27)</span> user_shark</div></div><span id="61949"></span><div id="comment-61949" class="comment"><div id="post-61949-score" class="comment-score"></div><div class="comment-text"><p>Hi Christian,</p><p>Please ignore the previous captures. Kind of getting a different traces now and the same issue. Please find below the capture from client and server side. <a href="https://drive.google.com/open?id=0ByHA0TOU8EmCZmgweDl3Wi1HZG8">https://drive.google.com/open?id=0ByHA0TOU8EmCZmgweDl3Wi1HZG8</a> <a href="https://drive.google.com/open?id=0ByHA0TOU8EmCWVpPMDM3V0o0MUU">https://drive.google.com/open?id=0ByHA0TOU8EmCWVpPMDM3V0o0MUU</a></p><p>Its showing unreassembled packet [incorrect tcp checksum] Even though I was able to get rid of this error by disabling tcp checksum offloading, still the issue remains.</p></div><div id="comment-61949-info" class="comment-info"><span class="comment-age">(12 Jun '17, 06:49)</span> user_shark</div></div></div><div id="comment-tools-61871" class="comment-tools"></div><div class="clear"></div><div id="comment-61871-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

