+++
type = "question"
title = "Can wireshark be used to identify AFDX(Avionics Full Duplex Switched Ethernet) frame?"
description = '''I want to know, can wireshark identify AFDX protocol? Or has anybody used wireshark to analyze AFDX frame? Many thanks.'''
date = "2012-09-04T01:29:00Z"
lastmod = "2017-04-24T02:49:00Z"
weight = 14012
keywords = [ "wireshark_afdx" ]
aliases = [ "/questions/14012" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can wireshark be used to identify AFDX(Avionics Full Duplex Switched Ethernet) frame?](/questions/14012/can-wireshark-be-used-to-identify-afdxavionics-full-duplex-switched-ethernet-frame)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14012-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to know, can wireshark identify AFDX protocol? Or has anybody used wireshark to analyze AFDX frame? Many thanks.</p></div><div id="question-tags" class="tags-container tags">wireshark_afdx</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Sep '12, 01:29</strong></p><img src="https://secure.gravatar.com/avatar/6f9a621604229d9d89d0d667c8689094?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gmyun&#39;s gravatar image" /><p>gmyun<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gmyun has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Sep '12, 22:39</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-14012" class="comments-container"></div><div id="comment-tools-14012" class="comment-tools"></div><div class="clear"></div><div id="comment-14012-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="14024"></span>

<div id="answer-container-14024" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14024-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>there is no AFDX dissector in the official code of Wireshark. So, no it cannot dissect that protocol.</p><blockquote><p>Or is there somebody has used wireshark to anylise AFDX frame?</p></blockquote><p>Hard to say. A lot of people/companies write their own plugins, but never publish the code. I bet, there is a AFDX plugin out there. See the following post:</p><blockquote><p><code>http://www.wireshark.org/lists/wireshark-dev/200803/msg00287.html</code></p></blockquote><p><strong>Cite:</strong> I already developped 2 wireshark plugins (dll) to dissect AFDX payloads included in A380 CMS messages.</p><p>I suggest to contact the author of the plugin and ask if he can provide it to you.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Sep '12, 02:34</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-14024" class="comments-container"><span id="14029"></span><div id="comment-14029" class="comment"><div id="post-14029-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I am learning AFDX Tools(a tool for sending, monitoring, filtering, recording and analysing of AFDX data)Guide, in the doc it said that"Wireshark is a free Ethernet analyzer and monitoring tool. You can use it to capture AFDX data and use the recorded file as input for the AFDX Tools." So I think maybe wireshark can be used to detect AFDX data, or maybe the data is only raw data that has not been dissected.</p></div><div id="comment-14029-info" class="comment-info"><span class="comment-age">(04 Sep '12, 04:16)</span> gmyun</div></div><span id="14031"></span><div id="comment-14031" class="comment"><div id="post-14031-score" class="comment-score"></div><div class="comment-text"><p>Wireshark can capture the data as AFDX is based on Ethernet, but it cannot "interpret" the AFDX protocol. That's why you need special AFDX Tools, unless you have a AFDX dissector in Wireshark (see my answer).</p></div><div id="comment-14031-info" class="comment-info"><span class="comment-age">(04 Sep '12, 04:33)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-14024" class="comment-tools"></div><div class="clear"></div><div id="comment-14024-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="60999"></span>

<div id="answer-container-60999" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60999-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can try this one:</p><p><a href="https://github.com/redlab-i/wireshark-plugin-afdx">https://github.com/redlab-i/wireshark-plugin-afdx</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Apr '17, 02:49</strong></p><img src="https://secure.gravatar.com/avatar/77cf013f3ec6cb326b88fe89a2c6c054?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gerasiov&#39;s gravatar image" /><p>gerasiov<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gerasiov has no accepted answers">0%</span></p></div></div><div id="comments-container-60999" class="comments-container"></div><div id="comment-tools-60999" class="comment-tools"></div><div class="clear"></div><div id="comment-60999-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

