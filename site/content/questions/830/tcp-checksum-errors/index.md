+++
type = "question"
title = "TCP Checksum errors"
description = '''Ok I read this wiki article Wireshark Wiki TCP checksum errors The checkbox was already deselected and yet I am still getting TCP packets with bad header checksums. Its always the TCP packets that are leaving my computer and not the ones coming in. is there another setting I am missing? Error looks ...'''
date = "2010-11-05T19:16:00Z"
lastmod = "2010-12-08T16:50:00Z"
weight = 830
keywords = [ "checksum", "errors", "tcp" ]
aliases = [ "/questions/830" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Checksum errors](/questions/830/tcp-checksum-errors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-830-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-830-score" class="post-score" title="current number of votes">0</div><span id="post-830-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Ok I read this wiki article</p><p><a href="http://wiki.wireshark.org/TCP_Checksum_Verification?highlight=%28Checksum%29">Wireshark Wiki TCP checksum errors</a></p><p>The checkbox was already deselected and yet I am still getting TCP packets with bad header checksums. Its always the TCP packets that are leaving my computer and not the ones coming in.</p><p>is there another setting I am missing?</p><p>Error looks like this</p><p>Header Checksum: 0X0000 [incorrect, should be 0xb2ae]</p><p>I gather this is TCP offloading as there is settings for this in my adapters configuration setups.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-checksum" rel="tag" title="see questions tagged &#39;checksum&#39;">checksum</span> <span class="post-tag tag-link-errors" rel="tag" title="see questions tagged &#39;errors&#39;">errors</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Nov '10, 19:16</strong></p><img src="https://secure.gravatar.com/avatar/c630ce01c9fcb9b76e90f8a0fd504880?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Treborprime&#39;s gravatar image" /><p><span>Treborprime</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Treborprime has no accepted answers">0%</span></p></div></div><div id="comments-container-830" class="comments-container"></div><div id="comment-tools-830" class="comment-tools"></div><div class="clear"></div><div id="comment-830-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="833"></span>

<div id="answer-container-833" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-833-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-833-score" class="post-score" title="current number of votes">0</div><span id="post-833-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The line "Header Checksum" is from the IP protocol details, not the TCP protocol details. So if checksums at the IP layer are calculated by the NIC as well (as can be indicated by the fact that every outgoing packet has a bad checksum), you need to disable checksumming in the IP protocol preferences too.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Nov '10, 03:28</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-833" class="comments-container"></div><div id="comment-tools-833" class="comment-tools"></div><div class="clear"></div><div id="comment-833-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1293"></span>

<div id="answer-container-1293" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1293-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1293-score" class="post-score" title="current number of votes">0</div><span id="post-1293-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Eric gave me your link on your HeaderChecksum. Got the same thing going here, Only mine are going out fine. It's what's coming in. Plus all Packets are Malformed and Errored or Warned. But here again the outgoing is fine. Plus many other server problems at my ISP. From their DNS, DHCP, and their Exchange Server. I don't think it could be possible their Routered relays are the problem. Took them 9 months just to get my contracted service speed (bandwidth) set right. Which literally amounted to turning a switch on. I can't imagine what getting this correct will take in an amount of time! I'm the Wireshark on PPPoE?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Dec '10, 16:50</strong></p><img src="https://secure.gravatar.com/avatar/5b11deb852a57a459c4fb39592d2fb02?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Algonquian_Cougar&#39;s gravatar image" /><p><span>Algonquian_C...</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Algonquian_Cougar has no accepted answers">0%</span></p></div></div><div id="comments-container-1293" class="comments-container"></div><div id="comment-tools-1293" class="comment-tools"></div><div class="clear"></div><div id="comment-1293-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

