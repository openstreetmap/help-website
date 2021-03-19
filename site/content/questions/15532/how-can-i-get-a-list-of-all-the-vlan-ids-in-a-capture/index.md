+++
type = "question"
title = "How can I get a list of all the VLAN IDs in a capture?"
description = '''is it possible to have only one entry in packet table for specific vlan id even if we got 1000 packets of that vlan id , diiferent or same protocol &amp;amp; whatever be contents of that packet ? Currently , we have to capture lot of packets then sort by vlan id &amp;amp; scroll through a long list to find ...'''
date = "2012-11-05T00:41:00Z"
lastmod = "2012-11-05T12:48:00Z"
weight = 15532
keywords = [ "vlan", "wireshark" ]
aliases = [ "/questions/15532" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can I get a list of all the VLAN IDs in a capture?](/questions/15532/how-can-i-get-a-list-of-all-the-vlan-ids-in-a-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15532-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>is it possible to have only one entry in packet table for specific vlan id even if we got 1000 packets of that vlan id , diiferent or same protocol &amp; whatever be contents of that packet ?</p><p>Currently , we have to capture lot of packets then sort by vlan id &amp; scroll through a long list to find what diferent vlan id's we received on our system.</p></div><div id="question-tags" class="tags-container tags">vlan wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Nov '12, 00:41</strong></p><img src="https://secure.gravatar.com/avatar/53678d5d74de68231af30b8c97c69166?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="manit&#39;s gravatar image" /><p>manit<br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="manit has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Nov '12, 12:49</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-15532" class="comments-container"></div><div id="comment-tools-15532" class="comment-tools"></div><div class="clear"></div><div id="comment-15532-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="15536"></span>

<div id="answer-container-15536" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15536-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can't do that in the GUI, but that's were <strong>tshark</strong> can help. Capture your data with either Wiresahrk, dumpcap or tshark and write it to input.cap.</p><p>Then call tshark to extract the VLAN IDs.</p><blockquote><p><code>tshark -r input.cap -T fields -e vlan.id</code><br />
</p></blockquote><p>This will print all vlan IDs. However, you will get duplicates. So you need to filter those duplicates with a script and/or other tools.</p><p>Sort the values in numerical ascending order and eliminate duplicates.</p><p><strong>Windows</strong></p><blockquote><p><code>powershell -command "tshark -r input.cap -T fields -e vlan.id | sort-object {[int] $_} -unique"</code><br />
</p></blockquote><p><strong>Linux</strong></p><blockquote><p><code>tshark -r input.cap -T fields -e vlan.id | sort -n -u</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Nov '12, 01:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-15536" class="comments-container"><span id="15537"></span><div id="comment-15537" class="comment"><div id="post-15537-score" class="comment-score"></div><div class="comment-text"><p>that worked well , kurt .</p><p>There ain't a way to tell wireshark to show one row for specific vlan id ignoring other fields. I wanted following scenario: Let us say , we add another column called 'packet-count' to table . If a packet appears then check its vlan-id . If it has been encountered before , then add 1 to packet count else add another row with that vlan-id. That would mean analysing while capturing . Seems , that is not posssible.</p></div><div id="comment-15537-info" class="comment-info"><span class="comment-age">(05 Nov '12, 01:37)</span> manit</div></div><span id="15538"></span><div id="comment-15538" class="comment"><div id="post-15538-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Seems , that is not posssible.</p></blockquote><p>that's not possible, unless you change the code of Wireshark.</p><p>You can write a vlan <a href="http://wiki.wireshark.org/Lua/Dissectors">dissector in Lua</a> and add a field for your packet counter there. HOWEVER: That will <strong>not</strong> eliminate multiple packets with the same VLAN ID in the packet list.</p><p>BTW: You are talking about packet count and unique VLAN IDs. What do you actually want to know? How many VLAN IDs you captured and/or how many packets per VLAN ID? If so, why do you need that while you are capturing the data?</p><p>Maybe there is another way !?!</p></div><div id="comment-15538-info" class="comment-info"><span class="comment-age">(05 Nov '12, 02:02)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-15536" class="comment-tools"></div><div class="clear"></div><div id="comment-15536-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15552"></span>

<div id="answer-container-15552" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15552-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>is it possible to have only one entry in packet table for specific vlan id even if we got 1000 packets of that vlan id , diiferent or same protocol &amp; whatever be contents of that packet ?</p></blockquote><p>No. That's not what the packet table is for. The "packet table" is a table of, well, <em>packets</em>, so there's one entry in the packet table for each packet.</p><p>It <em>would</em> be possible to have a <em>statistics tap</em> that displayed a table showing all VLAN IDs in the capture, just as we already have taps to show, for example, all Ethernet or IPv4 or IPv6 or... addresses in the capture. <a href="http://wiki.wireshark.org/Lua/Taps">Taps can be written in Lua</a>, although I'm not sure whether a Lua tap can pop up a table display in the GUI in Wireshark rather than just print it out as text in TShark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Nov '12, 12:48</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></br></p></div></div><div id="comments-container-15552" class="comments-container"></div><div id="comment-tools-15552" class="comment-tools"></div><div class="clear"></div><div id="comment-15552-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

