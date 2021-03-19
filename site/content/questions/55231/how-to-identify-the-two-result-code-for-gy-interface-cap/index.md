+++
type = "question"
title = "how to identify the two result code for gy interface cap"
description = '''For gy interface,MSCC layer result code and COMMAND layer result code filter conditions are both &quot;diameter.avp.code&quot;. If i add two result code as two column,the column name are the same. I look forward to be able to identify the two, each column can uniquely identify a CMD layer or layers MSCC ,How ...'''
date = "2016-08-31T04:40:00Z"
lastmod = "2016-08-31T04:40:00Z"
weight = 55231
keywords = [ "interface", "gy" ]
aliases = [ "/questions/55231" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to identify the two result code for gy interface cap](/questions/55231/how-to-identify-the-two-result-code-for-gy-interface-cap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55231-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>For gy interface,MSCC layer result code and COMMAND layer result code filter conditions are both "diameter.avp.code". If i add two result code as two column,the column name are the same. I look forward to be able to identify the two, each column can uniquely identify a CMD layer or layers MSCC ,How to deal with? Thank you very much.</p></div><div id="question-tags" class="tags-container tags">interface gy</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Aug '16, 04:40</strong></p><img src="https://secure.gravatar.com/avatar/3ee79f9a9cc3b6d8e854b72d6bd0a096?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wy527&#39;s gravatar image" /><p>wy527<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wy527 has no accepted answers">0%</span></p></div></div><div id="comments-container-55231" class="comments-container"><span id="55233"></span><div id="comment-55233" class="comment"><div id="post-55233-score" class="comment-score"></div><div class="comment-text"><p><code>diameter.avp.code</code> is a generic field which is present in any diameter AVP as it determines the meaning of the AVP. Can you provide an example pcap file with the two packets (one command and one result) and indicate in which values you are exactly interested?</p><p>It may not be easy, though, as if such value is inside an AVP, there is currently no way to tell Wireshark to look at the value of that one of the several AVPs in a message whose other field matches some condition.</p></div><div id="comment-55233-info" class="comment-info"><span class="comment-age">(31 Aug '16, 05:24)</span> sindy</div></div></div><div id="comment-tools-55231" class="comment-tools"></div><div class="clear"></div><div id="comment-55231-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

