+++
type = "question"
title = "tshark smb,srt filter error"
description = '''Hi All, i am trying to get some smb statistics for certain file using tshark , i think i am using the correct syntax but still getting errors as follows below even if i remove the &#92; i get invalid - &quot;New&quot; was unexpected in this context. Please advice Thanks C:&#92;traces_test&amp;gt;&quot;c:&#92;Program Files&#92;Wiresha...'''
date = "2013-10-19T10:22:00Z"
lastmod = "2013-10-20T16:31:00Z"
weight = 26215
keywords = [ "tshark" ]
aliases = [ "/questions/26215" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [tshark smb,srt filter error](/questions/26215/tshark-smbsrt-filter-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26215-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26215-score" class="post-score" title="current number of votes">0</div><span id="post-26215-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>i am trying to get some smb statistics for certain file using tshark , i think i am using the correct syntax but still getting errors as follows below even if i remove the \ i get invalid - "New" was unexpected in this context. Please advice Thanks</p><pre><code>C:\traces_test&gt;&quot;c:\Program Files\Wireshark\tshark.exe&quot; -n -r tracesmb_fileop1.pcap -q -z &quot;smb,srt,smb.file==\\New Video 12_20196.xml&quot;</code></pre><p>tshark: Couldn't register smb,srt tap: Filter "smb.file==\New Video 12_20196.xml" is invalid - "\" was unexpected in this context.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Oct '13, 10:22</strong></p><img src="https://secure.gravatar.com/avatar/491b248bc5431fa4cfed4498e4633f51?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tbaror&#39;s gravatar image" /><p><span>tbaror</span><br />
<span class="score" title="10 reputation points">10</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tbaror has no accepted answers">0%</span></p></div></div><div id="comments-container-26215" class="comments-container"><span id="26218"></span><div id="comment-26218" class="comment"><div id="post-26218-score" class="comment-score"></div><div class="comment-text"><p>Normally quoting or escaping does the trick, but I can't get this to work either. Note that you will probably have to escape the backslashes when we do work out what extra is required.</p><p>To work out what to put in filter try it out in the GUI, generally selecting the field, right clicking and choosing "Apply As Filter" then "Selected". You'll see for a file with the name <code>\server\path</code> the filter in the filter box becomes <code>\\server\\path</code></p></div><div id="comment-26218-info" class="comment-info"><span class="comment-age">(19 Oct '13, 12:47)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="26221"></span><div id="comment-26221" class="comment"><div id="post-26221-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the comment, but i do need tshark for scripting :-( i will give it further try with extra escaping. thanks</p></div><div id="comment-26221-info" class="comment-info"><span class="comment-age">(19 Oct '13, 21:41)</span> <span class="comment-user userinfo">tbaror</span></div></div></div><div id="comment-tools-26215" class="comment-tools"></div><div class="clear"></div><div id="comment-26215-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26226"></span>

<div id="answer-container-26226" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26226-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26226-score" class="post-score" title="current number of votes">2</div><span id="post-26226-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tbaror has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This was answered on the dev mailing list <a href="http://www.wireshark.org/lists/wireshark-users/201310/msg00022.html">here</a> by Evan. The answer is to escape the quotes required around the string to match and escape the backslash in the string, e.g.</p><p><code>tshark.exe" -n -r tracesmb_fileop1.pcap -q -z "smb,srt,smb.file==\"\\New Video 12_20196.xml\""</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '13, 16:31</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-26226" class="comments-container"></div><div id="comment-tools-26226" class="comment-tools"></div><div class="clear"></div><div id="comment-26226-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

