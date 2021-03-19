+++
type = "question"
title = "Uncertain How to Frame Question"
description = '''&quot;frame&quot; heh, pun not intended. I have what might be a network related issue, or it is OS related, I am unsure. I have a networking foundation, just little practical experience, and basically zero exp with Wireshark. Please be patient while I generically detail what I am experiencing, and please advi...'''
date = "2015-07-24T10:43:00Z"
lastmod = "2015-07-24T13:28:00Z"
weight = 44436
keywords = [ "application", "connectivity" ]
aliases = [ "/questions/44436" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Uncertain How to Frame Question](/questions/44436/uncertain-how-to-frame-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44436-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44436-score" class="post-score" title="current number of votes">0</div><span id="post-44436-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>"frame" heh, pun not intended.</p><p>I have what <em>might</em> be a network related issue, or it is OS related, I am unsure. I have a networking foundation, just little practical experience, and basically zero exp with Wireshark. Please be patient while I generically detail what I am experiencing, and please advise me as needed.</p><p>I have an Internet facing application that recently changed its behavior. (it is common for it to be patched) On a hardened, slipstreamed, tweaked win7proSP1(64bit) PC, this application previously would run under a USER account with no issue. Now, however, under this exact same system, under a USER account, the application complains of "can not connect."</p><p>YET! Under the Administrative account of this same system, the application runs as expected. The only change I have done was to log in under the admin account, NOTHING else. I ran this application while Wireshark was running under both accounts, and while the USER results are .. less noisy, they both seem the same. (results saved and provided upon request)</p><p>Here is the oddity the lends me to think it is OS realted. I have a similarly OS'd laptop, which has a few additional services enabled for wireless connectivity. Between the Desktop and Laptop, everything is nearly identical else-wise. The Laptop, has no issue running this same application from a USER account.</p><p>What guidance can be provided? Is this a networking issue? Is there a way using some other tool, to determine what this application is actually doing in terms of the OS relation? I apologize for my ignorance, and look forward to any assistance that can be provided. CAH</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-application" rel="tag" title="see questions tagged &#39;application&#39;">application</span> <span class="post-tag tag-link-connectivity" rel="tag" title="see questions tagged &#39;connectivity&#39;">connectivity</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jul '15, 10:43</strong></p><img src="https://secure.gravatar.com/avatar/b0a52427cf12346c149e66256d87306e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ceyarrecks&#39;s gravatar image" /><p><span>Ceyarrecks</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ceyarrecks has no accepted answers">0%</span></p></div></div><div id="comments-container-44436" class="comments-container"></div><div id="comment-tools-44436" class="comment-tools"></div><div class="clear"></div><div id="comment-44436-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44449"></span>

<div id="answer-container-44449" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44449-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44449-score" class="post-score" title="current number of votes">0</div><span id="post-44449-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>well. I have discovered the cause of the application's woes. By insecurely rechecking Use <strong>TLS 1.0</strong> under Internet Options now allows this, UNRELATED to web browsing, application to function as expected....</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '15, 13:28</strong></p><img src="https://secure.gravatar.com/avatar/b0a52427cf12346c149e66256d87306e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ceyarrecks&#39;s gravatar image" /><p><span>Ceyarrecks</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ceyarrecks has no accepted answers">0%</span></p></div></div><div id="comments-container-44449" class="comments-container"></div><div id="comment-tools-44449" class="comment-tools"></div><div class="clear"></div><div id="comment-44449-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

