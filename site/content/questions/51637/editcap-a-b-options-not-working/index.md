+++
type = "question"
title = "editcap -A -B options not working"
description = '''Hi, I&#x27;m using editcap.exe command from Windows 7 console and not getting desired output. The exact command is: C:&#92;&quot;C:&#92;Program Files&#92;Wireshark&#92;editcap.exe&quot; -v -A &quot;2016-04-13 14:09:00&quot; -B &quot;2016-04-13 14:18:00&quot; 160413csi05.snoop 160413csi05_narrowtime.snoop File 160413csi05.snoop is a Sun snoop capture...'''
date = "2016-04-13T08:33:00Z"
lastmod = "2016-04-14T11:48:00Z"
weight = 51637
keywords = [ "timestamps", "editcap" ]
aliases = [ "/questions/51637" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [editcap -A -B options not working](/questions/51637/editcap-a-b-options-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51637-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51637-score" class="post-score" title="current number of votes">0</div><span id="post-51637-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm using editcap.exe command from Windows 7 console and not getting desired output. The exact command is:</p><pre><code>C:\&quot;C:\Program Files\Wireshark\editcap.exe&quot; -v -A &quot;2016-04-13 14:09:00&quot; -B &quot;2016-04-13 14:18:00&quot; 160413csi05.snoop 160413csi05_narrowtime.snoop
File 160413csi05.snoop is a Sun snoop capture file.</code></pre><p>The 160413csi05_narrowtime.snoop is created with file size of 1K. The file opens in Wireshark GUI but there is nothing in file.</p><p>The original 160413csi05.snoop file date range is 2016-04-13 12:23:04 for frame 1 to 2016-04-13 14:43:42 for frame 92163.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timestamps" rel="tag" title="see questions tagged &#39;timestamps&#39;">timestamps</span> <span class="post-tag tag-link-editcap" rel="tag" title="see questions tagged &#39;editcap&#39;">editcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Apr '16, 08:33</strong></p><img src="https://secure.gravatar.com/avatar/73b51f0024ff1a0273aa7267f541b234?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="major&#39;s gravatar image" /><p><span>major</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="major has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Apr '16, 08:40</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-51637" class="comments-container"><span id="51639"></span><div id="comment-51639" class="comment"><div id="post-51639-score" class="comment-score"></div><div class="comment-text"><p>editcap version (<code>-V</code>)?</p></div><div id="comment-51639-info" class="comment-info"><span class="comment-age">(13 Apr '16, 08:42)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="51640"></span><div id="comment-51640" class="comment"><div id="post-51640-score" class="comment-score"></div><div class="comment-text"><p>C:&gt;"C:\Program Files\Wireshark\editcap.exe" -version C:\Program Files\Wireshark\editcap.exe: invalid option -- 'e' Editcap 1.12.4 (v1.12.4-0-gb4861da from master-1.12) Edit and/or translate the format of capture files. See <a href="http://www.wireshark.org">http://www.wireshark.org</a> for more information.</p></div><div id="comment-51640-info" class="comment-info"><span class="comment-age">(13 Apr '16, 09:03)</span> <span class="comment-user userinfo">major</span></div></div><span id="51646"></span><div id="comment-51646" class="comment"><div id="post-51646-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@grahamb</span> It's a lower-case <code>'v'</code>, not an uppercase <code>'v'</code>, so it's the verbose option.</p></div><div id="comment-51646-info" class="comment-info"><span class="comment-age">(13 Apr '16, 11:39)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="51649"></span><div id="comment-51649" class="comment"><div id="post-51649-score" class="comment-score"></div><div class="comment-text"><p><span>@cmaynard</span></p><p>The uppercase -V was to get the version info.</p></div><div id="comment-51649-info" class="comment-info"><span class="comment-age">(13 Apr '16, 13:57)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-51637" class="comment-tools"></div><div class="clear"></div><div id="comment-51637-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51673"></span>

<div id="answer-container-51673" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51673-score" class="post-score" title="current number of votes">0</div><span id="post-51673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><span>@major</span>, It works for me with <code>editcap</code> from 1.12.10, so I don't know why it doesn't work for you; however, if you want the output file to be a snoop file, you need to specify <code>-F snoop</code>.</p><p>One thought as to why it might not be working would be if the capture was taken in a different time zone than where you are, but you ought to be able to verify the timestamps by running <code>capinfos 160413csi05_narrowtime.snoop</code> and looking at the Start and End times.</p><p>(Moved from comment to answer since this was the solution.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Apr '16, 11:48</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-51673" class="comments-container"><span id="51668"></span><div id="comment-51668" class="comment"><div id="post-51668-score" class="comment-score"></div><div class="comment-text"><p>cmaynard's suggestion to check time zones using capinfo worked. The snoop was originally captured on a Solaris 10 system that uses UTC. My local laptop uses Central time. The below command worked:</p><pre><code>C:\&gt;&quot;C:\Program Files\Wireshark\editcap.exe&quot; -v -F snoop -A &quot;2016-04-13 09:09:00&quot; -B &quot;2016-04-13 09:18:00&quot; 160413csi05.snoop 160413csi05_narrowtime.snoop</code></pre><p>Thanks for all the assistance!</p></div><div id="comment-51668-info" class="comment-info"><span class="comment-age">(14 Apr '16, 07:28)</span> <span class="comment-user userinfo">major</span></div></div></div><div id="comment-tools-51673" class="comment-tools"></div><div class="clear"></div><div id="comment-51673-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

