+++
type = "question"
title = "The license of source in the Wireshark Wiki"
description = '''According to the comments of packet-rlc-lte.h in the https://wiki.wireshark.org/RLC-LTE, license, is written with the GPL.  However, it is on the same site, the comment of (BSD-licensed) Example program (rlc_lte_logger.c) is, &quot;This header file may also be distributed under the terms of the BSD Licen...'''
date = "2015-05-26T07:14:00Z"
lastmod = "2015-05-28T08:51:00Z"
weight = 42663
keywords = [ "license" ]
aliases = [ "/questions/42663" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [The license of source in the Wireshark Wiki](/questions/42663/the-license-of-source-in-the-wireshark-wiki)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42663-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42663-score" class="post-score" title="current number of votes">0</div><span id="post-42663-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>According to the comments of packet-rlc-lte.h in the <a href="https://wiki.wireshark.org/RLC-LTE,">https://wiki.wireshark.org/RLC-LTE,</a> license, is written with the GPL. However, it is on the same site, the comment of (BSD-licensed) Example program (rlc_lte_logger.c) is, "This header file may also be distributed under the terms of the BSD Licence" It is with.</p><p>Which will be the license of packet-rlc-lte.h?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-license" rel="tag" title="see questions tagged &#39;license&#39;">license</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 May '15, 07:14</strong></p><img src="https://secure.gravatar.com/avatar/a63d3b40bdcf5d86630b593ec9eb81ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dark&#39;s gravatar image" /><p><span>dark</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dark has no accepted answers">0%</span></p></div></div><div id="comments-container-42663" class="comments-container"></div><div id="comment-tools-42663" class="comment-tools"></div><div class="clear"></div><div id="comment-42663-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42676"></span>

<div id="answer-container-42676" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42676-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42676-score" class="post-score" title="current number of votes">0</div><span id="post-42676-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Which will be the license of packet-rlc-lte.h?</p></blockquote><p>packet-rlc-lte.h and packet-rlc-lte.c use GPL licensing, as stated in the files themselves. rlc_lte_logger.c is a tool, which is linked in the Wiki, but not distributed with the Wireshark code, and its license is BSD, as stated in the file itself.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 May '15, 14:02</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-42676" class="comments-container"><span id="42699"></span><div id="comment-42699" class="comment"><div id="post-42699-score" class="comment-score"></div><div class="comment-text"><p>The rlc_lte_logger.c, it is written with "This header file may also be distributed under the terms of the BSD Licence".</p><p>If the license of packet-rlc-lte.h is GPL, the idea of the next, correct?. I download a packet-rlc-lte.h from Wiki. The licenses of software using only revised packet-rlc-lte.h is GPL.</p></div><div id="comment-42699-info" class="comment-info"><span class="comment-age">(27 May '15, 07:09)</span> <span class="comment-user userinfo">dark</span></div></div><span id="42709"></span><div id="comment-42709" class="comment"><div id="post-42709-score" class="comment-score"></div><div class="comment-text"><p>What are you trying to do? What's the difference if you are using that code with GPL or BSD license?</p></div><div id="comment-42709-info" class="comment-info"><span class="comment-age">(27 May '15, 09:54)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="42726"></span><div id="comment-42726" class="comment"><div id="post-42726-score" class="comment-score"></div><div class="comment-text"><p>Use A UDP framing format for RLC-LTE defined in the packet-rlc-lte.h, if made software for outputting a file pcap format, I worry whether a license of the software becomes GPL. Is there the method without packet-rlc-lte.h?</p></div><div id="comment-42726-info" class="comment-info"><span class="comment-age">(28 May '15, 04:46)</span> <span class="comment-user userinfo">dark</span></div></div><span id="42731"></span><div id="comment-42731" class="comment"><div id="post-42731-score" class="comment-score"></div><div class="comment-text"><p>Richard Stallman's view about using GPL header files is this:</p><blockquote><p><a href="http://lkml.iu.edu/hypermail/linux/kernel/0301.1/0362.html">http://lkml.iu.edu/hypermail/linux/kernel/0301.1/0362.html</a></p></blockquote><p>Cite:</p><blockquote><p>using structure definitions, typedefs, enumeration constants, macros with simple bodies, etc., is NOT enough to make a derivative work.</p></blockquote><p>See also here:</p><blockquote><p><a href="http://elinux.org/Legal_Issues">http://elinux.org/Legal_Issues</a></p></blockquote><p>As the header file of packet-rlc-lte.h contains no "code" at all, your program should not fall under GPL. If you want confirmation, please consult a lawyer.</p><p>Regards Kurt</p></div><div id="comment-42731-info" class="comment-info"><span class="comment-age">(28 May '15, 06:16)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="42733"></span><div id="comment-42733" class="comment"><div id="post-42733-score" class="comment-score"></div><div class="comment-text"><p>FWIW I had the same view as Kurt/Richard when I first added the header file + BSD example logging code to work with the LTE MAC dissector - that people should be able to include the header file in non-GPL code if they wanted to.</p></div><div id="comment-42733-info" class="comment-info"><span class="comment-age">(28 May '15, 08:51)</span> <span class="comment-user userinfo">MartinM</span></div></div></div><div id="comment-tools-42676" class="comment-tools"></div><div class="clear"></div><div id="comment-42676-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

