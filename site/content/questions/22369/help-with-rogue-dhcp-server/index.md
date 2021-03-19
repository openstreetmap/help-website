+++
type = "question"
title = "Help with Rogue DHCP Server"
description = '''I have a rogue dhcp server and I was able to track down the machine without any problem. However, I can not determine how the machine is handing out addresses. It is a Snow Leopard Mac with Internet Sharing OFF. Also the DHCP Offer is to a specific machine which is actually a backuppc ubuntu server,...'''
date = "2013-06-26T11:23:00Z"
lastmod = "2013-06-26T16:44:00Z"
weight = 22369
keywords = [ "dhcp", "rogue" ]
aliases = [ "/questions/22369" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Help with Rogue DHCP Server](/questions/22369/help-with-rogue-dhcp-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22369-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a rogue dhcp server and I was able to track down the machine without any problem. However, I can not determine how the machine is handing out addresses. It is a Snow Leopard Mac with Internet Sharing OFF. Also the DHCP Offer is to a specific machine which is actually a backuppc ubuntu server, NOT a broadcast. Does anyone have any ideas what is going on here? I have included a screenshot below of the basic wireshark output. Any help is greatly appreciated.</p><p>You can see the screenshot at <a href="http://www.cfbangor.com/images/wireshark.png">http://www.cfbangor.com/images/wireshark.png</a></p><p><img></img><a href="http://www.cfbangor.com/images/wireshark.png">http://www.cfbangor.com/images/wireshark.png</a></p></div><div id="question-tags" class="tags-container tags">dhcp rogue</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '13, 11:23</strong></p><img src="https://secure.gravatar.com/avatar/c2cdfb97b9aa915f9b0b27613ef16621?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robp2175&#39;s gravatar image" /><p>robp2175<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robp2175 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 26 Jun '13, 11:24</p></div></div><div id="comments-container-22369" class="comments-container"></div><div id="comment-tools-22369" class="comment-tools"></div><div class="clear"></div><div id="comment-22369-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22379"></span>

<div id="answer-container-22379" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22379-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Also the DHCP Offer is to a specific machine</p></blockquote><p>That's not uncommon. See the sample capture in the Wireshark wiki.</p><blockquote><p><a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=dhcp.pcap">http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=dhcp.pcap</a></p></blockquote><p>If there is no DHCP server on your Mac box, are you sure that packets 8870 and 9180 are really DHCP Offer packets?</p><p>Maybe Wireshark simply decodes those packets as DHCP because those two machine are using a communication protocol at the same port that is usually used by DHCP (for whatever reason).</p><p>If you look at the content of those DHCP Offer packets. Do the values in that packets ((IP, MAC) make any sense in your environment?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '13, 16:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-22379" class="comments-container"></div><div id="comment-tools-22379" class="comment-tools"></div><div class="clear"></div><div id="comment-22379-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

