+++
type = "question"
title = "Error when opening Wireshark"
description = '''Hi guys,  When I want to open Wireshark I get this error :  error while loading shared libraries: libpcap.so.0.8: cannot open shared object file: No such file or directory I tried apt-get install libpcap08 unsucessfully. Any ideas ?  I took a look on plenty websites including searching for the libca...'''
date = "2013-01-30T04:20:00Z"
lastmod = "2013-01-31T01:49:00Z"
weight = 18094
keywords = [ "libpcap" ]
aliases = [ "/questions/18094" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Error when opening Wireshark](/questions/18094/error-when-opening-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18094-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys,</p><p>When I want to open Wireshark I get this error : error while loading shared libraries: libpcap.so.0.8: cannot open shared object file: No such file or directory</p><p>I tried apt-get install libpcap08 unsucessfully.</p><p>Any ideas ? I took a look on plenty websites including searching for the libcap error itself but still nothing :(</p></div><div id="question-tags" class="tags-container tags">libpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jan '13, 04:20</strong></p><img src="https://secure.gravatar.com/avatar/c6c7e0784038582d1b61f10659cfc340?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nymeria&#39;s gravatar image" /><p>Nymeria<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nymeria has no accepted answers">0%</span></p></div></div><div id="comments-container-18094" class="comments-container"><span id="18095"></span><div id="comment-18095" class="comment"><div id="post-18095-score" class="comment-score"></div><div class="comment-text"><p>What OS/distribution are you using and how did you get Wireshark on that machine?</p></div><div id="comment-18095-info" class="comment-info"><span class="comment-age">(30 Jan '13, 04:51)</span> grahamb ♦</div></div><span id="18102"></span><div id="comment-18102" class="comment"><div id="post-18102-score" class="comment-score"></div><div class="comment-text"><p>I use ubuntu 12.04 LTS 64 bits and I installed Wireshark with apt-get install Wireshark</p></div><div id="comment-18102-info" class="comment-info"><span class="comment-age">(30 Jan '13, 06:18)</span> Nymeria</div></div><span id="18206"></span><div id="comment-18206" class="comment"><div id="post-18206-score" class="comment-score"></div><div class="comment-text"><p>Did you try <code>apt-get install libpcap0.8</code>? The package is called "libpcap0.8", not "libpcap08". And <code>apt-get install wireshark</code> should have installed libpcap0.8, as that's a dependency of wireshark.</p></div><div id="comment-18206-info" class="comment-info"><span class="comment-age">(31 Jan '13, 18:41)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-18094" class="comment-tools"></div><div class="clear"></div><div id="comment-18094-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18121"></span>

<div id="answer-container-18121" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18121-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>what is the output of the following commands?</p><blockquote><p>which wireshark<br />
ldd `which wireshark` | grep pcap<br />
dpkg --list | grep pcap<br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '13, 12:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-18121" class="comments-container"></div><div id="comment-tools-18121" class="comment-tools"></div><div class="clear"></div><div id="comment-18121-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18157"></span>

<div id="answer-container-18157" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18157-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>easy solution is to use apt-get install wireshark* so that all dependent wireshark packages are installed. You further want to try apt-get wireshark-dev</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jan '13, 01:49</strong></p><img src="https://secure.gravatar.com/avatar/ceb9fa89fe77c08ded53b2ccf693aeaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aruna%20Sirigere&#39;s gravatar image" /><p>Aruna Sirigere<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aruna Sirigere has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-18157" class="comments-container"><span id="18205"></span><div id="comment-18205" class="comment"><div id="post-18205-score" class="comment-score"></div><div class="comment-text"><p>You shouldn't need wireshark-dev unless you're planning on modifying Wireshark's C code (whether it's adding dissectors or changing the UI or...). If you're only making changes using Lua, that shouldn't be necessary.</p></div><div id="comment-18205-info" class="comment-info"><span class="comment-age">(31 Jan '13, 18:38)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-18157" class="comment-tools"></div><div class="clear"></div><div id="comment-18157-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

