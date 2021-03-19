+++
type = "question"
title = "RANAP Missing from the trace"
description = '''I have install new version 1.10.7 and I cannot see RANAP protocal in the trace. I have been check Tab Analyze ....&amp;gt; Enabaled all Protocol and make sure RANAP has been enable. One of my collegue open the same trace in version 1.8.7 and he saw it but another collegue open form the same version and ...'''
date = "2014-05-01T18:51:00Z"
lastmod = "2014-05-04T11:38:00Z"
weight = 32371
keywords = [ "ranap" ]
aliases = [ "/questions/32371" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [RANAP Missing from the trace](/questions/32371/ranap-missing-from-the-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32371-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32371-score" class="post-score" title="current number of votes">0</div><span id="post-32371-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have install new version 1.10.7 and I cannot see RANAP protocal in the trace. I have been check Tab Analyze ....&gt; Enabaled all Protocol and make sure RANAP has been enable.</p><p>One of my collegue open the same trace in version 1.8.7 and he saw it but another collegue open form the same version and he didnt see it.</p><p>Please help, I need the RANAP protocal for my testing.</p><p>Thank you Natta</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ranap" rel="tag" title="see questions tagged &#39;ranap&#39;">ranap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 May '14, 18:51</strong></p><img src="https://secure.gravatar.com/avatar/3d2359db811bf4f25855cfe9ccb6d7a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Natt&#39;s gravatar image" /><p><span>Natt</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Natt has no accepted answers">0%</span></p></div></div><div id="comments-container-32371" class="comments-container"><span id="32373"></span><div id="comment-32373" class="comment"><div id="post-32373-score" class="comment-score"></div><div class="comment-text"><p>Do you have a sample trace you can share on cloudshark?</p></div><div id="comment-32373-info" class="comment-info"><span class="comment-age">(01 May '14, 19:46)</span> <span class="comment-user userinfo">Rooster_50</span></div></div></div><div id="comment-tools-32371" class="comment-tools"></div><div class="clear"></div><div id="comment-32371-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32503"></span>

<div id="answer-container-32503" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32503-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32503-score" class="post-score" title="current number of votes">1</div><span id="post-32503-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you're not correctly decoding an SS7-based protocol (such as RANAP) in Wireshark, a few things need to be checked:</p><ul><li>Make sure the SSN number is set to be decoded as the protocol in question. Under Edit &gt; Preferences &gt; Protocols &gt; RANAP, make sure the SSN you're using is listed there. By default that's SSN 142, but especially in test environments an SSN of 0 (or others) is common and Wireshark by default will not decode these as RANAP.</li><li>Make sure that you are using the correct MTP version. Under Edit &gt; Preferences &gt; Protocols, go to "MTP3" and set the MTP3 standard to whatever you're using (eg: ITU, ANSI).</li><li>If neither of those are the problem, upload the capture file (<a href="https://appliance.cloudshark.org/upload/">https://appliance.cloudshark.org/upload/</a> ) and post a link here so it can be reviewed as to why it would or wouldn't decode as RANAP.</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 May '14, 11:38</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-32503" class="comments-container"></div><div id="comment-tools-32503" class="comment-tools"></div><div class="clear"></div><div id="comment-32503-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

