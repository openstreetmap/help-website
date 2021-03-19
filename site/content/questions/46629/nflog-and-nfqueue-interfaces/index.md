+++
type = "question"
title = "Nflog and Nfqueue interfaces"
description = '''Is it normal to have nflog and nfqueue in my interfaces list? It&#x27;s an ubuntu desktop system running ufw. I don`t remember having those interfaces when i first installed wireshark.'''
date = "2015-10-16T12:23:00Z"
lastmod = "2015-10-17T11:03:00Z"
weight = 46629
keywords = [ "nfqueue", "nflog" ]
aliases = [ "/questions/46629" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nflog and Nfqueue interfaces](/questions/46629/nflog-and-nfqueue-interfaces)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46629-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46629-score" class="post-score" title="current number of votes">0</div><span id="post-46629-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it normal to have nflog and nfqueue in my interfaces list? It's an ubuntu desktop system running ufw. I don`t remember having those interfaces when i first installed wireshark.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nfqueue" rel="tag" title="see questions tagged &#39;nfqueue&#39;">nfqueue</span> <span class="post-tag tag-link-nflog" rel="tag" title="see questions tagged &#39;nflog&#39;">nflog</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Oct '15, 12:23</strong></p><img src="https://secure.gravatar.com/avatar/09969f35aabf81c9d74f3d55824861cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ciohap22&#39;s gravatar image" /><p><span>Ciohap22</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ciohap22 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Oct '15, 13:37</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-46629" class="comments-container"></div><div id="comment-tools-46629" class="comment-tools"></div><div class="clear"></div><div id="comment-46629-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46631"></span>

<div id="answer-container-46631" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46631-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46631-score" class="post-score" title="current number of votes">1</div><span id="post-46631-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is it normal to have nflog and nfqueue in my interfaces list?</p></blockquote><p>On Linux, with a sufficiently recent version of libpcap, yes, it's normal. People wanted to be able to capture some forms of netfilter traffic and analyze it with tcpdump, Wireshark, etc., so that capability was added to libpcap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '15, 13:37</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-46631" class="comments-container"><span id="46640"></span><div id="comment-46640" class="comment"><div id="post-46640-score" class="comment-score"></div><div class="comment-text"><p>So those are 2 interfaces created by wireshark when it was installed?</p></div><div id="comment-46640-info" class="comment-info"><span class="comment-age">(17 Oct '15, 01:01)</span> <span class="comment-user userinfo">Ciohap22</span></div></div><span id="46642"></span><div id="comment-46642" class="comment"><div id="post-46642-score" class="comment-score">1</div><div class="comment-text"><p>No. Wireshark doesn't create interfaces. Wireshark uses libpcap to do traffic capture; libpcap doesn't create interfaces, either, it just allows capturing on things that <em>aren't</em> regular network interfaces, such as the nflog and nfqueue hooks into the Linux netfilter mechanism.</p></div><div id="comment-46642-info" class="comment-info"><span class="comment-age">(17 Oct '15, 11:03)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-46631" class="comment-tools"></div><div class="clear"></div><div id="comment-46631-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

