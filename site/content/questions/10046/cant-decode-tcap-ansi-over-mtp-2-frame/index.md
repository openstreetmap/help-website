+++
type = "question"
title = "Can&#x27;t decode TCAP ANSI over MTP-2 frame."
description = '''Hi Guys, I&#x27;m trying to open a TCAP ANSI trace that is over MTP-2, but Wireshark decodes the lower layers (MTP-2 and MTP-3) as Ethernet. I tried to force the decode to MTP-2 using &quot;Decode As...&quot; but couldn&#x27;t find such option. Below you can an example: c0 af 28 83 22 73 02 02 e6 e1 0b 09 80 03 05 0a 0...'''
date = "2012-04-10T12:48:00Z"
lastmod = "2012-10-04T11:18:00Z"
weight = 10046
keywords = [ "decode", "mtp-2" ]
aliases = [ "/questions/10046" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can't decode TCAP ANSI over MTP-2 frame.](/questions/10046/cant-decode-tcap-ansi-over-mtp-2-frame)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10046-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10046-score" class="post-score" title="current number of votes">0</div><span id="post-10046-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Guys,</p><p>I'm trying to open a TCAP ANSI trace that is over MTP-2, but Wireshark decodes the lower layers (MTP-2 and MTP-3) as Ethernet. I tried to force the decode to MTP-2 using "Decode As..." but couldn't find such option.</p><p>Below you can an example:</p><p>c0 af 28 83 22 73 02 02 e6 e1 0b 09 80 03 05 0a</p><p>02 c1 0b 05 c3 08 02 e6 e1 11 e4 0f c7 04 04 00<br />
</p><p>0b 6c e8 07 ea 05 cf 01 01 f2 00 40 a4<br />
</p><p>Does anyone know the reason for this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span> <span class="post-tag tag-link-mtp-2" rel="tag" title="see questions tagged &#39;mtp-2&#39;">mtp-2</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Apr '12, 12:48</strong></p><img src="https://secure.gravatar.com/avatar/c2b40f9e0475b00c41a44d2cdfb81081?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fertonin&#39;s gravatar image" /><p><span>fertonin</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fertonin has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-10046" class="comments-container"></div><div id="comment-tools-10046" class="comment-tools"></div><div class="clear"></div><div id="comment-10046-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10048"></span>

<div id="answer-container-10048" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10048-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10048-score" class="post-score" title="current number of votes">1</div><span id="post-10048-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If this is a pcap or pcap-ng trace, the reason is probably that somebody put the wrong link-layer header type value in the capture file header (for pcap) or Interface Description Block for the interface (for pcap-ng).</p><p>Wireshark has no "Decode As" for overriding the link-layer header type, because that's not something that's supposed to be wrong. For pcap files, you could try using <code>editcap</code> to forcibly change the link-layer header type value, for example:</p><pre><code>editcap -T mtp2 {bad capture file} {name for new capture file}</code></pre><p>where {bad capture file} is the pathname of the file you're trying to open and {name for new capture file} is the pathname for the location where you want the fixed capture file to be put. If you can successfully read the new capture file, you can just replace the old capture file with the new one.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Apr '12, 15:33</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-10048" class="comments-container"><span id="10062"></span><div id="comment-10062" class="comment"><div id="post-10062-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot Guy, it worked, I ran the suggested command and was able to see the decode.</p></div><div id="comment-10062-info" class="comment-info"><span class="comment-age">(11 Apr '12, 13:53)</span> <span class="comment-user userinfo">fertonin</span></div></div><span id="10063"></span><div id="comment-10063" class="comment"><div id="post-10063-score" class="comment-score"></div><div class="comment-text"><p>So how was that trace produced? Whatever produced it put the wrong link-layer header type in the file, and should probably be fixed to use the right link-layer header type, so the files can directly be read by, for example, Wireshark.</p></div><div id="comment-10063-info" class="comment-info"><span class="comment-age">(11 Apr '12, 14:06)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="14701"></span><div id="comment-14701" class="comment"><div id="post-14701-score" class="comment-score"></div><div class="comment-text"><p>I have a pcap file with both ISUP over MTP-2 packets and ISUP over IP (Ethernet) packets. From what I understand the -T mtp2 is global for the whole packets in the pcap file. Is there a way to set the link-layer type for a packet?</p></div><div id="comment-14701-info" class="comment-info"><span class="comment-age">(04 Oct '12, 03:08)</span> <span class="comment-user userinfo">Erez</span></div></div><span id="14712"></span><div id="comment-14712" class="comment"><div id="post-14712-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I have a pcap file with both ISUP over MTP-2 packets and ISUP over IP (Ethernet) packets.</p></blockquote><p>The pcap file format has only a per-file link-layer type, so it can't handle files with a mixture of MTP2 packets and Ethernet packets. Whoever chose to write it out as a pcap file made a mistake by doing so; they should have used pcap-NG format instead.</p><p>You'd probably have to write your own tool to read the file, somehow figure out or be told by the user which packets are Ethernet packets and which packets are MTP2 packets, and write out a pcap-NG file.</p></div><div id="comment-14712-info" class="comment-info"><span class="comment-age">(04 Oct '12, 11:18)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-10048" class="comment-tools"></div><div class="clear"></div><div id="comment-10048-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

