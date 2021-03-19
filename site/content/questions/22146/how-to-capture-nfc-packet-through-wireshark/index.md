+++
type = "question"
title = "How to capture NFC packet through wireshark ?"
description = '''I want to capture NFC(near field communication) packet, which tool can be competent to do that?'''
date = "2013-06-18T23:04:00Z"
lastmod = "2013-06-22T02:33:00Z"
weight = 22146
keywords = [ "nfc", "wireshark" ]
aliases = [ "/questions/22146" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture NFC packet through wireshark ?](/questions/22146/how-to-capture-nfc-packet-through-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22146-score" class="post-score" title="current number of votes">0</div><span id="post-22146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to capture NFC(near field communication) packet, which tool can be competent to do that?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nfc" rel="tag" title="see questions tagged &#39;nfc&#39;">nfc</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jun '13, 23:04</strong></p><img src="https://secure.gravatar.com/avatar/f378a0d8809978a31afab288a17abb14?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TommyXu&#39;s gravatar image" /><p><span>TommyXu</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TommyXu has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Jun '13, 23:05</strong> </span></p></div></div><div id="comments-container-22146" class="comments-container"></div><div id="comment-tools-22146" class="comment-tools"></div><div class="clear"></div><div id="comment-22146-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22152"></span>

<div id="answer-container-22152" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22152-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22152-score" class="post-score" title="current number of votes">1</div><span id="post-22152-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is a NFC <strong>dissector</strong> plugin available at google code.</p><blockquote><p><code>http://code.google.com/p/wireshark-nfc/</code><br />
</p></blockquote><p>So, you will at least be able to <strong>dissect</strong> NFC traffic with Wireshark, <strong>if</strong> you are able to use that plugin with Wireshark (see the instructions on that site) <strong>and</strong> you have some hardware that is able to generate the NFC capture file (search google for: <strong>NFC protocol sniffer</strong>).</p><p>Regarding <strong>capturing</strong> NFC traffic with Wireshark.</p><p>This would require a NFC device that is supported by libpcap (Linux,etc.) or WinPcap (Windows). I'm not sure if such a device exists at the moment. I could not find anything with google.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '13, 05:06</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Jun '13, 05:06</strong> </span></p></div></div><div id="comments-container-22152" class="comments-container"><span id="22165"></span><div id="comment-22165" class="comment"><div id="post-22165-score" class="comment-score"></div><div class="comment-text"><p>Thank you for kindly help. I downloaded the NFC dissector plugin source code and built it on the Win8 plantform. But I don't known how to generate the NFC capture file. Is "NFC protocol sniffer" a hardware or a software?</p></div><div id="comment-22165-info" class="comment-info"><span class="comment-age">(19 Jun '13, 07:51)</span> <span class="comment-user userinfo">TommyXu</span></div></div><span id="22245"></span><div id="comment-22245" class="comment"><div id="post-22245-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Is "NFC protocol sniffer" a hardware or a software?</p></blockquote><p>mostly hardware</p></div><div id="comment-22245-info" class="comment-info"><span class="comment-age">(22 Jun '13, 02:33)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-22152" class="comment-tools"></div><div class="clear"></div><div id="comment-22152-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

