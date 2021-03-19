+++
type = "question"
title = "Details about &quot;Do not call subdissector for error packets&quot; TCP preference"
description = '''Hi everyone, I&#x27;m dealing with TLS secure communciations and I found out that retransmitted TLS handshake messages, recevied at the wrong time, can prevent the correct session decryption. By enabling the TCP preference &quot;Do not call subdissector for error packets&quot;, the decryption works fine. I&#x27;m wonde...'''
date = "2015-10-13T00:07:00Z"
lastmod = "2015-10-23T03:39:00Z"
weight = 46490
keywords = [ "tls", "ssl", "handshake", "preferences", "tcp" ]
aliases = [ "/questions/46490" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Details about "Do not call subdissector for error packets" TCP preference](/questions/46490/details-about-do-not-call-subdissector-for-error-packets-tcp-preference)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46490-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46490-score" class="post-score" title="current number of votes">1</div><span id="post-46490-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone,</p><p>I'm dealing with TLS secure communciations and I found out that retransmitted TLS handshake messages, recevied at the wrong time, can prevent the correct session decryption. By enabling the TCP preference "Do not call subdissector for error packets", the decryption works fine.</p><p>I'm wondering how this preference impact the subdissector, in particular <strong>which are these error packets handled differently?</strong></p><p>I also notice that enabling this preference has no effect on decryption when some TLS handshake messages are marked as TCP out-of-order segments: in this case wireshark won't decipher anyway.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tls" rel="tag" title="see questions tagged &#39;tls&#39;">tls</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-handshake" rel="tag" title="see questions tagged &#39;handshake&#39;">handshake</span> <span class="post-tag tag-link-preferences" rel="tag" title="see questions tagged &#39;preferences&#39;">preferences</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Oct '15, 00:07</strong></p><img src="https://secure.gravatar.com/avatar/eca830854093757dbe9847c9d44241b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="theo66&#39;s gravatar image" /><p><span>theo66</span><br />
<span class="score" title="91 reputation points">91</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="theo66 has one accepted answer">50%</span></p></div></div><div id="comments-container-46490" class="comments-container"></div><div id="comment-tools-46490" class="comment-tools"></div><div class="clear"></div><div id="comment-46490-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46498"></span>

<div id="answer-container-46498" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46498-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46498-score" class="post-score" title="current number of votes">3</div><span id="post-46498-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="theo66 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The "error" packets are the retransmissions. By default the TCP dissector will hand retransmissions to the subdissector (in this case the SSL/TLS dissector) which means that the subdissector sees the retransmitted data twice. If the subdissector is stateful (its behavior now is impacted by what packets it saw before) then this can/will confuse the subdissector. I think the TLS/SSL dissector is stateful since it's running decryption on the bytes as they go by. (Or something like that.)</p><p>The TCP dissector treats both retransmissions and "out of order" packets as error so it should behave the same in both cases. I'd guess that something else is going wrong to break the decryption in your second case.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Oct '15, 06:45</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-46498" class="comments-container"><span id="46544"></span><div id="comment-46544" class="comment"><div id="post-46544-score" class="comment-score"></div><div class="comment-text"><p>Thank for the reply. For the failed decryption with out-of-order TCP segments there's already the bug report 9641.</p><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9461">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9461</a></p></div><div id="comment-46544-info" class="comment-info"><span class="comment-age">(14 Oct '15, 00:32)</span> <span class="comment-user userinfo">theo66</span></div></div><span id="46566"></span><div id="comment-46566" class="comment"><div id="post-46566-score" class="comment-score"></div><div class="comment-text"><p>You're welcome. If an answer answers your question, please be sure to accept it (by clicking on the check mark next to the answer). That way the site will consider the question as answered--see the FAQ.</p></div><div id="comment-46566-info" class="comment-info"><span class="comment-age">(15 Oct '15, 07:16)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="46873"></span><div id="comment-46873" class="comment"><div id="post-46873-score" class="comment-score"></div><div class="comment-text"><p>You're right, I've missed to accept the answer, sorry!</p></div><div id="comment-46873-info" class="comment-info"><span class="comment-age">(23 Oct '15, 03:39)</span> <span class="comment-user userinfo">theo66</span></div></div></div><div id="comment-tools-46498" class="comment-tools"></div><div class="clear"></div><div id="comment-46498-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

