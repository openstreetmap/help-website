+++
type = "question"
title = "Wireshark not releasing memory back to OS while open..."
description = '''Hi all, I am running some tests with Wireshark 1.8.4 on OSX (10.8.6). Long story short:  Open 700MB capture with default settings except Sub-dissector reassembly disabled Wireshark memory usage at a nice 700 MB or so Follow stream that is huge Follow stream pop-up window displays Memory usage now at...'''
date = "2013-01-24T12:39:00Z"
lastmod = "2013-01-24T18:50:00Z"
weight = 17941
keywords = [ "wireshark", "follow.tcp.stream", "memory" ]
aliases = [ "/questions/17941" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark not releasing memory back to OS while open...](/questions/17941/wireshark-not-releasing-memory-back-to-os-while-open)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17941-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17941-score" class="post-score" title="current number of votes">1</div><span id="post-17941-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I am running some tests with Wireshark 1.8.4 on OSX (10.8.6). Long story short:</p><ul><li>Open 700MB capture with default settings except Sub-dissector reassembly disabled</li><li>Wireshark memory usage at a nice 700 MB or so</li><li>Follow stream that is huge</li><li>Follow stream pop-up window displays</li><li>Memory usage now at 3GB (meh, not great, but OK)</li><li>Close follow stream pop-up and clear tcp.stream filter</li><li>Memory usage now at 2.7GB</li></ul><p>Ideally I would expect the memory usage to drop back to the 700MB seen prior. Now if I do the same steps again, we creep from the current 2.7 GB back up to the 3GB. So it looks like Wireshark allocates as much memory as it needed to do the follow-stream filter, does not fully release it all, but reuses this leftover 2GB that was not released. In the end it does not seem to leak more memory, but it never releases all it had.</p><p>I'm not programming expert from a memory perspective, but for those have dug into this, any idea why Wireshark would not release all the way back to 700MB? With multiple captures and multiple instances of Wireshark open, I would rather not have one instance using more memory than what it needs at that time.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-follow.tcp.stream" rel="tag" title="see questions tagged &#39;follow.tcp.stream&#39;">follow.tcp.stream</span> <span class="post-tag tag-link-memory" rel="tag" title="see questions tagged &#39;memory&#39;">memory</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jan '13, 12:39</strong></p><img src="https://secure.gravatar.com/avatar/f4567d2db9c9f422c664030ac53a1873?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Magnus%20Mortensen&#39;s gravatar image" /><p><span>Magnus Morte...</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Magnus Mortensen has one accepted answer">50%</span></p></div></div><div id="comments-container-17941" class="comments-container"></div><div id="comment-tools-17941" class="comment-tools"></div><div class="clear"></div><div id="comment-17941-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17946"></span>

<div id="answer-container-17946" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17946-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17946-score" class="post-score" title="current number of votes">1</div><span id="post-17946-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>So it looks like Wireshark allocates as much memory as it needed to do the follow-stream filter, does not fully release it all, but reuses this leftover 2GB that was not released.</p></blockquote><p>That's how many memory allocators work - freeing the memory doesn't release it back to the OS, it just adds it to a pool from which future allocations are satisfied.</p><p>Note that what a memory allocator <em>really</em> allocates, on modern OSes, is virtual address space; not all of that virtual address space is necessarily in main memory - it might be on swap space.</p><p>What are you using to determine the memory usage? Activity Monitor and, if so, which column (real or virtual memory)? vmmap? Some other tool?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jan '13, 17:57</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-17946" class="comments-container"><span id="17949"></span><div id="comment-17949" class="comment"><div id="post-17949-score" class="comment-score"></div><div class="comment-text"><p>Guy, My hunch was what you indicated. For my tests I was using Activity Monitor, focussing on the 'Real Mem' column for wireshark-bin. The whole reason I started looking into this was that while going through two very large capture files (2 x 700MB, full packet) , simultaneously (two instances of wireshark-bin), OS X's indication of "Free Memory" dropped to near zero and anything being done at the moment in wirseshark ground to a halt. At the time this was happening there was over 2GB of what OS X dubs as 'Inactive Memory'. From my reading this memory is free to be used by the system, but still contains cached data from application that may have used it in the past. This pseudo-free memory seems never to be re-used by wireshark (just an observation, but I may be way off). When I reach &lt;50MB "Free" memory, I usually find that perforamcne is improved by running <strong>purge</strong> from the command line (frees inactive memory into free memory) and wireshark picks back up processing until we hit the &lt;50MB free situation again.</p><p>Ideally, if wireshark used only the memory it needed at the time, i could have both files open with wireshark humming at a svelt 700mb RAM usage. If I were to run a task on one capture (follow stream) and then close that stream (reverting back to the initial state of post-capture-loaded, I would hope to have just the two instances at 700MB of ram each. And...</p><p><img src="http://weknowmemes.com/wp-content/uploads/2012/01/theres-so-much-room-for-activities.jpg" alt="alt text" /></p></div><div id="comment-17949-info" class="comment-info"><span class="comment-age">(24 Jan '13, 18:39)</span> <span class="comment-user userinfo">Magnus Morte...</span></div></div></div><div id="comment-tools-17946" class="comment-tools"></div><div class="clear"></div><div id="comment-17946-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17950"></span>

<div id="answer-container-17950" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17950-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17950-score" class="post-score" title="current number of votes">0</div><span id="post-17950-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If "free memory" always has a large value on an OS X machine, that means you paid too much for your machine. :-)</p><p>Just because it's low, that's not necessarily a bad thing.</p><p>I'd have to spend some time looking at the xnu VM code to determine exactly what "free" and "inactive" memory are; if a page fault occurs that requires either a page-in from a file or swap space or the zero-fill-on-demand allocation of a page, the VM code will probably prefer to take a "free" page frame rather than an "inactive" page frame and would probably prefer to take an "inactive" page frame than an "active" page frame ("wired" page frames are ineligible, as they're "wired down" into memory). I'd have to spend some more time looking at the VM code to see what rules it uses to decide which "inactive" page frame to take.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jan '13, 18:50</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></img></div></div><div id="comments-container-17950" class="comments-container"></div><div id="comment-tools-17950" class="comment-tools"></div><div class="clear"></div><div id="comment-17950-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

