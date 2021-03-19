+++
type = "question"
title = "gsm_a vs e212"
description = '''Hi, I use Wireshark to convert gsmtap pcap&#x27;s to pdml. An example line from pdml file is shown below. I have a few questions about the way Wireshark converts pcap to pdml. I have two computers, one is running Wireshark 1.12 and the other is running Wireshark 1.99. Now, Wireshark 1.12 saves this line ...'''
date = "2015-10-22T02:27:00Z"
lastmod = "2015-10-22T03:23:00Z"
weight = 46826
keywords = [ "gsmtap" ]
aliases = [ "/questions/46826" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [gsm\_a vs e212](/questions/46826/gsm_a-vs-e212)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46826-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I use Wireshark to convert gsmtap pcap's to pdml. An example line from pdml file is shown below. I have a few questions about the way Wireshark converts pcap to pdml.<br />
I have two computers, one is running Wireshark 1.12 and the other is running Wireshark 1.99. Now, Wireshark 1.12 saves this line as shown below, Wireshark 1.99 would save it differently. The field "name" would be "e212.lac", the value in field "show" would be shown decimal and not hex.<br />
I had several scripts extracting the info from pdml file based on values in the field "name". With Wireshark 1.99 it all becomes useless, as the unique field values I was using changed the contents. Is there a way to run Wireshark 1.99 in such away that pdml files are backwards compatible? I do the pcap to pdml conversion this way:</p><pre><code>tshark -r abc.pcap -Y &#39;!icmp &amp;&amp; gsmtap&#39; -T pdml -2 -R &quot;gsm_a.dtap.msg_rr_type == 0x21&quot; &gt; abc.txt

field name=&quot;gsm_a.lac&quot; showname=&quot;Location Area Code (LAC): 0xe54c (58700)&quot; size=&quot;2&quot; pos=&quot;66&quot; show=&quot;0x0000e54c&quot; value=&quot;e54c&quot;</code></pre></div><div id="question-tags" class="tags-container tags">gsmtap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Oct '15, 02:27</strong></p><img src="https://secure.gravatar.com/avatar/f1885cad1acb7793978438a46ea62cb8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dictador&#39;s gravatar image" /><p>dictador<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dictador has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-46826" class="comments-container"></div><div id="comment-tools-46826" class="comment-tools"></div><div class="clear"></div><div id="comment-46826-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46828"></span>

<div id="answer-container-46828" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46828-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately there is no way to have backward compatibility. The new filter name allows to extract the info from various protocols at the same time, but as the drawback of breaking existing scripts. Sorry about that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '15, 03:23</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-46828" class="comments-container"></div><div id="comment-tools-46828" class="comment-tools"></div><div class="clear"></div><div id="comment-46828-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

