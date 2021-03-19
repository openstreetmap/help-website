+++
type = "question"
title = "linux capture filter problems"
description = '''Hi, i have some issues with capture filters not working on a Linux Server. Even a simple filter like &quot;x.x.x.x&quot; will cause no packets to be displayed. If i filter after capture using display filter it works fine &quot;ip.addr==x.x.x.x&quot;. I have tried this on a different network interface on the same machin...'''
date = "2011-08-29T23:34:00Z"
lastmod = "2011-08-30T00:16:00Z"
weight = 5941
keywords = [ "filter", "capture", "linux" ]
aliases = [ "/questions/5941" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [linux capture filter problems](/questions/5941/linux-capture-filter-problems)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5941-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, i have some issues with capture filters not working on a Linux Server. Even a simple filter like "x.x.x.x" will cause no packets to be displayed. If i filter after capture using display filter it works fine "ip.addr==x.x.x.x". I have tried this on a different network interface on the same machine and found capture filters are working fine on that one. The only difference i can think of between those 2 interfaces is that the first one has a lot of traffic on it (250Mbps+). Has anyone else faced a similar problem or knows of certain limitations for capture filters? thanks!</p></div><div id="question-tags" class="tags-container tags">filter capture linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Aug '11, 23:34</strong></p><img src="https://secure.gravatar.com/avatar/6ede277f6039c67a9dbee8b4849f8174?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="menumorut&#39;s gravatar image" /><p>menumorut<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="menumorut has no accepted answers">0%</span></p></div></div><div id="comments-container-5941" class="comments-container"><span id="5945"></span><div id="comment-5945" class="comment"><div id="post-5945-score" class="comment-score"></div><div class="comment-text"><p>After answering your question, I saw that it was deleted. I think this can be a useful question/answer to others, so I undeleted it. Please add the way you solved your issue as a comment.</p></div><div id="comment-5945-info" class="comment-info"><span class="comment-age">(30 Aug '11, 00:35)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-5941" class="comment-tools"></div><div class="clear"></div><div id="comment-5941-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5943"></span>

<div id="answer-container-5943" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5943-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>"x.x.x.x" is not a valid capture filter, you will have to use "host x.x.x.x", but assuming you did indeed use "host x.x.x.x" the problem might be that your packets are encapsulated. This can be either by vlan-tagging, pppoe, mpls etc.</p><p>Please capture a few packets without filter, then use the display filter and look for vlan-tagging or a protocol between the ethernet and the ip layer.</p><p>If the packets are vlan-tagged, then you can use "vlan and host x.x.x.x" as a capture filter. For other protocols it depends on the protocol what kind of filter you may need to use.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '11, 00:16</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5943" class="comments-container"></div><div id="comment-tools-5943" class="comment-tools"></div><div class="clear"></div><div id="comment-5943-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

