+++
type = "question"
title = "Bogus error"
description = '''Hi,  Analyzing a capture, Expert information shows an error I have never heard of: Expert Info (Error/Malformed): bogus, should be &amp;gt;= 8 Running WS Version 2.2.4 (v2.2.4-0-gcc3dc1b)on a dedicated Win 2008 R2 Enterprise server Does anybody know what this error means? There are more than 16000 of th...'''
date = "2017-07-11T02:52:00Z"
lastmod = "2017-07-11T07:25:00Z"
weight = 62662
keywords = [ "bogus" ]
aliases = [ "/questions/62662" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Bogus error](/questions/62662/bogus-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62662-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62662-score" class="post-score" title="current number of votes">0</div><span id="post-62662-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Analyzing a capture, Expert information shows an error I have never heard of: Expert Info (Error/Malformed): bogus, should be &gt;= 8</p><p>Running WS Version 2.2.4 (v2.2.4-0-gcc3dc1b)on a dedicated Win 2008 R2 Enterprise server</p><p>Does anybody know what this error means? There are more than 16000 of these in a 100kB file size for a time frame: Elapsed: 00:01:29</p><p>Thx.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bogus" rel="tag" title="see questions tagged &#39;bogus&#39;">bogus</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jul '17, 02:52</strong></p><img src="https://secure.gravatar.com/avatar/4fc43c83d14e6cb53bf36dd8013dbcf1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="profke&#39;s gravatar image" /><p><span>profke</span><br />
<span class="score" title="10 reputation points">10</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="profke has no accepted answers">0%</span></p></div></div><div id="comments-container-62662" class="comments-container"><span id="62665"></span><div id="comment-62665" class="comment"><div id="post-62665-score" class="comment-score"></div><div class="comment-text"><p>Not without an example of such packet (you can export a single packet from a capture file if you are concerned about privacy).</p><p>Each dissector has its own criteria to declare a packet malformed and each provides its own amount of additional information.</p></div><div id="comment-62665-info" class="comment-info"><span class="comment-age">(11 Jul '17, 03:09)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="62668"></span><div id="comment-62668" class="comment"><div id="post-62668-score" class="comment-score"></div><div class="comment-text"><p>Thanks , but How can I can upload a file?</p></div><div id="comment-62668-info" class="comment-info"><span class="comment-age">(11 Jul '17, 05:35)</span> <span class="comment-user userinfo">profke</span></div></div><span id="62669"></span><div id="comment-62669" class="comment"><div id="post-62669-score" class="comment-score"></div><div class="comment-text"><p>I show one packet with this message:</p><p><code> No.     Time                          Source                Destination           Protocol Length Window size value Time since previous frame in this TCP stream Info      17 2017-07-10 23:55:52.952907    170.86.43.201         170.86.39.97          TCP      1514   254               0.000422000                                  1526 → 54748 [ACK] Seq=8182 Ack=22 Win=254 Len=1460 Frame 17: 1514 bytes on wire (12112 bits), 1514 bytes captured (12112 bits) on interface 0 Ethernet II, Src: Cisco_12:67:c1 (e4:c7:22:12:67:c1), Dst: VMware_9d:00:33 (00:50:56:9d:00:33) Internet Protocol Version 4, Src: 170.86.43.201, Dst: 170.86.39.97 Transmission Control Protocol, Src Port: 1526, Dst Port: 54748, Seq: 8182, Ack: 22, Len: 1460 Tabular Data Stream     Type: Bulk load data (7)     Status: 0xdb     Length: 0         [Expert Info (Error/Malformed): bogus, should be &gt;= 8]             [bogus, should be &gt;= 8]             [Severity level: Error]             [Group: Malformed]</code></p></div><div id="comment-62669-info" class="comment-info"><span class="comment-age">(11 Jul '17, 05:57)</span> <span class="comment-user userinfo">profke</span></div></div><span id="62671"></span><div id="comment-62671" class="comment"><div id="post-62671-score" class="comment-score"></div><div class="comment-text"><p>In general, to post a pcap file "here" you have to upload it to Cloudshark or to any generic file sharing service, and provide a link to it here (preferably by editing the Question).</p><p>In case of a single packet, you can alternatively right-click the Frame layer in the packet dissection pane and use <code>Copy -&gt; ...as Hex Dump</code>, and then paste the clipboard here. Anyone can then import the hex dump into Wireshark.</p></div><div id="comment-62671-info" class="comment-info"><span class="comment-age">(11 Jul '17, 06:50)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-62662" class="comment-tools"></div><div class="clear"></div><div id="comment-62662-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62667"></span>

<div id="answer-container-62667" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62667-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62667-score" class="post-score" title="current number of votes">0</div><span id="post-62667-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It says (in general): "This field / length shall be greater or equal to 8, but it's less. This is an error in this protocol". So, nothing bogus about that, unless you can show exactly what protocol it is, what field / length it refers to and why it is valid.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jul '17, 04:24</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span> </br></p></div></div><div id="comments-container-62667" class="comments-container"><span id="62670"></span><div id="comment-62670" class="comment"><div id="post-62670-score" class="comment-score"></div><div class="comment-text"><p>Dag Jaap, wat bedoel je met "So, nothing bogus about that "?</p></div><div id="comment-62670-info" class="comment-info"><span class="comment-age">(11 Jul '17, 06:00)</span> <span class="comment-user userinfo">profke</span></div></div><span id="62673"></span><div id="comment-62673" class="comment"><div id="post-62673-score" class="comment-score">1</div><div class="comment-text"><p>Note that it's possible that the traffic isn't <em>Tablular Data Stream</em> traffic at all. If that's the case and you know what protocol it's supposed to be, you could try to right-click on the TDS information line of a TDS packet within the Packet Details Pane and then choose <em>"Decode As..."</em> to choose which protocol should be dissecting the packets for TCP port 1526. Alternatively, you could just disable the TDS dissector, even if temporarily, via <em>Analyze -&gt; Enabled Protocols -&gt; TDS</em> if you know it's not TDS traffic.</p><p>If it <strong>is</strong> TDS traffic though, then it's malformed, so Wireshark is correctly reporting a bogus <code>tds.length</code> field in that case as Jaap stated.</p></div><div id="comment-62673-info" class="comment-info"><span class="comment-age">(11 Jul '17, 07:25)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-62667" class="comment-tools"></div><div class="clear"></div><div id="comment-62667-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

