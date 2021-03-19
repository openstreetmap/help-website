+++
type = "question"
title = "RDP client sends 2 packet with identical sq number"
description = '''Hi can anybody help me find out why when I log into a remote desktop in Lan area in Wireshark shows me always 2 packets with the same sequence number sent from the client. They send in the range of 0.000020. The link below is an illustrative picture. Pakcet 13,14 have same sequence number. Does anyo...'''
date = "2011-04-02T13:48:00Z"
lastmod = "2011-04-06T18:06:00Z"
weight = 3293
keywords = [ "rdp" ]
aliases = [ "/questions/3293" ]
osqa_answers = 5
osqa_accepted = false
+++

<div class="headNormal">

# [RDP client sends 2 packet with identical sq number](/questions/3293/rdp-client-sends-2-packet-with-identical-sq-number)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3293-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3293-score" class="post-score" title="current number of votes">0</div><span id="post-3293-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi can anybody help me find out why when I log into a remote desktop in Lan area in Wireshark shows me always 2 packets with the same sequence number sent from the client. They send in the range of 0.000020. The link below is an illustrative picture. Pakcet 13,14 have same sequence number. Does anyone know why this is happening?</p><p>http://img151.imageshack.us/i/86983975.jpg/ http://img200.imageshack.us/i/28874023.jpg/</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rdp" rel="tag" title="see questions tagged &#39;rdp&#39;">rdp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Apr '11, 13:48</strong></p><img src="https://secure.gravatar.com/avatar/8b1b67d74a933506bfa431115c7a2e7d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Steeevee&#39;s gravatar image" /><p><span>Steeevee</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Steeevee has no accepted answers">0%</span></p></div></div><div id="comments-container-3293" class="comments-container"><span id="3297"></span><div id="comment-3297" class="comment"><div id="post-3297-score" class="comment-score"></div><div class="comment-text"><p>Are the IP ID's the same? You may be capturing it twice (entering and exiting the VLAN)</p></div><div id="comment-3297-info" class="comment-info"><span class="comment-age">(02 Apr '11, 17:48)</span> <span class="comment-user userinfo">hansangb</span></div></div></div><div id="comment-tools-3293" class="comment-tools"></div><div class="clear"></div><div id="comment-3293-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

5 Answers:

</div>

</div>

<span id="3299"></span>

<div id="answer-container-3299" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3299-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3299-score" class="post-score" title="current number of votes">1</div><span id="post-3299-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As hansangb pointed out, the IP-ID is your best bet to find out what's happening.</p><p>The IP-ID (IP Identification) is like a 16-Bit serial number assigned to each packet send by a computer. The IP-ID is often helpful when tracking packets through a NAT gateway - or like your case a "maybe-retransmission".</p><p>If you captured with a SPAN port Wireshark may see packets twice:</p><ul><li>First when the packet enters the switch. The process responsible for the SPAN port detects the packets as "yes forward to analyzer port"</li><li>Then the packet gets processed by the switch and is queued to be transmitted to the next hop</li><li>The second packet is forwarded to the analyzer port when the packet <em>leaves</em> the switch. That's your second packet.</li></ul><p>If both packets have the same IP-ID: Voila: It's the same packet.</p><p>The short delta time suggests that this is, what's happening in your trace.</p><p>If a routing engine is involved, say if you are working with a Layer 3 switch, the TTL in the IP header will be reduced by 1.</p><p>When working with a Layer 2 switch the duplicate packets will be absolutely identical. The utility editcap with parameter -d helps to eliminate duplicate packets. When working with editcap I also add the parameter -w to make sure that editcap does not toss out BPDU's (which are expected to be identical and show up every 2 seconds).</p><p>Good hunting!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Apr '11, 03:57</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-3299" class="comments-container"></div><div id="comment-tools-3299" class="comment-tools"></div><div class="clear"></div><div id="comment-3299-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3300"></span>

