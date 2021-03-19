+++
type = "question"
title = "Name resolution is not happening via host file in AppData directory"
description = '''Hi, I am using Version 2.2.0 (v2.2.0-0-g5368c50 from master-2.2) of Wireshark which the most recent one. I have updated the &quot;hosts&quot; file that is located in C:&#92;Users&#92;administrator&#92;AppData&#92;Roaming&#92;Wireshark Every time I reboot wireshark or reload capture files then name resolution does not get shown a...'''
date = "2016-10-05T02:14:00Z"
lastmod = "2016-10-05T08:38:00Z"
weight = 56148
keywords = [ "hostfileissue" ]
aliases = [ "/questions/56148" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Name resolution is not happening via host file in AppData directory](/questions/56148/name-resolution-is-not-happening-via-host-file-in-appdata-directory)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56148-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am using Version 2.2.0 (v2.2.0-0-g5368c50 from master-2.2) of Wireshark which the most recent one.</p><p>I have updated the "hosts" file that is located in <code>C:\Users\administrator\AppData\Roaming\Wireshark</code></p><p>Every time I reboot wireshark or reload capture files then name resolution does not get shown as per hosts file. I have tried different combination in check boxes of name resolution menu. That is keeping only view from hosts file, keeping multiple check boxes including view from hosts file, but no luck.</p><p>Please help.</p></div><div id="question-tags" class="tags-container tags">hostfileissue</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Oct '16, 02:14</strong></p><img src="https://secure.gravatar.com/avatar/bbad862d3f8e3b14c254bba392f1daa7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Engineer786&#39;s gravatar image" /><p>Engineer786<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Engineer786 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Oct '16, 06:23</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-56148" class="comments-container"><span id="56150"></span><div id="comment-56150" class="comment"><div id="post-56150-score" class="comment-score"></div><div class="comment-text"><p>Your OS?</p><p>What does the Help -&gt; About Wireshark -&gt; Folders dialog show for the Personal configuration location?</p></div><div id="comment-56150-info" class="comment-info"><span class="comment-age">(05 Oct '16, 03:06)</span> grahamb ♦</div></div><span id="56152"></span><div id="comment-56152" class="comment"><div id="post-56152-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>My OS is Win7.</p><p>The About Wireshark shows:</p><p>Personal configuration C:\Users\administrator\AppData\Roaming\Wireshark\</p><p>Thanks.</p></div><div id="comment-56152-info" class="comment-info"><span class="comment-age">(05 Oct '16, 03:34)</span> Engineer786</div></div><span id="56153"></span><div id="comment-56153" class="comment"><div id="post-56153-score" class="comment-score"></div><div class="comment-text"><p>Then that location is where you should be placing your hosts file.</p></div><div id="comment-56153-info" class="comment-info"><span class="comment-age">(05 Oct '16, 03:40)</span> grahamb ♦</div></div><span id="56154"></span><div id="comment-56154" class="comment"><div id="post-56154-score" class="comment-score"></div><div class="comment-text"><p>Yes. My hosts file is located over here. Do I need to specifically check and uncheck some options in Preferences &gt; Name resolution section?</p></div><div id="comment-56154-info" class="comment-info"><span class="comment-age">(05 Oct '16, 03:41)</span> Engineer786</div></div><span id="56155"></span><div id="comment-56155" class="comment"><div id="post-56155-score" class="comment-score"></div><div class="comment-text"><p>Your question states you have the hosts file in</p><blockquote>Users &gt; Admin &gt; App Data &gt; Wireshark</blockquote><p>which is not the same as</p><blockquote>Personal configuration C:\Users\administrator\AppData\Roaming\Wireshark</blockquote></div><div id="comment-56155-info" class="comment-info"><span class="comment-age">(05 Oct '16, 03:47)</span> grahamb ♦</div></div><span id="56156"></span><div id="comment-56156" class="comment not_top_scorer"><div id="post-56156-score" class="comment-score"></div><div class="comment-text"><p>Sorry, that was a typo. I was typing it from memory without copying paste the exact path.</p></div><div id="comment-56156-info" class="comment-info"><span class="comment-age">(05 Oct '16, 03:50)</span> Engineer786</div></div><span id="56157"></span><div id="comment-56157" class="comment not_top_scorer"><div id="post-56157-score" class="comment-score"></div><div class="comment-text"><p>Sorry, that was a typo. The hosts file in my PC is located over here:</p><p>C:\Users\administrator\AppData\Roaming\Wireshark</p></div><div id="comment-56157-info" class="comment-info"><span class="comment-age">(05 Oct '16, 03:54)</span> Engineer786</div></div><span id="56158"></span><div id="comment-56158" class="comment not_top_scorer"><div id="post-56158-score" class="comment-score"></div><div class="comment-text"><p>Works for me, edit hosts, load capture, new name shows up.</p><p>Can you show a (anonymized if necessary) snippet of your hosts file to ensure you have the data in the correct format?</p><p>What options do you have selected on the Name Resolution preferences?</p></div><div id="comment-56158-info" class="comment-info"><span class="comment-age">(05 Oct '16, 04:38)</span> grahamb ♦</div></div></div><div id="comment-tools-56148" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-56148-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56166"></span>

<div id="answer-container-56166" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56166-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi. It finally worked for me. I had to carry out few steps though. The names were one word without any space within hosts file. Check Resolve MAC addresses Check Resolve network (IP) addresses</p><p>Thanks for your kind support and looking into this.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Oct '16, 08:38</strong></p><img src="https://secure.gravatar.com/avatar/bbad862d3f8e3b14c254bba392f1daa7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Engineer786&#39;s gravatar image" /><p>Engineer786<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Engineer786 has no accepted answers">0%</span></p></div></div><div id="comments-container-56166" class="comments-container"><span id="56170"></span><div id="comment-56170" class="comment"><div id="post-56170-score" class="comment-score"></div><div class="comment-text"><p>The preference option you needed would have been Resolve network (IP) addresses</p></div><div id="comment-56170-info" class="comment-info"><span class="comment-age">(05 Oct '16, 11:44)</span> grahamb ♦</div></div></div><div id="comment-tools-56166" class="comment-tools"></div><div class="clear"></div><div id="comment-56166-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

