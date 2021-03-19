+++
type = "question"
title = "how to choose an interface?"
description = '''i recently downloaded wireshark and im new to the system. I was expirementing with it and was wondering how to know which interface to choose to collect packets off of my router. how do I know which one is my router. I tried the one receiving packets and tried to log onto something on my laptop whil...'''
date = "2013-03-20T17:58:00Z"
lastmod = "2013-03-20T18:16:00Z"
weight = 19701
keywords = [ "interface" ]
aliases = [ "/questions/19701" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to choose an interface?](/questions/19701/how-to-choose-an-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19701-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i recently downloaded wireshark and im new to the system. I was expirementing with it and was wondering how to know which interface to choose to collect packets off of my router. how do I know which one is my router. I tried the one receiving packets and tried to log onto something on my laptop while on the network to retrieve the password but it didn't show up in the packet. please help?</p></div><div id="question-tags" class="tags-container tags">interface</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Mar '13, 17:58</strong></p><img src="https://secure.gravatar.com/avatar/5a1ee49a8ad9327135e364653a937b99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jp7799&#39;s gravatar image" /><p>jp7799<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jp7799 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Mar '13, 10:58</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-19701" class="comments-container"></div><div id="comment-tools-19701" class="comment-tools"></div><div class="clear"></div><div id="comment-19701-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19702"></span>

<div id="answer-container-19702" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19702-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Open wireshark application and click interface list on home page. It shows all the interfaces tied to your system and you can select one. Do an ifconfig(un*x) or ipconfig(windows) to identify the correct interface for packet capturing.</p><p>Identifying your router: According to me your router is your default gateway(Correct me if i am wrong). Do <code>netstat -r -n</code> on a Un*x machine and <code>ipconfig/all</code> on your windows to identify your router aka default gateway. The output of <code>netstat -r -n</code> should have a line with "default" in the first column; the interface listed near the end of that line is the interface used to communicate with your router.</p><p>Not an iota of clue with rest of your question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '13, 18:16</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p>krishnayeddula<br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Mar '13, 00:39</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-19702" class="comments-container"></div><div id="comment-tools-19702" class="comment-tools"></div><div class="clear"></div><div id="comment-19702-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

