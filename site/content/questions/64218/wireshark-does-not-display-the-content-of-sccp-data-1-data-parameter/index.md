+++
type = "question"
title = "Wireshark does not display the content of SCCP DATA-1 Data Parameter"
description = '''I am monitoring Positioning Application Protocol (PCAP) with Wireshark. As CONNECTION-REQUEST SCCP message contains Calling &amp;amp; Called Address that contain SSN Wireshark decodes properly the content of the Data Parameter. For DATA-1 SCCP messages Wireshark does not decode the content of the Data P...'''
date = "2017-10-26T01:40:00Z"
lastmod = "2017-10-26T09:30:00Z"
weight = 64218
keywords = [ "wireshark" ]
aliases = [ "/questions/64218" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark does not display the content of SCCP DATA-1 Data Parameter](/questions/64218/wireshark-does-not-display-the-content-of-sccp-data-1-data-parameter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64218-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am monitoring Positioning Application Protocol (PCAP) with Wireshark. As CONNECTION-REQUEST SCCP message contains Calling &amp; Called Address that contain SSN Wireshark decodes properly the content of the Data Parameter. For DATA-1 SCCP messages Wireshark does not decode the content of the Data Parameter, it just display the raw data</p><p>Data: .....</p><p>I suppose that is because DATA-1 messages contain neither Calling nor Called Address and thus no SSN.</p><p>How can I force Wireshark to use PCAP decoder for all the SCCP DATA-1 Data Parameters.</p><p>Thank you in advance</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '17, 01:40</strong></p><img src="https://secure.gravatar.com/avatar/98c95d4003dec700239fba3670a70612?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="oaa&#39;s gravatar image" /><p>oaa<br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="oaa has no accepted answers">0%</span></p></div></div><div id="comments-container-64218" class="comments-container"></div><div id="comment-tools-64218" class="comment-tools"></div><div class="clear"></div><div id="comment-64218-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64243"></span>

<div id="answer-container-64243" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64243-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think you need to enable the <code>Trace Associations</code> preference in the SCCP dissector. That's what makes Wireshark store the called/calling addresses from the CR/CC so it knows how to dissect the DT-1 messages.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '17, 09:30</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-64243" class="comments-container"><span id="64268"></span><div id="comment-64268" class="comment"><div id="post-64268-score" class="comment-score"></div><div class="comment-text"><p>Fine, it worked</p><p>Thank you for your help</p></div><div id="comment-64268-info" class="comment-info"><span class="comment-age">(27 Oct '17, 00:47)</span> oaa</div></div><span id="64269"></span><div id="comment-64269" class="comment"><div id="post-64269-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-64269-info" class="comment-info"><span class="comment-age">(27 Oct '17, 01:48)</span> Jaap ♦</div></div><span id="64270"></span><div id="comment-64270" class="comment"><div id="post-64270-score" class="comment-score">1</div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-64270-info" class="comment-info"><span class="comment-age">(27 Oct '17, 01:48)</span> Jaap ♦</div></div></div><div id="comment-tools-64243" class="comment-tools"></div><div class="clear"></div><div id="comment-64243-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

