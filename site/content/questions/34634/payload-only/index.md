+++
type = "question"
title = "Payload only"
description = '''Hello, Does anyone know the easier way to get only the payload of IP packets (&quot;data&quot; on IP datagram). Indeed, when I capture packets, it returns me the entire datagram (with the addresses ...) but I only need the payload. Thanks, Regards'''
date = "2014-07-14T12:41:00Z"
lastmod = "2014-07-15T02:43:00Z"
weight = 34634
keywords = [ "payload" ]
aliases = [ "/questions/34634" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Payload only](/questions/34634/payload-only)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34634-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Does anyone know the easier way to get only the payload of IP packets ("data" on IP datagram).</p><p>Indeed, when I capture packets, it returns me the entire datagram (with the addresses ...) but I only need the payload.</p><p>Thanks, Regards</p></div><div id="question-tags" class="tags-container tags">payload</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jul '14, 12:41</strong></p><img src="https://secure.gravatar.com/avatar/98f142fc750f9de55290fc5ee5ec2525?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chi&#39;s gravatar image" /><p>chi<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Jul '14, 12:44</p></div></div><div id="comments-container-34634" class="comments-container"></div><div id="comment-tools-34634" class="comment-tools"></div><div class="clear"></div><div id="comment-34634-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34647"></span>

<div id="answer-container-34647" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34647-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Does anyone know the <strong>easier way</strong> to get only the payload of IP packets ("data" on IP datagram).</p></blockquote><p><strong>easier</strong> than what?</p><blockquote><p>Indeed, when I capture packets, it returns me the entire datagram (with the addresses ...)</p></blockquote><p>sure, that's what Wireshark is mainly used for. Troubleshooting network problems. For that you need several parts of the packets, especially the headers and also the payload. It depends on the problem.</p><blockquote><p>but I only need the payload.</p></blockquote><p>You can extract the payload with tshark or other pcap extraction tools. As you did not tell us enough details, I can only answer in a general way.</p><p>There are several ways to extract the payload of frames.</p><blockquote><p>tshark -nr input.pcap -T pdml</p></blockquote><p>and then parse the <strong>tshark pdml</strong> output.</p><blockquote><p>tshark -nr input.pcap -Vx</p></blockquote><p>and then parse the <strong>tshark</strong> output.</p><blockquote><p>tshark -nr input.pcap -z follow,tcp,1</p></blockquote><p>and then parse the <strong>tshark</strong> output. See the tshark man page for more details.</p><p>There are also other tools to extract data from a pcap file:</p><blockquote><p><a href="http://isc.sans.edu/diary/Tools+for+extracting+files+from+pcaps/6961">http://isc.sans.edu/diary/Tools+for+extracting+files+from+pcaps/6961</a></p></blockquote><p>If that isn't what you are looking for: Please add more details to your question!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '14, 02:43</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-34647" class="comments-container"><span id="34666"></span><div id="comment-34666" class="comment"><div id="post-34666-score" class="comment-score"></div><div class="comment-text"><p>That seems perfect, thanks a lot !</p><p>Regards, Chi</p></div><div id="comment-34666-info" class="comment-info"><span class="comment-age">(15 Jul '14, 08:22)</span> chi</div></div><span id="34668"></span><div id="comment-34668" class="comment"><div id="post-34668-score" class="comment-score"></div><div class="comment-text"><p>You're welcome.</p></div><div id="comment-34668-info" class="comment-info"><span class="comment-age">(15 Jul '14, 08:31)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-34647" class="comment-tools"></div><div class="clear"></div><div id="comment-34647-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

