+++
type = "question"
title = "Wireshark does not decrypt WLAN UDP broadcast packet from AP"
description = '''I am am trying to understand why Wireshark is not decrypting the WLAN UDP broadcast packets from the AP. In the example below you can see the UDP packet is sent (and decrypted) when sent to the AP in frame 68, however when it is rebroadcast by the AP in frame 70 Wireshark does not decrypt the packet...'''
date = "2016-05-10T09:22:00Z"
lastmod = "2016-07-17T03:09:00Z"
weight = 52397
keywords = [ "broadcast", "ap", "udp", "wlan", "802.11" ]
aliases = [ "/questions/52397" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark does not decrypt WLAN UDP broadcast packet from AP](/questions/52397/wireshark-does-not-decrypt-wlan-udp-broadcast-packet-from-ap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52397-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52397-score" class="post-score" title="current number of votes">0</div><span id="post-52397-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am am trying to understand why Wireshark is not decrypting the WLAN UDP broadcast packets from the AP.</p><p>In the example below you can see the UDP packet is sent (and decrypted) when sent to the AP in frame 68, however when it is rebroadcast by the AP in frame 70 Wireshark does not decrypt the packet. Can anybody explain why? is there a way to correct this?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/wireshark_7Mc91la.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-broadcast" rel="tag" title="see questions tagged &#39;broadcast&#39;">broadcast</span> <span class="post-tag tag-link-ap" rel="tag" title="see questions tagged &#39;ap&#39;">ap</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-wlan" rel="tag" title="see questions tagged &#39;wlan&#39;">wlan</span> <span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 May '16, 09:22</strong></p><img src="https://secure.gravatar.com/avatar/796d353373746c193c6e5c1ca1655320?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mw-ed&#39;s gravatar image" /><p><span>mw-ed</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mw-ed has one accepted answer">100%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 May '16, 09:25</strong> </span></p></div></div><div id="comments-container-52397" class="comments-container"></div><div id="comment-tools-52397" class="comment-tools"></div><div class="clear"></div><div id="comment-52397-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="52398"></span>

<div id="answer-container-52398" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52398-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52398-score" class="post-score" title="current number of votes">1</div><span id="post-52398-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>All data frames to the AP (ToDS) are actually unicast at layer 2, so would be encrypted using the unicast key, key index 0. Frames sent from the AP (FromDS) could be either unicast, again encrypted with key index 0, or multicast/broadcast, which could be using either key index 1 or 2. To see which key is in use, open the CCMP parameters field. So it appears Wireshark is congnizant of the PTK in this case, as it can decrypt the unicast frames. However, it is struggling with the GTK, or group key. They get out of sync, so it is possible Wireshark does not actually have it. It comes across with the four-way EAPOL handshake, assuming you are using WPA or some variant, but can be updated with a group rekey event (two-way handshake).</p><p>I have seen this behavior before, but never did a deep dive on it. Some tips:</p><ol><li>Make sure the eapol frames are there from a 4-way handshake, so we know you have the PTK.<br />
</li><li>Save the trace after seeing this issue, and then reload. That can usually help a lot.</li><li>Move the saved trace to airdecap-ng, one of the aircrack-ng tools.</li></ol><p>Be sure there are no other GTK rekey events - these would be encrypted with the unicast key so should be visible if you see the other unicast traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 May '16, 10:27</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p><span>Bob Jones</span><br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span> </br></p></div></div><div id="comments-container-52398" class="comments-container"><span id="52421"></span><div id="comment-52421" class="comment"><div id="post-52421-score" class="comment-score"></div><div class="comment-text"><p><span>@Bob Jones</span>, found this good enough to qualify as an answer.</p></div><div id="comment-52421-info" class="comment-info"><span class="comment-age">(10 May '16, 23:35)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-52398" class="comment-tools"></div><div class="clear"></div><div id="comment-52398-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="54112"></span>

<div id="answer-container-54112" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54112-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54112-score" class="post-score" title="current number of votes">0</div><span id="post-54112-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>WPA decoding in Wireshark was improved with the 2.0 release and the fixes also got backported to Old Stable some releases ago. But Wireshark 1.10.x is still using the old buggy code.</p><p>Wireshark 2.0 itself also still has known wpa decoding issues, so please try one of the current versions (2.0.4, 1.12.12 or 2.1.1). They have no known Wpa decoding bugs and support more than one (more or less random) group key. GTA rekeys really should be no longer an issue with any of those versions.</p><p>If that's not working I would like to get the capture to find out what's wrong. (Fyi: I have reworked the wpa decoding and know the code. If it's an bug I can fix it.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '16, 03:09</strong></p><img src="https://secure.gravatar.com/avatar/18515a703aba0eefe60e68fcec7ba929?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alexander%20Wetzel&#39;s gravatar image" /><p><span>Alexander We...</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alexander Wetzel has no accepted answers">0%</span></p></div></div><div id="comments-container-54112" class="comments-container"></div><div id="comment-tools-54112" class="comment-tools"></div><div class="clear"></div><div id="comment-54112-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

