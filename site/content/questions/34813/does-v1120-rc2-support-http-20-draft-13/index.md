+++
type = "question"
title = "Does v.1.12.0-rc2 support HTTP 2.0 draft-13 ?"
description = '''I saw wireshark already supported HTTP 2.0 draft-13. https://github.com/http2/http2-spec/wiki/Implementations But when I use v.1.12.0-rc2(newest development version), it got http 2.0 package and still prompt it&#x27;s a HTTP 2.0 draft-12 packet. I&#x27;m sure it&#x27;s a draft-13 packet. So what&#x27;s wrong with it ?'''
date = "2014-07-22T02:17:00Z"
lastmod = "2014-07-22T03:21:00Z"
weight = 34813
keywords = [ "http2.0" ]
aliases = [ "/questions/34813" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Does v.1.12.0-rc2 support HTTP 2.0 draft-13 ?](/questions/34813/does-v1120-rc2-support-http-20-draft-13)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34813-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I saw wireshark already supported HTTP 2.0 draft-13. <a href="https://github.com/http2/http2-spec/wiki/Implementations">https://github.com/http2/http2-spec/wiki/Implementations</a></p><p>But when I use v.1.12.0-rc2(newest development version), it got http 2.0 package and still prompt it's a HTTP 2.0 draft-12 packet. I'm sure it's a draft-13 packet. So what's wrong with it ?</p></div><div id="question-tags" class="tags-container tags">http2.0</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jul '14, 02:17</strong></p><img src="https://secure.gravatar.com/avatar/d12bdddc21f4634e4f56dd2e30fa4154?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="faramita10&#39;s gravatar image" /><p>faramita10<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="faramita10 has no accepted answers">0%</span></p></div></div><div id="comments-container-34813" class="comments-container"></div><div id="comment-tools-34813" class="comment-tools"></div><div class="clear"></div><div id="comment-34813-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34817"></span>

<div id="answer-container-34817" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34817-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The change for draft-13 was committed to the master branch on Jul 8 2014, and then backported to the 1.12 branch on Jul 11. This means that it isn't in the rc2 build (created on Jun 13). You'll need to either download one of the <a href="http://www.wireshark.org/download/automated/">automated builds</a> that are produced from master dated later than Jul 8, or build yourself from source, or wait until rc3 is built.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '14, 03:21</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-34817" class="comments-container"><span id="34821"></span><div id="comment-34821" class="comment"><div id="post-34821-score" class="comment-score"></div><div class="comment-text"><p>You gave me a big help. I love you!</p></div><div id="comment-34821-info" class="comment-info"><span class="comment-age">(22 Jul '14, 04:02)</span> faramita10</div></div><span id="34823"></span><div id="comment-34823" class="comment"><div id="post-34823-score" class="comment-score"></div><div class="comment-text"><p>You're welcome ;-)</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-34823-info" class="comment-info"><span class="comment-age">(22 Jul '14, 04:34)</span> grahamb ♦</div></div></div><div id="comment-tools-34817" class="comment-tools"></div><div class="clear"></div><div id="comment-34817-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

