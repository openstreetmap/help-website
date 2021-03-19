+++
type = "question"
title = "Only My Own Traffic"
description = '''Hi, I&#x27;m on a Dell XPS M1530 with an Intel 4965AGN card. I&#x27;ve tried this on both Windows 7 and Ubuntu 11.4. When I select my wireless adapter, set my card to promiscuous mode, and begin capture, I get no packets at all. This doesn&#x27;t make sense as there are probably a dozen WLANs around me. If I conne...'''
date = "2011-06-08T14:31:00Z"
lastmod = "2011-06-08T15:39:00Z"
weight = 4459
keywords = [ "intel4965agn", "windows7", "own", "traffic", "ubuntu" ]
aliases = [ "/questions/4459" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Only My Own Traffic](/questions/4459/only-my-own-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4459-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4459-score" class="post-score" title="current number of votes">0</div><span id="post-4459-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm on a Dell XPS M1530 with an Intel 4965AGN card. I've tried this on both Windows 7 and Ubuntu 11.4.</p><p>When I select my wireless adapter, set my card to promiscuous mode, and begin capture, I get no packets at all. This doesn't make sense as there are probably a dozen WLANs around me. If I connect to my own network, I can see my own traffic. But I cannot see traffic running through my own network when I disconnect from it.</p><p>Any ideas?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-intel4965agn" rel="tag" title="see questions tagged &#39;intel4965agn&#39;">intel4965agn</span> <span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span> <span class="post-tag tag-link-own" rel="tag" title="see questions tagged &#39;own&#39;">own</span> <span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '11, 14:31</strong></p><img src="https://secure.gravatar.com/avatar/b6f260d102916def8c69d8900e1c02aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zhouzhen&#39;s gravatar image" /><p><span>zhouzhen</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zhouzhen has no accepted answers">0%</span></p></div></div><div id="comments-container-4459" class="comments-container"><span id="4460"></span><div id="comment-4460" class="comment"><div id="post-4460-score" class="comment-score"></div><div class="comment-text"><p>As I understand it, wireless interfaces are a little different. Since you are using a non-Windows OS, you can use a program like airmon-ng to set your wireless adapter into monitor mode. If you try that and it doesn't help, maybe someone else knows what might be going on.</p></div><div id="comment-4460-info" class="comment-info"><span class="comment-age">(08 Jun '11, 14:47)</span> <span class="comment-user userinfo">multipleinte...</span></div></div></div><div id="comment-tools-4459" class="comment-tools"></div><div class="clear"></div><div id="comment-4459-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4461"></span>

<div id="answer-container-4461" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4461-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4461-score" class="post-score" title="current number of votes">0</div><span id="post-4461-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You might try reading through the Wireshark <a href="http://wiki.wireshark.org/CaptureSetup/WLAN">WLAN (IEEE 802.11) capture setup</a> wiki page.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jun '11, 15:39</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-4461" class="comments-container"></div><div id="comment-tools-4461" class="comment-tools"></div><div class="clear"></div><div id="comment-4461-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

