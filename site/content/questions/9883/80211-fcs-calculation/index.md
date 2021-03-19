+++
type = "question"
title = "802.11 FCS calculation"
description = '''Hi, Im trying to understand how 802.11 calculates the FCS. Im using scapy to build and dissect packets quickly and easily however the FCS field of 802.11 packet is not calculated automatically when building an 802.11 packet. The Dot11Wep packet calculates the IC -WEP specific IC- however there is a ...'''
date = "2012-04-01T04:44:00Z"
lastmod = "2012-04-01T21:33:00Z"
weight = 9883
keywords = [ "wep", "802.11", "fcs" ]
aliases = [ "/questions/9883" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [802.11 FCS calculation](/questions/9883/80211-fcs-calculation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9883-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9883-score" class="post-score" title="current number of votes">0</div><span id="post-9883-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Im trying to understand how 802.11 calculates the FCS. Im using scapy to build and dissect packets quickly and easily however the FCS field of 802.11 packet is not calculated automatically when building an 802.11 packet. The Dot11Wep packet calculates the IC -WEP specific IC- however there is a second redundancy check that is supposed to check the entire 802.11 packet including the wep data. As i understand it (incorrectly i might add) the FCS is CRC32 of the entire 802.11 packet however when I try this in scapy/python the answer differs from a packet that has been captured and analysed by wireshark to be "correct". How then is the FCS calculated? Cheers</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wep" rel="tag" title="see questions tagged &#39;wep&#39;">wep</span> <span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span> <span class="post-tag tag-link-fcs" rel="tag" title="see questions tagged &#39;fcs&#39;">fcs</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '12, 04:44</strong></p><img src="https://secure.gravatar.com/avatar/0faa0c8892005c5568ef0f82ef2505f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="keiza&#39;s gravatar image" /><p><span>keiza</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="keiza has no accepted answers">0%</span></p></div></div><div id="comments-container-9883" class="comments-container"></div><div id="comment-tools-9883" class="comment-tools"></div><div class="clear"></div><div id="comment-9883-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9890"></span>

<div id="answer-container-9890" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9890-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9890-score" class="post-score" title="current number of votes">1</div><span id="post-9890-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cmaynard has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The best way to find out how Wireshark calculates the FCS is to examine the source code. Try searching for <code>crc32_802_tvb</code> in the <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/dissectors/packet-ieee80211.c?revision=41645&amp;view=markup">IEEE 802.11</a> dissector. The calculation varies depending upon whether there's padding or not. The <code>crc32_802_tvb</code> function is implemented in the <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/crc32-tvb.c?revision=41523&amp;view=markup">crc32-tvb.c</a> file, and the <code>crc32_802_tvb_padded</code> is implemented within the IEEE 802.11 dissector itself.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Apr '12, 17:34</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-9890" class="comments-container"><span id="9893"></span><div id="comment-9893" class="comment"><div id="post-9893-score" class="comment-score"></div><div class="comment-text"><p>Wow, Thanks so much for your prompt reply and your helpful suggestions!</p></div><div id="comment-9893-info" class="comment-info"><span class="comment-age">(01 Apr '12, 21:33)</span> <span class="comment-user userinfo">keiza</span></div></div></div><div id="comment-tools-9890" class="comment-tools"></div><div class="clear"></div><div id="comment-9890-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

