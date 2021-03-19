+++
type = "question"
title = "Can I specify the magic number in pcap files?"
description = '''Can I save a trace file from Wireshark with a specific magic_number in the pcap header? I want to choose whether it will be 0xa1b2c3d4 or 0xd4c3b2a1, which will reflect the endianness of the platforms on which it will be used. Can I do that from Wireshark?'''
date = "2012-02-09T07:02:00Z"
lastmod = "2012-02-09T07:33:00Z"
weight = 8929
keywords = [ "file-format", "pcap" ]
aliases = [ "/questions/8929" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can I specify the magic number in pcap files?](/questions/8929/can-i-specify-the-magic-number-in-pcap-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8929-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can I save a trace file from Wireshark with a specific magic_number in the pcap header? I want to choose whether it will be <code>0xa1b2c3d4</code> or <code>0xd4c3b2a1</code>, which will reflect the endianness of the platforms on which it will be used. Can I do that from Wireshark?</p></div><div id="question-tags" class="tags-container tags">file-format pcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '12, 07:02</strong></p><img src="https://secure.gravatar.com/avatar/57510bb7c11c599b71161afa79b89c86?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kosta&#39;s gravatar image" /><p>Kosta<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kosta has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Feb '12, 07:35</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-8929" class="comments-container"></div><div id="comment-tools-8929" class="comment-tools"></div><div class="clear"></div><div id="comment-8929-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8932"></span>

<div id="answer-container-8932" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8932-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is no need to specify whether the magic number is written out in little-endian or big-endian format. Wireshark will read either format on either platform. The magic number identifies the file as a pcap file and how the data is recorded, not how it will be used.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '12, 07:33</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-8932" class="comments-container"><span id="8934"></span><div id="comment-8934" class="comment"><div id="post-8934-score" class="comment-score"></div><div class="comment-text"><p>I know that wireshark can read boat formats but my question is wheter I can choose how wireshark records data in pcap file. If wireshark can read both formats, can he write in both formats too?</p></div><div id="comment-8934-info" class="comment-info"><span class="comment-age">(09 Feb '12, 07:58)</span> Kosta</div></div><span id="8935"></span><div id="comment-8935" class="comment"><div id="post-8935-score" class="comment-score"></div><div class="comment-text"><p>The endianness of the output file is whatever the system endianness happens to be; Wireshark makes no specific election to use big-endian or little-endian format.</p></div><div id="comment-8935-info" class="comment-info"><span class="comment-age">(09 Feb '12, 08:06)</span> multipleinte...</div></div><span id="8936"></span><div id="comment-8936" class="comment"><div id="post-8936-score" class="comment-score"></div><div class="comment-text"><p>Ok. Thanks.</p></div><div id="comment-8936-info" class="comment-info"><span class="comment-age">(09 Feb '12, 08:41)</span> Kosta</div></div></div><div id="comment-tools-8932" class="comment-tools"></div><div class="clear"></div><div id="comment-8932-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

