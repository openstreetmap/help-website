+++
type = "question"
title = "Trace entries with protocol/type 0xa168"
description = '''Time Source Destination No. Protocol Length Info 11:50:37.416666 TZ-210W-ROUTER-X0 Broadcast 0xa168 42 PRI: 0 CFI: 0 ID: 200  Frame 53: 42 bytes on wire (336 bits), 42 bytes captured (336 bits)  Encapsulation type: Ethernet (1)  Arrival Time: Aug 23, 2014 11:50:37.416666000 Central Daylight Time  [T...'''
date = "2014-08-23T10:39:00Z"
lastmod = "2014-08-29T12:20:00Z"
weight = 35685
keywords = [ "protocol", "0xa168" ]
aliases = [ "/questions/35685" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Trace entries with protocol/type 0xa168](/questions/35685/trace-entries-with-protocoltype-0xa168)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35685-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35685-score" class="post-score" title="current number of votes">0</div><span id="post-35685-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>Time            Source                Destination           No.    Protocol Length Info
11:50:37.416666 TZ-210W-ROUTER-X0     Broadcast                    0xa168   42     PRI: 0  CFI: 0  ID: 200

Frame 53: 42 bytes on wire (336 bits), 42 bytes captured (336 bits)
    Encapsulation type: Ethernet (1)
    Arrival Time: Aug 23, 2014 11:50:37.416666000 Central Daylight Time
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1408812637.416666000 seconds
    [Time delta from previous captured frame: 0.100000000 seconds]
    [Time delta from previous displayed frame: 0.100000000 seconds]
    [Time since reference or first frame: 4.116666000 seconds]
    Frame Number: 53
    Frame Length: 42 bytes (336 bits)
    Capture Length: 42 bytes (336 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:ethertype:vlan:ethertype:data]
    [Coloring Rule Name: Broadcast]
    [Coloring Rule String: eth[0] &amp; 1]
Ethernet II, Src: TZ-210W-ROUTER-X0 (00:17:c5:42:be:5c), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
    Destination: Broadcast (ff:ff:ff:ff:ff:ff)
        Address: Broadcast (ff:ff:ff:ff:ff:ff)
        .... ..1. .... .... .... .... = LG bit: Locally administered address (this is NOT the factory default)
        .... ...1 .... .... .... .... = IG bit: Group address (multicast/broadcast)
    Source: TZ-210W-ROUTER-X0 (00:17:c5:42:be:5c)
        Address: TZ-210W-ROUTER-X0 (00:17:c5:42:be:5c)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Type: 802.1Q Virtual LAN (0x8100)
802.1Q Virtual LAN, PRI: 0, CFI: 0, ID: 200
    000. .... .... .... = Priority: Best Effort (default) (0)
    ...0 .... .... .... = CFI: Canonical (0)
    .... 0000 1100 1000 = ID: 200
    Type: Unknown (0xa168)
Data (24 bytes)
    Data: 25010018000000012af0ecc3a7e8df789603113dc54756a6
    [Length: 24]

0000  ff ff ff ff ff ff 00 17 c5 42 be 5c 81 00 00 c8   .........B.\....
0010  a1 68 25 01 00 18 00 00 00 01 2a f0 ec c3 a7 e8   .h%.......*.....
0020  df 78 96 03 11 3d c5 47 56 a6                     .x...=.GV.

Time            Source                Destination           No.    Protocol Length Info
11:50:37.416666 TZ-210W-ROUTER-X3     Broadcast                    0xa168   38     Ethernet II

Frame 54: 38 bytes on wire (304 bits), 38 bytes captured (304 bits)
    Encapsulation type: Ethernet (1)
    Arrival Time: Aug 23, 2014 11:50:37.416666000 Central Daylight Time
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1408812637.416666000 seconds
    [Time delta from previous captured frame: 0.000000000 seconds]
    [Time delta from previous displayed frame: 0.000000000 seconds]
    [Time since reference or first frame: 4.116666000 seconds]
    Frame Number: 54
    Frame Length: 38 bytes (304 bits)
    Capture Length: 38 bytes (304 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:ethertype:data]
    [Coloring Rule Name: Broadcast]
    [Coloring Rule String: eth[0] &amp; 1]
