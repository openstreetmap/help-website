+++
type = "question"
title = "Packet Capture Appliance Server"
description = '''I&#x27;m wondering if anyone on this board has experience to recommend (or not) a dedicated packet capture appliance. The goal would be to separate the idea of packet analysers/probes from the time-sensitive capture process itself, such that mirrors or a tap network would feed a central &quot;packet capture a...'''
date = "2016-02-24T14:38:00Z"
lastmod = "2016-02-25T01:35:00Z"
weight = 50490
keywords = [ "capture" ]
aliases = [ "/questions/50490" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Packet Capture Appliance Server](/questions/50490/packet-capture-appliance-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50490-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm wondering if anyone on this board has experience to recommend (or not) a dedicated packet capture appliance. The goal would be to separate the idea of packet analysers/probes from the time-sensitive capture process itself, such that mirrors or a tap network would feed a central "packet capture appliance", and that system would make resulting packet capture files available to remote servers for analysis (be it wireshark, snort, etc.).</p><p>A short list of things that such a system would need to do well:</p><ul><li>Record timestamps very accurately, preferably with nanosecond precision.</li><li>Write captures to disk very rapidly, such that several Gbps of payload on incoming interfaces would not exceed the rate at which capture data can be stored.</li><li>Disk capacity would need to be a lot, and ideally would be redundant/recoverable.</li><li>Ideally, the ability to sort/organize capture data based on app-level criteria would help (allowing some of this type of responsibilty to be offloaded from probes).</li><li>Ideally, the ability to host packet captures to remote Wireshark clients (via the GUI "remote interface").</li><li>Should to be rack-mountable (no need for portability).</li></ul><p>While an off-the-shelf server can do most of this, I also know that a few vendors have dedicated appliances tailored to some of these kinds of capture-specific requirements. So, my overall question here is, do people here have any good/bad experience to share about such appliances? In such a niche space, are there any that particularly stand out? Realizing it isn't directly a Wireshark tool question, I'm not sure if there is a better place where such a question would be asked.</p></div><div id="question-tags" class="tags-container tags">capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Feb '16, 14:38</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-50490" class="comments-container"><span id="50509"></span><div id="comment-50509" class="comment"><div id="post-50509-score" class="comment-score"></div><div class="comment-text"><p>if you send me an email creusch[at]crnetworks.de I can provide you my experience</p></div><div id="comment-50509-info" class="comment-info"><span class="comment-age">(25 Feb '16, 09:16)</span> Christian_R</div></div></div><div id="comment-tools-50490" class="comment-tools"></div><div class="clear"></div><div id="comment-50490-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50496"></span>

<div id="answer-container-50496" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50496-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I can recommend the <a href="http://www.riverbed.com/products/steelcentral/network-performance-management/application-aware-network-performance-management/steelcentral-netshark.html">NetShark appliances</a> (hardware as well as virtual) from Riverbed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Feb '16, 01:35</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p>Uli<br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div></div><div id="comments-container-50496" class="comments-container"></div><div id="comment-tools-50496" class="comment-tools"></div><div class="clear"></div><div id="comment-50496-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

