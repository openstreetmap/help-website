+++
type = "question"
title = "Working dissector for 1.7.1 not working for 1.9.0"
description = '''Hi Experts, I don&#x27;t know what changes wireshark underwent which has rendered my plugin useless in 1.9.0. I am not getting any compiler/install error but still my plugin is not working and i suspect it has to do with some recent changes of wireshark. One of the few new changes i did was to add &quot;void*...'''
date = "2013-03-05T00:06:00Z"
lastmod = "2013-03-05T05:44:00Z"
weight = 19143
keywords = [ "dissector", "wireshark" ]
aliases = [ "/questions/19143" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Working dissector for 1.7.1 not working for 1.9.0](/questions/19143/working-dissector-for-171-not-working-for-190)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19143-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Experts,</p><p>I don't know what changes wireshark underwent which has rendered my plugin useless in 1.9.0. I am not getting any compiler/install error but still my plugin is not working and i suspect it has to do with some recent changes of wireshark.</p><p>One of the few new changes i did was to add "void* data_U_" in dissector function arguments and post this change atleast i am not getting install error. I know it's a bit too much but if possible please take a quick look at my dissector code and let me know if you find any obvious fault.</p><p><a href="http://pastie.org/private/rf8jkdq7ewjumh0ehoydw">http://pastie.org/private/rf8jkdq7ewjumh0ehoydw</a><br />
</p></div><div id="question-tags" class="tags-container tags">dissector wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Mar '13, 00:06</strong></p><img src="https://secure.gravatar.com/avatar/d15cd2870e25518ba76d2eb42f56bbcb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yogeshg&#39;s gravatar image" /><p>yogeshg<br />
<span class="score" title="41 reputation points">41</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yogeshg has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-19143" class="comments-container"></div><div id="comment-tools-19143" class="comment-tools"></div><div class="clear"></div><div id="comment-19143-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19149"></span>

<div id="answer-container-19149" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19149-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You're in conflict with the IPv4/IPv6 dissector, registering for the same Ethertypes. This time you lost.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '13, 05:44</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Mar '13, 23:03</p></div></div><div id="comments-container-19149" class="comments-container"><span id="19198"></span><div id="comment-19198" class="comment"><div id="post-19198-score" class="comment-score"></div><div class="comment-text"><p>Thank you Jaap for your reply. I wish to check all ipv4 and ipv6 packets for my protocol that's why i did that. Is there any workaround for this ?</p></div><div id="comment-19198-info" class="comment-info"><span class="comment-age">(05 Mar '13, 21:21)</span> yogeshg</div></div><span id="19202"></span><div id="comment-19202" class="comment"><div id="post-19202-score" class="comment-score"></div><div class="comment-text"><p>You seem to be doing trailer dissection. There's a table for that, called eth.trailer called in packet-eth.c. Have a look there to see if you can hook in there.</p></div><div id="comment-19202-info" class="comment-info"><span class="comment-age">(05 Mar '13, 23:13)</span> Jaap ♦</div></div><span id="19346"></span><div id="comment-19346" class="comment"><div id="post-19346-score" class="comment-score"></div><div class="comment-text"><p>Can you please point an example dissector using eth.trailer ?</p></div><div id="comment-19346-info" class="comment-info"><span class="comment-age">(10 Mar '13, 23:29)</span> yogeshg</div></div><span id="19347"></span><div id="comment-19347" class="comment"><div id="post-19347-score" class="comment-score"></div><div class="comment-text"><p>Just grep eth.trailer epan/dissectors/packet*.c</p></div><div id="comment-19347-info" class="comment-info"><span class="comment-age">(10 Mar '13, 23:40)</span> Jaap ♦</div></div></div><div id="comment-tools-19149" class="comment-tools"></div><div class="clear"></div><div id="comment-19149-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

