+++
type = "question"
title = "UDP multicast, Windows 7 firewall, Labview"
description = '''I am sending UDP packets to a multicast address (224.1.1.1) on an unused port (60000) from an embedded board hooked into my network. When I run a Wireshark capture on my PC, I can see the UDP packets. Everything appears correct (including checksums). I developed a Labview script to read the incoming...'''
date = "2011-10-04T09:56:00Z"
lastmod = "2011-10-04T11:05:00Z"
weight = 6711
keywords = [ "firewall", "udp" ]
aliases = [ "/questions/6711" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [UDP multicast, Windows 7 firewall, Labview](/questions/6711/udp-multicast-windows-7-firewall-labview)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6711-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6711-score" class="post-score" title="current number of votes">0</div><span id="post-6711-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am sending UDP packets to a multicast address (224.1.1.1) on an unused port (60000) from an embedded board hooked into my network.</p><p>When I run a Wireshark capture on my PC, I can see the UDP packets. Everything appears correct (including checksums). I developed a Labview script to read the incoming UDP packets. However, it does not see the packets (i.e., times out when it tries to read the IP/port). My system is Windows 7, and the OS firewall is enabled. I have verified that Labview has firewall "privileges," but I have made no special provisions for the port in question (i.e., 60000).</p><p>Here's the interesting part: whenever I have a live capture going with Wireshark, the Labview script starts working (i.e., it sees the packets -- and agrees that they are formed correctly). It is very reliable and repeatable -- i.e., run the the Labview script. As I start and stop the Wireshark capture, the script can see and not see the packets, respectively.</p><p>Is Wireshark somehow letting packets through that would otherwise be blocked while in the act of sniffing?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-firewall" rel="tag" title="see questions tagged &#39;firewall&#39;">firewall</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Oct '11, 09:56</strong></p><img src="https://secure.gravatar.com/avatar/8095e06ec5259349d7ba1e984e2b4666?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hobbss&#39;s gravatar image" /><p><span>hobbss</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hobbss has no accepted answers">0%</span></p></div></div><div id="comments-container-6711" class="comments-container"></div><div id="comment-tools-6711" class="comment-tools"></div><div class="clear"></div><div id="comment-6711-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6712"></span>

<div id="answer-container-6712" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6712-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6712-score" class="post-score" title="current number of votes">2</div><span id="post-6712-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You are probably running Wireshark with the "Capture packets in promiscuous mode" option selected which will cause the NIC to "accept" all packets. I think your Labview script isn't following the rules for a windows multicast receiver. See <a href="http://msdn.microsoft.com/en-us/library/aa374475.aspx">this</a> MDSN link for more details</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Oct '11, 10:18</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-6712" class="comments-container"><span id="6713"></span><div id="comment-6713" class="comment"><div id="post-6713-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the response. Are you saying that the NIC is ignoring the packets when Wireshark is not running, but accepting them (and making them available to all processes on the PC) when Wireshark is running? This would make sense except for the fact that the UDP script in Labview was provided by National Instruments (example program). I expect them to make sure it works properly. Interestingly, if I run a UDP tx labview program on another PC with the same port number and multicast ip, the Rx works, whether or not Wireshark is running.</p></div><div id="comment-6713-info" class="comment-info"><span class="comment-age">(04 Oct '11, 10:50)</span> <span class="comment-user userinfo">hobbss</span></div></div><span id="6714"></span><div id="comment-6714" class="comment"><div id="post-6714-score" class="comment-score"></div><div class="comment-text"><p>As Graham pointed out, there are rules which must be followed when trying to receive multicasts. One step which must be done in the program: tell the OS that you want to receive multicasts on a particular multicast address.</p><p>If this isn't done your program may or may not work depending upon whether the NIC is running in promiscuous mode or whether some other program is already listening to that address.</p><p>Please read the link referenced for info.</p><p>Are you on Windows ?</p><p>Or: Is there some firewall issue ? Does the other PC have the same firewall setup ?</p></div><div id="comment-6714-info" class="comment-info"><span class="comment-age">(04 Oct '11, 11:05)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-6712" class="comment-tools"></div><div class="clear"></div><div id="comment-6712-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

