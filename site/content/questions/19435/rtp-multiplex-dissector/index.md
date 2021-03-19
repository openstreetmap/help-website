+++
type = "question"
title = "RTP Multiplex dissector"
description = '''Hello guys, I need to decode RTP Multiplex streams using Wireshark. Presently we can decode only Non -Multiplexed RTP streams in wireshark.  Also I need to know the steps to add dissector in Wireshark. Thanks// Vikas '''
date = "2013-03-13T02:48:00Z"
lastmod = "2013-03-15T04:56:00Z"
weight = 19435
keywords = [ "ipmux" ]
aliases = [ "/questions/19435" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [RTP Multiplex dissector](/questions/19435/rtp-multiplex-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19435-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello guys,</p><p>I need to decode RTP Multiplex streams using Wireshark. Presently we can decode only Non -Multiplexed RTP streams in wireshark.</p><p>Also I need to know the steps to add dissector in Wireshark.</p><p>Thanks// Vikas</p></div><div id="question-tags" class="tags-container tags">ipmux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '13, 02:48</strong></p><img src="https://secure.gravatar.com/avatar/5a33fae2fd3e576257f0660435437267?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Viki&#39;s gravatar image" /><p>Viki<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Viki has no accepted answers">0%</span></p></div></div><div id="comments-container-19435" class="comments-container"></div><div id="comment-tools-19435" class="comment-tools"></div><div class="clear"></div><div id="comment-19435-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19443"></span>

<div id="answer-container-19443" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19443-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>See the source code section of <a href="http://wiki.wireshark.org/SendingFilesToWireshark?highlight=%28submit%29">http://wiki.wireshark.org/SendingFilesToWireshark?highlight=%28submit%29</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '13, 05:30</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-19443" class="comments-container"><span id="19444"></span><div id="comment-19444" class="comment"><div id="post-19444-score" class="comment-score"></div><div class="comment-text"><p>Hi Anders,</p><p>Thanks for reply !! I am not a very experienced user of wireshark yet.I need to decode RTP Multiplex streams using Wireshark. As i understand wireshark not able to decode RTP Multiplexing packets,To decode RTP Multiplexing packet we need to load some dissector. So can you please let me know step by step how to load new plugin in wireshark for RTP multiplexing as i m not a coding software engineer.</p><p>I would appreciate if you could help me</p><p>Thanks// Vikas</p></div><div id="comment-19444-info" class="comment-info"><span class="comment-age">(13 Mar '13, 06:02)</span> Viki</div></div><span id="19473"></span><div id="comment-19473" class="comment"><div id="post-19473-score" class="comment-score"></div><div class="comment-text"><p>If you are talking about RFC 5761: "Multiplexing RTP Data and Control Packets on a Single Port". No one has written code to dissect that yet so there is no plugin to load but rather code to be written :-)</p></div><div id="comment-19473-info" class="comment-info"><span class="comment-age">(13 Mar '13, 13:37)</span> Anders ♦</div></div><span id="19531"></span><div id="comment-19531" class="comment"><div id="post-19531-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>I am talking about [RFC 3550 &amp; RFC 3551],,We implemented RTP header compression on Nb &amp; AoIP (3GPP TS 29.414 page no. 19 ).As per the "When header compression is used some fields (here called static fields) in the RTP header are not transmitted in the compressed RTP header, and other fields (here called dynamic fields) are transmitted in the compressed header"</p><p>So i just want to compare RTP header compressed &amp; uncompressed field in wireshark.</p><p>Thanks// Vikas</p></div><div id="comment-19531-info" class="comment-info"><span class="comment-age">(15 Mar '13, 02:38)</span> Viki</div></div><span id="19532"></span><div id="comment-19532" class="comment"><div id="post-19532-score" class="comment-score"></div><div class="comment-text"><p>In that case refer to this <a href="http://ask.wireshark.org/questions/18926/">question</a>.</p></div><div id="comment-19532-info" class="comment-info"><span class="comment-age">(15 Mar '13, 03:23)</span> Jaap ♦</div></div></div><div id="comment-tools-19443" class="comment-tools"></div><div class="clear"></div><div id="comment-19443-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19535"></span>

<div id="answer-container-19535" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19535-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can do "decode as" NB_RTPMUX on a Nb mux packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '13, 04:56</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-19535" class="comments-container"><span id="19609"></span><div id="comment-19609" class="comment"><div id="post-19609-score" class="comment-score"></div><div class="comment-text"><p>Hi Anders,</p><p>Thanks for reply..</p><p>Yes !! i want to decode the NB RTP multiplexing packet,,When i am using this option decode as "NB RTPMUX" it seems this decoded as standard format to both RTP compressed &amp; Uncompressed as same .i still not confirm this packet is RTP compressed or uncompressed ,and also some Malformed data in RTP packet.</p><p>Thanks// Vikas</p></div><div id="comment-19609-info" class="comment-info"><span class="comment-age">(18 Mar '13, 01:55)</span> Viki</div></div><span id="19616"></span><div id="comment-19616" class="comment"><div id="post-19616-score" class="comment-score"></div><div class="comment-text"><p>Are you using the latest version 1.8.6 or the development version 1.9.1? I think some bugs may have been fixed.</p></div><div id="comment-19616-info" class="comment-info"><span class="comment-age">(18 Mar '13, 06:23)</span> Anders ♦</div></div><span id="19633"></span><div id="comment-19633" class="comment"><div id="post-19633-score" class="comment-score"></div><div class="comment-text"><p>Hi, I have also check one more option to decode RTP Compressed &amp; Uncompressed packet in Decode as "CRTP" in Link. Could you please suggest if its relevant in my case.<br />
</p><p>Thanks// Vikas sharma</p></div><div id="comment-19633-info" class="comment-info"><span class="comment-age">(18 Mar '13, 23:36)</span> Viki</div></div></div><div id="comment-tools-19535" class="comment-tools"></div><div class="clear"></div><div id="comment-19535-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

