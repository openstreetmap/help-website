+++
type = "question"
title = "Wi-Fi how to filter packet with different modulation schemes"
description = '''Hello Guys, I&#x27;ve a question about how to sort Wi-Fi messages using the modulation as a filter. Do you have any suggestion for that? I saw the radiotap.channel.flags.cck filter that should provide the signals modulated with CCK.... but what about other modulation schemes?  Regards'''
date = "2016-09-02T05:32:00Z"
lastmod = "2016-09-02T06:04:00Z"
weight = 55286
keywords = [ "wi-fi", "filters" ]
aliases = [ "/questions/55286" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wi-Fi how to filter packet with different modulation schemes](/questions/55286/wi-fi-how-to-filter-packet-with-different-modulation-schemes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55286-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55286-score" class="post-score" title="current number of votes">0</div><span id="post-55286-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Guys,</p><p>I've a question about how to sort Wi-Fi messages using the modulation as a filter. Do you have any suggestion for that? I saw the radiotap.channel.flags.cck filter that should provide the signals modulated with CCK.... but what about other modulation schemes?</p><p>Regards</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wi-fi" rel="tag" title="see questions tagged &#39;wi-fi&#39;">wi-fi</span> <span class="post-tag tag-link-filters" rel="tag" title="see questions tagged &#39;filters&#39;">filters</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Sep '16, 05:32</strong></p><img src="https://secure.gravatar.com/avatar/9db113e37f406229e727f802becd6731?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="elwifi&#39;s gravatar image" /><p><span>elwifi</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="elwifi has no accepted answers">0%</span></p></div></div><div id="comments-container-55286" class="comments-container"><span id="55290"></span><div id="comment-55290" class="comment"><div id="post-55290-score" class="comment-score"></div><div class="comment-text"><p>Is there anything specific you are looking for? I found that the information that is contained in the radiotap header is VERY hardware dependent. Some adapters give lots of good information, others not so much. Especially with 802.11n, there are many ways to send frames.<br />
</p><p>For one of my adapters that I can use on Linux, an Intel 7260, I can get this from Linux with Wireshark:</p><pre><code>Radiotap Header v0, Length 33
    Header revision: 0
    Header pad: 0
    Header length: 33
    Present flags
    Flags: 0x10
    Channel frequency: 5745 [A 149]
    Channel flags: 0x0140, Orthogonal Frequency-Division Multiplexing (OFDM), 5 GHz spectrum
        .... .... ...0 .... = Turbo: False
        .... .... ..0. .... = Complementary Code Keying (CCK): False
        .... .... .1.. .... = Orthogonal Frequency-Division Multiplexing (OFDM): True
        .... .... 0... .... = 2 GHz spectrum: False
        .... ...1 .... .... = 5 GHz spectrum: True
        .... ..0. .... .... = Passive: False
        .... .0.. .... .... = Dynamic CCK-OFDM: False
        .... 0... .... .... = Gaussian Frequency Shift Keying (GFSK): False
        ...0 .... .... .... = GSM (900MHz): False
        ..0. .... .... .... = Static Turbo: False
        .0.. .... .... .... = Half Rate Channel (10MHz Channel Width): False
        0... .... .... .... = Quarter Rate Channel (5MHz Channel Width): False
    SSI Signal: -46 dBm
    RX flags: 0x0000
    MCS information
    [Data Rate: 72.2 Mb/s]
    SSI Signal: -47 dBm
    Antenna: 0
    SSI Signal: -46 dBm
    Antenna: 1

802.11 radio information
    PHY type: 802.11n (7)
    MCS index: 7
    Bandwidth: 20 MHz (0)
    Short GI: True
    FEC: BEC (0)
    Number of STBC streams: 0
    Data rate: 72.2 Mb/s
    Channel: 149
    Frequency: 5745 MHz
    Signal strength (dBm): -46 dBm</code></pre><p>Any of these fields would be filterable, I believe.</p></div><div id="comment-55290-info" class="comment-info"><span class="comment-age">(02 Sep '16, 06:04)</span> <span class="comment-user userinfo">Bob Jones</span></div></div></div><div id="comment-tools-55286" class="comment-tools"></div><div class="clear"></div><div id="comment-55286-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

