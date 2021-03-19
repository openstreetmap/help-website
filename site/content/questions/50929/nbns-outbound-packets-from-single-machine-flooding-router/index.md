+++
type = "question"
title = "nbns outbound packets from single machine, flooding router"
description = '''I have a lenovo laptop, windows 8.1, which apparently recently started flooding the network with nbns packets to a block of ip addresses, which then floods the router. Shortly after unplugging the physical cable or turning off wifi, as it happens over either interface, will clear the problem and oth...'''
date = "2016-03-15T08:49:00Z"
lastmod = "2016-03-15T11:26:00Z"
weight = 50929
keywords = [ "ip-flooding", "nbns" ]
aliases = [ "/questions/50929" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [nbns outbound packets from single machine, flooding router](/questions/50929/nbns-outbound-packets-from-single-machine-flooding-router)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50929-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50929-score" class="post-score" title="current number of votes">0</div><span id="post-50929-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a lenovo laptop, windows 8.1, which apparently recently started flooding the network with nbns packets to a block of ip addresses, which then floods the router. Shortly after unplugging the physical cable or turning off wifi, as it happens over either interface, will clear the problem and other devices can now access the internet. Any additional info on this "flood" would be great:</p><p>Here is a partial listing from Wireshark (the destination 203.52.141.70 will run sequentially until the last in about 10 seconds of 203.52.255.178, the 3 trials I have run I get differing ip hosts)</p><pre><code>117 5.825761    192.168.1.14    203.52.141.70   NBNS    92  Name query NBSTAT *&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;

Frame 117: 92 bytes on wire (736 bits), 92 bytes captured (736 bits)
    Encapsulation type: Ethernet (1)
    Arrival Time: Mar 15, 2016 12:03:30.988206000 Eastern Daylight Time
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1458057810.988206000 seconds
    [Time delta from previous captured frame: 0.000000000 seconds]
    [Time delta from previous displayed frame: 0.000000000 seconds]
    [Time since reference or first frame: 5.825761000 seconds]
    Frame Number: 117
    Frame Length: 92 bytes (736 bits)
    Capture Length: 92 bytes (736 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:ethertype:ip:udp:nbns]
    [Coloring Rule Name: SMB]
    [Coloring Rule String: smb || nbss || nbns || nbipx || ipxsap || netbios]
Internet Protocol Version 4, Src: 192.168.1.14, Dst: 203.52.141.70
    0100 .... = Version: 4
    .... 0101 = Header Length: 20 bytes
    Differentiated Services Field: 0x00 (DSCP: CS0, ECN: Not-ECT)
    Total Length: 78
    Identification: 0x7d2e (32046)
    Flags: 0x00
    Fragment offset: 0
    Time to live: 128
    Protocol: UDP (17)
    Header checksum: 0xa33f [validation disabled]
    Source: 192.168.1.14
    Destination: 203.52.141.70
    [Source GeoIP: Unknown]
    [Destination GeoIP: Unknown]</code></pre><p>URL: <a href="https://www.cloudshark.org/captures/8635910ab655">https://www.cloudshark.org/captures/8635910ab655</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip-flooding" rel="tag" title="see questions tagged &#39;ip-flooding&#39;">ip-flooding</span> <span class="post-tag tag-link-nbns" rel="tag" title="see questions tagged &#39;nbns&#39;">nbns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Mar '16, 08:49</strong></p><img src="https://secure.gravatar.com/avatar/38b94595ff95e166847319953c37c3e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmarckese&#39;s gravatar image" /><p><span>mmarckese</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmarckese has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Mar '16, 10:40</strong> </span></p></div></div><div id="comments-container-50929" class="comments-container"><span id="50930"></span><div id="comment-50930" class="comment"><div id="post-50930-score" class="comment-score"></div><div class="comment-text"><p>Please publish the complete capture file somewhere (preferably cloudshark but dropbox, google drive, MS one drive should do as well) for login-free access and edit your question with a link to it. By text dump of packet headers no one can help you.</p><p>The capture should include the beginning of the flood, i.e. if you capture on the laptop which is the source of the flood, you should boot it while isolated from the network in a way which allows to start the capture (i.e. the interface needs to be physically up), then start the capture, and then "unplug" the communication. You may use firewall settings to do that, or another switch which you would connect to the PC before booting it but only connect it to the network after starting the capture.</p><p>If you cannot post the capture for privacy reasons, check whether shaving off the payload above the tcp layer using tracewrangler would be secure enough for you.</p></div><div id="comment-50930-info" class="comment-info"><span class="comment-age">(15 Mar '16, 09:07)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="50934"></span><div id="comment-50934" class="comment"><div id="post-50934-score" class="comment-score"></div><div class="comment-text"><p>Hopefully this will help: URL: <a href="https://www.cloudshark.org/captures/8635910ab655">https://www.cloudshark.org/captures/8635910ab655</a></p></div><div id="comment-50934-info" class="comment-info"><span class="comment-age">(15 Mar '16, 10:38)</span> <span class="comment-user userinfo">mmarckese</span></div></div></div><div id="comment-tools-50929" class="comment-tools"></div><div class="clear"></div><div id="comment-50929-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50935"></span>

<div id="answer-container-50935" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50935-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50935-score" class="post-score" title="current number of votes">1</div><span id="post-50935-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mmarckese has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hm, my conclusion is that your notebook has become a zombie in a botnet, and its boss asks it to take part in DDoS-attacks to various networks (note that in this capture, the tagret network differs from the one you've mentioned in your Question).</p><p>The "NBNS" packets your notebook sends contain a bogus payload, and the "recipient" (actually, target) or some firewall in front of it already filter the attack - see e.g. packet 71, which is an icmp message informing you that you've been blacklisted.</p><p>The reason why I wanted to see the very beginning after boot was to see the control process of the zombie "calling home" for instruction whom to attack.</p><p>I'd recommend to cut the laptop off the network immediately and use some good anti-virus software to clean it up. It may be necessary to use a bootable anti-virus or to connect the disk from the laptop as an additional disk to another computer as some viruses can get active before the anti-virus and fool it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '16, 11:09</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-50935" class="comments-container"><span id="50938"></span><div id="comment-50938" class="comment"><div id="post-50938-score" class="comment-score"></div><div class="comment-text"><p>Excellent, to you not the situation. Thank You.</p></div><div id="comment-50938-info" class="comment-info"><span class="comment-age">(15 Mar '16, 11:26)</span> <span class="comment-user userinfo">mmarckese</span></div></div></div><div id="comment-tools-50935" class="comment-tools"></div><div class="clear"></div><div id="comment-50935-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

