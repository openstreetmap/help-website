+++
type = "question"
title = "How do I decode my mobile capture?"
description = '''Hi, I have this problem. To try and figure out what the problem is I have created two dumps, one over Wifi and one over 3G / HSDPA by running tcpdump on the Android device. The Wifi dump is decoded by Wireshark no problem.  But the 3G dump isn&#x27;t very helpful.  Does anyone know how I can get Wireshar...'''
date = "2012-04-15T22:42:00Z"
lastmod = "2012-04-16T11:01:00Z"
weight = 10167
keywords = [ "mobile", "hsdpa", "android", "3g" ]
aliases = [ "/questions/10167" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I decode my mobile capture?](/questions/10167/how-do-i-decode-my-mobile-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10167-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have <a href="http://forums.tvcatchup.com/showthread.php?9307-Fails-to-stream-over-Wifi-but-works-on-every-other-connection">this</a> problem. To try and figure out what the problem is I have created two dumps, one over Wifi and one over 3G / HSDPA by running tcpdump on the Android device.</p><p>The Wifi dump is decoded by Wireshark no problem.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/wifi.jpg" alt="Wifi" /></p><p>But the 3G dump isn't very helpful.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/3g.jpg" alt="3G / HSDPA" /></p><p>Does anyone know how I can get Wireshark to decode this data so I can figure out what the problem might be?</p><p>Thanks,</p><p>Ken</p></div><div id="question-tags" class="tags-container tags">mobile hsdpa android 3g</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Apr '12, 22:42</strong></p><img src="https://secure.gravatar.com/avatar/928ce60dc1f66793a7443b3f0e94e06d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="unclekennybobs&#39;s gravatar image" /><p>unclekennybobs<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="unclekennybobs has no accepted answers">0%</span></p></img></div></div><div id="comments-container-10167" class="comments-container"><span id="10186"></span><div id="comment-10186" class="comment"><div id="post-10186-score" class="comment-score"></div><div class="comment-text"><p>can you provide a sample trace e.g. on cloudshark with the 3g capture ?</p></div><div id="comment-10186-info" class="comment-info"><span class="comment-age">(16 Apr '12, 06:42)</span> Landi</div></div><span id="10191"></span><div id="comment-10191" class="comment"><div id="post-10191-score" class="comment-score"></div><div class="comment-text"><p>Not really. It will contain private data. I'll have a look though and will update if I get a decent trace. Thanks.</p></div><div id="comment-10191-info" class="comment-info"><span class="comment-age">(16 Apr '12, 09:54)</span> unclekennybobs</div></div></div><div id="comment-tools-10167" class="comment-tools"></div><div class="clear"></div><div id="comment-10167-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10194"></span>

<div id="answer-container-10194" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10194-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately, it appears that either tcpdump, libpcap, or the network software on your Android machine is buggy; the packets in the 3G capture almost certainly do <em>NOT</em> have an Ethernet packet header, but the capture file has a link-layer header type of "Ethernet".</p><p>The capture appears not to have any link-layer headers - the first octet of each packet is 0x45, which strongly suggests an IPv4 header ("4" for the IP version, "5" for the header length in 4-byte units, hence 20 bytes, which is the length of an IPv4 header with no options).</p><p>This is a common problem on Android - for various annoying reasons having to do, apparently, with DHCP software, some mobile-phone-network interfaces supply <code>ARPHRD_ETHER</code> as their <code>ARPHRD_</code> type, rather than <code>ARPHRD_NONE</code>, even though they supply packets with no link-layer header.</p><p>I've checked into the trunk of libpcap a hack to work around this by checking the interface name. Hopefully that will end up in libpcap on various Android devices and make this problem show up less often.</p><p>The hack handles this the only way I know how to do so, namely to check the interface name against names known to have this problem. What was the name of the interface on which you captured the traffic?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '12, 11:01</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 21 Mar '14, 11:18</p></div></div><div id="comments-container-10194" class="comments-container"></div><div id="comment-tools-10194" class="comment-tools"></div><div class="clear"></div><div id="comment-10194-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

