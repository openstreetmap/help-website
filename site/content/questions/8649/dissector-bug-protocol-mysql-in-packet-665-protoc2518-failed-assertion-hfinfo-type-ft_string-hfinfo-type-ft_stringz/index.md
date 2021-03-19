+++
type = "question"
title = "Dissector bug, protocol MySQL, in packet 665: proto.c:2518: failed assertion &quot;hfinfo-&gt;type == FT_STRING || hfinfo-&gt;type == FT_STRINGZ&quot;"
description = '''I am getting this error: WARNING **: Dissector bug, protocol MySQL, in packet 665: proto.c:2518: failed assertion &quot;hfinfo-&amp;gt;type == FT_STRING || hfinfo-&amp;gt;type == FT_STRINGZ&quot;  What is the possible reason?'''
date = "2012-01-27T04:04:00Z"
lastmod = "2012-01-27T17:29:00Z"
weight = 8649
keywords = [ "development", "exception", "dissector", "wireshark" ]
aliases = [ "/questions/8649" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Dissector bug, protocol MySQL, in packet 665: proto.c:2518: failed assertion "hfinfo-&gt;type == FT\_STRING || hfinfo-&gt;type == FT\_STRINGZ"](/questions/8649/dissector-bug-protocol-mysql-in-packet-665-protoc2518-failed-assertion-hfinfo-type-ft_string-hfinfo-type-ft_stringz)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8649-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am getting this error:</p><pre><code>WARNING **: Dissector bug, protocol MySQL, in packet 665: proto.c:2518: failed assertion &quot;hfinfo-&gt;type == FT_STRING || hfinfo-&gt;type == FT_STRINGZ&quot;</code></pre><p>What is the possible reason?</p></div><div id="question-tags" class="tags-container tags">development exception dissector wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jan '12, 04:04</strong></p><img src="https://secure.gravatar.com/avatar/425d250364423a7595a3eb9dea779cb2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanny_D&#39;s gravatar image" /><p>Sanny_D<br />
<span class="score" title="0 reputation points">0</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanny_D has 3 accepted answers">50%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Jan '12, 06:20</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-8649" class="comments-container"></div><div id="comment-tools-8649" class="comment-tools"></div><div class="clear"></div><div id="comment-8649-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="8658"></span>

<div id="answer-container-8658" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8658-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I believe the problem is likely because of a bug that was fixed in <a href="http://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=39873">revision 39873</a>. Unfortunately, the fix was not back-ported to the 1.6 branch, but <a href="http://wiki.wireshark.org/Development/Roadmap">I have scheduled it</a> for 1.6.6.<br />
</p><p>Of course, without a capture file to test against, it's impossible to say for sure if this is the actual problem or not. If you can apply the patch yourself and test it, that would confirm it. Alternatively, you could post a small capture file to either the wireshark-dev or wireshark-users <a href="http://www.wireshark.org/lists/">mailing lists</a>, and someone could probably test it.</p><p>Another option would be to download and install a development version of the Wireshark installer post-r39873, such as one of those found <a href="http://www.wireshark.org/download/automated/win32/">here</a>, then test it to see if the problem is resolved.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jan '12, 17:29</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span> </br></p></div></div><div id="comments-container-8658" class="comments-container"><span id="8659"></span><div id="comment-8659" class="comment"><div id="post-8659-score" class="comment-score"></div><div class="comment-text"><p><a href="http://code.google.com/p/loganon/source/browse/lib/tests/libwireshark-dissection/shark-test.c?r=929dc4492abf156d1cdc1b492361f2e1c7a80830">http://code.google.com/p/loganon/source/browse/lib/tests/libwireshark-dissection/shark-test.c?r=929dc4492abf156d1cdc1b492361f2e1c7a80830</a></p><p>this is the code m using!</p><p>its not reading a capture file.. directly its dissecting the u_char* packet</p></div><div id="comment-8659-info" class="comment-info"><span class="comment-age">(27 Jan '12, 21:11)</span> Sanny_D</div></div><span id="8677"></span><div id="comment-8677" class="comment"><div id="post-8677-score" class="comment-score"></div><div class="comment-text"><p>None of that matters; the dissection code neither knows nor cares whether you're reading a capture file.</p><p>As Chris noted, there's a bug in the MySQL dissector that can cause it to report an exception, and there's nothing you can do in <em>your</em> code to avoid it (other than not calling <code>epan_dissect_run()</code>, but then your code wouldn't actually dissect anything :-)) - you need to get a version of libwireshark that doesn't have the bug, either by waiting for Wireshark 1.6.6, using the development version, or patching the Wireshark source yourself.</p></div><div id="comment-8677-info" class="comment-info"><span class="comment-age">(28 Jan '12, 12:30)</span> Guy Harris ♦♦</div></div><span id="8687"></span><div id="comment-8687" class="comment"><div id="post-8687-score" class="comment-score"></div><div class="comment-text"><p>thanks harris :-) patching the 1.6.4 is the solution :-)</p></div><div id="comment-8687-info" class="comment-info"><span class="comment-age">(30 Jan '12, 02:05)</span> Sanny_D</div></div></div><div id="comment-tools-8658" class="comment-tools"></div><div class="clear"></div><div id="comment-8658-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8654"></span>

<div id="answer-container-8654" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8654-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should try running Wireshark using a debugger; this will help you isolate what line in your dissector code is failing. Looking at <code>epan/proto.c</code> on line 2518 from the latest SVN version doesn't seem particularly helpful:</p><pre><code> 2517:               const char *format, ...)
&gt;2518:{
 2519:  proto_item      *pi;</code></pre><p>What version of the source are you using, and have you made any modifications to <code>proto.c</code>?</p><p><strong>Edit:</strong> The line in question for 1.6.4 is this:</p><pre><code>    header_field_info *hfinfo;</code></pre><p>I'm going to guess that the problem is really from line 2522:</p><pre><code>    DISSECTOR_ASSERT(hfinfo-&gt;type == FT_STRING || hfinfo-&gt;type == FT_STRINGZ);</code></pre><p>I'm going to guess that you have called <code>proto_tree_add_string</code> with an <code>hfindex</code> that does not reference an <code>FT_STRING</code> or <code>FT_STRINGZ</code> type field. I would strongly recommend running the application in a debugger to inspect the actual values at runtime, and very likely find whatever is causing this error so that you can fix it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jan '12, 06:23</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Jan '12, 07:03</p></div></div><div id="comments-container-8654" class="comments-container"><span id="8655"></span><div id="comment-8655" class="comment"><div id="post-8655-score" class="comment-score"></div><div class="comment-text"><p>wireshark 1.6.4</p><p>no.. i havent done any modification to proto.c</p></div><div id="comment-8655-info" class="comment-info"><span class="comment-age">(27 Jan '12, 06:54)</span> Sanny_D</div></div></div><div id="comment-tools-8654" class="comment-tools"></div><div class="clear"></div><div id="comment-8654-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

