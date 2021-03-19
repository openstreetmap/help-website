+++
type = "question"
title = "tshark:How to get the wlan management frame payload"
description = '''I am trying to extract the complete wlan_mgt portion of a frame from a saved capture file using tshark. What is interesting is using the field &quot;data&quot; will dump the data layer of a data frame but using the field &quot;wlan_mgt&quot; just prints the text &quot;wlan_mgt&quot; in the output but is accepted by tshark as a v...'''
date = "2016-02-04T12:14:00Z"
lastmod = "2016-02-04T12:46:00Z"
weight = 49856
keywords = [ "wlan_mgt", "wlan", "tshark" ]
aliases = [ "/questions/49856" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark:How to get the wlan management frame payload](/questions/49856/tsharkhow-to-get-the-wlan-management-frame-payload)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49856-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to extract the complete wlan_mgt portion of a frame from a saved capture file using tshark. What is interesting is using the field "data" will dump the data layer of a data frame but using the field "wlan_mgt" just prints the text "wlan_mgt" in the output but is accepted by tshark as a valid field.</p><p>Using command: $ tshark -r wpa.full.cap -2 -O wlan -T fields -e wlan.fc.type -e wlan.fc.subtype -e wlan.fcs_good -e wlan_mgt -e data -E separator=,</p><p>I get:</p><p>0,8,,wlan_mgt,</p><p>0,4,,wlan_mgt,</p><p>0,5,,wlan_mgt,</p><p>0,11,,wlan_mgt,</p><p>0,11,,wlan_mgt,</p><p>0,0,,wlan_mgt,</p><p>0,1,,wlan_mgt,</p><p>2,0,,,</p><p>2,0,,,</p><p>2,0,,,</p><p>2,0,,,</p><p>2,0,,,3e71a281c4c01e01f06998bc85cb64a3189f078ab63f9a4e7a09765f5e8fa2d4f3b3db4a3fc0eeb7afc74317a502 f8c5e25979800f93501534bd29a28f730763f7eea056cb18988973e786ad2ede9e5f071d16ae9de80bdd80d142ce0734f4 159701299da1c983e45f5f0f05bf5adf3bf8924b6b79c9693276058b339246adacc874ab71f74fba491eaa0a4676a58f89 62e95005f22ba1</p></div><div id="question-tags" class="tags-container tags">wlan_mgt wlan tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Feb '16, 12:14</strong></p><img src="https://secure.gravatar.com/avatar/ccc3f50ef99e10e348a902ee8483f93c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ted%20Wards&#39;s gravatar image" /><p>Ted Wards<br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ted Wards has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Feb '16, 12:42</p></div></div><div id="comments-container-49856" class="comments-container"></div><div id="comment-tools-49856" class="comment-tools"></div><div class="clear"></div><div id="comment-49856-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49863"></span>

<div id="answer-container-49863" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49863-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>using the field "data" will dump the data layer of a data frame</p></blockquote><p>Not necessarily:</p><pre><code>$ tshark -V -r ~/captures/802.11/llc.cap
Frame 1: 68 bytes on wire (544 bits), 68 bytes captured (544 bits)
    Encapsulation type: IEEE 802.11 Wireless LAN (20)

       ...

IEEE 802.11 Data, Flags: ..m...F.
    Type/Subtype: Data (0x0020)
    Frame Control Field: 0x0822
        .... ..00 = Version: 0
        .... 10.. = Type: Data frame (2)
        0000 .... = Subtype: 0
        Flags: 0x22
            .... ..10 = DS status: Frame from DS to a STA via AP(To DS: 0 From DS: 1) (0x2)
            .... .0.. = More Fragments: This is the last fragment
            .... 0... = Retry: Frame is not being retransmitted
            ...0 .... = PWR MGT: STA will stay up
            ..1. .... = More Data: Data is buffered for STA at AP
            .0.. .... = Protected flag: Data is not protected
            0... .... = Order flag: Not strictly ordered
    .000 0000 0000 0000 = Duration: 0 microseconds
    Receiver address: Broadcast (ff:ff:ff:ff:ff:ff)
    Destination address: Broadcast (ff:ff:ff:ff:ff:ff)
    Transmitter address: &lt;censored&gt;
    Source address: &lt;censored&gt;
    BSS Id: &lt;censored&gt;
    STA address: Broadcast (ff:ff:ff:ff:ff:ff)
    .... .... .... 0101 = Fragment number: 5
    0000 0000 1010 .... = Sequence number: 10
Internetwork Packet eXchange
    Checksum: 0xffff
    Length: 40 bytes
    Transport Control: 0 hops
    Packet Type: RIP (0x01)
    Destination Network: 6 (0x00000006)
    Destination Node: Broadcast (ff:ff:ff:ff:ff:ff)
    Destination Socket: RIP (0x0453)
    Source Network: 6 (0x00000006)
    Source Node: &lt;censored&gt;
    Source Socket: RIP (0x0453)
IPX Routing Information Protocol
    RIP packet type: Response (2)
    Route Vector: ABBAABBA (0xABBAABBA)
    Hops: 1
    Ticks: 111 ms

         ...

$ ./tshark -T fields -e data -r ~/captures/802.11/llc.cap

$</code></pre><p>Using the field "data" will dump anything shown as the protocol "data", which is anything that can't be dissected in any <em>other</em> fashion. Encrypted (WEP, WPA/WPA2) 802.11 payloads would be dissected as "data" if they can't be decrypted, but any <em>unencrypted</em> 802.11 payload won't be dissected as "data", nor will any encrypted payloads that Wireshark/TShark can decrypt.</p><p>The management frames are probably not encrypted in your capture, and are therefore dissected as management frames, not as "data", so "data" won't show them.</p><p>There appears to be some inconsistency in the way "-T fields" handles "fields" that are protocols - "frame" shows the top-level line in the display of frame, "ipx"/"ipxrip"/"wlan_mgt"/etc. show the protocol's "filter name", and "data" shows the data. File a bug on this.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '16, 12:46</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-49863" class="comments-container"><span id="49892"></span><div id="comment-49892" class="comment"><div id="post-49892-score" class="comment-score"></div><div class="comment-text"><p>Yes. In my example, the data frames(wlan.fc.type=2) which do not show any data have EAPOL protocol and therefore have no "data" layer (or protocol). The last frame is an encrypted frame so it does have the "data" layer(or protocol). It would be nice to have a consistent way to extract the byte string of all layers or protocols as well as the full frame. I guess I am blocked for now trying to do what I need with tshark.</p></div><div id="comment-49892-info" class="comment-info"><span class="comment-age">(05 Feb '16, 03:58)</span> Ted Wards</div></div><span id="49900"></span><div id="comment-49900" class="comment"><div id="post-49900-score" class="comment-score"></div><div class="comment-text"><p>Thanks for filing <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12086">bug 12086</a> on this.</p></div><div id="comment-49900-info" class="comment-info"><span class="comment-age">(05 Feb '16, 11:39)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-49863" class="comment-tools"></div><div class="clear"></div><div id="comment-49863-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