Ethernet II, Src: TZ-210W-ROUTER-X3 (00:17:c5:42:be:5f), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
    Destination: Broadcast (ff:ff:ff:ff:ff:ff)
        Address: Broadcast (ff:ff:ff:ff:ff:ff)
        .... ..1. .... .... .... .... = LG bit: Locally administered address (this is NOT the factory default)
        .... ...1 .... .... .... .... = IG bit: Group address (multicast/broadcast)
    Source: TZ-210W-ROUTER-X3 (00:17:c5:42:be:5f)
        Address: TZ-210W-ROUTER-X3 (00:17:c5:42:be:5f)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Type: Unknown (0xa168)
Data (24 bytes)
    Data: 25010018000000012af0ecc3a7e8df789603113dc54756a6
    [Length: 24]

0000  ff ff ff ff ff ff 00 17 c5 42 be 5f a1 68 25 01   .........B._.h%.
0010  00 18 00 00 00 01 2a f0 ec c3 a7 e8 df 78 96 03   ......*......x..
0020  11 3d c5 47 56 a6                                 .=.GV.
</code></pre><p>Does anyone know what these are?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span> <span class="post-tag tag-link-0xa168" rel="tag" title="see questions tagged &#39;0xa168&#39;">0xa168</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Aug '14, 10:39</strong></p><img src="https://secure.gravatar.com/avatar/5b1802a3dde015a758fb13baafb1605f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="proj964&#39;s gravatar image" /><p><span>proj964</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="proj964 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Aug '14, 07:44</strong> </span></p></div></div><div id="comments-container-35685" class="comments-container"><span id="35701"></span><div id="comment-35701" class="comment"><div id="post-35701-score" class="comment-score"></div><div class="comment-text"><p>This looks a bit strange - I can't see neither the MAC addresses nor the ether type 0xa168 you mention in the hex dump lines. Did you edit the output?</p></div><div id="comment-35701-info" class="comment-info"><span class="comment-age">(25 Aug '14, 01:51)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="35710"></span><div id="comment-35710" class="comment"><div id="post-35710-score" class="comment-score"></div><div class="comment-text"><p>Hi. I didn't edit the output...just didn't get it all. I have replaced the original trace entry with two different consecutive samples that show all of the data (I hope).</p></div><div id="comment-35710-info" class="comment-info"><span class="comment-age">(25 Aug '14, 07:45)</span> <span class="comment-user userinfo">proj964</span></div></div></div><div id="comment-tools-35685" class="comment-tools"></div><div class="clear"></div><div id="comment-35685-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35729"></span>

<div id="answer-container-35729" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35729-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35729-score" class="post-score" title="current number of votes">0</div><span id="post-35729-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The source MAC is apparently a Dell SonicWall TZ-210W (interface X0 and X3). As the frame destination is the broadcast address, this could be part of a propietary SonicWall protocol, maybe part of the HA cluster protocol (if there is a cluster configured) or something similar. If you want to know for sure, please contact the Dell SonicWall support and ask them for an explanation. Please don't forget to add a comment here as well, for the benefit of other sites users ;-))</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Aug '14, 15:21</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-35729" class="comments-container"><span id="35883"></span><div id="comment-35883" class="comment"><div id="post-35883-score" class="comment-score"></div><div class="comment-text"><p>From Sonicwall Tech Sppt: I just wanted to inform about Ether type 0xa168, it is SDP ( Sonicpoint Discovery Protocol) which is a SonicWALL proprietary protocol and is used to Discover Sonicpoint APs on the network.</p></div><div id="comment-35883-info" class="comment-info"><span class="comment-age">(29 Aug '14, 12:20)</span> <span class="comment-user userinfo">proj964</span></div></div></div><div id="comment-tools-35729" class="comment-tools"></div><div class="clear"></div><div id="comment-35729-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

