+++
type = "question"
title = "Dissector extra info"
description = '''Hello, I&#x27;m trying to build a protocol dissector. The dissector works just fine, however the problem is the body is encrypted. I already reversed everything and i can retrieve the session key from within the dissector (its hackish but w/e). However as the key changes, and we can not store extra info ...'''
date = "2012-03-12T16:46:00Z"
lastmod = "2012-03-12T18:34:00Z"
weight = 9501
keywords = [ "decryption", "dissector", "plugin" ]
aliases = [ "/questions/9501" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Dissector extra info](/questions/9501/dissector-extra-info)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9501-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm trying to build a protocol dissector.</p><p>The dissector works just fine, however the problem is the body is encrypted. I already reversed everything and i can retrieve the session key from within the dissector (its hackish but w/e).</p><p>However as the key changes, and we can not store extra info somewhere to link a key to a pcap file.</p><p>So my question is, is there a way to: A) Store the key somewhere related to pcap file to load the key in the dissector for each pcap file B) Save modified packets to pcap file (its a hell, already tried, but perhaps i looked wrong)</p><p>Kind regards, ~Intline9</p></div><div id="question-tags" class="tags-container tags">decryption dissector plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Mar '12, 16:46</strong></p><img src="https://secure.gravatar.com/avatar/89122178d3ce7d3cf4c61718875a95d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Intline9&#39;s gravatar image" /><p>Intline9<br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Intline9 has no accepted answers">0%</span></p></div></div><div id="comments-container-9501" class="comments-container"></div><div id="comment-tools-9501" class="comment-tools"></div><div class="clear"></div><div id="comment-9501-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9503"></span>

<div id="answer-container-9503" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9503-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>A) The capture files that Wireshark can read can be in a number of formats; the <em>only</em> format that allows arbitrary information of that sort to be stored in it is pcap-NG format, so that's not a general solution. It also involves registering a new block type for pcap-NG and adding code to support that.</p><p>B) Wireshark does not support saving decrypted data out in a conversation (that's why it was hell to try to do so).</p><p>Your only general alternative would be to store the extra information in another file, with a preference pointing to that file, or store it in a preference; that's what's used for the other flavors of decryption supported by Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Mar '12, 18:34</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-9503" class="comments-container"><span id="9886"></span><div id="comment-9886" class="comment"><div id="post-9886-score" class="comment-score"></div><div class="comment-text"><p>After loads of thinkin i thought of another way, we could keep track of packet stream key pairs by getting a checksum of a packet we know that is unique each session and save the checksum with the session key.</p><p>Working now to implement that!</p></div><div id="comment-9886-info" class="comment-info"><span class="comment-age">(01 Apr '12, 08:59)</span> Intline9</div></div></div><div id="comment-tools-9503" class="comment-tools"></div><div class="clear"></div><div id="comment-9503-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

