+++
type = "question"
title = "How not to add a new tab to packet bytes pane with a new tvb?"
description = '''Hi, I&#x27;m writing a dissector for a protocol that has many values from disjoint bytes. For example, one 8-byte value can be stored in offset 0-4 and 16-20. I realized that using the byteArray:tvb() to create a new tvb and then apply the tvb:int64() is the best way to get the values. However, whenever ...'''
date = "2014-02-27T09:13:00Z"
lastmod = "2014-02-27T09:13:00Z"
weight = 30239
keywords = [ "tabs", "disjoint", "bytearray.tvb", "pane" ]
aliases = [ "/questions/30239" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How not to add a new tab to packet bytes pane with a new tvb?](/questions/30239/how-not-to-add-a-new-tab-to-packet-bytes-pane-with-a-new-tvb)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30239-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm writing a dissector for a protocol that has many values from disjoint bytes. For example, one 8-byte value can be stored in offset 0-4 and 16-20. I realized that using the byteArray:tvb() to create a new tvb and then apply the tvb:int64() is the best way to get the values. However, whenever I create a new tvb with the ByteArray:tvb() function, a new tab is added to the packet bytes pane in the wireshark GUI. And since I have lots of these tabs, I believe it is the reason why my wireshark is crashing now whenever I click on a tree item that refers to a newly created tvb. Is there a way to read the values out of the disjoint bytes without creating all the new tabs?</p><p>Thanks so much, YX</p></div><div id="question-tags" class="tags-container tags">tabs disjoint bytearray.tvb pane</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Feb '14, 09:13</strong></p><img src="https://secure.gravatar.com/avatar/b18cada3e3589f311e24f5ffbd1737bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YXI&#39;s gravatar image" /><p>YXI<br />
<span class="score" title="21 reputation points">21</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YXI has no accepted answers">0%</span></p></div></div><div id="comments-container-30239" class="comments-container"></div><div id="comment-tools-30239" class="comment-tools"></div><div class="clear"></div><div id="comment-30239-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

