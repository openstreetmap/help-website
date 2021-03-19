+++
type = "question"
title = "I need to get broadcast message from IP Camera"
description = '''This is a partial report from Wireshark, I need to do this in my program. How would I get same info with winsock? No. Time Source Destination Protocol Length Info  67 20.309244000 192.168.1.27 192.168.1.20 MDNS 214 Standard query response 0x0000 PTR ipcamera(id:E8ABFA182279, alias:Und Deck - Wireles...'''
date = "2013-02-08T14:49:00Z"
lastmod = "2013-02-08T23:14:00Z"
weight = 18451
keywords = [ "programming" ]
aliases = [ "/questions/18451" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [I need to get broadcast message from IP Camera](/questions/18451/i-need-to-get-broadcast-message-from-ip-camera)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18451-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18451-score" class="post-score" title="current number of votes">0</div><span id="post-18451-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This is a partial report from Wireshark, I need to do this in my program. How would I get same info with winsock?</p><pre><code>No.     Time           Source                Destination           Protocol Length Info
     67 20.309244000   192.168.1.27          192.168.1.20          MDNS     214    Standard query response 0x0000  PTR ipcamera(id:E8ABFA182279, alias:Und Deck - Wireless)._http._tcp.local

Frame 67: 214 bytes on wire (1712 bits), 214 bytes captured (1712 bits) on interface 0
    Interface id: 0
    WTAP_ENCAP: 1
    Arrival Time: Feb  8, 2013 13:59:18.741482000 Eastern Standard Time
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1360349958.741482000 seconds
    [Time delta from previous captured frame: 0.167049000 seconds]
    [Time delta from previous displayed frame: 0.167049000 seconds]
    [Time since reference or first frame: 20.309244000 seconds]
    Frame Number: 67
    Frame Length: 214 bytes (1712 bits)
    Capture Length: 214 bytes (1712 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:ip:udp:dns]
    [Coloring Rule Name: UDP]
    [Coloring Rule String: udp]
Ethernet II, Src: B-LinkEl_4f:cf:d1 (48:02:2a:4f:cf:d1), Dst: HonHaiPr_14:7b:84 (78:e4:00:14:7b:84)
    Destination: HonHaiPr_14:7b:84 (78:e4:00:14:7b:84)
    Source: B-LinkEl_4f:cf:d1 (48:02:2a:4f:cf:d1)
    Type: IP (0x0800)
Internet Protocol Version 4, Src: 192.168.1.27 (192.168.1.27), Dst: 192.168.1.20 (192.168.1.20)
    Version: 4
    Header length: 20 bytes
    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
    Total Length: 200
    Identification: 0x0000 (0)
    Flags: 0x02 (Don&#39;t Fragment)
    Fragment offset: 0
    Time to live: 255
    Protocol: UDP (17)
    Header checksum: 0xf7a4 [correct]
    Source: 192.168.1.27 (192.168.1.27)
    Destination: 192.168.1.20 (192.168.1.20)
    [Source GeoIP: Unknown]
    [Destination GeoIP: Unknown]
User Datagram Protocol, Src Port: mdns (5353), Dst Port: 54254 (54254)
    Source port: mdns (5353)
    Destination port: 54254 (54254)</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-programming" rel="tag" title="see questions tagged &#39;programming&#39;">programming</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Feb '13, 14:49</strong></p><img src="https://secure.gravatar.com/avatar/ca74fbb5a41545305130c127534beaf6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BHill&#39;s gravatar image" /><p><span>BHill</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BHill has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Feb '13, 16:39</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-18451" class="comments-container"><span id="18463"></span><div id="comment-18463" class="comment"><div id="post-18463-score" class="comment-score"></div><div class="comment-text"><p>Not really a Wireshark question. You will probably get better help on a site aimed at Winsock programming, e.g. <a href="http://stackoverflow.com">Stack Overflow</a>.</p></div><div id="comment-18463-info" class="comment-info"><span class="comment-age">(08 Feb '13, 23:14)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-18451" class="comment-tools"></div><div class="clear"></div><div id="comment-18451-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

