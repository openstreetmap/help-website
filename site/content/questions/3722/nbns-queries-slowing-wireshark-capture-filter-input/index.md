+++
type = "question"
title = "NBNS queries slowing Wireshark capture filter input"
description = '''I wondered why Wireshark (I run 1.5 SVN Rev 35637) always stopped after the first octet (and usually after each other octet as well) whenever I entered a capture filter starting like &quot;host 192.168.0.1&quot;, so I captured my PC with a second Wireshark while entering the filter in the first.  What I found...'''
date = "2011-04-26T10:24:00Z"
lastmod = "2011-04-27T09:04:00Z"
weight = 3722
keywords = [ "capture-filter", "nbns", "wireshark" ]
aliases = [ "/questions/3722" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [NBNS queries slowing Wireshark capture filter input](/questions/3722/nbns-queries-slowing-wireshark-capture-filter-input)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3722-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I wondered why Wireshark (I run 1.5 SVN Rev 35637) always stopped after the first octet (and usually after each other octet as well) whenever I entered a capture filter starting like "host 192.168.0.1", so I captured my PC with a second Wireshark while entering the filter in the first.</p><p>What I found was, that my PC (running Win7x64) tried to do a NBNS query for "192&lt;00&gt;", then another for "192.168&lt;00&gt;", then "192.168.0&lt;00&gt;" and finally "192.168.0.1&lt;00&gt;". Each query was repeated at least twice (with no answer coming in), taking about 800ms per try.</p><p>My question is: why does Wireshark do that, and what is THIS good for? It is really really annoying :-)</p></div><div id="question-tags" class="tags-container tags">capture-filter nbns wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Apr '11, 10:24</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-3722" class="comments-container"></div><div id="comment-tools-3722" class="comment-tools"></div><div class="clear"></div><div id="comment-3722-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3750"></span>

<div id="answer-container-3750" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3750-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That is due to the "capture filter syntax checking" that was introduced (by me actually). It is listed as <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5356">bug 5356</a> on bugzilla and needs to be fixed :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '11, 09:04</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-3750" class="comments-container"><span id="3751"></span><div id="comment-3751" class="comment"><div id="post-3751-score" class="comment-score"></div><div class="comment-text"><p>Thanks, good to know :-)</p></div><div id="comment-3751-info" class="comment-info"><span class="comment-age">(27 Apr '11, 09:06)</span> Jasper ♦♦</div></div></div><div id="comment-tools-3750" class="comment-tools"></div><div class="clear"></div><div id="comment-3750-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

