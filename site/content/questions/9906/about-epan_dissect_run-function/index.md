+++
type = "question"
title = "About epan_dissect_run function"
description = '''I am now reading source code of wireshark and have leaned much from it. Thank you for all developers. But I am confused about &quot;epan_dissect_run&quot; function. When we get a packet from the capture file, we used &quot;read_packet&quot; function to read and dissect the packet; In the &quot;read_packet&quot; we call the funct...'''
date = "2012-04-02T20:45:00Z"
lastmod = "2012-08-24T01:04:00Z"
weight = 9906
keywords = [ "epan" ]
aliases = [ "/questions/9906" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [About epan\_dissect\_run function](/questions/9906/about-epan_dissect_run-function)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9906-score" class="post-score" title="current number of votes">0</div><span id="post-9906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am now reading source code of wireshark and have leaned much from it. Thank you for all developers.</p><p>But I am confused about "epan_dissect_run" function.</p><p>When we get a packet from the capture file, we used "read_packet" function to read and dissect the packet; In the "read_packet" we call the function named "epan_dissect_run" to dissect the packet;But I also find the "epan_dissect_run" function called in the callback fuction "show_cell_data_func";</p><p>My first question : why "epan_dissect_run" function is called two times?</p><p>Second Question: I set a breakpoint at my dissector.Through the stack view by vs2005, I always find it Reaches the breakpoint just called by "show_cell_data_func", why not called by "read_packet"?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-epan" rel="tag" title="see questions tagged &#39;epan&#39;">epan</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Apr '12, 20:45</strong></p><img src="https://secure.gravatar.com/avatar/2f2143723c2bece1840d64bbd18dc04d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="taiyangluoyu&#39;s gravatar image" /><p><span>taiyangluoyu</span><br />
<span class="score" title="0 reputation points">0</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="taiyangluoyu has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Apr '12, 08:14</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-9906" class="comments-container"></div><div id="comment-tools-9906" class="comment-tools"></div><div class="clear"></div><div id="comment-9906-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9915"></span>

<div id="answer-container-9915" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9915-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9915-score" class="post-score" title="current number of votes">3</div><span id="post-9915-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>First question:</p><p><code>epan_dissect_run()</code> is being called twice because it's called when a capture is read in (that's the call from <code>read_packet()</code>), when a packet's summary information is displayed in the packet list in the GUI (that's the call from <code>show_cell_data_func()</code>), when you click on the packet to show its details, when you filter the display, when you use some of the Analyze and Statistics menu items, etc.. Wireshark does <em>not</em> save the information from the dissections done when the capture is read in, because that would greatly increase its memory usage and slow it down.</p><p>Therefore, your dissector <em>MUST</em> be prepared to be called more than once.</p><p>Second question:</p><p>The dissector that calls your dissector might be buggy and not always calling subdissectors such as yours. How are you registering your dissector to be called?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Apr '12, 08:13</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-9915" class="comments-container"><span id="13857"></span><div id="comment-13857" class="comment"><div id="post-13857-score" class="comment-score"></div><div class="comment-text"><p>I changed the source ip address value in dissect_ip() while debugging ,during first epan_dissect_run .</p><p>When i hit second break point i could see this time when i apply filter the epan_dissect_run() is called but the data which is kept is last iteration itself is used, Why does it decode it again if every thing he is going to consumed from last pass .?</p></div><div id="comment-13857-info" class="comment-info"><span class="comment-age">(24 Aug '12, 01:04)</span> <span class="comment-user userinfo">Harsha</span></div></div></div><div id="comment-tools-9915" class="comment-tools"></div><div class="clear"></div><div id="comment-9915-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

