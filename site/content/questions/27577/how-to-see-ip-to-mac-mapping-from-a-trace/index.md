+++
type = "question"
title = "How to see IP to MAC mapping from a trace"
description = '''Hi, this is my first post here.  I have a trace I&#x27;m analyzing, and I need to extract a list of all ip addresses with the corresponding mac addresses. Or the other way around, either way is fine.  Thank you, Michael'''
date = "2013-11-29T16:26:00Z"
lastmod = "2013-11-29T20:42:00Z"
weight = 27577
keywords = [ "ip", "mac", "mapping", "to" ]
aliases = [ "/questions/27577" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to see IP to MAC mapping from a trace](/questions/27577/how-to-see-ip-to-mac-mapping-from-a-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27577-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, this is my first post here.</p><p>I have a trace I'm analyzing, and I need to extract a list of all ip addresses with the corresponding mac addresses. Or the other way around, either way is fine.</p><p>Thank you, Michael</p></div><div id="question-tags" class="tags-container tags">ip mac mapping to</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Nov '13, 16:26</strong></p><img src="https://secure.gravatar.com/avatar/ad8bbf0e30f89bf79f0362afa8c0f04a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MichaelSB&#39;s gravatar image" /><p>MichaelSB<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MichaelSB has no accepted answers">0%</span></p></div></div><div id="comments-container-27577" class="comments-container"></div><div id="comment-tools-27577" class="comment-tools"></div><div class="clear"></div><div id="comment-27577-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27579"></span>

<div id="answer-container-27579" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27579-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You might want to use <code>tshark</code>, rather than <code>wireshark</code>, for this purpose. Assuming Ethernet encapsulation, you could try extracting each source MAC/IP address pair and each destination MAC/IP address pair using something along the lines of:</p><p><code>     tshark -r infile.pcap -T fields -e eth.src -e ip.src -e eth.dst -e ip.dst &gt; tmp.txt     sort -u tmp.txt &gt; mac_ip.txt</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Nov '13, 20:42</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-27579" class="comments-container"><span id="27581"></span><div id="comment-27581" class="comment"><div id="post-27581-score" class="comment-score"></div><div class="comment-text"><p>Thanks! Just what I needed. I wonder why this is not available in Wireshark GUI.</p></div><div id="comment-27581-info" class="comment-info"><span class="comment-age">(29 Nov '13, 22:07)</span> MichaelSB</div></div></div><div id="comment-tools-27579" class="comment-tools"></div><div class="clear"></div><div id="comment-27579-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

