+++
type = "question"
title = "Link own libpcap.a"
description = '''Hey, I downloaded the wireshark source code and I was wondering if it&#x27;s possible to link my own libpcap.a?'''
date = "2012-03-08T12:08:00Z"
lastmod = "2012-03-08T14:36:00Z"
weight = 9439
keywords = [ "link", "library", "libpcap" ]
aliases = [ "/questions/9439" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Link own libpcap.a](/questions/9439/link-own-libpcapa)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9439-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey, I downloaded the wireshark source code and I was wondering if it's possible to link my own libpcap.a?</p></div><div id="question-tags" class="tags-container tags">link library libpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Mar '12, 12:08</strong></p><img src="https://secure.gravatar.com/avatar/22d944885f6c4d1f1364c00035916d80?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Freaky&#39;s gravatar image" /><p>Freaky<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Freaky has no accepted answers">0%</span></p></div></div><div id="comments-container-9439" class="comments-container"></div><div id="comment-tools-9439" class="comment-tools"></div><div class="clear"></div><div id="comment-9439-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9445"></span>

<div id="answer-container-9445" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9445-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You'd have to install your own libpcap.a (or libpcap shared library) and:</p><ul><li>if you're building Wireshark with autotools, so that you're running the <code>./configure</code> script before you run <code>make</code>, you need to run the configure script with the <code>--with-pcap=</code><em>directory</em> command-line option, where <em>directory</em> is the install directory for your libpcap ("install directory" doesn't mean "the directory containing the library", it's the directory above that, e.g. if it's in <code>/usr/local/lib</code>, <em>directory</em> would be <code>/usr/local</code>; you would also have to install libpcap's header files as well);</li><li>if you're building Wireshark with CMake, so that you're running <code>cmake</code> before you run <code>make</code>, you need to run cmake with the <code>-DCMAKE_PREFIX_PATH=</code><em>directory</em> command-line option, where <em>directory</em> is the install directory for your libpcap.</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Mar '12, 14:36</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 May '16, 16:08</p></div></div><div id="comments-container-9445" class="comments-container"><span id="9450"></span><div id="comment-9450" class="comment"><div id="post-9450-score" class="comment-score"></div><div class="comment-text"><p>Thank you, but how do I configure Wireshark with the parameter? Is there a configuration file or do I add the parameter when I build/compile it?</p></div><div id="comment-9450-info" class="comment-info"><span class="comment-age">(08 Mar '12, 23:46)</span> Freaky</div></div><span id="9457"></span><div id="comment-9457" class="comment"><div id="post-9457-score" class="comment-score"></div><div class="comment-text"><p>That's a parameter for the configure step in the build.</p></div><div id="comment-9457-info" class="comment-info"><span class="comment-age">(09 Mar '12, 08:27)</span> Jaap ♦</div></div><span id="9460"></span><div id="comment-9460" class="comment"><div id="post-9460-score" class="comment-score">1</div><div class="comment-text"><p>And, in fact, I already said, in my answer, how to set that parameter:</p><blockquote><p>...and configure Wireshark with <code>--with-pcap=</code><em>directory</em>, where <em>directory</em> is the install directory for your libpcap ("install directory" doesn't mean "the directory containing the library", it's the directory above that, e.g. if it's in <code>/usr/local/lib</code>, <em>directory</em> would be <code>/usr/local</code>; you would also have to install libpcap's header files as well).</p></blockquote><p>"configure wireshark with..." means "run Wireshark's <code>configure</code> script with ... as an argument".</p></div><div id="comment-9460-info" class="comment-info"><span class="comment-age">(09 Mar '12, 10:32)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-9445" class="comment-tools"></div><div class="clear"></div><div id="comment-9445-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

