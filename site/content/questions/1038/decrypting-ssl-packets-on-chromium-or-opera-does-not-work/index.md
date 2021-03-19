+++
type = "question"
title = "decrypting SSL packets on Chromium or Opera does not work?"
description = '''I seem to be able to decrypt SSL sessions by following the http://wiki.wireshark.org/SSL HOWTO for Safari, but not for Opera or Chrome.  To test this I have a very simple java server available at https://github.com/bblfish/TLS_test I posted a bug report on this https://bugs.wireshark.org/bugzilla/sh...'''
date = "2010-11-20T09:03:00Z"
lastmod = "2010-11-20T09:18:00Z"
weight = 1038
keywords = [ "ssl", "decryption" ]
aliases = [ "/questions/1038" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [decrypting SSL packets on Chromium or Opera does not work?](/questions/1038/decrypting-ssl-packets-on-chromium-or-opera-does-not-work)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1038-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1038-score" class="post-score" title="current number of votes">0</div><span id="post-1038-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I seem to be able to decrypt SSL sessions by following the http://wiki.wireshark.org/SSL HOWTO for Safari, but not for Opera or Chrome. To test this I have a very simple java server available at https://github.com/bblfish/TLS_test</p><p>I posted a bug report on this https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5423</p><p>Go and vote for that bug. It's important for the web if it is going to be secure and allow us to have https everywhere that Wireshark function well on all browsers. http://www.eff.org/deeplinks/2010/10/message-firesheep-baaaad-websites-implement</p><p>(Or let me know what I am doing wrong! :-)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Nov '10, 09:03</strong></p><img src="https://secure.gravatar.com/avatar/5d537347eb54566c1b9d975a30fc0147?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bblfish&#39;s gravatar image" /><p><span>bblfish</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bblfish has no accepted answers">0%</span></p></div></div><div id="comments-container-1038" class="comments-container"></div><div id="comment-tools-1038" class="comment-tools"></div><div class="clear"></div><div id="comment-1038-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1040"></span>

<div id="answer-container-1040" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1040-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1040-score" class="post-score" title="current number of votes">2</div><span id="post-1040-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="bblfish has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I checked the Opera capture file in the bugreport and it shows that a Diffie Hellman cipher has been chosen. By the nature of the DH protocol, decryption will not work without supplying the keying material that is dynamically created. You can restrict the list of acceptable ciphers to circumvent this problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '10, 09:12</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1040" class="comments-container"><span id="1041"></span><div id="comment-1041" class="comment"><div id="post-1041-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot SYNbit. That will help me debug my server at least.</p><p>I'll respond further on the bug report.</p></div><div id="comment-1041-info" class="comment-info"><span class="comment-age">(20 Nov '10, 09:18)</span> <span class="comment-user userinfo">bblfish</span></div></div></div><div id="comment-tools-1040" class="comment-tools"></div><div class="clear"></div><div id="comment-1040-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

