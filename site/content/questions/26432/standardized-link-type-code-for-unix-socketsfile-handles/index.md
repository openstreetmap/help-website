+++
type = "question"
title = "Standardized link type code for unix sockets/file handles"
description = '''I&#x27;m writing a utility which uses SSH as the transport, much like Git uses SSH for pushes. Additionally I wrote a utility which executes a command and then captures the STDIN, STDOUT, and STDERR to the executed command. The capture utility currently writes the dump file so that it appears as a RAW li...'''
date = "2013-10-26T21:48:00Z"
lastmod = "2013-10-28T02:35:00Z"
weight = 26432
keywords = [ "pipe", "linktype", "socket" ]
aliases = [ "/questions/26432" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Standardized link type code for unix sockets/file handles](/questions/26432/standardized-link-type-code-for-unix-socketsfile-handles)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26432-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26432-score" class="post-score" title="current number of votes">0</div><span id="post-26432-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm writing a utility which uses SSH as the transport, much like Git uses SSH for pushes. Additionally I wrote a utility which executes a command and then captures the STDIN, STDOUT, and STDERR to the executed command. The capture utility currently writes the dump file so that it appears as a RAW link type and UDP packets.</p><p>Is it possible to create a new link type code for raw file handles?</p><p>I'm envisioning a packet structure which contains:</p><p>4 byte file descriptor 1 byte (0x01 == read data, 0x02 == write data, 0x03 == UTF8 error message) 3 byte errno code (if error) ? byte data</p><p>This would remove the confusion of the source/destination IP address and ports when I send the capture to co-workers. It would also allow future development to create a Follow Shell session for file descriptors STDIN_FILENO, STDOUT_FILENO, and STDERR_FILENO much like the follow TCP or follow UDP features.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pipe" rel="tag" title="see questions tagged &#39;pipe&#39;">pipe</span> <span class="post-tag tag-link-linktype" rel="tag" title="see questions tagged &#39;linktype&#39;">linktype</span> <span class="post-tag tag-link-socket" rel="tag" title="see questions tagged &#39;socket&#39;">socket</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '13, 21:48</strong></p><img src="https://secure.gravatar.com/avatar/71a12eeab93dcad7f31a41637075e3d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="syzdek&#39;s gravatar image" /><p><span>syzdek</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="syzdek has no accepted answers">0%</span></p></div></div><div id="comments-container-26432" class="comments-container"></div><div id="comment-tools-26432" class="comment-tools"></div><div class="clear"></div><div id="comment-26432-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="26445"></span>

<div id="answer-container-26445" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26445-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26445-score" class="post-score" title="current number of votes">0</div><span id="post-26445-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="syzdek has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I wrote a utility which executes a command and then captures the STDIN, STDOUT, and STDERR to the executed command.</p></blockquote><p>Here is how I understand what you are trying to do.</p><ul><li>You are capturing/recording the raw data (payload) of STD*</li><li>You write that in a pcap like file structure</li><li>You have a data structure to distinguish the three STD* 'channels'</li><li>You need a new link type (for what exactly)?</li></ul><p>Here is what you could do</p><ul><li>Use a user defined link layer type (DLT_USER 0-15, DLT = 147-163), see here: <a href="http://wiki.wireshark.org/HowToDissectAnything">http://wiki.wireshark.org/HowToDissectAnything</a></li><li>Write your own dissector that is able to handle your data structure and which shows the content of the STD* 'channels' with or without 'Follow Stream' functionality (needs to be added additionally to the dissector).</li></ul><p>If that's is <strong>not</strong> what you are trying to do:</p><p>please add more details, as I might not fully understand your intention.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '13, 11:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-26445" class="comments-container"></div><div id="comment-tools-26445" class="comment-tools"></div><div class="clear"></div><div id="comment-26445-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26436"></span>

<div id="answer-container-26436" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26436-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26436-score" class="post-score" title="current number of votes">0</div><span id="post-26436-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The tcpdump/libpcap folks are the ones who look after this. See <a href="http://www.tcpdump.org/linktypes.html">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '13, 07:02</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-26436" class="comments-container"><span id="26458"></span><div id="comment-26458" class="comment"><div id="post-26458-score" class="comment-score"></div><div class="comment-text"><p>When looking at the tcpdump link types, I missed the user defined types and they were not mentioned in the PCAP Next Generation Format. I wanted a link type which would not require me to encapsulate the data within bogus IP/UDP or IP/TCP packets. Briefly scanning the linked wiki article,it appears the user defined link layer types should work perfectly. Thanks.</p></div><div id="comment-26458-info" class="comment-info"><span class="comment-age">(28 Oct '13, 02:35)</span> <span class="comment-user userinfo">syzdek</span></div></div></div><div id="comment-tools-26436" class="comment-tools"></div><div class="clear"></div><div id="comment-26436-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

