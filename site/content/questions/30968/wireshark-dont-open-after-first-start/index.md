+++
type = "question"
title = "wireshark don&#x27;t open after first start"
description = '''wireshark don&#x27;t open after first start. Reinstall didn&#x27;t help, wireshark ones starts okay, but on next attempt don&#x27;t open, freezes on 100%. My system is windows 8.1 x64.'''
date = "2014-03-19T13:06:00Z"
lastmod = "2014-03-20T04:31:00Z"
weight = 30968
keywords = [ "open", "error" ]
aliases = [ "/questions/30968" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark don't open after first start](/questions/30968/wireshark-dont-open-after-first-start)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30968-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30968-score" class="post-score" title="current number of votes">0</div><span id="post-30968-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>wireshark don't open after first start. Reinstall didn't help, wireshark ones starts okay, but on next attempt don't open, freezes on 100%. My system is windows 8.1 x64.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-open" rel="tag" title="see questions tagged &#39;open&#39;">open</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Mar '14, 13:06</strong></p><img src="https://secure.gravatar.com/avatar/46e330e7e369b4e2447351bdd722a9aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="belnarto&#39;s gravatar image" /><p><span>belnarto</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="belnarto has no accepted answers">0%</span></p></div></div><div id="comments-container-30968" class="comments-container"></div><div id="comment-tools-30968" class="comment-tools"></div><div class="clear"></div><div id="comment-30968-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30969"></span>

<div id="answer-container-30969" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30969-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30969-score" class="post-score" title="current number of votes">0</div><span id="post-30969-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds similar to the following question:</p><blockquote><p><a href="http://ask.wireshark.org/questions/26361/loading-configuration-files">http://ask.wireshark.org/questions/26361/loading-configuration-files</a></p></blockquote><p>Please check if there is a dumpcap.exe process running in the background. If so, kill it and Wireshark should start again.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Mar '14, 13:12</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Mar '14, 13:40</strong> </span></p></div></div><div id="comments-container-30969" class="comments-container"><span id="30983"></span><div id="comment-30983" class="comment"><div id="post-30983-score" class="comment-score"></div><div class="comment-text"><p>I made - In the registry, change HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\NPF\Start to 0x3 (SERVICE_DEMAND_START) and wireshark work normal, thanks you!</p></div><div id="comment-30983-info" class="comment-info"><span class="comment-age">(20 Mar '14, 04:31)</span> <span class="comment-user userinfo">belnarto</span></div></div></div><div id="comment-tools-30969" class="comment-tools"></div><div class="clear"></div><div id="comment-30969-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

