+++
type = "question"
title = "Simple block in PCapNg"
description = '''Hello, I have included PCapNg files support to my program, so it can open, read and write such files. It works fine when it writes enhanced blocks to the output file, they are seen and interpreted in WireShark correctly. Though when it writes simple blocks the output file starts looking for WireShar...'''
date = "2013-09-27T08:25:00Z"
lastmod = "2013-09-28T09:29:00Z"
weight = 25317
keywords = [ "simple", "pcap-ng" ]
aliases = [ "/questions/25317" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Simple block in PCapNg](/questions/25317/simple-block-in-pcapng)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25317-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I have included PCapNg files support to my program, so it can open, read and write such files. It works fine when it writes enhanced blocks to the output file, they are seen and interpreted in WireShark correctly. Though when it writes simple blocks the output file starts looking for WireShark as corrupted and it issues an error "pcapng: interface index 3111035224 is not less than interface count 1". I don't know where it takes such wierd index cause there is no Interface id link in simple blocks as it was clearly mentioned in PCapNg specification.</p></div><div id="question-tags" class="tags-container tags">simple pcap-ng</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Sep '13, 08:25</strong></p><img src="https://secure.gravatar.com/avatar/9b46c715cf0bfeca20dd3927c55be5fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ravil&#39;s gravatar image" /><p>Ravil<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ravil has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Sep '13, 08:29</p></div></div><div id="comments-container-25317" class="comments-container"><span id="25322"></span><div id="comment-25322" class="comment"><div id="post-25322-score" class="comment-score"></div><div class="comment-text"><p>Can you put a sample file somewhere so that I can take a look?</p></div><div id="comment-25322-info" class="comment-info"><span class="comment-age">(27 Sep '13, 10:59)</span> Jasper ♦♦</div></div></div><div id="comment-tools-25317" class="comment-tools"></div><div class="clear"></div><div id="comment-25317-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25331"></span>

<div id="answer-container-25331" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25331-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I verified this by creating a PCAPng file with frames in Simple Packet Blocks and opening them in Wireshark. In an older version I had the same interface index message; with the latest developer build it says that the file seems to be "cut short in the middle of a packet". So I opened a <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9200">bug report</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '13, 09:29</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-25331" class="comments-container"><span id="25335"></span><div id="comment-25335" class="comment"><div id="post-25335-score" class="comment-score">1</div><div class="comment-text"><p>Several things were wrong with the code to read SPBs. Fixes have been checked into the trunk and the 1.10 and 1.8 branches.</p></div><div id="comment-25335-info" class="comment-info"><span class="comment-age">(28 Sep '13, 15:07)</span> Guy Harris ♦♦</div></div><span id="25337"></span><div id="comment-25337" class="comment"><div id="post-25337-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot, Guy, awesome work!</p></div><div id="comment-25337-info" class="comment-info"><span class="comment-age">(29 Sep '13, 01:13)</span> Jasper ♦♦</div></div></div><div id="comment-tools-25331" class="comment-tools"></div><div class="clear"></div><div id="comment-25331-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

