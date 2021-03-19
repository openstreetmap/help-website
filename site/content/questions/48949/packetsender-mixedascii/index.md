+++
type = "question"
title = "[closed] PacketSender- mixedAscii"
description = '''hey there, i need to send some hex strings via tcp/ip from device to device, directly connected, so i tried first to connect the server device to the computer and send the commands manually via PacketSender. The device opens connection after i send the commands and acts the way it&#x27;s supposed to. but...'''
date = "2016-01-07T09:28:00Z"
lastmod = "2016-01-07T10:11:00Z"
weight = 48949
keywords = [ "hex", "tcppackets", "ascii" ]
aliases = [ "/questions/48949" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] PacketSender- mixedAscii](/questions/48949/packetsender-mixedascii)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48949-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48949-score" class="post-score" title="current number of votes">0</div><span id="post-48949-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hey there,</p><p>i need to send some hex strings via tcp/ip from device to device, directly connected, so i tried first to connect the server device to the computer and send the commands manually via PacketSender. The device opens connection after i send the commands and acts the way it's supposed to.</p><p>but when i connect the device that is supposed to send that commands , that are already formatted ( the string i used to test is one of the strings that the master device outputs ) , it doesn't open the connection. does packetsender adds extra content to the string? i don't have access to source codes to check this out.</p><p>After all this i installed wireshark and kinda traced what is happening. it shows a error "ETHERNET FRAME CHECK SEQUENCE INCORRECT" after asking for the device at 192.168.0.180( server device ip). i read before that this is normal when using wireshark. yet, after this, there's no connection open.</p><p>In conclusion, can someone explain how does packetsender works? i read that it uses mixed-Ascii.. but it shows the Hex values too. and i'm formatting the master device to output hex string too..</p><p>thank you!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-hex" rel="tag" title="see questions tagged &#39;hex&#39;">hex</span> <span class="post-tag tag-link-tcppackets" rel="tag" title="see questions tagged &#39;tcppackets&#39;">tcppackets</span> <span class="post-tag tag-link-ascii" rel="tag" title="see questions tagged &#39;ascii&#39;">ascii</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jan '16, 09:28</strong></p><img src="https://secure.gravatar.com/avatar/035068c392a65bca74db5ead0126438a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="geniodomal&#39;s gravatar image" /><p><span>geniodomal</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="geniodomal has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> closed <strong>07 Jan '16, 10:11</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-48949" class="comments-container"><span id="48950"></span><div id="comment-48950" class="comment"><div id="post-48950-score" class="comment-score"></div><div class="comment-text"><p>PacketSender is not part of the Wireshark suite, you'll have to look for support for it over at their <a href="https://packetsender.com/">site</a>.</p></div><div id="comment-48950-info" class="comment-info"><span class="comment-age">(07 Jan '16, 10:11)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-48949" class="comment-tools"></div><div class="clear"></div><div id="comment-48949-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by grahamb 07 Jan '16, 10:11

</div>

</div>

</div>

