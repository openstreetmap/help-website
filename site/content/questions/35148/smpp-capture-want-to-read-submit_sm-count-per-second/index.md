+++
type = "question"
title = "SMPP Capture : Want to Read submit_sm count per second"
description = '''tshark -nr C:&#92;Users&#92;Ravi kiran&#92;Documents&#92;atctest1.pcap -R &quot;smpp.command_id == 0x80000004&quot; -T fields -E header=y -E separator=; -e frame.time_relative -e frame.number my out put: tshark: Read filters were specified both with &quot;-R&quot; and with additional command-l ine arguments.'''
date = "2014-08-04T04:35:00Z"
lastmod = "2014-08-04T14:54:00Z"
weight = 35148
keywords = [ "tshark" ]
aliases = [ "/questions/35148" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SMPP Capture : Want to Read submit\_sm count per second](/questions/35148/smpp-capture-want-to-read-submit_sm-count-per-second)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35148-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>tshark -nr C:\Users\Ravi kiran\Documents\atctest1.pcap -R "smpp.command_id == 0x80000004" -T fields -E header=y -E separator=; -e frame.time_relative -e frame.number</p><p>my out put: tshark: Read filters were specified both with "-R" and with additional command-l ine arguments.</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Aug '14, 04:35</strong></p><img src="https://secure.gravatar.com/avatar/8e722b2fe8fa42ca6ba26d7c14ca22d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="newbeets&#39;s gravatar image" /><p>newbeets<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="newbeets has no accepted answers">0%</span></p></div></div><div id="comments-container-35148" class="comments-container"><span id="35149"></span><div id="comment-35149" class="comment"><div id="post-35149-score" class="comment-score"></div><div class="comment-text"><p>tshark version?</p></div><div id="comment-35149-info" class="comment-info"><span class="comment-age">(04 Aug '14, 04:52)</span> grahamb ♦</div></div><span id="35168"></span><div id="comment-35168" class="comment"><div id="post-35168-score" class="comment-score"></div><div class="comment-text"><p>Tshark 1.8.2</p></div><div id="comment-35168-info" class="comment-info"><span class="comment-age">(04 Aug '14, 13:18)</span> newbeets</div></div></div><div id="comment-tools-35148" class="comment-tools"></div><div class="clear"></div><div id="comment-35148-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35171"></span>

<div id="answer-container-35171" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35171-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>tshark -nr C:\Users\Ravi kiran\Documents\atctest1.pcap</p></blockquote><p>looks like a quote problem in the DoS box, due to the blank in the path. Please try this:</p><blockquote><p>tshark -nr "C:\Users\Ravi kiran\Documents\atctest1.pcap" -R "smpp.command_id == 0x80000004" -T fields -E header=y -E separator=; -e frame.time_relative -e frame.number</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Aug '14, 14:54</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-35171" class="comments-container"><span id="35208"></span><div id="comment-35208" class="comment"><div id="post-35208-score" class="comment-score"></div><div class="comment-text"><p>Thank you Kurt,Its resolved.</p></div><div id="comment-35208-info" class="comment-info"><span class="comment-age">(05 Aug '14, 05:53)</span> newbeets</div></div><span id="35214"></span><div id="comment-35214" class="comment"><div id="post-35214-score" class="comment-score"></div><div class="comment-text"><p>good to hear!</p></div><div id="comment-35214-info" class="comment-info"><span class="comment-age">(05 Aug '14, 06:54)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-35171" class="comment-tools"></div><div class="clear"></div><div id="comment-35171-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

