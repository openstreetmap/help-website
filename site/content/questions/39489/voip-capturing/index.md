+++
type = "question"
title = "VOIP Capturing"
description = '''Hi I&#x27;m trying to setup VOIP capture, and I&#x27;m not seeing any results. Installed Wireshark, setup the interface, I have 2 nics, one is Internet based, with only the protocols used for internet. File/Print and Client for Microsoft turned off. This is the interface for capturing. The second nic is used ...'''
date = "2015-01-29T13:59:00Z"
lastmod = "2015-01-31T15:20:00Z"
weight = 39489
keywords = [ "sip", "voip" ]
aliases = [ "/questions/39489" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [VOIP Capturing](/questions/39489/voip-capturing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39489-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39489-score" class="post-score" title="current number of votes">0</div><span id="post-39489-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I'm trying to setup VOIP capture, and I'm not seeing any results.</p><p>Installed Wireshark, setup the interface, I have 2 nics, one is Internet based, with only the protocols used for internet. File/Print and Client for Microsoft turned off. This is the interface for capturing. The second nic is used for the local area connection, and has no access to the internet. From this point I started the capture, using promiscuous mode. No filters were setup, as I want to see all the PC's running VOIP (5 pc's). Running the analysis for a least an hour, I then tried to view the VOIP packets, but there are none, and i have people on VOIP phones as I type this message. All the phones whether they are hardphones/softphones, there all plugged into a switch. The scanning interface is plugged into the router. I also tried scanning from an interface plugged into the switch. VOIP is running on a outside hosted pbx</p><p>any thoughts, what am i doing wrong. thx</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span> <span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '15, 13:59</strong></p><img src="https://secure.gravatar.com/avatar/f0e1d3f2a8a74a32efcdb402738b65ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Terra&#39;s gravatar image" /><p><span>Terra</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Terra has no accepted answers">0%</span></p></div></div><div id="comments-container-39489" class="comments-container"><span id="39490"></span><div id="comment-39490" class="comment"><div id="post-39490-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure I totally understand the network topology and how you're trying to get the packets here. You say you have five PCs connected to a switch, and that the "scanning interface", in contrast, is connected to an upstream router which can also route to the external PBX acting as a softswitch - In that scenario, how are you having the router forward the VoIP traffic to the PC you're running Wireshark on?</p><p>Is this the topology?:</p><p>[PBX and Internet]</p><p>|</p><p>[router] -- [PC with Wireshark]</p><p>|</p><p>[switch]</p><p>|</p><p>[5 PCs]</p><p>Also, do you see any traffic at all, aside from just not seeing the VoIP traffic? I'm assuming from the tags this is a SIP/RTP network we're talking about?</p></div><div id="comment-39490-info" class="comment-info"><span class="comment-age">(29 Jan '15, 15:13)</span> <span class="comment-user userinfo">Quadratic</span></div></div><span id="39505"></span><div id="comment-39505" class="comment"><div id="post-39505-score" class="comment-score"></div><div class="comment-text"><p>Hi</p><p>Topology [PBX] outside provider...no access to PBX</p><p>Internet[Cable Modem][Router][PC w/Wireshark]</p><p>[switch] 5 PC's running VOIP softphone - 5 PC's non VOIP - 3 Hardphones (VOIP)[PC w/Wireshark also, for testing].</p><p>It is a SIP/RTP network. I ss all kinds of traffic TCP/UDP/ICMP/ARP...etc.</p><p>I'm running Wireshark from the PC connected to the router, in promiscuous mode.</p></div><div id="comment-39505-info" class="comment-info"><span class="comment-age">(30 Jan '15, 10:03)</span> <span class="comment-user userinfo">Terra</span></div></div></div><div id="comment-tools-39489" class="comment-tools"></div><div class="clear"></div><div id="comment-39489-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39513"></span>

<div id="answer-container-39513" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39513-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39513-score" class="post-score" title="current number of votes">0</div><span id="post-39513-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You need to ensure that the packets you want to receive are making it to your PC (which is not accomplished just by running in promiscuous mode). From your topology diagram, your PC is connected to an upstream router, and isn't in the same LAN as the PCs whose traffic you are trying to intercept. So, if you're routing packets between the PC LAN and the Internet, the IP router is not normally going to duplicate that traffic and send it also to your Wireshark-running PC.</p><p>I suggest you either limit your Wireshark trace to one of the softphone PCs that is in the line-of-path of the VoIP traffic, or you get a switch that can support port mirroring (or "SPAN"), to have the VoIP-related traffic mirrored to the port you're running Wireshark on.</p><p>Now, for the PC running a soft phone, do you see the SIP/RTP traffic when running Wireshark on this PC? Can you confirm what port/transport protocol you're using for SIP, and whether you are having these decoded as SIP (check this under Edit &gt; Preferences &gt; Protocols &gt; SIP and make sure the port info is correct for your implementation)?</p><p>As for the "all kinds of traffic" issue on the PC with the softphone, have you tried just typing "sip" in the search bar and filtering on that to see if you do indeed have any SIP packets showing up there?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '15, 15:11</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Jan '15, 15:13</strong> </span></p></div></div><div id="comments-container-39513" class="comments-container"><span id="39527"></span><div id="comment-39527" class="comment"><div id="post-39527-score" class="comment-score"></div><div class="comment-text"><p>Not an issue, as I ran Wireshark on the target PC." All pc's are on the same lan/subnet Switch is a non managed switch...no port mirroring possible. I did try searching for SIP</p><p>It's all moot now.</p><p>Thx!</p></div><div id="comment-39527-info" class="comment-info"><span class="comment-age">(31 Jan '15, 15:20)</span> <span class="comment-user userinfo">Terra</span></div></div></div><div id="comment-tools-39513" class="comment-tools"></div><div class="clear"></div><div id="comment-39513-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

