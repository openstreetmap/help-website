+++
type = "question"
title = "Who has a pcap file with RARP-reply packet?"
description = '''I try to find it, but I can&#x27;t. There is only RARP-request.'''
date = "2013-12-05T05:11:00Z"
lastmod = "2013-12-06T04:56:00Z"
weight = 27804
keywords = [ "rarp" ]
aliases = [ "/questions/27804" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Who has a pcap file with RARP-reply packet?](/questions/27804/who-has-a-pcap-file-with-rarp-reply-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27804-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27804-score" class="post-score" title="current number of votes">0</div><span id="post-27804-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I try to find it, but I can't. There is only RARP-request.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rarp" rel="tag" title="see questions tagged &#39;rarp&#39;">rarp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '13, 05:11</strong></p><img src="https://secure.gravatar.com/avatar/6ea9dee45098683ffc6bd92101d0cde5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DariaS&#39;s gravatar image" /><p><span>DariaS</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DariaS has no accepted answers">0%</span></p></div></div><div id="comments-container-27804" class="comments-container"></div><div id="comment-tools-27804" class="comment-tools"></div><div class="clear"></div><div id="comment-27804-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27820"></span>

<div id="answer-container-27820" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27820-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27820-score" class="post-score" title="current number of votes">0</div><span id="post-27820-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Here we go</p><blockquote><p><a href="http://cloudshark.org/captures/c6729d0fc558">http://cloudshark.org/captures/c6729d0fc558</a></p></blockquote><p>As I did not have such a capture file and no working rarp daemon, I created the file with a Hex editor, according to <a href="http://www.ietf.org/rfc/rfc903.txt">RFC 903</a>. It should be correct, at least Wireshark shows the reply correctly ;-)) Have fun!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '13, 08:13</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Dec '13, 05:04</strong> </span></p></div></div><div id="comments-container-27820" class="comments-container"><span id="27858"></span><div id="comment-27858" class="comment"><div id="post-27858-score" class="comment-score"></div><div class="comment-text"><p>Kurt, thank u very much for this file. But the reverse-ARP protocol in std of Ethernet II has code 0x8035. In your pcap it's ARP proto with needed opcode.</p></div><div id="comment-27858-info" class="comment-info"><span class="comment-age">(06 Dec '13, 04:42)</span> <span class="comment-user userinfo">DariaS</span></div></div><span id="27863"></span><div id="comment-27863" class="comment"><div id="post-27863-score" class="comment-score"></div><div class="comment-text"><p>Try this: <a href="http://cloudshark.org/captures/085306acbc43">http://cloudshark.org/captures/085306acbc43</a></p><p>I just used a hex editor to replace 0x0800 with 0x8035. Seems to work in Wireshark and Cloudshark</p></div><div id="comment-27863-info" class="comment-info"><span class="comment-age">(06 Dec '13, 04:51)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="27864"></span><div id="comment-27864" class="comment"><div id="post-27864-score" class="comment-score"></div><div class="comment-text"><p>Good find! You're right, I overlooked that, because the Wireshark ARP dissector registers both for ARP and RARP and thus it shows the frame correctly, even with the 'wrong' ethertype.</p><p>Anyway, I fixed the ethertype and edited my answer. The cloudshark link points to the corrected file now.</p><p>EDIT: <span></span><span>@Jasper</span> was a few minutes faster in starting the Hex editor :-))</p></div><div id="comment-27864-info" class="comment-info"><span class="comment-age">(06 Dec '13, 04:56)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-27820" class="comment-tools"></div><div class="clear"></div><div id="comment-27820-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

