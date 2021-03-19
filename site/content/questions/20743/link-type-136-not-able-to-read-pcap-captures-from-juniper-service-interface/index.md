+++
type = "question"
title = "link type 136 (not able to read pcap captures from juniper service interface)"
description = '''hi all: i captured some data and stored as pcap format on a service interface of juniper mx960 (sp-1/0/0) but i am not able to open them up since i keep getting following errors: &quot;The file &amp;lt;whatever-name.pcap&amp;gt; is capture of for a network type that Wireshark doesn&#x27;t support (pcap: network type ...'''
date = "2013-04-23T14:16:00Z"
lastmod = "2013-04-23T14:30:00Z"
weight = 20743
keywords = [ "linktype", "juniper" ]
aliases = [ "/questions/20743" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [link type 136 (not able to read pcap captures from juniper service interface)](/questions/20743/link-type-136-not-able-to-read-pcap-captures-from-juniper-service-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20743-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi all:</p><p>i captured some data and stored as pcap format on a service interface of juniper mx960 (sp-1/0/0) but i am not able to open them up since i keep getting following errors:</p><p>"The file &lt;whatever-name.pcap&gt; is capture of for a network type that Wireshark doesn't support (pcap: network type 136 unknown or unsupported)"</p><p>i checked the list of tcpdump supported link types and it doesn't have 136. does it mean i would not be able to view the pcap files at all?</p><p>are there any possible workarounds for this?</p><p>thanks</p><p>_m</p></div><div id="question-tags" class="tags-container tags">linktype juniper</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '13, 14:16</strong></p><img src="https://secure.gravatar.com/avatar/454eee520803ce3243a9c988f6d3707c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="desperado&#39;s gravatar image" /><p>desperado<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="desperado has no accepted answers">0%</span></p></div></div><div id="comments-container-20743" class="comments-container"></div><div id="comment-tools-20743" class="comment-tools"></div><div class="clear"></div><div id="comment-20743-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20746"></span>

<div id="answer-container-20746" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20746-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What version of Wireshark are you using? Support for the Juniper Services PIC was <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8513">added a month ago</a>. It is available in the current <a href="http://www.wireshark.org/download/automated/">development packages</a> and will be in 1.10.0 when it is released.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '13, 14:30</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-20746" class="comments-container"><span id="20747"></span><div id="comment-20747" class="comment"><div id="post-20747-score" class="comment-score"></div><div class="comment-text"><p>thanks gerald. so i should be able to read those files if i install "development packages"?</p></div><div id="comment-20747-info" class="comment-info"><span class="comment-age">(23 Apr '13, 14:41)</span> desperado</div></div><span id="20748"></span><div id="comment-20748" class="comment"><div id="post-20748-score" class="comment-score"></div><div class="comment-text"><p>btw, which package under <a href="http://www.wireshark.org/download/automated/win32/">http://www.wireshark.org/download/automated/win32/</a> should i install?</p></div><div id="comment-20748-info" class="comment-info"><span class="comment-age">(23 Apr '13, 14:44)</span> desperado</div></div><span id="20749"></span><div id="comment-20749" class="comment"><div id="post-20749-score" class="comment-score"></div><div class="comment-text"><p>thanks gerald: yeah it works!</p><p>best</p><p>_m</p></div><div id="comment-20749-info" class="comment-info"><span class="comment-age">(23 Apr '13, 15:00)</span> desperado</div></div></div><div id="comment-tools-20746" class="comment-tools"></div><div class="clear"></div><div id="comment-20746-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

