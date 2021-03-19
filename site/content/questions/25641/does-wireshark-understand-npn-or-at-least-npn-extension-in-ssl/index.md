+++
type = "question"
title = "Does Wireshark understand NPN (or at least NPN extension in SSL)"
description = '''I am using wireshark 1.6.7 on windowx XP. It does not seem to understand if the SSL client sends NPN (next protocol negotiation) extension. I tried to run on centos 1.2.15 with the same result. I have googled but it is not clear from the documentation if NPN is recognized or if some patch needs to b...'''
date = "2013-10-04T06:22:00Z"
lastmod = "2013-10-04T06:49:00Z"
weight = 25641
keywords = [ "npn" ]
aliases = [ "/questions/25641" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Does Wireshark understand NPN (or at least NPN extension in SSL)](/questions/25641/does-wireshark-understand-npn-or-at-least-npn-extension-in-ssl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25641-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25641-score" class="post-score" title="current number of votes">0</div><span id="post-25641-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using wireshark 1.6.7 on windowx XP. It does not seem to understand if the SSL client sends NPN (next protocol negotiation) extension. I tried to run on centos 1.2.15 with the same result. I have googled but it is not clear from the documentation if NPN is recognized or if some patch needs to be applied Thanks for any answers</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-npn" rel="tag" title="see questions tagged &#39;npn&#39;">npn</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Oct '13, 06:22</strong></p><img src="https://secure.gravatar.com/avatar/95763e65fd1ff9f48963e8973d054db9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rv%20Rv&#39;s gravatar image" /><p><span>Rv Rv</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rv Rv has no accepted answers">0%</span></p></div></div><div id="comments-container-25641" class="comments-container"></div><div id="comment-tools-25641" class="comment-tools"></div><div class="clear"></div><div id="comment-25641-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="25642"></span>

<div id="answer-container-25642" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25642-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25642-score" class="post-score" title="current number of votes">1</div><span id="post-25642-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Rv Rv has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>1.6.7 is pretty old by now - have you tried the latest builds? Maybe they do support those extensions now. 1.2 is even older, so if you can, get 1.10, or compile it yourself if there is no package.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Oct '13, 06:28</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-25642" class="comments-container"></div><div id="comment-tools-25642" class="comment-tools"></div><div class="clear"></div><div id="comment-25642-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25643"></span>

<div id="answer-container-25643" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25643-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25643-score" class="post-score" title="current number of votes">1</div><span id="post-25643-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is support for NPN:</p><pre><code>static gint dissect_ssl3_hnd_hello_ext_npn(tvbuff_t *tvb,
                                       proto_tree *tree, guint32 offset, guint32 ext_len);</code></pre><p>(from epan/dissectors/packet-ssl.c)</p><p>Checking <a href="http://www.wireshark.org/docs/dfref/s/ssl.html">"Display Filter Reference: Secure Sockets Layer"</a> gives:</p><pre><code>ssl.handshake.extensions_npn    Next Protocol   Character string    1.8.0 to 1.10.2</code></pre><p>So it has been supported since 1.8.0. Please upgrade wireshark or compile a recent version yourself if not available for your distro.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Oct '13, 06:49</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-25643" class="comments-container"></div><div id="comment-tools-25643" class="comment-tools"></div><div class="clear"></div><div id="comment-25643-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

