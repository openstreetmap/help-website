+++
type = "question"
title = "Problem updating Wireshark in Ubuntu 16.04"
description = '''Hi I am running Ubuntu 16.04 and have Wireshark 2.0.2 installed. I want to update it to the latest version supported by that o/s and so did: $ sudo -E apt-get install wireshark Reading package lists... Done Building dependency tree  Reading state information... Done wireshark is already the newest v...'''
date = "2017-07-24T07:10:00Z"
lastmod = "2017-07-24T07:57:00Z"
weight = 63044
keywords = [ "installation", "ubuntu" ]
aliases = [ "/questions/63044" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Problem updating Wireshark in Ubuntu 16.04](/questions/63044/problem-updating-wireshark-in-ubuntu-1604)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63044-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I am running Ubuntu 16.04 and have Wireshark 2.0.2 installed. I want to update it to the latest version supported by that o/s and so did:</p><pre><code>$ sudo -E apt-get install wireshark
Reading package lists... Done
Building dependency tree       
Reading state information... Done
wireshark is already the newest version (2.2.7-1~xenial1).
0 to upgrade, 0 to newly install, 0 to remove and 13 not to upgrade.</code></pre><p>But when I run Wireshark from the command line, version 2.0.2 still starts up.</p><p>In case it helps:</p><pre><code>$ which wireshark
/usr/bin/wireshark
[email protected]:~$ /usr/bin/wireshark --version
Wireshark 2.0.2 (SVN Rev Unknown from unknown)</code></pre><p>Do I need to explicitly uninstall 2.0.2? If so, how?</p><p>Best regards</p><p>David</p></div><div id="question-tags" class="tags-container tags">installation ubuntu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jul '17, 07:10</strong></p><img src="https://secure.gravatar.com/avatar/cfb0228285e3c9494d763ba825e7a76c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DavidA_2015&#39;s gravatar image" /><p>DavidA_2015<br />
<span class="score" title="11 reputation points">11</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DavidA_2015 has one accepted answer">50%</span></p></div></div><div id="comments-container-63044" class="comments-container"><span id="63047"></span><div id="comment-63047" class="comment"><div id="post-63047-score" class="comment-score"></div><div class="comment-text"><p>What is the list of files installed by the package, e.g. <code>dpkg -L wireshark</code>, has the binary been put somewhere else?</p></div><div id="comment-63047-info" class="comment-info"><span class="comment-age">(24 Jul '17, 07:40)</span> grahamb ♦</div></div><span id="63048"></span><div id="comment-63048" class="comment"><div id="post-63048-score" class="comment-score"></div><div class="comment-text"><p><code> ~$  dpkg -L wireshark /. /usr /usr/share /usr/share/doc /usr/share/doc/wireshark /usr/share/doc/wireshark/README.Debian /usr/share/doc/wireshark/changelog.Debian.gz /usr/share/doc/wireshark/copyright</code></p></div><div id="comment-63048-info" class="comment-info"><span class="comment-age">(24 Jul '17, 07:42)</span> DavidA_2015</div></div></div><div id="comment-tools-63044" class="comment-tools"></div><div class="clear"></div><div id="comment-63044-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63049"></span>

<div id="answer-container-63049" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63049-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As you can see the package you've installed is just the debian README. Looking for other Ubuntu packages for Wireshark I can see wireshark-qt and wireshark-gtk for the Qt and GTK+ versions respectively that might do what you want.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '17, 07:57</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-63049" class="comments-container"></div><div id="comment-tools-63049" class="comment-tools"></div><div class="clear"></div><div id="comment-63049-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

