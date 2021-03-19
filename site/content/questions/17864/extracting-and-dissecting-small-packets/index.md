+++
type = "question"
title = "Extracting and dissecting small packets"
description = '''Hi Forum I am writing a protocol dissector. The protocol data packets are small and always prefixed with a message length. Multiple messages are contained inside one TCP packet. To date I have process the tvb buffer and called tvb_new_subset with the length and offset to -1 and processed the new pac...'''
date = "2013-01-22T11:54:00Z"
lastmod = "2013-01-22T13:39:00Z"
weight = 17864
keywords = [ "disecctor", "help" ]
aliases = [ "/questions/17864" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Extracting and dissecting small packets](/questions/17864/extracting-and-dissecting-small-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17864-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17864-score" class="post-score" title="current number of votes">0</div><span id="post-17864-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Forum</p><p>I am writing a protocol dissector. The protocol data packets are small and always prefixed with a message length. Multiple messages are contained inside one TCP packet.</p><p>To date I have process the tvb buffer and called tvb_new_subset with the length and offset to -1 and processed the new packet. But this leads me to a problem is the message length (currently unused in my approach) is actually greater than the fields I am aware of in the packet I end up starting thinking I have a new message before I have consumed all the previous packet.<br />
</p><p>Is there a way I can read n bytes from main tvb buffer into a tmp tvb for processing and continue using the tvb_new_subset to recursively continue processing the messages.</p><p>If there an example protocol I could look at for achieving this?</p><p>Thanks</p><p>Stuart</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-disecctor" rel="tag" title="see questions tagged &#39;disecctor&#39;">disecctor</span> <span class="post-tag tag-link-help" rel="tag" title="see questions tagged &#39;help&#39;">help</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jan '13, 11:54</strong></p><img src="https://secure.gravatar.com/avatar/e12bbe1b488f2a19cdf565465e260d19?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="StuieNorris&#39;s gravatar image" /><p><span>StuieNorris</span><br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="StuieNorris has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-17864" class="comments-container"></div><div id="comment-tools-17864" class="comment-tools"></div><div class="clear"></div><div id="comment-17864-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17868"></span>

<div id="answer-container-17868" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17868-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17868-score" class="post-score" title="current number of votes">1</div><span id="post-17868-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at "<code>tcp_dissect_pdus()</code>" (see also paragraph 2.7.1 in <a href="http://anonsvn.wireshark.org/viewvc/trunk/doc/README.developer?revision=46847&amp;view=markup">doc/README.developer</a>). It might be just the thing you're looking for.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '13, 13:39</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-17868" class="comments-container"></div><div id="comment-tools-17868" class="comment-tools"></div><div class="clear"></div><div id="comment-17868-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

