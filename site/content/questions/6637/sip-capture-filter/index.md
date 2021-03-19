+++
type = "question"
title = "SIP capture filter"
description = '''Hi, I&#x27;m trying to apply a filter to capture only SIP traffic and running into an odd situation. When I leave wireshark with no capture filter, I see the packets I want to capture from host X to host Y on UDP port 5060. So I applied these filters on the capture options screen one by one: -port 5060 -...'''
date = "2011-09-29T09:26:00Z"
lastmod = "2011-09-29T09:46:00Z"
weight = 6637
keywords = [ "capture", "sip", "filters" ]
aliases = [ "/questions/6637" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [SIP capture filter](/questions/6637/sip-capture-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6637-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm trying to apply a filter to capture only SIP traffic and running into an odd situation. When I leave wireshark with no capture filter, I see the packets I want to capture from host X to host Y on UDP port 5060.</p><p>So I applied these filters on the capture options screen one by one: -port 5060 -udp port 5060 -host X</p><p>All of them returned nothing. Is there something I'm missing here?</p></div><div id="question-tags" class="tags-container tags">capture sip filters</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Sep '11, 09:26</strong></p><img src="https://secure.gravatar.com/avatar/747b439daf0b71f45c74d62b55d16885?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CulverTech&#39;s gravatar image" /><p>CulverTech<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CulverTech has no accepted answers">0%</span></p></div></div><div id="comments-container-6637" class="comments-container"></div><div id="comment-tools-6637" class="comment-tools"></div><div class="clear"></div><div id="comment-6637-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6638"></span>

<div id="answer-container-6638" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6638-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>My bet would be that the SIP traffic is vlan tagged (you can check this by looking closer to the unfiltered SIP traffic). If this is true, prepend your capture filters with "vlan and ..." so the filters will become:</p><pre><code>vlan and port 5060
vlan and udp port 5060
vlan and host X</code></pre><p>Hope this helps.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '11, 09:46</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-6638" class="comments-container"><span id="6640"></span><div id="comment-6640" class="comment"><div id="post-6640-score" class="comment-score"></div><div class="comment-text"><p>Aha! yes, they're tagged, didn't realize I had to add that to the filter. Thanks so much</p></div><div id="comment-6640-info" class="comment-info"><span class="comment-age">(29 Sep '11, 10:02)</span> CulverTech</div></div></div><div id="comment-tools-6638" class="comment-tools"></div><div class="clear"></div><div id="comment-6638-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

