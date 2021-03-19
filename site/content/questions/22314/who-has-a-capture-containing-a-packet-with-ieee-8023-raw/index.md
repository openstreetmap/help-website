+++
type = "question"
title = "Who has a capture containing a packet with IEEE 802.3 Raw?"
description = '''I need to get this type of frame. If somebody captures it, please, send it to me.'''
date = "2013-06-25T04:37:00Z"
lastmod = "2013-06-26T13:53:00Z"
weight = 22314
keywords = [ "capture", "802.3", "raw" ]
aliases = [ "/questions/22314" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Who has a capture containing a packet with IEEE 802.3 Raw?](/questions/22314/who-has-a-capture-containing-a-packet-with-ieee-8023-raw)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22314-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22314-score" class="post-score" title="current number of votes">0</div><span id="post-22314-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to get this type of frame. If somebody captures it, please, send it to me.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-802.3" rel="tag" title="see questions tagged &#39;802.3&#39;">802.3</span> <span class="post-tag tag-link-raw" rel="tag" title="see questions tagged &#39;raw&#39;">raw</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jun '13, 04:37</strong></p><img src="https://secure.gravatar.com/avatar/6ea9dee45098683ffc6bd92101d0cde5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DariaS&#39;s gravatar image" /><p><span>DariaS</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DariaS has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Jun '13, 05:30</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-22314" class="comments-container"><span id="22336"></span><div id="comment-22336" class="comment"><div id="post-22336-score" class="comment-score">1</div><div class="comment-text"><p>For those unfamiliar with it, "802.3 Raw" means "the really old mechanism Netware used to send Netware packets directly over 802.3 Ethernet, without an Ethernet type value and without an 802.2 header". You're unlikely to see that on a modern network. See <a href="http://www.ee.siue.edu/~bnoble/comp/networks/frametypes.html">Ethernet Frame Types: Don Provan's Definitive Answer</a> for more than you ever wanted to know about Ethernet frame types and the history thereof; the Wireshark term "IEEE 802.3 Raw" is "Ethernet_802.3" in Don's paper.</p><p>(Note also that current versions of IEEE 802.3 include both "Ethernet_II" and "Ethernet_802.2", to use Don's terminology.)</p></div><div id="comment-22336-info" class="comment-info"><span class="comment-age">(25 Jun '13, 18:17)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="22346"></span><div id="comment-22346" class="comment"><div id="post-22346-score" class="comment-score"></div><div class="comment-text"><p>I know that Raw can only carry IPX packets. And that Novell IPX isn't used in our days I know too. But may be somebody picked up the kernel of IPX protocol and got this type of packet. I caught it on Windows Server 2003. But it was only one packet and it's not enough for me.</p></div><div id="comment-22346-info" class="comment-info"><span class="comment-age">(26 Jun '13, 00:49)</span> <span class="comment-user userinfo">DariaS</span></div></div></div><div id="comment-tools-22314" class="comment-tools"></div><div class="clear"></div><div id="comment-22314-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22362"></span>

<div id="answer-container-22362" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22362-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22362-score" class="post-score" title="current number of votes">3</div><span id="post-22362-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I found one in the Wireshark menagerie, <code>ipx2.cap</code>, and uploaded it to cloudshark, since I'm not sure how to find out which bug it might have been attached to or which mailing it came from. It just contains EIGRP packets though, so I'm not sure how useful it will be to you. (Since it only contains EIGRP packets, I felt it was safe to upload it to cloudshark, since there's no real sensitive data in it, so I can be reasonably assured that it wasn't posted to a bug report and marked as private.)</p><p>You can view and/or download it from: <a href="http://cloudshark.org/captures/2b92f86afbd1">http://cloudshark.org/captures/2b92f86afbd1</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '13, 08:17</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-22362" class="comments-container"><span id="22374"></span><div id="comment-22374" class="comment"><div id="post-22374-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much. It's very usefull.</p></div><div id="comment-22374-info" class="comment-info"><span class="comment-age">(26 Jun '13, 13:53)</span> <span class="comment-user userinfo">DariaS</span></div></div></div><div id="comment-tools-22362" class="comment-tools"></div><div class="clear"></div><div id="comment-22362-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

