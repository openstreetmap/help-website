+++
type = "question"
title = "Decode 802.11 traffic to TCP/IP packets"
description = '''Hi all, My intention is to monitor the activities between 2 wireless stations. I can successfully capture the wireless (802.11) traffic and decrypt them. Now I see a lot of LLC packets. Is it possible for Wireshark to decode such packets and give me the TCP/IP packets? Thanks ! BR, NewWireShark'''
date = "2013-01-06T17:51:00Z"
lastmod = "2015-05-26T08:20:00Z"
weight = 17480
keywords = [ "802.11" ]
aliases = [ "/questions/17480" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decode 802.11 traffic to TCP/IP packets](/questions/17480/decode-80211-traffic-to-tcpip-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17480-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17480-score" class="post-score" title="current number of votes">0</div><span id="post-17480-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>My intention is to monitor the activities between 2 wireless stations.</p><p>I can successfully capture the wireless (802.11) traffic and decrypt them.</p><p>Now I see a lot of LLC packets. Is it possible for Wireshark to decode such packets and give me the TCP/IP packets?</p><p>Thanks !</p><p>BR, NewWireShark</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jan '13, 17:51</strong></p><img src="https://secure.gravatar.com/avatar/d1bebed81e6b2a8de3a4ce24b4c3a1be?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="newwireshark&#39;s gravatar image" /><p><span>newwireshark</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="newwireshark has no accepted answers">0%</span></p></div></div><div id="comments-container-17480" class="comments-container"><span id="42665"></span><div id="comment-42665" class="comment"><div id="post-42665-score" class="comment-score"></div><div class="comment-text"><p>Can you post the capture to an accessible webpage (such as cloudshark or Google-Drive)? If you post the capture, please include the SSID and passphrase so we can decrypt the capture.</p><p>Have you selected a Data or QoS Data frame in Wireshark? If yes, you should see the following in the Packet Details pane: 1. Frame 2. Radiotap or PPI 3. IEEE 802.11 header 4. LLC 5. IP 6. TCP</p><p>The Radiotap/PPI section may be omitted depending on your wireless driver.</p></div><div id="comment-42665-info" class="comment-info"><span class="comment-age">(26 May '15, 08:20)</span> <span class="comment-user userinfo">Amato_C</span></div></div></div><div id="comment-tools-17480" class="comment-tools"></div><div class="clear"></div><div id="comment-17480-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

