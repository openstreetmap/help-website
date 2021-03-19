+++
type = "question"
title = "IP based transfer"
description = '''Anyone have any ideas on analyzing a purely IP based transfer? I&#x27;m analyzing a trace file supposedly of a low throughput for replication over the WAN. The trace only show IP with no TCP so I&#x27;m not sure what flags to look for. I believe the customer is using a Brocade storage router. Screenshot '''
date = "2012-11-18T09:52:00Z"
lastmod = "2012-11-18T14:20:00Z"
weight = 16012
keywords = [ "ip" ]
aliases = [ "/questions/16012" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [IP based transfer](/questions/16012/ip-based-transfer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16012-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Anyone have any ideas on analyzing a purely IP based transfer? I'm analyzing a trace file supposedly of a low throughput for replication over the WAN. The trace only show IP with no TCP so I'm not sure what flags to look for. I believe the customer is using a Brocade storage router.</p><p>Screenshot</p><p><img src="https://osqa-ask.wireshark.org/upfiles/EasyCapture4.bmp" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">ip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Nov '12, 09:52</strong></p><img src="https://secure.gravatar.com/avatar/9d629f265392eaf7b61f921e25f9f730?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ws2006&#39;s gravatar image" /><p>ws2006<br />
<span class="score" title="1 reputation points">1</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ws2006 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 18 Nov '12, 14:14</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-16012" class="comments-container"><span id="16014"></span><div id="comment-16014" class="comment"><div id="post-16014-score" class="comment-score">1</div><div class="comment-text"><p>The field Protocol in the IP header indicates the next protocol what does it say in your case?</p></div><div id="comment-16014-info" class="comment-info"><span class="comment-age">(18 Nov '12, 10:55)</span> Anders ♦</div></div><span id="16018"></span><div id="comment-16018" class="comment"><div id="post-16018-score" class="comment-score"></div><div class="comment-text"><p>see screenshots</p></div><div id="comment-16018-info" class="comment-info"><span class="comment-age">(18 Nov '12, 13:39)</span> ws2006</div></div><span id="16021"></span><div id="comment-16021" class="comment"><div id="post-16021-score" class="comment-score"></div><div class="comment-text"><p>I added your screenshot to the question, as it's easier to read that way</p></div><div id="comment-16021-info" class="comment-info"><span class="comment-age">(18 Nov '12, 14:16)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-16012" class="comment-tools"></div><div class="clear"></div><div id="comment-16012-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16022"></span>

<div id="answer-container-16022" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16022-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>As the <strong>Protocol:</strong> field says, Wireshark interprets the IP protocol number 61 as <strong>SHIM6 header</strong>, that used to be the "old IP number" for <a href="http://en.wikipedia.org/wiki/Site_Multihoming_by_IPv6_Intermediation">SHIM6</a>.</p><p>After checking the code...</p><p>The code for Wireshark 1.8.0 contains a definition for IP protocol 61:</p><p><code> IP_PROTO_SHIM6_OLD, "SHIM6 header" },         / 61  any host internal protocol [Internet_Assigned_Numbers_Authority] /</code></p><p>This leads to the following conclusion:</p><ul><li>The IP protocol used (61) is something vendor specific and that's why you cannot dissect it with Wireshark, even with the latest version.</li></ul><p>So, what can you do:</p><ul><li>Ask the vendor about the protocol used and if they provide a Wireshark dissector plugin for that protocol or any other tool to analyze the protocol.</li><li>Analyzing the traffic with Wireshark might help a bit. You can still look at the throughput (see Statistics and IO Graphs), but that's basically it. Without insight into the protocol, you will have a hard time to figure out the reason for the performance problems. After all, it could be the MPLS network itself or the local connection to the MPLS (local router / link).</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Nov '12, 14:20</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Nov '12, 14:31</p></div></div><div id="comments-container-16022" class="comments-container"><span id="16030"></span><div id="comment-16030" class="comment"><div id="post-16030-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt.</p></div><div id="comment-16030-info" class="comment-info"><span class="comment-age">(18 Nov '12, 19:38)</span> ws2006</div></div></div><div id="comment-tools-16022" class="comment-tools"></div><div class="clear"></div><div id="comment-16022-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

