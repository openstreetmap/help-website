+++
type = "question"
title = "could you tell me how to dissect fp over udp？"
description = '''could you tell me how to dissect fp over udp？ Gr.'''
date = "2012-07-03T01:11:00Z"
lastmod = "2012-07-03T22:28:00Z"
weight = 12388
keywords = [ "fp", "over", "udp" ]
aliases = [ "/questions/12388" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [could you tell me how to dissect fp over udp？](/questions/12388/could-you-tell-me-how-to-dissect-fp-over-udp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12388-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12388-score" class="post-score" title="current number of votes">1</div><span id="post-12388-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>could you tell me how to dissect fp over udp？ Gr.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fp" rel="tag" title="see questions tagged &#39;fp&#39;">fp</span> <span class="post-tag tag-link-over" rel="tag" title="see questions tagged &#39;over&#39;">over</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jul '12, 01:11</strong></p><img src="https://secure.gravatar.com/avatar/f6eeed42d5aadabfed2ca2cb1faabff1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smilezuzu&#39;s gravatar image" /><p><span>smilezuzu</span><br />
<span class="score" title="20 reputation points">20</span><span title="32 badges"><span class="badge1">●</span><span class="badgecount">32</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smilezuzu has no accepted answers">0%</span></p></div></div><div id="comments-container-12388" class="comments-container"></div><div id="comment-tools-12388" class="comment-tools"></div><div class="clear"></div><div id="comment-12388-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12430"></span>

<div id="answer-container-12430" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12430-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12430-score" class="post-score" title="current number of votes">1</div><span id="post-12430-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can't dissect FP over UDP and the higer layers without prior knowledge of the content/Configuration hence the FP dissector requires a "per-packet" structure to be filed in in order to do the dissection. The NBAP dissectore has code to set up a conversation and fill parts of the required information should NBAP signaling be present in the trace(Work in progress). There is provissions for a pseudo UDP FP format should your equipment be able to produce it. See the wireshark wiki and simmilar questions asked before. The FP-hint dissector also handles some pseudo format. It might be possible to constuct a heuristic FP dissector but it might requre "three-pass" dissection. 1) Use the header CRC to confirm FP packet. 1b)Use the command code to find the channel type. If it's not a DCH channel there might be enough information to dissect the rest of the packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jul '12, 22:28</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-12430" class="comments-container"></div><div id="comment-tools-12430" class="comment-tools"></div><div class="clear"></div><div id="comment-12430-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

