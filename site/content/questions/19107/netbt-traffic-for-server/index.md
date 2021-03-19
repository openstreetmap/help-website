+++
type = "question"
title = "NetBT traffic for server"
description = '''Hello We are looking at disabling Netbios over TCP/IP on some of our Windows 2008 application servers. Since we don&#x27;t use WINS, the server will be sending broadcasts for name resolution as far as I understand. What I&#x27;d like to do is capture Netbios over TCP traffic using Wireshark Server IP: 192.168...'''
date = "2013-03-03T13:03:00Z"
lastmod = "2013-07-02T09:23:00Z"
weight = 19107
keywords = [ "netbios" ]
aliases = [ "/questions/19107" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [NetBT traffic for server](/questions/19107/netbt-traffic-for-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19107-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19107-score" class="post-score" title="current number of votes">0</div><span id="post-19107-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>We are looking at disabling Netbios over TCP/IP on some of our Windows 2008 application servers. Since we don't use WINS, the server will be sending broadcasts for name resolution as far as I understand.</p><p>What I'd like to do is capture Netbios over TCP traffic using Wireshark</p><p>Server IP: 192.168.20.5 / 24</p><p>Is it just a case of display filtering on 137?</p><p>Also, would wireshark be any help in comparing the number of broadcast packets within a certain period with NetBT disabled and enabled so we can see how much broadcast traffic we're reducing?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-netbios" rel="tag" title="see questions tagged &#39;netbios&#39;">netbios</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Mar '13, 13:03</strong></p><img src="https://secure.gravatar.com/avatar/01e83725a9ab911ceacb32eb9dcde317?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TonyRobbins1978&#39;s gravatar image" /><p><span>TonyRobbins1978</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TonyRobbins1978 has no accepted answers">0%</span></p></div></div><div id="comments-container-19107" class="comments-container"></div><div id="comment-tools-19107" class="comment-tools"></div><div class="clear"></div><div id="comment-19107-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19111"></span>

<div id="answer-container-19111" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19111-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19111-score" class="post-score" title="current number of votes">1</div><span id="post-19111-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="TonyRobbins1978 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Since we don't use WINS, the server will be sending broadcasts for name resolution as far as I understand.</p></blockquote><p>For purely-NetBIOS-based services, if there are any, disabling NetBIOS-over-TCP would probably either completely disable the service or force it to use the NetBIOS Frame (NBF) protocol, which only works on the same LAN segment as the server. I don't even know whether Windows 2008 supports NBF; I don't think modern versions of Windows do, although I think some of them can run the NBF driver from older versions of Windows. Name resolution for NBF is broadcast-based, but doesn't run over IP.</p><p>For SMB/CIFS file service, disabling NetBIOS-over-TCP would still allow SMB to run directly over TCP on port 445. Name resolution for SMB-over-TCP would be done using DNS, which isn't broadcast-based. SMB/CIFS can also run over NBF; as indicated, NBF name resolution is broadcast-based.</p><p>Note that "NetBIOS-over-TCP" really means "NetBIOS-over-IP" or "NetBIOS-over-TCP-and-UDP", as UDP is used for name resolution and the NetBIOS datagram services. If you want to see whether there is any NetBIOS-over-TCP name resolution happening after you disable NetBIOS-over-TCP on the server, look for packets going to or from UDP port 137; you can use a <em>capture</em> filter of "udp port 137" for that (the display filter would be "nbns", for "NetBIOS Name Service").</p><p>If you want to check for NBF traffic, then, at least with sufficiently recent versions of libpcap/WinPcap being used by Wireshark, a capture filter of "netbeui" (or a display filter of "netbios") would work. (Yes, both NetBEUI and NetBIOS are the wrong terms for NBF, but that's what libpcap and Wireshark are using.)</p><p>A capture filter of "broadcast" will check for all LAN broadcasts. If you only want to find out how much NetBIOS-over-TCP broadcast name resolution is occurring, try "broadcast and udp port 137" when capturing.</p><p>And, yes, you should be able to use Wireshark to see how much NetBIOS-over-TCP broadcast name resolution is occurring; just compare the results of capturing with "broadcast and udp port 137" with NetBT enabled and with NetBT disabled.</p><p>(For NBF and NetBT broadcast name resolution, the capture filter would be "broadcast and (netbeui or udp port 137)".)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Mar '13, 17:29</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-19111" class="comments-container"><span id="19113"></span><div id="comment-19113" class="comment"><div id="post-19113-score" class="comment-score"></div><div class="comment-text"><p>Thank you, Guy.</p><p>As regards the packet count, is there a way in WS to count how many broadcast packets were sent out from the server for NBNS (without having to manually count)?</p></div><div id="comment-19113-info" class="comment-info"><span class="comment-age">(03 Mar '13, 18:46)</span> <span class="comment-user userinfo">TonyRobbins1978</span></div></div><span id="19115"></span><div id="comment-19115" class="comment"><div id="post-19115-score" class="comment-score"></div><div class="comment-text"><p>The status bar (at the bottom of the window) has 3 sections; the middle section has the number of packets in the capture and the number of those packets that are being displayed. If you used the capture filter, the number of packets in the capture would be the number of NBNS broadcasts; if you used the display filter, the number of displayed packets in the capture would be the number of NBNS broadcasts.</p></div><div id="comment-19115-info" class="comment-info"><span class="comment-age">(03 Mar '13, 22:45)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-19111" class="comment-tools"></div><div class="clear"></div><div id="comment-19111-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22557"></span>

<div id="answer-container-22557" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22557-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22557-score" class="post-score" title="current number of votes">0</div><span id="post-22557-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Using the display filters mentioned above or display filter <strong><em>eth.dst==ff:ff:ff:ff:ff:ff &amp;&amp; udp port 137</em></strong> and click on the statistics --&gt; Summary menu. This will give you min/max/avg per second stats for all the NBT broadcast traffic displayed. You can also add filter criteria to see stats for a specific host (e.g., <strong><em>ip.addr==10.10.10.10 &amp;&amp; (eth.dst==ff:ff:ff:ff:ff:ff &amp;&amp; udp port 137)</em></strong>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jul '13, 09:23</strong></p><img src="https://secure.gravatar.com/avatar/dfa864459179bdadc35de414b97cb75d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mbwalker&#39;s gravatar image" /><p><span>mbwalker</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mbwalker has no accepted answers">0%</span></p></div></div><div id="comments-container-22557" class="comments-container"></div><div id="comment-tools-22557" class="comment-tools"></div><div class="clear"></div><div id="comment-22557-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

