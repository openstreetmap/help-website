+++
type = "question"
title = "What is a &quot;capture dissector&quot; and how is it different from a normal dissector?"
description = '''Hi, I was reading packet-udp.c and I encountered the following code that I do not understand capture_dissector_handle_t udp_cap_handle;  dissector_add_uint(&quot;ip.proto&quot;, IP_PROTO_UDP, udp_handle); dissector_add_uint(&quot;ip.proto&quot;, IP_PROTO_UDPLITE, udplite_handle);  udp_cap_handle = create_capture_dissec...'''
date = "2017-07-13T17:57:00Z"
lastmod = "2017-07-14T09:53:00Z"
weight = 62768
keywords = [ "subdissector", "dissector-table" ]
aliases = [ "/questions/62768" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [What is a "capture dissector" and how is it different from a normal dissector?](/questions/62768/what-is-a-capture-dissector-and-how-is-it-different-from-a-normal-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62768-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I was reading packet-udp.c and I encountered the following code that I do not understand</p><pre><code>capture_dissector_handle_t udp_cap_handle;

dissector_add_uint(&quot;ip.proto&quot;, IP_PROTO_UDP, udp_handle);
dissector_add_uint(&quot;ip.proto&quot;, IP_PROTO_UDPLITE, udplite_handle);

udp_cap_handle = create_capture_dissector_handle(capture_udp, hfi_udp-&gt;id);
capture_dissector_add_uint(&quot;ip.proto&quot;, IP_PROTO_UDP, udp_cap_handle);
udp_cap_handle = create_capture_dissector_handle(capture_udp, hfi_udplite-&gt;id);
capture_dissector_add_uint(&quot;ip.proto&quot;, IP_PROTO_UDPLITE, udp_cap_handle);</code></pre><p>The <code>dissector_add_uint</code>, as I understand, register the udp dissector in the sub-dissector table <code>ip.proto</code> However, I fail to understand what the <code>capture_dissector_add_uint</code> does. I read no information about "capture dissector" in README.dissector, and capture_dissector.h did not answer the question either.</p><p>Is it creating udp's own sub-dissector table? if so, why is "ip.proto" in the argument field?</p><p>Could someone clear things up for me? Thank you very much!</p><p>Nick</p></div><div id="question-tags" class="tags-container tags">subdissector dissector-table</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jul '17, 17:57</strong></p><img src="https://secure.gravatar.com/avatar/4222adcf6d70b2c359746d893f30c045?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nickzhang&#39;s gravatar image" /><p>nickzhang<br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nickzhang has no accepted answers">0%</span></p></div></div><div id="comments-container-62768" class="comments-container"></div><div id="comment-tools-62768" class="comment-tools"></div><div class="clear"></div><div id="comment-62768-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="62784"></span>

<div id="answer-container-62784" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62784-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is part of a feature in the the GTK (so called legacy) interface which has not (yet?) been implemented in the Qt interface. While doing a capture you can choose to have the packet list updated in real time or not, and you can choose to have a capture info dialog presented or not. To update the capture info dialog the incoming packets need to be dissected at a very high level. This is performed by these so called capture dissectors. Through this dialog you can see that the packet types which you expect are coming in, while not burdening the capture platform with detailed packet dissection, which may prove too time consuming for the rate of incoming packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jul '17, 09:53</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jul '17, 08:51</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-62784" class="comments-container"><span id="62815"></span><div id="comment-62815" class="comment"><div id="post-62815-score" class="comment-score"></div><div class="comment-text"><p>Thank you, this answers my question clearly.</p></div><div id="comment-62815-info" class="comment-info"><span class="comment-age">(15 Jul '17, 19:34)</span> nickzhang</div></div></div><div id="comment-tools-62784" class="comment-tools"></div><div class="clear"></div><div id="comment-62784-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="62778"></span>

<div id="answer-container-62778" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62778-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>These came in via <a href="https://code.wireshark.org/review/#/c/12607/">change 12607</a>. It appears their purpose is lightweight dissection for statistics purposes (look at the packet-ethertype.c capture dissector for an example).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jul '17, 06:58</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-62778" class="comments-container"><span id="62816"></span><div id="comment-62816" class="comment"><div id="post-62816-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the helpful information.</p></div><div id="comment-62816-info" class="comment-info"><span class="comment-age">(15 Jul '17, 19:35)</span> nickzhang</div></div></div><div id="comment-tools-62778" class="comment-tools"></div><div class="clear"></div><div id="comment-62778-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

