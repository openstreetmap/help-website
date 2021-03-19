+++
type = "question"
title = "wireshark coredumps during load"
description = '''I have a wireshark dissector plugin. I also have a wireshark installed from apt-get. The wireshark loads fine without the plugin inserted in the right place. When I include the plugin .so file and try to run wireshark, I get the following error: $ wireshark 08:23:45 Err register_subtree_array: subtr...'''
date = "2013-12-03T08:40:00Z"
lastmod = "2013-12-03T10:50:00Z"
weight = 27721
keywords = [ "gdb", "dissector", "wireshark", "plugin", "linux" ]
aliases = [ "/questions/27721" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark coredumps during load](/questions/27721/wireshark-coredumps-during-load)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27721-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a wireshark dissector plugin. I also have a wireshark installed from apt-get.</p><p>The wireshark loads fine without the plugin inserted in the right place. When I include the plugin .so file and try to run wireshark, I get the following error:</p><pre><code>$ wireshark
08:23:45          Err  register_subtree_array: subtree item type (ett_...) not -1 ! This is a development error: Either the subtree item type has already been assigned or was not initialized to -1.
Trace/breakpoint trap (core dumped)</code></pre><p>I tried understanding the problem. It says the subtree was already assigned (I'm assuming assigned an ett value) or was not initialized with -1.</p><p>there are 3 files in my plugin where the API is called and I checked the values of ett[] being supplied to the API in each of these places. They are all initialized to -1.</p><p>Stuck in a roadblock. Any suggestion would be helpful.</p><p>Also, I do not understand where wireshark dumps the core. I could not find any core. Any idea about this?</p></div><div id="question-tags" class="tags-container tags">gdb dissector wireshark plugin linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Dec '13, 08:40</strong></p><img src="https://secure.gravatar.com/avatar/0a3500d83a034d54be7470d7ed010604?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pysudhir&#39;s gravatar image" /><p>pysudhir<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pysudhir has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Dec '13, 08:41</p></div></div><div id="comments-container-27721" class="comments-container"><span id="27722"></span><div id="comment-27722" class="comment"><div id="post-27722-score" class="comment-score"></div><div class="comment-text"><p>As I indicated at <a href="http://stackoverflow.com/questions/20323798/how-to-debug-wireshark-plugin-using-gdb:">http://stackoverflow.com/questions/20323798/how-to-debug-wireshark-plugin-using-gdb:</a></p><p>You need to first ensure that you can build wireshark and your plugin and that this dev wireshark/plugin load and work.</p><p>Based upon your comments, I get the impression that you are building just the plugin and then trying to use it with an installed wireshark. This may work, but it's not the place to start.</p></div><div id="comment-27722-info" class="comment-info"><span class="comment-age">(03 Dec '13, 09:04)</span> Bill Meier ♦♦</div></div><span id="27723"></span><div id="comment-27723" class="comment"><div id="post-27723-score" class="comment-score"></div><div class="comment-text"><p>I have seen a similar thing happen with an older wireshark. That's the reason I wasn't very worried about the approach. However, I believe that this question is a little different compared to that.</p></div><div id="comment-27723-info" class="comment-info"><span class="comment-age">(03 Dec '13, 09:07)</span> pysudhir</div></div></div><div id="comment-tools-27721" class="comment-tools"></div><div class="clear"></div><div id="comment-27721-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27727"></span>

<div id="answer-container-27727" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27727-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>register_subtree_array: subtree item type (ett_...) not -1</p></blockquote><p>...</p><blockquote><p>there are 3 files in my plugin where the API is called and I checked the values of ett[] being supplied to the API in each of these places. They are all initialized to -1.</p></blockquote><p>To which API are you referring? You must not call <code>register_subtree_array()</code> on any particular <code>ett_</code> array more than once; if you're calling it twice, the first call will cause the <code>ett_</code> values in the array to be set to values different from -1, so the next call will fail with that error.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Dec '13, 10:50</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-27727" class="comments-container"><span id="27740"></span><div id="comment-27740" class="comment"><div id="post-27740-score" class="comment-score"></div><div class="comment-text"><p>That was exactly what I thought. And the error is pretty self explanatory. But, I have checked all the instances of the API register_subtre_array and found that none of the instances are making use of the same ett_ array.</p></div><div id="comment-27740-info" class="comment-info"><span class="comment-age">(03 Dec '13, 19:18)</span> pysudhir</div></div><span id="27744"></span><div id="comment-27744" class="comment"><div id="post-27744-score" class="comment-score"></div><div class="comment-text"><p>Would it be possible to post your plugin code?</p></div><div id="comment-27744-info" class="comment-info"><span class="comment-age">(03 Dec '13, 23:31)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-27727" class="comment-tools"></div><div class="clear"></div><div id="comment-27727-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

