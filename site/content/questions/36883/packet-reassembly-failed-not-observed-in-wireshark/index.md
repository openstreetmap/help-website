+++
type = "question"
title = "packet reassembly failed - not observed in wireshark"
description = '''I am trying to run netperf between two machines. with UDP_STREAM case.  While running netperf client , I can see &quot;packet reassemblies failed&quot; count incremented to a huge number in netserver using the command &quot;netstat -s&quot;. I run the wireshark during the same time, but CANNOT observe any errors as suc...'''
date = "2014-10-07T00:20:00Z"
lastmod = "2014-10-07T00:20:00Z"
weight = 36883
keywords = [ "ethernet", "udp", "wireshark" ]
aliases = [ "/questions/36883" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [packet reassembly failed - not observed in wireshark](/questions/36883/packet-reassembly-failed-not-observed-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36883-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to run netperf between two machines. with UDP_STREAM case.</p><p>While running netperf client , I can see "packet reassemblies failed" count incremented to a huge number in netserver using the command "netstat -s".</p><p>I run the wireshark during the same time, but CANNOT observe any errors as such. My understanding is, Wireshark should be able to notice these packets as errors and display the same.??</p><p>Is that mean, even before wireshark capture these "packet reassemblies failed" packets, they get dropped ??</p><p>Please help.</p></div><div id="question-tags" class="tags-container tags">ethernet udp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Oct '14, 00:20</strong></p><img src="https://secure.gravatar.com/avatar/03741fde046267f91ecf3e1989f88cc2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="saro&#39;s gravatar image" /><p>saro<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="saro has no accepted answers">0%</span></p></div></div><div id="comments-container-36883" class="comments-container"><span id="36892"></span><div id="comment-36892" class="comment"><div id="post-36892-score" class="comment-score"></div><div class="comment-text"><p>From the info above I guess that the packets are over UDP. If there is no dissector in Wireshark for the UDP packets there will be no reassembly done as Wireshar only "see" UDP datagrams and have no notion of the content.</p></div><div id="comment-36892-info" class="comment-info"><span class="comment-age">(07 Oct '14, 03:29)</span> Anders ♦</div></div><span id="36893"></span><div id="comment-36893" class="comment"><div id="post-36893-score" class="comment-score"></div><div class="comment-text"><p>Yes, I am talking about UDP only.</p></div><div id="comment-36893-info" class="comment-info"><span class="comment-age">(07 Oct '14, 06:41)</span> saro</div></div><span id="36894"></span><div id="comment-36894" class="comment"><div id="post-36894-score" class="comment-score"></div><div class="comment-text"><p>I have another related question. There is an option called UFO (UDP fragmentation offload). Fragmentation is related to IP layer..Why it is tied to UDP alone? why not TCP also? bit confused here. ( Reason for the question is: I see issue only with UFO ON)</p></div><div id="comment-36894-info" class="comment-info"><span class="comment-age">(07 Oct '14, 06:42)</span> saro</div></div></div><div id="comment-tools-36883" class="comment-tools"></div><div class="clear"></div><div id="comment-36883-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

