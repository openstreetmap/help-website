+++
type = "question"
title = "Decode Multiple ports as Radius"
description = '''Hi Experts, is there a way to let Wireshark always decode a range of UDP ports as Radius? in radius potocol setting there is a way to add one alternate port only, also decode as menu configurations are not persistant and only applied in the current window. Thanks.'''
date = "2011-02-07T05:33:00Z"
lastmod = "2015-08-13T11:46:00Z"
weight = 2189
keywords = [ "decode", "multiple", "ports" ]
aliases = [ "/questions/2189" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Decode Multiple ports as Radius](/questions/2189/decode-multiple-ports-as-radius)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2189-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Experts,</p><p>is there a way to let Wireshark always decode a range of UDP ports as Radius? in radius potocol setting there is a way to add one alternate port only, also decode as menu configurations are not persistant and only applied in the current window.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">decode multiple ports</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Feb '11, 05:33</strong></p><img src="https://secure.gravatar.com/avatar/19c5ebaffe062dc2f1df407c5bffc6a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Belal&#39;s gravatar image" /><p>Belal<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Belal has no accepted answers">0%</span></p></div></div><div id="comments-container-2189" class="comments-container"><span id="3528"></span><div id="comment-3528" class="comment"><div id="post-3528-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>Just as a work around - if you know udp ports - you can select 1 packet in wireshark and decode it as radius. Did you try this? Did this work for you?</p></div><div id="comment-3528-info" class="comment-info"><span class="comment-age">(15 Apr '11, 22:40)</span> Vijay Gharge</div></div></div><div id="comment-tools-2189" class="comment-tools"></div><div class="clear"></div><div id="comment-2189-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2193"></span>

<div id="answer-container-2193" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2193-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is not possible at the moment. If you really need this, then you would need to change the radius dissector to accept a range of ports in its preferences. You can either program this yourself, hire someone to do it for you or file an enhancement request on https://bugs.wireshark.org. In the latter case, you are not sure if and when it will be developed as someone needs to take an interest in your request.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Feb '11, 07:37</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-2193" class="comments-container"></div><div id="comment-tools-2193" class="comment-tools"></div><div class="clear"></div><div id="comment-2193-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="45066"></span>

<div id="answer-container-45066" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45066-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sorry for being a few years late but it will be fixed in a few next days. A proper fix sits in my GitHub's repository and will be submitted for the review very soon:</p><ul><li><a href="https://code.wireshark.org/review/#/c/10015/">Review request at Wireshark's Gerrit(in progress)</a></li><li><a href="https://github.com/lemenkov/wireshark/commit/ab71f64">GitHub</a></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '15, 11:46</strong></p><img src="https://secure.gravatar.com/avatar/acff1f85f010b5fd2b9c212d195e28b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peter%20Lemenkov&#39;s gravatar image" /><p>Peter Lemenkov<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peter Lemenkov has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Aug '15, 11:47</p></div></div><div id="comments-container-45066" class="comments-container"></div><div id="comment-tools-45066" class="comment-tools"></div><div class="clear"></div><div id="comment-45066-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

