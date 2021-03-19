+++
type = "question"
title = "PCAPNG: timestamps get changed when tshark reads and saves a pcang file"
description = '''When you try to read a pcapng file and save it to a new pcapng file, the timestamp was trimmed down! The decimal place is moved to the front and the last digit is rounded off. The timestamp is no longer correct. Could anyone please help how to correct it?  Thanks a lot! -----------------------------...'''
date = "2012-07-02T20:54:00Z"
lastmod = "2012-07-10T12:21:00Z"
weight = 12382
keywords = [ "timestamp", "pcapng", "tshark" ]
aliases = [ "/questions/12382" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [PCAPNG: timestamps get changed when tshark reads and saves a pcang file](/questions/12382/pcapng-timestamps-get-changed-when-tshark-reads-and-saves-a-pcang-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12382-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12382-score" class="post-score" title="current number of votes">0</div><span id="post-12382-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When you try to read a pcapng file and save it to a new pcapng file, the timestamp was trimmed down! The decimal place is moved to the front and the last digit is rounded off. The timestamp is no longer correct. Could anyone please help how to correct it? Thanks a lot!</p><pre><code>--------------------------------------------------
$ tshark -r capture.20120625.pcapng -t e | head -3
1 1340398414.509256500 Cisco_fe:3b:7d -&gt; Spanning-tree-(for-bridges)_00 STP 53 RST. Root = 32768/20/00:05:73:fe:3b:81  Cost = 0  Port = 0x80b6
2 1340398416.805447300 Cisco_fe:3b:7d -&gt; Spanning-tree-(for-bridges)_00 STP 53 RST. Root = 32768/20/00:05:73:fe:3b:81  Cost = 0  Port = 0x80b6
3 1340398417.391487800 Cisco_fe:3b:7d -&gt; CDP/VTP/DTP/PAgP/UDLD UDLD 128 Device ID: SSI1516004B  Port ID: Ethernet1/50/2enter code here`
--------------------------------------------------
$ tshark -F pcapng -r capture.20120625.pcapng -w testout.pcapng -c 3

--------------------------------------------------
$ tshark -r testout.pcapng -t e | head -3
1 134039841.450925600 Cisco_fe:3b:7d -&gt; Spanning-tree-(for-bridges)_00 STP 53 RST. Root = 32768/20/00:05:73:fe:3b:81  Cost = 0  Port = 0x80b6
2 134039841.680544700 Cisco_fe:3b:7d -&gt; Spanning-tree-(for-bridges)_00 STP 53 RST. Root = 32768/20/00:05:73:fe:3b:81  Cost = 0  Port = 0x80b6
3 134039841.739148700 Cisco_fe:3b:7d -&gt; CDP/VTP/DTP/PAgP/UDLD UDLD 128 Device ID: SSI1516004B  Port ID: Ethernet1/50/2
--------------------------------------------------</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timestamp" rel="tag" title="see questions tagged &#39;timestamp&#39;">timestamp</span> <span class="post-tag tag-link-pcapng" rel="tag" title="see questions tagged &#39;pcapng&#39;">pcapng</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jul '12, 20:54</strong></p><img src="https://secure.gravatar.com/avatar/93e97990f1e376a3e714949b7b107751?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Holy&#39;s gravatar image" /><p><span>Holy</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Holy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Jul '12, 16:08</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-12382" class="comments-container"></div><div id="comment-tools-12382" class="comment-tools"></div><div class="clear"></div><div id="comment-12382-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="12419"></span>

<div id="answer-container-12419" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12419-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12419-score" class="post-score" title="current number of votes">1</div><span id="post-12419-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I tried this in 1.8.0 (well, actually the trunk) and did not have the problem. Are you using 1.8.0 or a previous version? If you're using an older version, please upgrade.</p><p>If you're using 1.8.0, please file a <a href="https://bugs.wireshark.org">bug report</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jul '12, 11:35</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-12419" class="comments-container"></div><div id="comment-tools-12419" class="comment-tools"></div><div class="clear"></div><div id="comment-12419-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12424"></span>

<div id="answer-container-12424" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12424-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12424-score" class="post-score" title="current number of votes">1</div><span id="post-12424-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That's not losing precision, that's getting significantly changed - the <em>integer</em> portions of 1340398414.509256500 and 134039841.450925600 are significantly different.</p><p>Please file a bug against whatever versions of Wireshark have this problem, even if it's prior to 1.8.0. TShark might be failing to set the time stamp resolution correctly in the Interface Description Block(s) in the output file:</p><pre><code>$ bc
bc 1.06
Copyright 1991-1994, 1997, 1998, 2000 Free Software Foundation, Inc.
This is free software with ABSOLUTELY NO WARRANTY.
For details type `warranty&#39;. 
1340398414.509256500/134039841.450925600
10</code></pre><p>so the resolution might be off by a factor of 10.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jul '12, 16:12</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-12424" class="comments-container"><span id="12425"></span><div id="comment-12425" class="comment"><div id="post-12425-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your quick response!</p><p>I checked that my <strong>if_tsresol</strong> field in the original <strong>IS block</strong> is 7. So effectively the timestamp lost its least significant digit but the program still wanted to maintain the original number of decimal places. As a result, the decimal point is moved to the front by 1 digit.</p><p>I am using:</p><p>libpcap-1.3.0<br />
wireshark-1.8.0 ( downloaded from <a href="http://www.wireshark.org/download.html">http://www.wireshark.org/download.html</a> )</p><p>Are there any other components that may affect the precision?</p><p>Thanks again!</p></div><div id="comment-12425-info" class="comment-info"><span class="comment-age">(03 Jul '12, 17:29)</span> <span class="comment-user userinfo">Holy</span></div></div><span id="12426"></span><div id="comment-12426" class="comment"><div id="post-12426-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Are there any other components that may affect the precision?</p></blockquote><p>I don't know. Please file a bug on this on <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>, so that we can track it and note when it's fixed.</p></div><div id="comment-12426-info" class="comment-info"><span class="comment-age">(03 Jul '12, 17:54)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="12519"></span><div id="comment-12519" class="comment"><div id="post-12519-score" class="comment-score"></div><div class="comment-text"><p>It's here now: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7457">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7457</a></p></div><div id="comment-12519-info" class="comment-info"><span class="comment-age">(08 Jul '12, 18:58)</span> <span class="comment-user userinfo">Holy</span></div></div><span id="12569"></span><div id="comment-12569" class="comment"><div id="post-12569-score" class="comment-score"></div><div class="comment-text"><p>Fixed in rev 43649, and fix backported to the 1.8 branch, so it'll be fixed in 1.8.1. It's not TShark-specific - anything that reads pcap-ng files with an interface that doesn't have the default 1-microsecond time stamp resolution and writes out packets from that interface will get it wrong.</p></div><div id="comment-12569-info" class="comment-info"><span class="comment-age">(10 Jul '12, 12:21)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-12424" class="comment-tools"></div><div class="clear"></div><div id="comment-12424-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

