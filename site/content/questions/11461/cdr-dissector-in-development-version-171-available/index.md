+++
type = "question"
title = "CDR dissector in development version 1.7.1, available?"
description = '''Could anyone please let me know how to decode a CDR in ASN.1 BER format using wireshark?'''
date = "2012-05-29T22:47:00Z"
lastmod = "2012-05-30T07:25:00Z"
weight = 11461
keywords = [ "gtp-prime" ]
aliases = [ "/questions/11461" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [CDR dissector in development version 1.7.1, available?](/questions/11461/cdr-dissector-in-development-version-171-available)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11461-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11461-score" class="post-score" title="current number of votes">0</div><span id="post-11461-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Could anyone please let me know how to decode a CDR in ASN.1 BER format using wireshark?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gtp-prime" rel="tag" title="see questions tagged &#39;gtp-prime&#39;">gtp-prime</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 May '12, 22:47</strong></p><img src="https://secure.gravatar.com/avatar/3049b0591ff8c37f5897da12d3eceb35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nanzone&#39;s gravatar image" /><p><span>nanzone</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nanzone has no accepted answers">0%</span></p></div></div><div id="comments-container-11461" class="comments-container"><span id="11466"></span><div id="comment-11466" class="comment"><div id="post-11466-score" class="comment-score"></div><div class="comment-text"><p>CDR being what?</p></div><div id="comment-11466-info" class="comment-info"><span class="comment-age">(30 May '12, 00:36)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="11467"></span><div id="comment-11467" class="comment"><div id="post-11467-score" class="comment-score"></div><div class="comment-text"><p>call data record used in GTP prime protocol message DRT</p></div><div id="comment-11467-info" class="comment-info"><span class="comment-age">(30 May '12, 00:38)</span> <span class="comment-user userinfo">nanzone</span></div></div></div><div id="comment-tools-11461" class="comment-tools"></div><div class="clear"></div><div id="comment-11461-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11473"></span>

<div id="answer-container-11473" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11473-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11473-score" class="post-score" title="current number of votes">0</div><span id="post-11473-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark's GTP dissector handles CDRs in BER format since 1.6 (the 1.4 versions do not). If you're using 1.6.x and the CDR is not decoded, try the latest development version (1.7.1). If that also does not work, I'd suggest you open a <a href="https://bugs.wireshark.org">bug report</a> with a sample capture so that support for it can be added (or fixed).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 May '12, 07:25</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-11473" class="comments-container"></div><div id="comment-tools-11473" class="comment-tools"></div><div class="clear"></div><div id="comment-11473-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

