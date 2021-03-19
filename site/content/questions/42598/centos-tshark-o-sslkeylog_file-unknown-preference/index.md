+++
type = "question"
title = "centos tshark -o ssl.keylog_file unknown preference"
description = '''I&#x27;m on CentOS 6.4 and followed the instructions at http://unix.stackexchange.com/a/192567 in order to get wireshark 1.12.4 running. the installation seems to be successful and tshark -v shows version 1.12.4. when I run the command tshark -r mypcap.pcapng -o &quot;ssl.keylog_file:keylog.txt&quot; -qz follow,ss...'''
date = "2015-05-21T04:18:00Z"
lastmod = "2015-05-21T06:18:00Z"
weight = 42598
keywords = [ "ssl", "centos" ]
aliases = [ "/questions/42598" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [centos tshark -o ssl.keylog\_file unknown preference](/questions/42598/centos-tshark-o-sslkeylog_file-unknown-preference)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42598-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm on CentOS 6.4 and followed the instructions at <a href="http://unix.stackexchange.com/a/192567">http://unix.stackexchange.com/a/192567</a> in order to get wireshark 1.12.4 running. the installation seems to be successful and tshark -v shows version 1.12.4.</p><p>when I run the command</p><pre><code>tshark -r mypcap.pcapng -o &quot;ssl.keylog_file:keylog.txt&quot; -qz follow,ssl,ascii,1 &gt; &quot;ssl.stream.1.txt&quot;</code></pre><p>i get the error</p><pre><code>tshark -o &quot;ssl.keylog_file:keylog.txt&quot; unknown preference</code></pre><p>did I miss something? why is the preference unknown?</p></div><div id="question-tags" class="tags-container tags">ssl centos</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 May '15, 04:18</strong></p><img src="https://secure.gravatar.com/avatar/47ec8baf3c5b06ac0aa861705428d6c4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="divadpoc&#39;s gravatar image" /><p>divadpoc<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="divadpoc has no accepted answers">0%</span></p></div></div><div id="comments-container-42598" class="comments-container"><span id="42600"></span><div id="comment-42600" class="comment"><div id="post-42600-score" class="comment-score"></div><div class="comment-text"><p>Show us all of the tshark -v output. Does it include support for SSL?</p></div><div id="comment-42600-info" class="comment-info"><span class="comment-age">(21 May '15, 06:12)</span> Jaap ♦</div></div></div><div id="comment-tools-42598" class="comment-tools"></div><div class="clear"></div><div id="comment-42598-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42601"></span>

<div id="answer-container-42601" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42601-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think I figured it out, with the help from <a href="https://ask.wireshark.org/questions/10805/ssl-decode">https://ask.wireshark.org/questions/10805/ssl-decode</a></p><p>I added the following dependencies:</p><pre><code>yum install -y gnutls gnutls-devel openssl openssl-devel crypto-utils</code></pre><p>and had to call configure with "--with-ssl"</p><pre><code>./configure --with-gtk2 --with-ssl</code></pre><p>If I got something wrong please correct me, but for now it's working</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 May '15, 06:18</strong></p><img src="https://secure.gravatar.com/avatar/47ec8baf3c5b06ac0aa861705428d6c4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="divadpoc&#39;s gravatar image" /><p>divadpoc<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="divadpoc has no accepted answers">0%</span></p></div></div><div id="comments-container-42601" class="comments-container"><span id="42602"></span><div id="comment-42602" class="comment"><div id="post-42602-score" class="comment-score"></div><div class="comment-text"><p>Yeah, that should do it. Except that you don't (AFAIK) need openssl/openssl-devel/--with-ssl . gnutls is sufficient.</p></div><div id="comment-42602-info" class="comment-info"><span class="comment-age">(21 May '15, 07:41)</span> JeffMorriss ♦</div></div><span id="42603"></span><div id="comment-42603" class="comment"><div id="post-42603-score" class="comment-score">1</div><div class="comment-text"><p>So your initial build was without SSL support, therefore that instance of tshark did not understand the preference ssl.keylog_file. This is because the code that registers that preference does not get build when the required conditions are not met, ie. the build is not configured for the required libraries.</p></div><div id="comment-42603-info" class="comment-info"><span class="comment-age">(21 May '15, 07:46)</span> Jaap ♦</div></div><span id="42716"></span><div id="comment-42716" class="comment"><div id="post-42716-score" class="comment-score"></div><div class="comment-text"><p>thanks for the infos. @JeffMorriss I'll try without openssl at some point. @Jaap, I didn't know I had to tell him explicitly that I want --with-ssl</p></div><div id="comment-42716-info" class="comment-info"><span class="comment-age">(28 May '15, 00:05)</span> divadpoc</div></div></div><div id="comment-tools-42601" class="comment-tools"></div><div class="clear"></div><div id="comment-42601-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

