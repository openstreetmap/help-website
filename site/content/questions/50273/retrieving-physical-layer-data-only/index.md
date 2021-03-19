+++
type = "question"
title = "Retrieving Physical Layer Data Only"
description = '''I know how to use the filter on both Wireshark and Tshark, however, I want to go even deeper into the analysis of the data. To do this I want to access only the physical layer transmissions of the specified type. For example, the following drag-n-drop batch file will filter out all IP packets in a p...'''
date = "2016-02-17T08:27:00Z"
lastmod = "2016-02-18T03:15:00Z"
weight = 50273
keywords = [ "wireshark", "layer", "display-filter", "tshark", "physical" ]
aliases = [ "/questions/50273" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Retrieving Physical Layer Data Only](/questions/50273/retrieving-physical-layer-data-only)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50273-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I know how to use the filter on both Wireshark and Tshark, however, I want to go even deeper into the analysis of the data. To do this I want to access only the physical layer transmissions of the specified type.</p><p>For example, the following drag-n-drop batch file will filter out <strong><em>all</em></strong> IP packets in a pcap file:</p><pre><code>&quot;C:\Program Files\Wireshark\tshark.exe&quot; -nr &quot;%~1&quot; -P -Y &quot;ip&quot; -o &quot;gui.column.format:\&quot;Time\&quot;,\&quot;%%t\&quot;&quot;  &gt; &quot;%~1.ip.tt&quot;</code></pre><p>My dilemma is that I only want the times at which IP packets were sent at the physical layer, not all layers. What do I need to do (/add to this batch file) to filter those packets out?</p><p>A Tshark approach is much more preferred.</p></div><div id="question-tags" class="tags-container tags">wireshark layer display-filter tshark physical</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Feb '16, 08:27</strong></p><img src="https://secure.gravatar.com/avatar/3a4bc2ba5c09d24f214dc472eb5b7993?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Midimistro&#39;s gravatar image" /><p>Midimistro<br />
<span class="score" title="11 reputation points">11</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Midimistro has one accepted answer">50%</span></p></div></div><div id="comments-container-50273" class="comments-container"><span id="50281"></span><div id="comment-50281" class="comment"><div id="post-50281-score" class="comment-score"></div><div class="comment-text"><p>Are you saying that the timestamp you get now is something different? Are you aware where this timestamp comes from and what it represents?</p></div><div id="comment-50281-info" class="comment-info"><span class="comment-age">(17 Feb '16, 12:29)</span> Jaap ♦</div></div><span id="50283"></span><div id="comment-50283" class="comment"><div id="post-50283-score" class="comment-score"></div><div class="comment-text"><p>I am quite aware of where these timestamps come from. The filter above includes all the instances of the IP protocol, whether the instance is in the physical layer or not. What I am looking for is physical layer IP instances, and nothing more.</p></div><div id="comment-50283-info" class="comment-info"><span class="comment-age">(17 Feb '16, 13:09)</span> Midimistro</div></div></div><div id="comment-tools-50273" class="comment-tools"></div><div class="clear"></div><div id="comment-50273-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="50296"></span>

<div id="answer-container-50296" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50296-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>What I am looking for is physical layer IP instances, and nothing more.</p></blockquote><p>If you want a general solution, there isn't one.</p><p>If you want a solution for a particular link layer, try, for example, "eth.type == 0x0800 || eth.type == 0x86dd" for IPv4 or IPv6 directly atop Ethernet.</p><p>However, that won't filter out Ethernet transported atop some other protocol ultimately running atop physical Ethernet. There <em>is</em> no solution for that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Feb '16, 00:23</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-50296" class="comments-container"></div><div id="comment-tools-50296" class="comment-tools"></div><div class="clear"></div><div id="comment-50296-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="50302"></span>

<div id="answer-container-50302" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50302-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Could you slice the capture with editcap so there is nothing beyond the first IP layer, e.g. <code>editcap -s xx in.pcap out.pcap</code>, then use the sliced capture for your calcs?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Feb '16, 03:15</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-50302" class="comments-container"><span id="50335"></span><div id="comment-50335" class="comment"><div id="post-50335-score" class="comment-score"></div><div class="comment-text"><p>Thats not what I am looking for. What I am trying to do is get packet information from the PHY layer as described in this picture and only that data, no other layer info (aka I want to leave out all the layers above it):</p><p><img src="http://www.tutorialspoint.com/lte/images/lte_data_flow.jpg" alt="lte_data_flow diagram" /></p><p>If this is possible, let me know. Whether it be the IP packets themselves or the transport block, as long as its one or the other, and not both, that's what I am looking for.</p></div><div id="comment-50335-info" class="comment-info"><span class="comment-age">(19 Feb '16, 04:37)</span> Midimistro</div></div><span id="50336"></span><div id="comment-50336" class="comment"><div id="post-50336-score" class="comment-score"></div><div class="comment-text"><p>Can you show a picture of the packet tree in Wireshark indicating the data you want? Even better, add a capture as well.</p></div><div id="comment-50336-info" class="comment-info"><span class="comment-age">(19 Feb '16, 04:42)</span> grahamb ♦</div></div><span id="50354"></span><div id="comment-50354" class="comment"><div id="post-50354-score" class="comment-score"></div><div class="comment-text"><p>I can add a small snapshot, but because the data is confidential, I cannot release the capture.</p></div><div id="comment-50354-info" class="comment-info"><span class="comment-age">(19 Feb '16, 12:19)</span> Midimistro</div></div></div><div id="comment-tools-50302" class="comment-tools"></div><div class="clear"></div><div id="comment-50302-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

