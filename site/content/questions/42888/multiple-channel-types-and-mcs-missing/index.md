+++
type = "question"
title = "Multiple Channel types and MCS missing"
description = '''Hi, Why are they multiple channel types in my packet capture? I have this one: Channel type: 802.11a (0x0140), Orthogonal Frequency-Division Multiplexing (OFDM), 5 GHz spectrum and this one Channel type: 802.11n (ht20, 5 GHz) (0x00010140), Orthogonal Frequency-Division Multiplexing (OFDM), 5 GHz spe...'''
date = "2015-06-04T10:15:00Z"
lastmod = "2015-06-22T18:23:00Z"
weight = 42888
keywords = [ "apple" ]
aliases = [ "/questions/42888" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Multiple Channel types and MCS missing](/questions/42888/multiple-channel-types-and-mcs-missing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42888-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42888-score" class="post-score" title="current number of votes">1</div><span id="post-42888-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Why are they multiple channel types in my packet capture?</p><p>I have this one: Channel type: 802.11a (0x0140), Orthogonal Frequency-Division Multiplexing (OFDM), 5 GHz spectrum</p><p>and this one</p><p>Channel type: 802.11n (ht20, 5 GHz) (0x00010140), Orthogonal Frequency-Division Multiplexing (OFDM), 5 GHz spectrum, HT Channel (20MHz Channel Width)</p><p>And how come there is no MCS info?`</p><pre><code>      1 0.000000       d0:84:b0:70:bd:8d     8c:29:37:e8:29:34     802.11   347    QoS Data, SN=2412, FN=0, Flags=.p....F..
Frame 1: 347 bytes on wire (2776 bits), 347 bytes captured (2776 bits)
Radiotap Header v0, Length 52
    Header revision: 0
    Header pad: 0
    Header length: 52
    Present flags
    MAC timestamp: 429790384
    Flags: 0x14
        .... ...0 = CFP: False
        .... ..0. = Preamble: Long
        .... .1.. = WEP: True
        .... 0... = Fragmentation: False
        ...1 .... = FCS at end: True
        ..0. .... = Data Pad: False
        .0.. .... = Bad FCS: False
        0... .... = Short GI: False
    Channel frequency: 5260 [A 52]
    Channel type: 802.11a (0x0140), Orthogonal Frequency-Division Multiplexing (OFDM), 5 GHz spectrum
    SSI Noise: -89 dBm
    Antenna: 1
    Channel number: 52
    Channel frequency: 5260
    Channel type: 802.11n (ht20, 5 GHz) (0x00010140), Orthogonal Frequency-Division Multiplexing (OFDM), 5 GHz Spectrum, HT Channel (20MHz Channel Width)
    A-MPDU status
        A-MPDU reference number: 2412
        A-MPDU flags: 0x0004
            .... .... .... ...0 = Driver reports 0-length subframes in this A-MPDU: False
            .... .... .... ..0. = This is a 0-length subframe: False
            .... .... .... .1.. = Last subframe of this A-MPDU is known: True
            .... .... .... 0... = This is the last subframe of this A-MPDU: False
            .... .... ...0 .... = Delimiter CRC error on this subframe: False
    VHT information
        Known VHT information: 0x1ff
            .... .... .... ...1 = STBC: True
            .... .... .... ..1. = TXOP_PS_NOT_ALLOWED: True
            .... .... .... .1.. = Guard interval: True
            .... .... .... 1... = SGI Nsym disambiguation: True
            .... .... ...1 .... = LDPC extra OFDM symbol: True
            .... .... ..1. .... = Beamformed: True
            .... .... .1.. .... = Bandwidth: True
            .... .... 1... .... = Group ID: True
            .... ...1 .... .... = Partial AID: True
        .... ...0 = STBC: Off
        .... ..1. = TXOP_PS_NOT_ALLOWED: True
        .... .1.. = Guard interval: short (1)
        .... 0... = SGI Nsym disambiguation: False
        ...0 .... = LDPC extra OFDM symbol: False
        ..0. .... = Beamformed: False
        Bandwidth: 80 MHz (4)
        User 0: MCS 9
            1001 .... = MCS index 0: 9 (256-QAM 5/6)
            .... 0010 = Spatial streams 0: 2
            Space-time streams 0: 2
            Coding 0: LDPC (1)
            [Data Rate: 866.6 Mb/s]
        Group Id: 0
        Partial AID: 0
IEEE 802.11 QoS Data, Flags: .p....F..
    Type/Subtype: QoS Data (0x0028)
    Frame Control Field: 0x8842
        .... ..00 = Version: 0
        .... 10.. = Type: Data frame (2)
        1000 .... = Subtype: 8
        Flags: 0x42
            .... ..10 = DS status: Frame from DS to a STA via AP(To DS: 0 From DS: 1) (0x02)
            .... .0.. = More Fragments: This is the last fragment
            .... 0... = Retry: Frame is not being retransmitted
            ...0 .... = PWR MGT: STA will stay up
            ..0. .... = More Data: No data buffered
            .1.. .... = Protected flag: Data is protected
            0... .... = Order flag: Not strictly ordered
    .000 0000 0011 0000 = Duration: 48 microseconds
    Receiver address: Apple_e8:29:34 (8c:29:37:e8:29:34)
    Destination address: Apple_e8:29:34 (8c:29:37:e8:29:34)
    Transmitter address: 00:84:b0:70:bd:9c (00:84:b0:70:bd:9c)
    Source address: Sagemcom_70:bd:8d (d0:84:b0:70:bd:8d)
    BSS Id: 00:84:b0:70:bd:9c (00:84:b0:70:bd:9c)
    .... .... .... 0000 = Fragment number: 0
    1001 0110 1100 .... = Sequence number: 2412
    Frame check sequence: 0xb7c2ac4a [incorrect, should be 0x464e2f60]
        [Good: False]
        [Bad: True]
    Qos Control: 0x0000
    CCMP parameters
        CCMP Ext. Initialization Vector: 0x0000000009B2
        Key Index: 0
Data (257 bytes)</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-apple" rel="tag" title="see questions tagged &#39;apple&#39;">apple</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jun '15, 10:15</strong></p><img src="https://secure.gravatar.com/avatar/643016a5caf72098dc71453e85f884f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joe%20C&#39;s gravatar image" /><p><span>Joe C</span><br />
<span class="score" title="4 reputation points">4</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joe C has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Jun '15, 17:08</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-42888" class="comments-container"><span id="42893"></span><div id="comment-42893" class="comment"><div id="post-42893-score" class="comment-score"></div><div class="comment-text"><p>What WiFi adapter are you using to capture the traffic?</p></div><div id="comment-42893-info" class="comment-info"><span class="comment-age">(04 Jun '15, 12:14)</span> <span class="comment-user userinfo">Amato_C</span></div></div><span id="42894"></span><div id="comment-42894" class="comment"><div id="post-42894-score" class="comment-score"></div><div class="comment-text"><p>It's a 2014 MacBook Air with a 802.11 AC 2x2 apple airport internal card.</p><p>AirPort Extreme (0x14E4, 0x117) Firmware Version: Broadcom BCM43xx 1.0 (7.15.166.24.3)</p></div><div id="comment-42894-info" class="comment-info"><span class="comment-age">(04 Jun '15, 12:30)</span> <span class="comment-user userinfo">Joe C</span></div></div></div><div id="comment-tools-42888" class="comment-tools"></div><div class="clear"></div><div id="comment-42888-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="42898"></span>

<div id="answer-container-42898" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42898-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42898-score" class="post-score" title="current number of votes">1</div><span id="post-42898-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The Radiotap information is provided by the driver. I have seen many drivers provide the incorrect information for the Radiotap header. However, your driver is providing some very good information for example:</p><ol><li>MCS index 0: 9 (256-QAM 5/6) - MCS for 11ac</li><li>Guard interval: short (1)</li><li>Spatial streams: 2 Space-time streams</li><li>Bandwidth: 80 MHz - Bandwidth only used in 11ac</li></ol><p>Using the above information, we can calculate that your link speed = 866.7Mbps And your WiFi driver is reporting = Data Rate: 866.6 Mb/s</p><p>So you have all the information in the packet. Yes it is hidden, but it is there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jun '15, 13:00</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-42898" class="comments-container"><span id="42904"></span><div id="comment-42904" class="comment"><div id="post-42904-score" class="comment-score"></div><div class="comment-text"><p>How do I see what the driver version is and where it is? I have different MacBook models and I get different information back, and it's making difficult to interpret the data. :(</p></div><div id="comment-42904-info" class="comment-info"><span class="comment-age">(04 Jun '15, 19:08)</span> <span class="comment-user userinfo">Joe C</span></div></div><span id="42905"></span><div id="comment-42905" class="comment"><div id="post-42905-score" class="comment-score"></div><div class="comment-text"><p>Any idea why certain frames have an actually MCS info tab and some don't? I think QOS Data has it (sometimes)</p></div><div id="comment-42905-info" class="comment-info"><span class="comment-age">(04 Jun '15, 19:10)</span> <span class="comment-user userinfo">Joe C</span></div></div><span id="42911"></span><div id="comment-42911" class="comment"><div id="post-42911-score" class="comment-score"></div><div class="comment-text"><blockquote><p>How do I see what the driver version is and where it is?</p></blockquote><p>Not clear. Selecting "About This Mac" from the Apple menu, clicking the "More Info..." button in its dialog, clicking on "System Report..." in the new dialog, and selecting "Wi-Fi" under "Network" will give you the hardware, but, on my machine, it just reports it as "AirPort Extreme (0x14E4, 0xEF)" with the firmware being "Broadcom BCM43xx 1.0", but that's not good enough to figure out which kext in /System/Library/Extensions/IO80211Family.kext/Contents/PlugIns" is the driver for the adapter on my machine.</p></div><div id="comment-42911-info" class="comment-info"><span class="comment-age">(05 Jun '15, 03:20)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="42929"></span><div id="comment-42929" class="comment"><div id="post-42929-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Any idea why certain frames have an actually MCS info tab and some don't?</p></blockquote><p>Beacons are generally sent out using classic 802.11 - no, not even 802.11b, much less 11g, 11a, 11n, or 11ac) - so that <em>all</em> stations can see the network. Those won't have MCS information, as there's no MCS information to have. If you capture in monitor mode, you'll probably see a significant number of beacons.</p></div><div id="comment-42929-info" class="comment-info"><span class="comment-age">(05 Jun '15, 09:24)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-42898" class="comment-tools"></div><div class="clear"></div><div id="comment-42898-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42900"></span>

<div id="answer-container-42900" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42900-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42900-score" class="post-score" title="current number of votes">1</div><span id="post-42900-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Part of the problem here is that Apple are "helpfully" providing both a <a href="http://www.radiotap.org/defined-fields/Channel">Channel</a> field and an <a href="http://www.radiotap.org/suggested-fields/XChannel">XChannel</a> field in the radiotap header. The first of those is the one that says it's 11a; the second of those says it's 11n.</p><p>However, 11n is "HT", or "High Throughput"; the "VHT", or "Very High Throughput", information says it's 11ac.</p><p>Either the radiotap dissector can show all the raw radiotap information, or it can try to digest it and ignore, for example, older radiotap fields that can't handle 11n or 11ac if there are also newer radiotap fields that indicate that it's using a later standard. Perhaps there should be better way of presenting radio metadata, e.g. pass a cleaned-up version to the 802.11 dissector and have it present the cleaned-up version, and let the user open up the radiotap header if they want to see the raw metadata (bearing in mind that it may have somewhat self-contradictory information).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jun '15, 17:26</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-42900" class="comments-container"><span id="42903"></span><div id="comment-42903" class="comment"><div id="post-42903-score" class="comment-score"></div><div class="comment-text"><p>So how does one discern what the correct mode is?</p></div><div id="comment-42903-info" class="comment-info"><span class="comment-age">(04 Jun '15, 19:06)</span> <span class="comment-user userinfo">Joe C</span></div></div><span id="42907"></span><div id="comment-42907" class="comment"><div id="post-42907-score" class="comment-score"></div><div class="comment-text"><p>must you use radiotap info? For me it worked better with Per Packet Information.</p></div><div id="comment-42907-info" class="comment-info"><span class="comment-age">(04 Jun '15, 23:29)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="42930"></span><div id="comment-42930" class="comment"><div id="post-42930-score" class="comment-score"></div><div class="comment-text"><blockquote><p>So how does one discern what the correct mode is?</p></blockquote><p>Unfortunately, you have to look at several items and deduce it from that, the way Amato_C and I did. As I said in the third paragraph in my answer, Wireshark should really do a better job here.</p></div><div id="comment-42930-info" class="comment-info"><span class="comment-age">(05 Jun '15, 09:26)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="42931"></span><div id="comment-42931" class="comment"><div id="post-42931-score" class="comment-score"></div><div class="comment-text"><blockquote><p>For me it worked better with Per Packet Information.</p></blockquote><p>Worked better because there was more information from the PPI header, or worked better because the information there is easier to understand when you read Wireshark's dissection of it? My goal is to enhance radiotap or its processing by programs in order eliminate all reasons to prefer other radio headers, including PPI, to radiotap.</p></div><div id="comment-42931-info" class="comment-info"><span class="comment-age">(05 Jun '15, 09:28)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="42933"></span><div id="comment-42933" class="comment"><div id="post-42933-score" class="comment-score"></div><div class="comment-text"><p><code>Worked better because there was more information from the PPI header, or worked better because the information there is easier to understand when you read Wireshark's dissection of it?</code> So for me it was easier to read, because it shows me clearly that I am on the 2.4GHz 802.11n. But the only one machine who is able to capture ppi is my mac. With Ubuntu Notebook only Radiohead is possible. So if you need more Info please tell me. I can take some traces for you.</p></div><div id="comment-42933-info" class="comment-info"><span class="comment-age">(05 Jun '15, 16:03)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="42937"></span><div id="comment-42937" class="comment not_top_scorer"><div id="post-42937-score" class="comment-score"></div><div class="comment-text"><p>OK, that sounds like a presentation issue, which should be fixed in Wireshark, as per the last paragraph of my answer.</p><blockquote><p>With Ubuntu Notebook only Radiohead is possible.</p></blockquote><p>So what does Thom Yorke think about this? :-)</p></div><div id="comment-42937-info" class="comment-info"><span class="comment-age">(05 Jun '15, 18:15)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="43469"></span><div id="comment-43469" class="comment not_top_scorer"><div id="post-43469-score" class="comment-score"></div><div class="comment-text"><blockquote><p>OK, that sounds like a presentation issue, which should be fixed in Wireshark, as per the last paragraph of my answer.</p></blockquote><p>Now <em>is</em> fixed in Wireshark, in the master branch. There will be an "802.11 radio information" subtree after the radiotap subtree and before the 802.11 subtree, and it'll have a reasonably-digested version of the radio information, including showing the PHY and (if available) band information, e.g. showing "802.11n" (or "802.11n 2.4 GHz" or "802.11n 5 GHz") for 802.11n packets or "802.11ac" for 802.11ac packets.</p><p>Obviously, it won't show information that's not available in the radiotap or PPI or whatever other radio header is there, but it should show a summary of the information that's there. (11ac needs some more work, but it should have a reasonably complete display of 11n and older standards.)</p></div><div id="comment-43469-info" class="comment-info"><span class="comment-age">(22 Jun '15, 18:23)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-42900" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-42900-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

