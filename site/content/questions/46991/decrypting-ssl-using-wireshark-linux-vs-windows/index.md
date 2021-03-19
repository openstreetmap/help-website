+++
type = "question"
title = "Decrypting SSL using Wireshark Linux vs Windows"
description = '''I&#x27;m working on decrypting my own traffic that gets sent through Wireshark and I&#x27;ve been following this guide for reference. I have been using the SSLKEYLOGFILE environment variable and I can get the key files populated on both Windows 8.1 and Ubuntu 14.04 LTS.  The test I&#x27;m using is logging on to Fa...'''
date = "2015-10-27T09:10:00Z"
lastmod = "2015-10-29T02:53:00Z"
weight = 46991
keywords = [ "windows", "ssl", "decryption", "linux" ]
aliases = [ "/questions/46991" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Decrypting SSL using Wireshark Linux vs Windows](/questions/46991/decrypting-ssl-using-wireshark-linux-vs-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46991-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm working on decrypting my own traffic that gets sent through Wireshark and I've been following <a href="https://jimshaver.net/2015/02/11/decrypting-tls-browser-traffic-with-wireshark-the-easy-way/">this guide</a> for reference. I have been using the <code>SSLKEYLOGFILE</code> environment variable and I can get the key files populated on both Windows 8.1 and Ubuntu 14.04 LTS.</p><p>The test I'm using is logging on to Facebook and looking for the Decrypted SSL Data tab on Wireshark. It appears while running Windows, but it's nowhere to be found on Linux. I've also noticed that in the Protocol tab, SSL will appear among all the protocols in Windows, but it's nowhere to be found on the Linux version. Both still show TLSv1.2, so I don't believe I'm connecting to an unsecured version of Facebook.</p><p>The Linux version of Wireshark is compiled with GnuTLS 2.12.23, so that is not the issue either. Can anyone help?</p></div><div id="question-tags" class="tags-container tags">windows ssl decryption linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Oct '15, 09:10</strong></p><img src="https://secure.gravatar.com/avatar/2fd6399acaba8522401cb2e0474a3fa2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="testmagee&#39;s gravatar image" /><p>testmagee<br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="testmagee has no accepted answers">0%</span></p></div></div><div id="comments-container-46991" class="comments-container"><span id="46992"></span><div id="comment-46992" class="comment"><div id="post-46992-score" class="comment-score"></div><div class="comment-text"><p>What's the version of Wireshark on Windows and Linux?</p></div><div id="comment-46992-info" class="comment-info"><span class="comment-age">(27 Oct '15, 09:40)</span> Kurt Knochner ♦</div></div><span id="46994"></span><div id="comment-46994" class="comment"><div id="post-46994-score" class="comment-score"></div><div class="comment-text"><p>My version is 1.10.6 on Linux and 1.12.8 on Windows.</p></div><div id="comment-46994-info" class="comment-info"><span class="comment-age">(27 Oct '15, 10:24)</span> testmagee</div></div></div><div id="comment-tools-46991" class="comment-tools"></div><div class="clear"></div><div id="comment-46991-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47051"></span>

<div id="answer-container-47051" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47051-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark 1.10.x has <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9144">some bugs</a> that might prevent successful decryption of SSL/TLS data. Version 1.12 has seen many improvements in that area and is recommended. On Ubuntu 14.04, you can <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9144">install</a> the <a href="https://launchpad.net/~wireshark-dev/+archive/ubuntu/stable">wireshark-dev/stable</a> PPA:</p><pre><code>sudo apt-add-repository ppa:wireshark-dev/stable
sudo apt-get update
sudo apt-get upgrade</code></pre><p>That repository is currently maintained by the Debian maintainer of Wireshark. The current version in that repo is wireshark 1.12.8+g5b6e543-2~trusty1.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Oct '15, 02:53</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-47051" class="comments-container"><span id="47078"></span><div id="comment-47078" class="comment"><div id="post-47078-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much. I previously installed from the Ubuntu software center. I guess it didn't have the most recent version. This solved my issue.</p></div><div id="comment-47078-info" class="comment-info"><span class="comment-age">(29 Oct '15, 14:52)</span> testmagee</div></div></div><div id="comment-tools-47051" class="comment-tools"></div><div class="clear"></div><div id="comment-47051-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

