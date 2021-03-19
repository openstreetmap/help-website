+++
type = "question"
title = "How to create multiple dissectors for same port number"
description = '''Hi,  I am trying to create wireshark dissectors in Lua for different types of packets. All these packets work on the same port number. My issue is that when I added the dissectors to init.lua and opened wireshark, some of the dissectors in Wireshark stopped working altogether. If I only add one of t...'''
date = "2016-07-13T11:32:00Z"
lastmod = "2016-07-13T12:13:00Z"
weight = 54042
keywords = [ "filter", "lua", "dissector", "ask.wireshark.org", "wireshark" ]
aliases = [ "/questions/54042" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to create multiple dissectors for same port number](/questions/54042/how-to-create-multiple-dissectors-for-same-port-number)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54042-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am trying to create wireshark dissectors in Lua for different types of packets. All these packets work on the same port number. My issue is that when I added the dissectors to init.lua and opened wireshark, some of the dissectors in Wireshark stopped working altogether. If I only add one of the dissectors in Wireshark, it works fine, but if I try to add multiple dissectors, only some dissectors work, the others stop working altogether. Please let me know what can be done in this regards. I know that I can create a huge dissector that can dissect all these packets but then I will lose the functionality of filtering based on a particular packet type or attribute of a packet type. Thanks.</p></div><div id="question-tags" class="tags-container tags">filter lua dissector ask.wireshark.org wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jul '16, 11:32</strong></p><img src="https://secure.gravatar.com/avatar/3aaad26a48e6f507d8f9137404269a46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shobhit_garg91&#39;s gravatar image" /><p>shobhit_garg91<br />
<span class="score" title="16 reputation points">16</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shobhit_garg91 has no accepted answers">0%</span></p></div></div><div id="comments-container-54042" class="comments-container"></div><div id="comment-tools-54042" class="comment-tools"></div><div class="clear"></div><div id="comment-54042-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54044"></span>

<div id="answer-container-54044" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54044-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>How do you tell the different types of packets apart? Are these packet types different <em>protocols</em> or just different types of packets within the same protocol? If the latter then you really should just have one big dissector for that protocol. You shouldn't lose any filtering functionality by doing that--worst case the filters are a little longer.</p><p>If these really are different protocols then you fundamentally have 2 options:</p><ol><li>Create a "base" dissector that registers for the common port number and then looks at each packet and chooses which of the other dissectors to call for that packet</li><li>(or) create several heuristic dissectors (see the Lua function <code>register_heuristic()</code>) which look at each packet and either accept (and dissect) the packet or tell wireshark "That's not my protocol" so Wireshark will try another of the heuristic dissectors.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jul '16, 12:13</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-54044" class="comments-container"><span id="54046"></span><div id="comment-54046" class="comment"><div id="post-54046-score" class="comment-score"></div><div class="comment-text"><p>Hi, all my packets have certain fields at certain locations that have a fixed value, these parameters enable me to identify one message from the other. I cannot use heuristic dissectors because it may cause my packet to be identified incorrectly. I am thinking of creating a single dissector that dissects out the packet based upon its type. This would help in applying the filters easily. Please let me know if there are any known drawbacks of using a single large dissector as opposed to creating multiple smaller dissectors and a generic dissector such that the generic dissector decides the type of packet and sends the packet to the corresponding smaller dissector. Also I don't understand why multiple dissectors with the same port number don't work in Wireshark. When I added the first three small dissectors having the same port no to init.lua and opened wireshark, everything worked fine, but when I added the fourth dissector, then couple of these dissectors stopped working altogether. Thanks for your help.</p></div><div id="comment-54046-info" class="comment-info"><span class="comment-age">(13 Jul '16, 13:05)</span> shobhit_garg91</div></div><span id="54048"></span><div id="comment-54048" class="comment"><div id="post-54048-score" class="comment-score"></div><div class="comment-text"><p>Heuristic dissectors work by being able to identify whether the packet looks like the dissector's protocol or not--it sounds like that's the case here (you mentioned that certain locations have fixed values--that makes for a very good heuristic). They just have to do that check before starting dissection of the packet.</p><p>I'm not sure why it <em>would</em> work with 3 dissectors registered on the same port. I'd expect that only one of the dissectors would ever be called in that case.</p><p>Are these packets part of the same protocol or different protocols? Knowing that would make the best direction clearer...</p></div><div id="comment-54048-info" class="comment-info"><span class="comment-age">(13 Jul '16, 14:36)</span> JeffMorriss ♦</div></div><span id="54142"></span><div id="comment-54142" class="comment"><div id="post-54142-score" class="comment-score"></div><div class="comment-text"><p>Hi Jeff, sorry for the delayed reply. They are different protocols. I am not sure why the 3 different dissectors registered on the same port number worked fine. I cannot use heuristic dissectors since there is a possibility of the packet being dissected incorrectly which I cannot afford to. I'd rather let the dissectors fail instead. For now I have created a single dissector which dissects the packets based on there type. I am having another issue though now. The details of that can be found at <a href="https://ask.wireshark.org/questions/54141/how-to-read-input-from-user-for-a-wireshark-dissector">https://ask.wireshark.org/questions/54141/how-to-read-input-from-user-for-a-wireshark-dissector</a></p><p>Thanks again for the help.</p></div><div id="comment-54142-info" class="comment-info"><span class="comment-age">(18 Jul '16, 13:10)</span> shobhit_garg91</div></div><span id="54144"></span><div id="comment-54144" class="comment"><div id="post-54144-score" class="comment-score"></div><div class="comment-text"><p>You're welcome. If an answer has answered your question, please be sure to Accept it by clicking the little checkmark next to the answer. That way the question won't show in the list of unanswered questions--among other things (see the FAQ).</p></div><div id="comment-54144-info" class="comment-info"><span class="comment-age">(18 Jul '16, 13:26)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-54044" class="comment-tools"></div><div class="clear"></div><div id="comment-54044-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

