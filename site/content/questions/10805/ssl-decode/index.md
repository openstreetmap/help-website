+++
type = "question"
title = "SSL decode"
description = '''Hi, I just downloaded the 1.7.1 source and build it by, ./configure; make  When I run this wireshark and try to setup SSL decode (RSA Key list), I don&#x27;t find out any such option in preference/protocols/SSL. All I find is the check-boxes and nothing else.  Do I need to build with some extra flags or ...'''
date = "2012-05-08T23:15:00Z"
lastmod = "2012-05-08T23:57:00Z"
weight = 10805
keywords = [ "ssl" ]
aliases = [ "/questions/10805" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SSL decode](/questions/10805/ssl-decode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10805-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I just downloaded the 1.7.1 source and build it by,</p><pre><code>./configure; make</code></pre><p>When I run this wireshark and try to setup SSL decode (RSA Key list), I don't find out any such option in preference/protocols/SSL. All I find is the check-boxes and nothing else.</p><p>Do I need to build with some extra flags or something?</p><p>BTW, I am on Ubuntu 12.04 and want to write a decoder for some custom messages which are sent over SSL.</p><p>Thanks in advance, Rajib</p></div><div id="question-tags" class="tags-container tags">ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 May '12, 23:15</strong></p><img src="https://secure.gravatar.com/avatar/90d3e9b2815f8bb8bed16ef615b827cb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajib%20Karmakar&#39;s gravatar image" /><p>Rajib Karmakar<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajib Karmakar has no accepted answers">0%</span></p></div></div><div id="comments-container-10805" class="comments-container"></div><div id="comment-tools-10805" class="comment-tools"></div><div class="clear"></div><div id="comment-10805-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10807"></span>

<div id="answer-container-10807" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10807-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please check if GnuTLS is missing on your system. configure will automatically check for it's existence. If it's not available, SSL/TLS decryption will be disabled. Output of configure in this case: "GnuTLS not found, disabling SSL decryption".</p><p><strong>Check results</strong><br />
<code>grep -i gnutls config.log</code><br />
</p><p><strong>Install libgnutls-dev</strong><br />
<code>apt-get install libgnutls-dev</code><br />
</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 May '12, 23:57</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 May '12, 00:17</p></div></div><div id="comments-container-10807" class="comments-container"><span id="10832"></span><div id="comment-10832" class="comment"><div id="post-10832-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Thanks for your reply. I installed the gnutls package but it still remains the same. when I configure wireshark as,</p><pre><code>./configure --with-ssl</code></pre><p>it says that,</p><pre><code>configure: error: SSL crypto library was requested, but is not available</code></pre><p>Please help.</p><p>Regards, Rajib</p></div><div id="comment-10832-info" class="comment-info"><span class="comment-age">(09 May '12, 06:02)</span> Rajib Karmakar</div></div><span id="10833"></span><div id="comment-10833" class="comment"><div id="post-10833-score" class="comment-score"></div><div class="comment-text"><p>(I converted your "answer" to a "comment", please see the FAQ for details on how to use this site best)</p><p>As per the error message, you tell configure to use the SSL libraries, but they are not found on your system. You need to install the GnuTLS (dev) libraries with apt-get. Have a look at the <a href="http://www.wireshark.org/docs/wsdg_html_chunked/">development guide</a> for more details on how to setup up a proper environment to build wireshark yourself.</p></div><div id="comment-10833-info" class="comment-info"><span class="comment-age">(09 May '12, 06:10)</span> SYN-bit ♦♦</div></div><span id="10835"></span><div id="comment-10835" class="comment"><div id="post-10835-score" class="comment-score"></div><div class="comment-text"><p>Just run this command</p><blockquote><p><code>apt-get install libgnutls-dev</code><br />
</p></blockquote><p>and then re-run configure.</p></div><div id="comment-10835-info" class="comment-info"><span class="comment-age">(09 May '12, 06:51)</span> Kurt Knochner ♦</div></div><span id="10841"></span><div id="comment-10841" class="comment"><div id="post-10841-score" class="comment-score">1</div><div class="comment-text"><p><code>apt-get build-dep wireshark</code> should also work.</p></div><div id="comment-10841-info" class="comment-info"><span class="comment-age">(09 May '12, 08:25)</span> Gerald Combs ♦♦</div></div></div><div id="comment-tools-10807" class="comment-tools"></div><div class="clear"></div><div id="comment-10807-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