<div id="answer-container-3300" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3300-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3300-score" class="post-score" title="current number of votes">0</div><span id="post-3300-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, id of packets are 13 and 14, I do not know why but when I'm on lan that are sent just two in a row with the same sequence number, the delay between this packet is about 0.000020 - 50, the packet goes from me(client) to the RDP server is always sent to 2 times - I mean with the same sequence number, as shown in the accompanying pictures.</p><p>Thank you for help</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Apr '11, 04:00</strong></p><img src="https://secure.gravatar.com/avatar/8b1b67d74a933506bfa431115c7a2e7d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Steeevee&#39;s gravatar image" /><p><span>Steeevee</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Steeevee has no accepted answers">0%</span></p></div></div><div id="comments-container-3300" class="comments-container"><span id="3301"></span><div id="comment-3301" class="comment"><div id="post-3301-score" class="comment-score"></div><div class="comment-text"><p>The "ID" is not the packet number shown in the Wireshark packet list.</p><p>We are referring to a field in the IP header. Open the IP header in the decode and look for the field "Identification". We want to know if the (hex) number in the field is the same for your packets 13 and 14.</p></div><div id="comment-3301-info" class="comment-info"><span class="comment-age">(03 Apr '11, 07:37)</span> <span class="comment-user userinfo">packethunter</span></div></div><span id="3338"></span><div id="comment-3338" class="comment"><div id="post-3338-score" class="comment-score"></div><div class="comment-text"><p>Anyone want to tackle this: "the delay between this packet is about 0.000020 - 50"</p><p>Can we trust anything to 20μs? I tend to get on my soapbox when it comes to using/trusting timings this exact with today's hardware.</p></div><div id="comment-3338-info" class="comment-info"><span class="comment-age">(05 Apr '11, 05:11)</span> <span class="comment-user userinfo">GeonJay</span></div></div></div><div id="comment-tools-3300" class="comment-tools"></div><div class="clear"></div><div id="comment-3300-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3306"></span>

<div id="answer-container-3306" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3306-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3306-score" class="post-score" title="current number of votes">0</div><span id="post-3306-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I am sorry, these packets(13,14) has the same identification number 0x6311, so that was the problem, perhaps it is due to how you write up, I try to connect directly to a PC and see. Thank you very much</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Apr '11, 11:22</strong></p><img src="https://secure.gravatar.com/avatar/8b1b67d74a933506bfa431115c7a2e7d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Steeevee&#39;s gravatar image" /><p><span>Steeevee</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Steeevee has no accepted answers">0%</span></p></div></div><div id="comments-container-3306" class="comments-container"></div><div id="comment-tools-3306" class="comment-tools"></div><div class="clear"></div><div id="comment-3306-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3329"></span>

<div id="answer-container-3329" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3329-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3329-score" class="post-score" title="current number of votes">0</div><span id="post-3329-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi I joined a peer to peer with RDP server without any switch or router and i see in the wireshark the aame problem, 2 packets with the same identification number, do you know why?</p><p>Thank you very much</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '11, 11:35</strong></p><img src="https://secure.gravatar.com/avatar/8b1b67d74a933506bfa431115c7a2e7d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Steeevee&#39;s gravatar image" /><p><span>Steeevee</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Steeevee has no accepted answers">0%</span></p></div></div><div id="comments-container-3329" class="comments-container"><span id="3334"></span><div id="comment-3334" class="comment"><div id="post-3334-score" class="comment-score"></div><div class="comment-text"><p>Can you layout your network?? PC --&gt; ? --&gt; ? --&gt; server Can you fill in the details and tell us where you're capturing from?</p></div><div id="comment-3334-info" class="comment-info"><span class="comment-age">(04 Apr '11, 18:51)</span> <span class="comment-user userinfo">hansangb</span></div></div></div><div id="comment-tools-3329" class="comment-tools"></div><div class="clear"></div><div id="comment-3329-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3337"></span>

<div id="answer-container-3337" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3337-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3337-score" class="post-score" title="current number of votes">0</div><span id="post-3337-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>PC -2m patchcord - RDP server, I tried to connect to remote desktop from another PC in the same network and in wireshark 2 identical packets I donť see. Perhaps it is in my notebook, I've got a lot of VPN connections and network adapters installed there</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '11, 01:33</strong></p><img src="https://secure.gravatar.com/avatar/8b1b67d74a933506bfa431115c7a2e7d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Steeevee&#39;s gravatar image" /><p><span>Steeevee</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Steeevee has no accepted answers">0%</span></p></div></div><div id="comments-container-3337" class="comments-container"><span id="3383"></span><div id="comment-3383" class="comment"><div id="post-3383-score" class="comment-score">1</div><div class="comment-text"><p>Aha! There you go. In the past, having QoS Scheduler (for example) caused duplicate packets. Or it may be due to vpn adapters, or you may be using some other shim that's causing winpcap to capture duplicates. Use editcap.exe from the command line. "editcap.exe -d OriginalFileHere.pcap NewFileHere.pcap" will create the new file w/o duplicates.</p></div><div id="comment-3383-info" class="comment-info"><span class="comment-age">(06 Apr '11, 18:06)</span> <span class="comment-user userinfo">hansangb</span></div></div></div><div id="comment-tools-3337" class="comment-tools"></div><div class="clear"></div><div id="comment-3337-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

