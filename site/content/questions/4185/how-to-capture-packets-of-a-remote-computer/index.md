+++
type = "question"
title = "How to Capture packets of a remote computer ??"
description = '''I wanna capture packets from a remote computer, let say my friend is chatting with me, is it possible to capture all his ingoing and outgoing traffic by WireShark ?'''
date = "2011-05-23T05:18:00Z"
lastmod = "2011-05-23T08:00:00Z"
weight = 4185
keywords = [ "capture", "remote" ]
aliases = [ "/questions/4185" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to Capture packets of a remote computer ??](/questions/4185/how-to-capture-packets-of-a-remote-computer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4185-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I wanna capture packets from a remote computer, let say my friend is chatting with me, is it possible to capture all his ingoing and outgoing traffic by WireShark ?</p></div><div id="question-tags" class="tags-container tags">capture remote</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 May '11, 05:18</strong></p><img src="https://secure.gravatar.com/avatar/281102043dad57cd317adb369935e5f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nzhacker&#39;s gravatar image" /><p>nzhacker<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nzhacker has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>retagged 24 May '11, 15:56</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-4185" class="comments-container"></div><div id="comment-tools-4185" class="comment-tools"></div><div class="clear"></div><div id="comment-4185-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4186"></span>

<div id="answer-container-4186" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4186-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes or no, depending where your friend is. If he's right next to you, sharing a hub (not switch) with you that will "broadcast" all frames, you can capture everything. If he's on a switch or even at another location then no, you can't.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 May '11, 05:31</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-4186" class="comments-container"></div><div id="comment-tools-4186" class="comment-tools"></div><div class="clear"></div><div id="comment-4186-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4188"></span>

<div id="answer-container-4188" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4188-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm guessing at what you're wanting to accomplish, but if you are trying to help your friend resolve a problem and have their cooperation you can use "rpcapd" to do remote capture if you need to get all of the connection-type traffic, plus the upper-layer traffic.<br />
If you are 'chatting' using something like Windows live messenger, and interested more in the actual message traffic, as I recall that traffic is sent in clear text, and your capture file will have both the incoming and outgoing traffic/text related to those messages in it without doing a remote capture on the other computer. Or as Jasper mentioned, you can use a hub at the remote location and capture all traffic broadcasted/received in parallel with the remote computer.</p><p>Hope this is helpful, John</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 May '11, 08:00</strong></p><img src="https://secure.gravatar.com/avatar/1f3966b6e9de3a63326e2d3fd51c8c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Modlin&#39;s gravatar image" /><p>John_Modlin<br />
<span class="score" title="120 reputation points">120</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Modlin has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-4188" class="comments-container"></div><div id="comment-tools-4188" class="comment-tools"></div><div class="clear"></div><div id="comment-4188-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

