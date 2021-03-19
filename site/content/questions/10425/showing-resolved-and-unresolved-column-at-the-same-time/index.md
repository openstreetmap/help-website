+++
type = "question"
title = "Showing resolved and unresolved column at the same time"
description = '''Hi I have a problem with the name resolution in wireshark 1.6.2 on ubuntu. I want to display both the IP and , when possible, the resolved ip in two separate columns. I added both the Src addr (resolved) and Src adr (unresolved). The problem is that both column always show the same value. Either the...'''
date = "2012-04-24T21:40:00Z"
lastmod = "2012-04-27T08:05:00Z"
weight = 10425
keywords = [ "resolution", "preferences", "columns", "wireshark" ]
aliases = [ "/questions/10425" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Showing resolved and unresolved column at the same time](/questions/10425/showing-resolved-and-unresolved-column-at-the-same-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10425-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10425-score" class="post-score" title="current number of votes">0</div><span id="post-10425-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I have a problem with the name resolution in wireshark 1.6.2 on ubuntu. I want to display both the IP and , when possible, the resolved ip in two separate columns. I added both the Src addr (resolved) and Src adr (unresolved). The problem is that both column always show the same value. Either the resolved value or the IP depending on name resolution settings.I have the same behaviour in tshark.</p><p>my column format column.format: "No.", "%m",<br />
"Time", "%t",<br />
"Src unres", "%us",<br />
"Source", "%rs",<br />
"Source port", "%uS",<br />
"Destination", "%rd",<br />
"Destination", "%ud",<br />
"Dst port", "%uD",<br />
"Protocol", "%p",<br />
"Length", "%L",<br />
"Info", "%i"<br />
</p><p>Column config<br />
<a href="http://imm.io/n9Wz">http://imm.io/n9Wz</a></p><p>Display<br />
<a href="http://imm.io/n9X0">http://imm.io/n9X0</a></p><p>Tshark<br />
<a href="http://pastebin.com/p8jGm0Ts">http://pastebin.com/p8jGm0Ts</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-resolution" rel="tag" title="see questions tagged &#39;resolution&#39;">resolution</span> <span class="post-tag tag-link-preferences" rel="tag" title="see questions tagged &#39;preferences&#39;">preferences</span> <span class="post-tag tag-link-columns" rel="tag" title="see questions tagged &#39;columns&#39;">columns</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Apr '12, 21:40</strong></p><img src="https://secure.gravatar.com/avatar/3a1bc812f76e8111695bc25a059cce22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dirum&#39;s gravatar image" /><p><span>Dirum</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dirum has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-10425" class="comments-container"></div><div id="comment-tools-10425" class="comment-tools"></div><div class="clear"></div><div id="comment-10425-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10488"></span>

<div id="answer-container-10488" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10488-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10488-score" class="post-score" title="current number of votes">0</div><span id="post-10488-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't know what's wrong, but it sounds like a bug to me. I'd suggest opening a <a href="https://bugs.wireshark.org">bug report</a> about it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '12, 08:05</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span> </br></br></p></div></div><div id="comments-container-10488" class="comments-container"></div><div id="comment-tools-10488" class="comment-tools"></div><div class="clear"></div><div id="comment-10488-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

