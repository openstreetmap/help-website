+++
type = "question"
title = "CAP session"
description = '''Dear All, how to delimite a complete CAP seesion in a given .pcap file ? i wanna see all sequences since the beggining to the end for a given MSISDN. thank you. mohamed'''
date = "2012-01-02T10:16:00Z"
lastmod = "2012-01-03T02:46:00Z"
weight = 8192
keywords = [ "capture-filter" ]
aliases = [ "/questions/8192" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [CAP session](/questions/8192/cap-session)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8192-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8192-score" class="post-score" title="current number of votes">0</div><span id="post-8192-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear All,</p><p>how to delimite a complete CAP seesion in a given .pcap file ?</p><p>i wanna see all sequences since the beggining to the end for a given MSISDN.</p><p>thank you. mohamed</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jan '12, 10:16</strong></p><img src="https://secure.gravatar.com/avatar/de613821f3a6e82e3760b1beeb4d9918?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mzakour&#39;s gravatar image" /><p><span>mzakour</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mzakour has no accepted answers">0%</span></p></div></div><div id="comments-container-8192" class="comments-container"><span id="8195"></span><div id="comment-8195" class="comment"><div id="post-8195-score" class="comment-score"></div><div class="comment-text"><p>in other terms:</p><p>i wanna know how to identify packets related for a complete call flow.</p></div><div id="comment-8195-info" class="comment-info"><span class="comment-age">(02 Jan '12, 11:36)</span> <span class="comment-user userinfo">mzakour</span></div></div></div><div id="comment-tools-8192" class="comment-tools"></div><div class="clear"></div><div id="comment-8192-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8200"></span>

<div id="answer-container-8200" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8200-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8200-score" class="post-score" title="current number of votes">0</div><span id="post-8200-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>After finding the CAP message with the calling or called party number use the TCAP transaction Id(s) to fileter out the sequence.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '12, 22:54</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-8200" class="comments-container"><span id="8204"></span><div id="comment-8204" class="comment"><div id="post-8204-score" class="comment-score"></div><div class="comment-text"><p>Dear Anders,</p><p>thank you for your feedback, i located the initDPGPRS() in the trace, it's the first packet sent to create pdp, i took the tcap transaction id and filter, but i founded only packets related to pdp create. how to check if there is packet lost ?</p></div><div id="comment-8204-info" class="comment-info"><span class="comment-age">(03 Jan '12, 02:46)</span> <span class="comment-user userinfo">mzakour</span></div></div></div><div id="comment-tools-8200" class="comment-tools"></div><div class="clear"></div><div id="comment-8200-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

