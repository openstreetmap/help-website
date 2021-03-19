+++
type = "question"
title = "No interface for capture to be done on ubuntu server 14.04."
description = '''Hello wireshark gurus, I&#x27;ve been banging my head against the computer screen for 2 days with this problem. Newly installed wireshark, runs fine under root but when I run it as a non-root user I get &quot;No interface for capture to be done&quot;, I know it has to do with the rights and permissions, I gone thr...'''
date = "2014-10-15T05:33:00Z"
lastmod = "2014-10-21T06:56:00Z"
weight = 37061
keywords = [ "no_interface" ]
aliases = [ "/questions/37061" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [No interface for capture to be done on ubuntu server 14.04.](/questions/37061/no-interface-for-capture-to-be-done-on-ubuntu-server-1404)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37061-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello wireshark gurus,</p><p>I've been banging my head against the computer screen for 2 days with this problem. Newly installed wireshark, runs fine under root but when I run it as a non-root user I get "No interface for capture to be done", I know it has to do with the rights and permissions, I gone through the creating wireshark group, adding the user, elevating the file permission to 750 and setting setcap. I doesn't matter what I do, wireshark just doesn't display interfaces to capture on when I run it as a non-root user. Does wireshark need a static ip address, can it work normally in a multihome computer (more than one NIC) or does the code need to be modified? I'm new to linix and wireshark so please dum down your explanations for a newb. Many thanks.</p></div><div id="question-tags" class="tags-container tags">no_interface</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Oct '14, 05:33</strong></p><img src="https://secure.gravatar.com/avatar/c36e5e6ea1d1acd2fc562d03889a827c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="valenski&#39;s gravatar image" /><p>valenski<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="valenski has no accepted answers">0%</span></p></div></div><div id="comments-container-37061" class="comments-container"><span id="37069"></span><div id="comment-37069" class="comment"><div id="post-37069-score" class="comment-score"></div><div class="comment-text"><p>Add yourself to the wireshark group, logout, login again, test. Is this what you did?</p></div><div id="comment-37069-info" class="comment-info"><span class="comment-age">(15 Oct '14, 08:47)</span> Jaap ♦</div></div></div><div id="comment-tools-37061" class="comment-tools"></div><div class="clear"></div><div id="comment-37061-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37236"></span>

<div id="answer-container-37236" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37236-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The key is to run <strong>setcap</strong> on the <strong>dumpcap</strong> binary. See my answer and comments in the following questions:</p><blockquote><p><a href="https://ask.wireshark.org/questions/19675/error-when-running-wireshark-on-ubuntu-as-non-root-user">https://ask.wireshark.org/questions/19675/error-when-running-wireshark-on-ubuntu-as-non-root-user</a><br />
<a href="https://ask.wireshark.org/questions/25242/wireshark-and-linux">https://ask.wireshark.org/questions/25242/wireshark-and-linux</a></p></blockquote><p>See also other similar answers:</p><blockquote><p><a href="https://ask.wireshark.org/questions/16343/install-wireshark-on-ubuntu">https://ask.wireshark.org/questions/16343/install-wireshark-on-ubuntu</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '14, 06:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-37236" class="comments-container"></div><div id="comment-tools-37236" class="comment-tools"></div><div class="clear"></div><div id="comment-37236-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

