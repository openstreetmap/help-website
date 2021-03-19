+++
type = "question"
title = "Performance: bandwidth + packets"
description = '''Hi All, I might sound like a noob but I had to ask after attempts after attempts for several hours to determine a simple thing. I need to determine the rate (speed, bandwidth) at which a file(600MB) is transferred from PC-A to PC-B and whether any packets are dropped. I&#x27;ve connected two computers to...'''
date = "2014-06-02T03:43:00Z"
lastmod = "2016-01-13T11:02:00Z"
weight = 33264
keywords = [ "bandwidth", "packet", "mbs" ]
aliases = [ "/questions/33264" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Performance: bandwidth + packets](/questions/33264/performance-bandwidth-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33264-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I might sound like a noob but I had to ask after attempts after attempts for several hours to determine a simple thing.</p><p>I need to determine the rate (speed, bandwidth) at which a file(600MB) is transferred from PC-A to PC-B and whether any packets are dropped.</p><p>I've connected two computers together over Ethernet. Host A : 192.168.1.10 - running wireshark and downloading large file from Host B through Network drive. Host B : 192.168.1.20 - Having a large file in its network drive for Host A to download.</p><p>Question 1 - What's the most effective way to find out the speed of file transfer in MBps ? Question 2 - How can I tell if none of the packets are dropped.</p><p>Thanks ALOT in advance.</p><p>Note: I am not being lazy and trying to find a quick solution, I had actually spend hours and hours to go through guide and manuals but my brain just went numb. Thanks</p></div><div id="question-tags" class="tags-container tags">bandwidth packet mbs</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jun '14, 03:43</strong></p><img src="https://secure.gravatar.com/avatar/ea378ada3a5c942cdc2ce7a07b1dae5d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andrea_89&#39;s gravatar image" /><p>Andrea_89<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andrea_89 has no accepted answers">0%</span></p></div></div><div id="comments-container-33264" class="comments-container"></div><div id="comment-tools-33264" class="comment-tools"></div><div class="clear"></div><div id="comment-33264-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="49176"></span>

<div id="answer-container-49176" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49176-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Aside from the following, Wireshark really doesn't provide such a value:</p><ul><li>tshark.exe filename.pcap -r -T fields -e "radiotap.datarate" &gt; filename.datarate.txt</li><li>see "radiotap" WireShark documentation;</li><li>also search tshark documentation if you have issues running tshark;</li><li>this is best put into a batch file if coded properly.</li><li>Statistics &gt;&gt; Follow TCP Stream &gt;&gt; Look in header info</li><li>Statistics &gt;&gt; Conversations or Statistics &gt;&gt; Conversation List &gt;&gt; [Protocol] ; one of the colums contains the rate</li><li>Summary &gt;&gt; Avg. MBps</li><li>In an external program such as matlab, calculate it using ((cumulativedata/relativetime)* 8 / 10^6)</li></ul><p>Other than that, through extensive research on this issue (3 Weeks of searching myself), I don't think there is any other forms of available information that Wireshark can give you as far as I am concerned.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '16, 08:55</strong></p><img src="https://secure.gravatar.com/avatar/3a4bc2ba5c09d24f214dc472eb5b7993?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Midimistro&#39;s gravatar image" /><p>Midimistro<br />
<span class="score" title="11 reputation points">11</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Midimistro has one accepted answer">50%</span></p></div></div><div id="comments-container-49176" class="comments-container"></div><div id="comment-tools-49176" class="comment-tools"></div><div class="clear"></div><div id="comment-49176-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="49182"></span>

<div id="answer-container-49182" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49182-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Τhe answer depends on the protocol/application you use to transfer the file.</p><p>If you use ftp, one tcp session is used for control and another one gets open ad-hoc for the file transfer itself, so it is easy to use <code>Statistics -&gt; Conversations</code> to find the counts of packets and bytes and duration of the session and calculate the average transmission speed. <code>Statistics -&gt; TCP Stream Graphs -&gt; Throughput</code> will show you the throughput over time.</p><p>If you use protocols which use a single common tcp session for control and data, like SMB/SMB2 or scp, sftp, you may have to use information contained in the control messages of that protocol to identify the first and last packet of the particular file you are interested in (if you actually are only interested in a single file).</p><p>In both cases, I am also unable to find any method to provide summary information about the number of retransmitted (due to loss) packets. But if it is enough for you to know whether the total transfer time was longer than you've expected due to packet loss or due to something else: if, after applying a display filter <code>tcp.analysis.retransmission</code> , you can see some packets, then there were retransmissions. Otherwise, the reason of the slowness is something else.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '16, 11:02</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-49182" class="comments-container"></div><div id="comment-tools-49182" class="comment-tools"></div><div class="clear"></div><div id="comment-49182-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

