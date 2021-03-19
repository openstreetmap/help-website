+++
type = "question"
title = "Endianess Issue with Lua Dissector"
description = '''For the dissector I&#x27;m creating I have to dissect 11 bits from two bytes. The bytes in the hex dump are: CF 81 which is the following in binary: 1100 1111 1000 0001 However, I need the bytes organized as: 81 CF So I can get the bits as: 1000 0001 1100 1111 Where the bolded bits are the bits of intere...'''
date = "2016-12-14T16:03:00Z"
lastmod = "2017-01-04T06:27:00Z"
weight = 58124
keywords = [ "big-endian", "lua", "bits", "little-endian", "wireshark" ]
aliases = [ "/questions/58124" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Endianess Issue with Lua Dissector](/questions/58124/endianess-issue-with-lua-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58124-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>For the dissector I'm creating I have to dissect 11 bits from two bytes. The bytes in the hex dump are:</p><p>CF 81</p><p>which is the following in binary:</p><p>1100 1111 1000 0001</p><p>However, I need the bytes organized as:</p><p>81 CF</p><p>So I can get the bits as:</p><p>1000 0<strong>001 1100 1111</strong></p><p>Where the bolded bits are the bits of interest. My attempt was to store the two bytes in a separate variable using the tvbuf:bitfield() method. Then, after extracting the 11 bits desired, adding them to the display tree with tree:add_le() method. However, I am not getting the proper value.</p><p>Thank you for your consideration!</p></div><div id="question-tags" class="tags-container tags">big-endian lua bits little-endian wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Dec '16, 16:03</strong></p><img src="https://secure.gravatar.com/avatar/00cd850e8d2944c2c7dcdc13baf50a81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Irfan%20Hossain&#39;s gravatar image" /><p>Irfan Hossain<br />
<span class="score" title="11 reputation points">11</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Irfan Hossain has no accepted answers">0%</span></p></div></div><div id="comments-container-58124" class="comments-container"></div><div id="comment-tools-58124" class="comment-tools"></div><div class="clear"></div><div id="comment-58124-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58499"></span>

<div id="answer-container-58499" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58499-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you having trouble getting the data in the dissection tree correctly or in your local variable correctly?</p><p>If the former then you should be able to use <a href="https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Tree.html#lua_fn_treeitem_add_packet_field_protofield___tvbrange___encoding___label__"><code>treeitem:add_packet_field</code></a> with an encoding of <code>ENC_LITTLE_ENDIAN</code> to tell Wireshark to flip the bytes. Of course you'd want the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Proto.html#lua_class_ProtoField"><code>ProtoField</code></a> to be a <code>ftypes.UINT16</code> and you'd presumably want to give it a <code>mask</code> of 0x7FF (so Wireshark will use only the lower 11 bits in calculating the value).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jan '17, 06:27</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-58499" class="comments-container"><span id="58502"></span><div id="comment-58502" class="comment"><div id="post-58502-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your answer! The original problem was fixed a different way due to the data organization, but this fixed another issue I had with endianess. Thanks!</p></div><div id="comment-58502-info" class="comment-info"><span class="comment-age">(04 Jan '17, 09:13)</span> Irfan Hossain</div></div></div><div id="comment-tools-58499" class="comment-tools"></div><div class="clear"></div><div id="comment-58499-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

