+++
type = "question"
title = "Can mergecap write gzipped files directly?"
description = '''I see in the documentation that mergecap reads and expands gzipped pcap files on the fly. However, I can&#x27;t see any option for creating a gzipped file as the result of the merge, ditto for editcap. I&#x27;m using Windows 7. Does such an option exist? If not, are there any plans to add it?'''
date = "2016-04-26T17:41:00Z"
lastmod = "2016-04-27T06:30:00Z"
weight = 51979
keywords = [ "mergecap" ]
aliases = [ "/questions/51979" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can mergecap write gzipped files directly?](/questions/51979/can-mergecap-write-gzipped-files-directly)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51979-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I see in the documentation that mergecap reads and expands gzipped pcap files on the fly. However, I can't see any option for creating a gzipped file as the result of the merge, ditto for editcap. I'm using Windows 7.</p><p>Does such an option exist?</p><p>If not, are there any plans to add it?</p></div><div id="question-tags" class="tags-container tags">mergecap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Apr '16, 17:41</strong></p><img src="https://secure.gravatar.com/avatar/ec459a9dbac1eaa624ca207ad1e5f4c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LurkingKiwi&#39;s gravatar image" /><p>LurkingKiwi<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LurkingKiwi has no accepted answers">0%</span></p></div></div><div id="comments-container-51979" class="comments-container"></div><div id="comment-tools-51979" class="comment-tools"></div><div class="clear"></div><div id="comment-51979-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52013"></span>

<div id="answer-container-52013" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52013-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, there doesn't appear to be a way to convince mergecap or editcap to write gzip'd files.</p><p>It appears making 'editcap' do it would be quite easy: it just needs a command-line option and to pass a boolean (based on that option) to <code>wtap_dump_open_ng()</code>.</p><p>mergecap doesn't currently use the wiretap routines so making it write gzip'd files would be harder.</p><p>I can't find any enhancement requests asking for such functionality. You could always <a href="https://bugs.wireshark.org">open one</a> if you could use the functionality. If you do, please be sure to:</p><ol><li>Mention this question in the bug</li><li>Add a comment here with a link to the bug</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '16, 06:30</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-52013" class="comments-container"><span id="52028"></span><div id="comment-52028" class="comment"><div id="post-52028-score" class="comment-score"></div><div class="comment-text"><p>Enhancement request created: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12385">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12385</a></p></div><div id="comment-52028-info" class="comment-info"><span class="comment-age">(27 Apr '16, 16:42)</span> LurkingKiwi</div></div></div><div id="comment-tools-52013" class="comment-tools"></div><div class="clear"></div><div id="comment-52013-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

