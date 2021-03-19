+++
type = "question"
title = "PTP announce message expects TLV"
description = '''Hello For some reason wire shark expects announce PTPoE packet to contain an additional TLV. It is not expected in PTPoIP packet. I&#x27;d appreciate if you looked into it. Yossi Fridman'''
date = "2014-10-22T07:34:00Z"
lastmod = "2014-10-22T07:58:00Z"
weight = 37283
keywords = [ "malformed", "ptp" ]
aliases = [ "/questions/37283" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [PTP announce message expects TLV](/questions/37283/ptp-announce-message-expects-tlv)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37283-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello For some reason wire shark expects announce PTPoE packet to contain an additional TLV. It is not expected in PTPoIP packet. I'd appreciate if you looked into it. Yossi Fridman</p></div><div id="question-tags" class="tags-container tags">malformed ptp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Oct '14, 07:34</strong></p><img src="https://secure.gravatar.com/avatar/e4fe79875c5746ae60f16115f3a3fd55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YossiFr&#39;s gravatar image" /><p>YossiFr<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YossiFr has no accepted answers">0%</span></p></div></div><div id="comments-container-37283" class="comments-container"><span id="37284"></span><div id="comment-37284" class="comment"><div id="post-37284-score" class="comment-score"></div><div class="comment-text"><p>can you provide a sample capture file that shows the "problem"? If so, please upload it somewhere (google drive, dropbox, box.com or appliance.cloudshark.org/upload/) and post the link here.</p></div><div id="comment-37284-info" class="comment-info"><span class="comment-age">(22 Oct '14, 07:40)</span> Kurt Knochner ♦</div></div><span id="37285"></span><div id="comment-37285" class="comment"><div id="post-37285-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt Here is the link. You can find the malformed announce packet there.</p><p><a href="https://drive.google.com/file/d/0BzEOuYj_hS_GdTJzeEtxSmpGc00/view?usp=sharing">https://drive.google.com/file/d/0BzEOuYj_hS_GdTJzeEtxSmpGc00/view?usp=sharing</a></p></div><div id="comment-37285-info" class="comment-info"><span class="comment-age">(22 Oct '14, 07:49)</span> YossiFr</div></div></div><div id="comment-tools-37283" class="comment-tools"></div><div class="clear"></div><div id="comment-37283-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37286"></span>

<div id="answer-container-37286" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37286-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>there are 4 more bytes in the frame than the dissector expects. Please file a bug report at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> and add as much information as you can, including the sample capture file. Thank you!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '14, 07:58</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-37286" class="comments-container"><span id="37287"></span><div id="comment-37287" class="comment"><div id="post-37287-score" class="comment-score"></div><div class="comment-text"><p>OK, thanks, I will. Does this mean my packet is good?</p></div><div id="comment-37287-info" class="comment-info"><span class="comment-age">(22 Oct '14, 08:00)</span> YossiFr</div></div><span id="37289"></span><div id="comment-37289" class="comment"><div id="post-37289-score" class="comment-score"></div><div class="comment-text"><p>Sorry, but I have no idea. Somebody will have to check the PTPv2 specs to figure out if the packet is O.K. or not.</p></div><div id="comment-37289-info" class="comment-info"><span class="comment-age">(22 Oct '14, 08:09)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-37286" class="comment-tools"></div><div class="clear"></div><div id="comment-37286-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

