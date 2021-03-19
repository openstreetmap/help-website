+++
type = "question"
title = "Differences on 2.4ghz and 5ghz dual band"
description = '''Hi There, I&#x27;ve been working on setting up some local network monitoring of my wpa2, dual band, home network. I have a particular configuration that&#x27;s working great for the 2.4ghz, but after switching channels to my 5ghz network I don&#x27;t have as much luck. I&#x27;m using Kali Linux on RPI-3 and the Alfa AW...'''
date = "2017-01-31T19:16:00Z"
lastmod = "2017-02-01T05:56:00Z"
weight = 59201
keywords = [ "decryption", "tshark" ]
aliases = [ "/questions/59201" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Differences on 2.4ghz and 5ghz dual band](/questions/59201/differences-on-24ghz-and-5ghz-dual-band)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59201-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59201-score" class="post-score" title="current number of votes">0</div><span id="post-59201-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi There, I've been working on setting up some local network monitoring of my wpa2, dual band, home network. I have a particular configuration that's working great for the 2.4ghz, but after switching channels to my 5ghz network I don't have as much luck. I'm using Kali Linux on RPI-3 and the Alfa AWUS051NH adapter. Here's my validation / setup:</p><p><strong>First on 2.4ghz -- this works</strong></p><p><code>airmon-ng start wlan1mon 6 tshark -i wlan1mon -I -o wlan.check_fcs:FALSE -o "wlan.ignore_wep:Yes - with IV" -o wlan.enable_decryption:TRUE -o "uat:80211_keys:\"wpa-psk\",\"xxxxxxx\"" -o capture.prom_mode:TRUE -Y "eapol or dns or http"</code></p><p>After re-authenticating one of my 2.4ghz devices, I then see the eapol handshake and start seeing various dns and http requests.</p><p><strong>Then I try 5ghz -- this doesn't work</strong></p><p><code>airmon-ng start wlan1mon 36 tshark -i wlan1mon -I -o wlan.check_fcs:FALSE -o "wlan.ignore_wep:Yes - with IV" -o wlan.enable_decryption:TRUE -o "uat:80211_keys:\"wpa-psk\",\"xxxxxxx\"" -o capture.prom_mode:TRUE -Y "eapol or dns or http"</code></p><p>I see the eapol handshake but it seems that the decryption doesn't work and no dns or http packets are provided.</p><hr /><p>I've been theorizing that this might have to do with my dual band network having the same SSID name but not sure and could use some advice on where to look next. Thank you!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jan '17, 19:16</strong></p><img src="https://secure.gravatar.com/avatar/27d169447d3d133c75af8fc8edcb8e6d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mveilleux&#39;s gravatar image" /><p><span>mveilleux</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mveilleux has no accepted answers">0%</span></p></div></div><div id="comments-container-59201" class="comments-container"></div><div id="comment-tools-59201" class="comment-tools"></div><div class="clear"></div><div id="comment-59201-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59220"></span>

<div id="answer-container-59220" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59220-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59220-score" class="post-score" title="current number of votes">0</div><span id="post-59220-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is most often attributed to not capturing data to decrypt instead of decryption does not work (assuming, of course, you have all four EAPOL handshake packets and the correct key, etc...).</p><p>This is most often due to a mismatch in capture capability - the capture adapter cannot pickup high speed data frames from the actual communications channel. You may have to add some configuration to the capture device as well.<br />
</p><p>If you search here there are many instances of this. Disable any 802.11n/ac capability on the AP so you only have 802.11a on the 5GHz channel and see if it works. Then add in the higher rates/capability allowed through 802.11n/ac and see where it breaks. There is relevant information on device capabilities in:</p><p>Network traffic</p><pre><code>Beacons
Probe requests/responses
Association requests/responses</code></pre><p>as well as inside Linux with</p><pre><code>iw dev
iw list</code></pre><p>Long term, you will want to match the capture device to your communications channel. So if you know how you are communicating, we can then select a capture device that is appropriate (802.11n or ac, number of spatial streams, guard interval, LDPC capable, etc.). Alternatively, reduce the communication channel capability to what the capture device can handle.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '17, 05:56</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p><span>Bob Jones</span><br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span> </br></p></div></div><div id="comments-container-59220" class="comments-container"></div><div id="comment-tools-59220" class="comment-tools"></div><div class="clear"></div><div id="comment-59220-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

