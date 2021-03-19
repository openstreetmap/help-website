+++
type = "question"
title = "Can I filter out frames without renumbering the frames?"
description = '''When I used TShark to filter a capture file, the new output file starts with a new frame numbering, different from the frame number of the original file. Is there a way to indicate/instruct tshark to retain the frame number of the original file and not create a new frame number?'''
date = "2013-08-25T16:53:00Z"
lastmod = "2013-08-25T17:01:00Z"
weight = 24045
keywords = [ "filter", "numbering", "tshark" ]
aliases = [ "/questions/24045" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can I filter out frames without renumbering the frames?](/questions/24045/can-i-filter-out-frames-without-renumbering-the-frames)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24045-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I used TShark to filter a capture file, the new output file starts with a new frame numbering, different from the frame number of the original file. Is there a way to indicate/instruct tshark to retain the frame number of the original file and not create a new frame number?</p></div><div id="question-tags" class="tags-container tags">filter numbering tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Aug '13, 16:53</strong></p><img src="https://secure.gravatar.com/avatar/981f5e7be0c0e73e3f429d0038fb3eed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hunted&#39;s gravatar image" /><p>Hunted<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hunted has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted to question 25 Aug '13, 16:59</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-24045" class="comments-container"></div><div id="comment-tools-24045" class="comment-tools"></div><div class="clear"></div><div id="comment-24045-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24046"></span>

<div id="answer-container-24046" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24046-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Frame numbers are simply the ordinal numbers of frames within a file; they are not, in any of the file formats we support, stored as a property of the frame. Therefore, the only way to retain the frame numbers would be to write the file in a capture file format that supports per-frame comments, and make the original frame number a comment for the frame; you can't retain the frame numbers.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Aug '13, 17:01</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-24046" class="comments-container"><span id="24057"></span><div id="comment-24057" class="comment"><div id="post-24057-score" class="comment-score"></div><div class="comment-text"><p>This has been discussed earlier and there is an entry in the pcapng wishlist. See the following question and the link therein</p><blockquote><p><a href="http://ask.wireshark.org/questions/13934/preserve-the-original-packet-number-after-applying-a-filter-on-a-pcap-file">http://ask.wireshark.org/questions/13934/preserve-the-original-packet-number-after-applying-a-filter-on-a-pcap-file</a></p></blockquote></div><div id="comment-24057-info" class="comment-info"><span class="comment-age">(26 Aug '13, 06:02)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-24046" class="comment-tools"></div><div class="clear"></div><div id="comment-24046-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

