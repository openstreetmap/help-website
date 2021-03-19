+++
type = "question"
title = "Computer malfunctioning on network?"
description = '''I am new to using Wireshark, and I see source computer IP address (removed actual ip address) that has destination as 255.255.255.255 I see this many times with this same computer in the Wireshark output when I use the bootp filter. What is going on with this computer? Is it malfunctioning? I am usi...'''
date = "2015-12-31T08:03:00Z"
lastmod = "2016-01-01T04:24:00Z"
weight = 48770
keywords = [ "dhcp" ]
aliases = [ "/questions/48770" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Computer malfunctioning on network?](/questions/48770/computer-malfunctioning-on-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48770-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48770-score" class="post-score" title="current number of votes">0</div><span id="post-48770-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am new to using Wireshark, and I see source computer IP address (removed actual ip address) that has destination as 255.255.255.255 I see this many times with this same computer in the Wireshark output when I use the bootp filter. What is going on with this computer? Is it malfunctioning? I am using bootp as a filter.</p><p>Thanks in advance for any help with this. Here is the output for one of the lines:</p><pre><code>Frame 1070: 342 bytes on wire (2736 bits), 342 bytes captured (2736 bits) on interface 0
    Interface id: 0 (\Device\NPF_{61CD5C01-EBFC-46A1-B953-C3286E5CD4A7})
    Encapsulation type: Ethernet (1)
    Arrival Time: Dec 30, 2015 15:16:06.823921000 US Mountain Standard Time
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1451513766.823921000 seconds
    [Time delta from previous captured frame: 0.000760000 seconds]
    [Time delta from previous displayed frame: 0.000000000 seconds]
    [Time since reference or first frame: 7.488743000 seconds]
    Frame Number: 1070
    Frame Length: 342 bytes (2736 bits)
    Capture Length: 342 bytes (2736 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:ethertype:ip:udp:bootp]
    [Coloring Rule Name: UDP]
    [Coloring Rule String: udp]
Ethernet II, Src: Dell_f1:1c:42 (20:47:47:f1:1c:42), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
    Destination: Broadcast (ff:ff:ff:ff:ff:ff)
    Source: Dell_f1:1c:42 (20:47:47:f1:1c:42)
    Type: IPv4 (0x0800)
Internet Protocol Version 4, Src: IP Address, Dst: 255.255.255.255
    0100 .... = Version: 4
    .... 0101 = Header Length: 20 bytes
    Differentiated Services Field: 0x00 (DSCP: CS0, ECN: Not-ECT)
    Total Length: 328
    Identification: 0x7a24 (31268)
    Flags: 0x00
    Fragment offset: 0
    Time to live: 128
    Protocol: UDP (17)
    Header checksum: 0xb414 [validation disabled]
    Source: IP Address
    Destination: 255.255.255.255
    [Source GeoIP: Unknown]
    [Destination GeoIP: Unknown]
User Datagram Protocol, Src Port: 68 (68), Dst Port: 67 (67)
    Source Port: 68
    Destination Port: 67
    Length: 308
    Checksum: 0x6847 [validation disabled]
    [Stream index: 67]
Bootstrap Protocol (Inform)
    Message type: Boot Request (1)
    Hardware type: Ethernet (0x01)
    Hardware address length: 6
    Hops: 0
    Transaction ID: 0xbe7f61ba
    Seconds elapsed: 0
    Bootp flags: 0x8000, Broadcast flag (Broadcast)
    Client IP address: IP Address
    Your (client) IP address: 0.0.0.0
    Next server IP address: 0.0.0.0
    Relay agent IP address: 0.0.0.0
    Client MAC address: Dell_f1:1c:42 (20:47:47:f1:1c:42)
    Client hardware address padding: 00000000000000000000
    Server host name not given
    Boot file name not given
    Magic cookie: DHCP
    Option: (53) DHCP Message Type (Inform)
    Option: (61) Client identifier
    Option: (12) Host Name</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dhcp" rel="tag" title="see questions tagged &#39;dhcp&#39;">dhcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Dec '15, 08:03</strong></p><img src="https://secure.gravatar.com/avatar/2e69b18a32cff2d4eba8f50eb6986eda?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="techygal&#39;s gravatar image" /><p><span>techygal</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="techygal has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Dec '15, 08:18</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-48770" class="comments-container"></div><div id="comment-tools-48770" class="comment-tools"></div><div class="clear"></div><div id="comment-48770-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48772"></span>

<div id="answer-container-48772" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48772-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48772-score" class="post-score" title="current number of votes">0</div><span id="post-48772-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The IPv4 address 255.255.255.255 is the broadcast address for the <em>zero network</em> which by convention is the local network. See also <a href="https://en.wikipedia.org/wiki/Broadcast_address">here</a>.</p><p>DHCP makes use of broadcast addresses in some phases of the protocol, see <a href="https://www.ietf.org/rfc/rfc2131.txt">RFC 2131</a> for more info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Dec '15, 08:49</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Dec '15, 09:06</strong> </span></p></div></div><div id="comments-container-48772" class="comments-container"><span id="48780"></span><div id="comment-48780" class="comment"><div id="post-48780-score" class="comment-score"></div><div class="comment-text"><p>It is only one computer that I see doing this.</p></div><div id="comment-48780-info" class="comment-info"><span class="comment-age">(31 Dec '15, 14:28)</span> <span class="comment-user userinfo">techygal</span></div></div><span id="48784"></span><div id="comment-48784" class="comment"><div id="post-48784-score" class="comment-score"></div><div class="comment-text"><p>Wireshark tells you <em>what</em> happens; you have to find out yourself <em>why</em> it happens.</p><p>As <span>@grahamb</span> wrote, look at the complete DHCP working principle. E.g. the discovery message is sent to a broadcast IP (255.255.255.255) normally and on purpose, i.e. use of broadcast IP as destination is not wrong as such.</p><p>There are many reasons why the computer may send DHCP messages to broadcast IP repeatedly - e.g., your DHCP server may ignore it. To learn more, i.e. to identify the reason and eventually the guilty equipment/configuration, you have to capture at the DHCP server (or the switch port it is connected to) and at that computer (or the switch port it is connected to) and see what happens and at which stage things go wrong.</p><p>I'd <em>guess</em> that in your case, the DHCP server ignores the DHCPinform message because there is no source IP in it, so you have to find out why it is missing. Or maybe there is simply no DHCP server in your network and the network adaptor of the computer in question is configured to obtain IP address dynamically? Maybe because you have configured one network adaptor with static IP and connected another adaptor to the network by mistake?</p><p>Without description of the network topology and the capture of the DHCP traffic at the computer in question, you cannot expect more than guesses from the community.</p></div><div id="comment-48784-info" class="comment-info"><span class="comment-age">(01 Jan '16, 04:24)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-48772" class="comment-tools"></div><div class="clear"></div><div id="comment-48772-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

