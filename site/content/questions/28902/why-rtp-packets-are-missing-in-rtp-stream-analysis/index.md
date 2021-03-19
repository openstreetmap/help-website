+++
type = "question"
title = "Why RTP Packets are missing in RTP Stream Analysis"
description = '''Why all RTP Packets dont show up in RTP Analysis Stream window? Since RTP uses UDP, Can we consider UDP packets as RTP Packets? '''
date = "2014-01-15T03:52:00Z"
lastmod = "2014-01-16T21:43:00Z"
weight = 28902
keywords = [ "rtp" ]
aliases = [ "/questions/28902" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Why RTP Packets are missing in RTP Stream Analysis](/questions/28902/why-rtp-packets-are-missing-in-rtp-stream-analysis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28902-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Why all RTP Packets dont show up in RTP Analysis Stream window?</p><p>Since RTP uses UDP, Can we consider UDP packets as RTP Packets?</p></div><div id="question-tags" class="tags-container tags">rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jan '14, 03:52</strong></p><img src="https://secure.gravatar.com/avatar/f06f6b3ad79b8afedef1058c188cc863?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lte007&#39;s gravatar image" /><p>lte007<br />
<span class="score" title="41 reputation points">41</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lte007 has one accepted answer">100%</span></p></div></div><div id="comments-container-28902" class="comments-container"></div><div id="comment-tools-28902" class="comment-tools"></div><div class="clear"></div><div id="comment-28902-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="28981"></span>

<div id="answer-container-28981" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28981-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please dont worry about it...i figured out the problem... While analyzing wireshark considers 1 source &amp; 1 destination at a time...thanks for the comments though...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jan '14, 21:43</strong></p><img src="https://secure.gravatar.com/avatar/f06f6b3ad79b8afedef1058c188cc863?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lte007&#39;s gravatar image" /><p>lte007<br />
<span class="score" title="41 reputation points">41</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lte007 has one accepted answer">100%</span></p></div></div><div id="comments-container-28981" class="comments-container"></div><div id="comment-tools-28981" class="comment-tools"></div><div class="clear"></div><div id="comment-28981-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28903"></span>

<div id="answer-container-28903" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28903-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not sure what the question is. If the packet's are not identified as RT the will not turn up in RTP Analysis obviously. If you know which UDP packets that are RTP you can do "decode as" or you could try the RTP preference "Try to decode RTP outside of conversations".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jan '14, 04:02</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-28903" class="comments-container"><span id="28946"></span><div id="comment-28946" class="comment"><div id="post-28946-score" class="comment-score"></div><div class="comment-text"><p>thanks Anders, can i have your email-id please. would send you a screenshot as i am not able to upload here....</p></div><div id="comment-28946-info" class="comment-info"><span class="comment-age">(15 Jan '14, 21:53)</span> lte007</div></div><span id="28949"></span><div id="comment-28949" class="comment"><div id="post-28949-score" class="comment-score"></div><div class="comment-text"><p>thanks Anders, can i have your email-id please. would send you a screenshot as i am not able to upload here....</p></div><div id="comment-28949-info" class="comment-info"><span class="comment-age">(15 Jan '14, 23:43)</span> lte007</div></div><span id="28956"></span><div id="comment-28956" class="comment"><div id="post-28956-score" class="comment-score"></div><div class="comment-text"><p>Folks such as @Anders provide helpful answers on the site, not via a personal consultation using email.</p><p>The image posting restrictions are unfortunately down to the behaviour of the bottom-feeding spammers. You can post your image elsewhere and hopefully provide a link back here (if that isn't also blocked).</p><p>Another option (that is much easier for folks to help you with) is to post the capture somewhere (e.g. <a href="http://cloudshark.org">Cloudshark</a>) and then post the link here of the capture. This method is only suitable if the capture doesn't contain confidential information.</p></div><div id="comment-28956-info" class="comment-info"><span class="comment-age">(16 Jan '14, 02:07)</span> grahamb ♦</div></div><span id="28959"></span><div id="comment-28959" class="comment"><div id="post-28959-score" class="comment-score"></div><div class="comment-text"><blockquote><p>The image posting restrictions are unfortunately down to</p></blockquote><p>Do you know if those restrictions are related to the number of karma points?</p></div><div id="comment-28959-info" class="comment-info"><span class="comment-age">(16 Jan '14, 02:26)</span> Kurt Knochner ♦</div></div><span id="28960"></span><div id="comment-28960" class="comment"><div id="post-28960-score" class="comment-score"></div><div class="comment-text"><p>I would guess so, so that no-one can immediately register, post a question or comment and add spam to it.</p></div><div id="comment-28960-info" class="comment-info"><span class="comment-age">(16 Jan '14, 02:53)</span> grahamb ♦</div></div><span id="28961"></span><div id="comment-28961" class="comment not_top_scorer"><div id="post-28961-score" class="comment-score"></div><div class="comment-text"><p>O.K.</p><p>@lte007, please try again to post the screenshot.</p></div><div id="comment-28961-info" class="comment-info"><span class="comment-age">(16 Jan '14, 02:59)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-28903" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-28903-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

