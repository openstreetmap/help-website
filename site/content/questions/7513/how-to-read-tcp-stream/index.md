+++
type = "question"
title = "how to read TCP stream"
description = '''I am very new to this so forgive me if my question has a simply answer I am missing. I am trying to decipher a TCP Stream. I see some of the information is readable. However, there is a large section that needs to be decoded. Below is the beginning of what I would like to decode.  &amp;lt;detection&amp;gt; ...'''
date = "2011-11-18T23:06:00Z"
lastmod = "2012-03-22T12:56:00Z"
weight = 7513
keywords = [ "analysis", "stream", "tcp" ]
aliases = [ "/questions/7513" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [how to read TCP stream](/questions/7513/how-to-read-tcp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7513-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am very new to this so forgive me if my question has a simply answer I am missing. I am trying to decipher a TCP Stream. I see some of the information is readable. However, there is a large section that needs to be decoded. Below is the beginning of what I would like to decode.</p><pre><code>&lt;detection&gt;
    &lt;keyId&gt;1&lt;/keyId&gt;
    &lt;data&gt;!CDATA[T8PdjhIeYyFvWdI+lB5Gkh0A1uBtCNt6avFGFV3nzMiU1kZQgVOzF50dAfk8YZOHFEVbptTA/d8QWo7+wJ4vX934tZGjg+bz5wwfGyLMrS9Uq78PnH5EPgtUZwBulHWHL2StofzO94IpMe8A1r7/fMPQ94p3rgPvTvRCCkRifmMV03I1kwn8c7</code></pre><p>Can someone point me in the direction of what I need to do to successfully decode this section of the stream?</p></div><div id="question-tags" class="tags-container tags">analysis stream tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Nov '11, 23:06</strong></p><img src="https://secure.gravatar.com/avatar/512127e76e432c573b41f2cea72100e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="criag0&#39;s gravatar image" /><p>criag0<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="criag0 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Nov '11, 14:57</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-7513" class="comments-container"></div><div id="comment-tools-7513" class="comment-tools"></div><div class="clear"></div><div id="comment-7513-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="7516"></span>

<div id="answer-container-7516" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7516-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What you refer to is a protocol, for that Wireshark has 'dissectors' which decode and present the protocol elements. Now the problem is that the dissectors are to be written according to the specification of the protocol. So you must have that. Then you have to choose what language/API to program against. Most powerful are dissectors in native C, other options are Lua or Python.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '11, 01:12</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-7516" class="comments-container"></div><div id="comment-tools-7516" class="comment-tools"></div><div class="clear"></div><div id="comment-7516-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7519"></span>

<div id="answer-container-7519" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7519-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>"What [you'd] like to decode" looks like XML. Wireshark has an XML dissector, but to dissect it as anything much more than raw text would require the DTD for the XML in question. See <a href="http://wiki.wireshark.org/XML">the Wireshark Wiki page on XML</a> for more information.</p><p>You'd also need to have Wireshark somehow invoke the XML dissector for the data in question. Is this just raw XML over a TCP connection, or is it, for example, XML transported over HTTP?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '11, 13:04</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-7519" class="comments-container"><span id="7583"></span><div id="comment-7583" class="comment"><div id="post-7583-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the information I will read over what you have provided.</p><p>The information i believe is raw XML. I am trying to see what was transmitted back to a company when installing a program on my computer.</p><p>Thank you in advance.</p></div><div id="comment-7583-info" class="comment-info"><span class="comment-age">(23 Nov '11, 10:04)</span> criag0</div></div></div><div id="comment-tools-7519" class="comment-tools"></div><div class="clear"></div><div id="comment-7519-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9708"></span>

<div id="answer-container-9708" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9708-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What you see inside the CDATA section is a base64encoded representation of (potentially) binary information. You can try base64 decoding it, but if the result is not readable as text then the program which is "checking in" has its own proprietary format for sending whatever data it has collected about your machine, etc.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '12, 12:56</strong></p><img src="https://secure.gravatar.com/avatar/b64129b7a3bf2a9f1760fbdee1b3b74c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="inetdog&#39;s gravatar image" /><p>inetdog<br />
<span class="score" title="167 reputation points">167</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="inetdog has 3 accepted answers">14%</span></p></div></div><div id="comments-container-9708" class="comments-container"></div><div id="comment-tools-9708" class="comment-tools"></div><div class="clear"></div><div id="comment-9708-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

