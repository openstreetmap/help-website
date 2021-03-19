+++
type = "question"
title = "preserve the original packet number after applying a filter on a pcap file"
description = '''hi there i want to apply a filter on pcap file to filter the RTP packets, but when i do that the packet number changes and starts from 1 . i know this should be like this, but i need to know the previous packet number, so i can modify the corresponding packet in the original pcap file . tnx'''
date = "2012-08-28T07:51:00Z"
lastmod = "2012-08-31T14:48:00Z"
weight = 13934
keywords = [ "number", "packet" ]
aliases = [ "/questions/13934" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [preserve the original packet number after applying a filter on a pcap file](/questions/13934/preserve-the-original-packet-number-after-applying-a-filter-on-a-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13934-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi there i want to apply a filter on pcap file to filter the RTP packets, but when i do that the packet number changes and starts from 1 . i know this should be like this, but i need to know the previous packet number, so i can modify the corresponding packet in the original pcap file . tnx</p></div><div id="question-tags" class="tags-container tags">number packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Aug '12, 07:51</strong></p><img src="https://secure.gravatar.com/avatar/fb8d994046301235446cac25ccced08d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="reza&#39;s gravatar image" /><p>reza<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="reza has no accepted answers">0%</span></p></div></div><div id="comments-container-13934" class="comments-container"></div><div id="comment-tools-13934" class="comment-tools"></div><div class="clear"></div><div id="comment-13934-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="13946"></span>

<div id="answer-container-13946" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13946-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p><em>"..., so i can modify the corresponding packet in the <strong>original</strong> pcap file ."</em></p></blockquote><p>In reading this, I believe <a href="http://ask.wireshark.org/users/3332/reza">reza</a> has filtered RTP packets from one capture file and saved those filtered RTP packets into a new capture file. In this case, the packets will be renumbered in the newly created capture file.</p><p>I recall in a somewhat recent discussion, on -dev I think, that there was a desire to add this capability (being able to track things like original capture file frame numbers, etc.) using pcapng, but as far as I am aware, there is no support for this yet. I have added a bullet item to the <a href="http://wiki.wireshark.org/Development/PcapNg#Wishlist">pcapng wishlist</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Aug '12, 15:58</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-13946" class="comments-container"></div><div id="comment-tools-13946" class="comment-tools"></div><div class="clear"></div><div id="comment-13946-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13943"></span>

<div id="answer-container-13943" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13943-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>but when i do that the packet number changes and starts from 1</p></blockquote><p>it does <strong>not</strong> do that on my system (Win XP SP3) for Wireshark 1.6.x and 1.8.x, if I apply a display filter for an already opened pcap file!</p><ul><li>What is your Wireshark version?</li><li>Can you please test with the latest Wireshark version?</li></ul><p>However, it <strong>does 'renumber'</strong> the frames if you apply a display filter while opening a pcap file. If <strong>that</strong> is your problem, just open the whole file <strong>without filter</strong> and then apply the display filter.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Aug '12, 11:13</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Aug '12, 11:23</p></div></div><div id="comments-container-13943" class="comments-container"></div><div id="comment-tools-13943" class="comment-tools"></div><div class="clear"></div><div id="comment-13943-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13976"></span>

<div id="answer-container-13976" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13976-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I solved my problem by using the sequence number of packets instead of frame number, but having the feature to be able to track the original packet after applying a filter is very useful, tnx christopher</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Aug '12, 14:48</strong></p><img src="https://secure.gravatar.com/avatar/fb8d994046301235446cac25ccced08d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="reza&#39;s gravatar image" /><p>reza<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="reza has no accepted answers">0%</span></p></div></div><div id="comments-container-13976" class="comments-container"><span id="13977"></span><div id="comment-13977" class="comment"><div id="post-13977-score" class="comment-score"></div><div class="comment-text"><p>Well, since Chris ahs put it on the Wishlist for pcanng features you might be lucky in the future :-)</p><p>One question, how should the packet numbers after two iterations of selective saving?</p></div><div id="comment-13977-info" class="comment-info"><span class="comment-age">(31 Aug '12, 15:06)</span> SYN-bit ♦♦</div></div><span id="13979"></span><div id="comment-13979" class="comment"><div id="post-13979-score" class="comment-score"></div><div class="comment-text"><p>I supose this discussion should be held elsewhere but some sort of file history (display filters etc) has also been discussed, perhaps packet number over file iterations could be saved ( File 1, pkt x, File 2, pkt y ...) displaying the info in a meaningful way is another topic :-)</p></div><div id="comment-13979-info" class="comment-info"><span class="comment-age">(31 Aug '12, 15:30)</span> Anders ♦</div></div></div><div id="comment-tools-13976" class="comment-tools"></div><div class="clear"></div><div id="comment-13976-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

