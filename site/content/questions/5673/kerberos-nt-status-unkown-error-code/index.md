+++
type = "question"
title = "Kerberos - NT Status: Unkown error code?"
description = '''I&#x27;m trying to diagnose a potential Active Directory authentication issue and, in the AS reply packet there seems to be a possible issue in the pre-authentication part. If I expand padata and expand PA-PW-SALT, I see a value string. If I expand that, I see NT Status: Unknown (0x41495341), Unknown: 0x...'''
date = "2011-08-12T01:55:00Z"
lastmod = "2011-08-12T08:12:00Z"
weight = 5673
keywords = [ "as-rep", "krb5", "kerberos", "kerb" ]
aliases = [ "/questions/5673" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Kerberos - NT Status: Unkown error code?](/questions/5673/kerberos-nt-status-unkown-error-code)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5673-score" class="post-score" title="current number of votes">0</div><span id="post-5673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to diagnose a potential Active Directory authentication issue and, in the AS reply packet there seems to be a possible issue in the pre-authentication part. If I expand padata and expand PA-PW-SALT, I see a value string. If I expand that, I see NT Status: Unknown (0x41495341), Unknown: 0x2e434150 and Unknown: 0x4a2e4441. Interestingly, a similar AS-REP packet can be seen in the Wireshark example Kerberos trace.</p><p>Is this a benign 'error'? What does it mean?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-as-rep" rel="tag" title="see questions tagged &#39;as-rep&#39;">as-rep</span> <span class="post-tag tag-link-krb5" rel="tag" title="see questions tagged &#39;krb5&#39;">krb5</span> <span class="post-tag tag-link-kerberos" rel="tag" title="see questions tagged &#39;kerberos&#39;">kerberos</span> <span class="post-tag tag-link-kerb" rel="tag" title="see questions tagged &#39;kerb&#39;">kerb</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Aug '11, 01:55</strong></p><img src="https://secure.gravatar.com/avatar/18ed41067e893000fc55a998869b01ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ian_uk1975&#39;s gravatar image" /><p><span>ian_uk1975</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ian_uk1975 has no accepted answers">0%</span></p></div></div><div id="comments-container-5673" class="comments-container"></div><div id="comment-tools-5673" class="comment-tools"></div><div class="clear"></div><div id="comment-5673-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5674"></span>

<div id="answer-container-5674" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5674-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5674-score" class="post-score" title="current number of votes">0</div><span id="post-5674-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As a comparison I loaded the example capture in Network Monitor 3.4, and that shows the padata item is of type <code>PA_PW_SALT</code> with an octect string value as shown by the wireshark <code>Value</code> field. There is no other interpretation of this field in NM so the subsequent fields shown by Wireshark are probably in error and can be ignored.</p><p>It would be nice if you could raise a bug report for this on the Wireshark <a href="https://bugs.wireshark.org/bugzilla/">Bugzilla</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Aug '11, 02:33</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-5674" class="comments-container"><span id="5676"></span><div id="comment-5676" class="comment"><div id="post-5676-score" class="comment-score"></div><div class="comment-text"><p>Thanks for confirmation.</p><p>Bug raised #6234.</p></div><div id="comment-5676-info" class="comment-info"><span class="comment-age">(12 Aug '11, 03:04)</span> <span class="comment-user userinfo">ian_uk1975</span></div></div><span id="5677"></span><div id="comment-5677" class="comment"><div id="post-5677-score" class="comment-score"></div><div class="comment-text"><p>Can you make your "answer" into a further comment and mark the original answer as an answer.</p><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6234">Link</a> to the bug item.</p></div><div id="comment-5677-info" class="comment-info"><span class="comment-age">(12 Aug '11, 04:53)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="5682"></span><div id="comment-5682" class="comment"><div id="post-5682-score" class="comment-score"></div><div class="comment-text"><p>(converted your "answer" to a "comment" please see the FAQ for details. Could you also "accept" Graham's answer if it indeed answered your question?)</p></div><div id="comment-5682-info" class="comment-info"><span class="comment-age">(12 Aug '11, 08:12)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-5674" class="comment-tools"></div><div class="clear"></div><div id="comment-5674-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

