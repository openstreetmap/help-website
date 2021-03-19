+++
type = "question"
title = "How do I make a Wireshark built from source not require root on Linux?"
description = '''Hi, I have installed the brandnew wireshark 2.0.0. Its great! The &quot;old workaround&quot; for nonroot-users would not run. Wireshark starts without interfaces. What shall I do to tun Wireshark 2.0 as normal user? Thank You for your support. Bernhard Hauser'''
date = "2015-11-30T11:15:00Z"
lastmod = "2015-12-02T13:09:00Z"
weight = 48101
keywords = [ "nonroot", "linux" ]
aliases = [ "/questions/48101" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How do I make a Wireshark built from source not require root on Linux?](/questions/48101/how-do-i-make-a-wireshark-built-from-source-not-require-root-on-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48101-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have installed the brandnew wireshark 2.0.0. Its great! The "old workaround" for nonroot-users would not run. Wireshark starts without interfaces. What shall I do to tun Wireshark 2.0 as normal user?</p><p>Thank You for your support.</p><p>Bernhard Hauser</p></div><div id="question-tags" class="tags-container tags">nonroot linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Nov '15, 11:15</strong></p><img src="https://secure.gravatar.com/avatar/5df15cb7413a11a5897331507b8d9631?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uri&#39;s gravatar image" /><p>Uri<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uri has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Dec '15, 13:05</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-48101" class="comments-container"><span id="48114"></span><div id="comment-48114" class="comment"><div id="post-48114-score" class="comment-score"></div><div class="comment-text"><p>What is your Linux distribution and what is the "old workaround" you are refering to?</p></div><div id="comment-48114-info" class="comment-info"><span class="comment-age">(30 Nov '15, 17:33)</span> Kurt Knochner ♦</div></div><span id="48121"></span><div id="comment-48121" class="comment"><div id="post-48121-score" class="comment-score"></div><div class="comment-text"><p>Hi, I am using Ubuntu 14.04 LTS.</p></div><div id="comment-48121-info" class="comment-info"><span class="comment-age">(01 Dec '15, 02:38)</span> Uri</div></div></div><div id="comment-tools-48101" class="comment-tools"></div><div class="clear"></div><div id="comment-48101-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="48150"></span>

<div id="answer-container-48150" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48150-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I can successfully capture with the new wireshark V2 on Ubuntu 15.10.<br />
I didn't have to change any of the settings but I think I once followed the advice in<br />
<a href="https://ask.wireshark.org/questions/1949/wireshark-says-there-are-no-interfaces-on-which-a-capture-can-be-done-how-do-i-fix-this">wireshark-says-there-are-no-interfaces-on-which-a-capture-can-be-done-how-do-i-fix-this</a><br />
</p><p>On Ubuntu</p><pre><code>sudo apt-get install wireshark libcap2-bin
sudo groupadd wireshark
sudo usermod -a -G wireshark $USER
sudo chgrp wireshark /usr/bin/dumpcap
sudo chmod 755 /usr/bin/dumpcap
sudo setcap cap_net_raw,cap_net_admin=eip /usr/bin/dumpcap (step 6 to make the interfaces visible)</code></pre><p>Is that the workaround you referred to ?</p><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Dec '15, 10:44</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-48150" class="comments-container"><span id="48161"></span><div id="comment-48161" class="comment"><div id="post-48161-score" class="comment-score"></div><div class="comment-text"><p>What I did with wireshark 1.12 was this (shown in several threads):</p><pre><code>sudo groupadd wireshark
sudo usermod -a -G wireshark dionysius
sudo dpkg-reconfigure wireshark-common (and said there YES)</code></pre><p>... and wireshark runs without root privilidges.</p><p>The same procedure after compiling wireshark 2.0.0 on the same machine shows no interfaces when i run it as normal user. Running as root shows the interfaces.</p></div><div id="comment-48161-info" class="comment-info"><span class="comment-age">(01 Dec '15, 13:48)</span> Uri</div></div><span id="48162"></span><div id="comment-48162" class="comment"><div id="post-48162-score" class="comment-score"></div><div class="comment-text"><p>Compiling you say? That's not what you did with 1.12 I presume? There you installed Debian packages.</p><p>If you try to run wireshark in your build directory use the setcap command as listed on your newly build dumpcap.</p></div><div id="comment-48162-info" class="comment-info"><span class="comment-age">(01 Dec '15, 13:53)</span> Jaap ♦</div></div><span id="48176"></span><div id="comment-48176" class="comment"><div id="post-48176-score" class="comment-score"></div><div class="comment-text"><p>I compiled the legacy wireshark on the same machines like wireshark v2 with the same OS...</p></div><div id="comment-48176-info" class="comment-info"><span class="comment-age">(02 Dec '15, 01:22)</span> Uri</div></div><span id="48189"></span><div id="comment-48189" class="comment"><div id="post-48189-score" class="comment-score"></div><div class="comment-text"><p>Compiled and build Debian packages from that, which you then installed?</p><p>I'm asking because you state executing dpkg-reconfigure wireshark-common.</p></div><div id="comment-48189-info" class="comment-info"><span class="comment-age">(02 Dec '15, 04:55)</span> Jaap ♦</div></div></div><div id="comment-tools-48150" class="comment-tools"></div><div class="clear"></div><div id="comment-48150-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="48207"></span>

<div id="answer-container-48207" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48207-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, I have not built packages, I compiled directly to my system.</p><p>I now have removed the older version with <code>sudo apt-get remove wireshark</code> and changed the setcap-path to my current installation:</p><pre><code>sudo setcap cap_net_raw,cap_net_admin=eip /usr/local/bin/dumpcap</code></pre><p>This fixed the problem! Thanks for your support,</p><p>Uri!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '15, 11:33</strong></p><img src="https://secure.gravatar.com/avatar/5df15cb7413a11a5897331507b8d9631?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uri&#39;s gravatar image" /><p>Uri<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uri has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-48207" class="comments-container"><span id="48210"></span><div id="comment-48210" class="comment"><div id="post-48210-score" class="comment-score"></div><div class="comment-text"><blockquote><p>No, I have not built packages, I compiled directly to my system.</p></blockquote><p>If by that you mean that you downloaded the Wireshark source tree, built it, and did "make install", then <code>sudo dpkg-reconfigure wireshark-common</code> will have no effect on what you installed - that command is for people who have installed Wireshark from a Debian-style package, not for people who are building Wireshark themselves from source.</p></div><div id="comment-48210-info" class="comment-info"><span class="comment-age">(02 Dec '15, 13:11)</span> Guy Harris ♦♦</div></div><span id="48211"></span><div id="comment-48211" class="comment"><div id="post-48211-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I now have removed the older version with sudo apt-get remove wireshark</p></blockquote><p>Which means that the older version was installed as a package, not directly built from source and installed from the source build.</p></div><div id="comment-48211-info" class="comment-info"><span class="comment-age">(02 Dec '15, 13:12)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-48207" class="comment-tools"></div><div class="clear"></div><div id="comment-48207-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="48209"></span>

<div id="answer-container-48209" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48209-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you're building directly from source, try running the configure script with the <code>--enable-setcap-install</code> option if you're building with autotools or setting the <code>DUMPCAP_INSTALL_OPTION</code> build option to <code>capabilities</code> if you're building with CMake.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '15, 13:09</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-48209" class="comments-container"></div><div id="comment-tools-48209" class="comment-tools"></div><div class="clear"></div><div id="comment-48209-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

