+++
type = "question"
title = "tshark capture input and output"
description = '''I created a Tshark script, I realized that I am only filtering incoming messages so I can not see anything. Can someone help me? Tshark.exe -i rpcap://[172.16.254.6]/&#92;Device&#92;NPF_{CF9CFF46-79FF-4A97-802A-F6CEF5896D29} -f &quot;tcp[20:4]=0x383D4649 and tcp[24:1]=0x58&quot; -i rpcap://[172.16.254.6]/&#92;Device&#92;NPF_...'''
date = "2017-06-29T11:17:00Z"
lastmod = "2017-06-29T12:12:00Z"
weight = 62417
keywords = [ "filter", "tshark", "wireshark" ]
aliases = [ "/questions/62417" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark capture input and output](/questions/62417/tshark-capture-input-and-output)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62417-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I created a Tshark script, I realized that I am only filtering incoming messages so I can not see anything. Can someone help me?</p><pre><code>Tshark.exe -i rpcap://[172.16.254.6]/\Device\NPF_{CF9CFF46-79FF-4A97-802A-F6CEF5896D29} -f &quot;tcp[20:4]=0x383D4649 and tcp[24:1]=0x58&quot; -i rpcap://[172.16.254.6]/\Device\NPF_{0E94BE7D-D6F0-43B0-B561-5CE3FC9A6AD7} -f &quot;tcp[20:4]=0x383D4649 and tcp[24:1]=0x58&quot; -w &quot;D:\fix\%DATE:~4,2%%DATE:~7,2%%DATE:~10,4%_APP01.pcap&quot;</code></pre></div><div id="question-tags" class="tags-container tags">filter tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jun '17, 11:17</strong></p><img src="https://secure.gravatar.com/avatar/a95becaa9162bc901663cdd569efda99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JorgeMiguelr210&#39;s gravatar image" /><p>JorgeMiguelr210<br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JorgeMiguelr210 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Jun '17, 11:19</p></div></div><div id="comments-container-62417" class="comments-container"></div><div id="comment-tools-62417" class="comment-tools"></div><div class="clear"></div><div id="comment-62417-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62418"></span>

<div id="answer-container-62418" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62418-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I may be wrong nowadays, but the last time I've tried a couple of months ago, you could capture from just a single input queue. If this is still true, to achieve your goal, you'll have to run two instances of tshark, each capturing from another remote device, and then merge the result files.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '17, 12:12</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-62418" class="comments-container"></div><div id="comment-tools-62418" class="comment-tools"></div><div class="clear"></div><div id="comment-62418-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

