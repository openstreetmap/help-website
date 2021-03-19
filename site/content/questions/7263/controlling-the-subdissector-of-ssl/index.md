+++
type = "question"
title = "Controlling the subdissector of SSL"
description = '''I&#x27;m trying to decrypt data transmitted over SSL. I have set the RSA Keys section in Preferences / Protocol / SSL appropriately so that I can read the encrypted data. The problem is that my data is not HTTP nor any other protocol (that I can find) for specifying which subdisector to use. If I put in ...'''
date = "2011-11-07T10:02:00Z"
lastmod = "2011-11-08T15:42:00Z"
weight = 7263
keywords = [ "ssl", "subdissector" ]
aliases = [ "/questions/7263" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Controlling the subdissector of SSL](/questions/7263/controlling-the-subdissector-of-ssl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7263-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7263-score" class="post-score" title="current number of votes">0</div><span id="post-7263-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to decrypt data transmitted over SSL. I have set the RSA Keys section in Preferences / Protocol / SSL appropriately so that I can read the encrypted data.</p><p>The problem is that my data is not HTTP nor any other protocol (that I can find) for specifying which subdisector to use. If I put in "http", I get a complaint about a Malformed GIF Image. (My data is simply "hello".) As a result, "Follow SSL Stream" also doesn't work.</p><p>How can I tell Wireshark not to interpret my encrypted data?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-subdissector" rel="tag" title="see questions tagged &#39;subdissector&#39;">subdissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '11, 10:02</strong></p><img src="https://secure.gravatar.com/avatar/106e02ff0a10bc691f72f6bc1ff48f1c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ELavy&#39;s gravatar image" /><p><span>ELavy</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ELavy has no accepted answers">0%</span></p></div></div><div id="comments-container-7263" class="comments-container"></div><div id="comment-tools-7263" class="comment-tools"></div><div class="clear"></div><div id="comment-7263-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7264"></span>

<div id="answer-container-7264" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7264-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7264-score" class="post-score" title="current number of votes">1</div><span id="post-7264-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use "data" instead of "http" to tell the SSL dissector to pass the decrypted data to the "data" dissector. The data dissector does not try to further dissect the (decrypted) data.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '11, 11:16</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-7264" class="comments-container"><span id="7298"></span><div id="comment-7298" class="comment"><div id="post-7298-score" class="comment-score"></div><div class="comment-text"><p>Perfect! Thanks.</p><p>I noticed that changes to the subdissector didn't take effect until I restarted WireShark, but I can deal with that.</p></div><div id="comment-7298-info" class="comment-info"><span class="comment-age">(08 Nov '11, 15:42)</span> <span class="comment-user userinfo">ELavy</span></div></div></div><div id="comment-tools-7264" class="comment-tools"></div><div class="clear"></div><div id="comment-7264-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

