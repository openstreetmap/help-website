+++
type = "question"
title = "SSL decryption only works in promiscuous mode?"
description = '''With capture filter tcp port https I only seem to capture decrypted HTTP requests when promiscuous mode is enabled. Found the problem by accident and was wondering why this might be. '''
date = "2011-12-15T20:26:00Z"
lastmod = "2011-12-17T03:02:00Z"
weight = 8004
keywords = [ "ssl", "promiscuous", "troubleshooting", "https" ]
aliases = [ "/questions/8004" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [SSL decryption only works in promiscuous mode?](/questions/8004/ssl-decryption-only-works-in-promiscuous-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8004-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8004-score" class="post-score" title="current number of votes">0</div><span id="post-8004-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>With capture filter <code>tcp port https</code> I only seem to capture decrypted HTTP requests when promiscuous mode is enabled. Found the problem by accident and was wondering why this might be.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-promiscuous" rel="tag" title="see questions tagged &#39;promiscuous&#39;">promiscuous</span> <span class="post-tag tag-link-troubleshooting" rel="tag" title="see questions tagged &#39;troubleshooting&#39;">troubleshooting</span> <span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Dec '11, 20:26</strong></p><img src="https://secure.gravatar.com/avatar/22de692b5c4bba0665322370e0a98ae0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kcd&#39;s gravatar image" /><p><span>kcd</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kcd has no accepted answers">0%</span></p></div></div><div id="comments-container-8004" class="comments-container"></div><div id="comment-tools-8004" class="comment-tools"></div><div class="clear"></div><div id="comment-8004-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8027"></span>

<div id="answer-container-8027" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8027-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8027-score" class="post-score" title="current number of votes">0</div><span id="post-8027-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kcd has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It might be that you do not receive all HTTPS packets when promiscuous mode is not enabled. Or maybe you started the non-promiscuous trace without restarting the browser, which means you will see only reused ssl sessions, which do not contain the session-key exchange.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '11, 03:02</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-8027" class="comments-container"></div><div id="comment-tools-8027" class="comment-tools"></div><div class="clear"></div><div id="comment-8027-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

