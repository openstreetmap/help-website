+++
type = "question"
title = "How do I merge about 50 pcap files into one pcap?"
description = '''I used the Mergcap command and it does not seem to take *.pcap as the input for multiple files. Is that a Mergcap limitation?'''
date = "2010-11-25T12:24:00Z"
lastmod = "2011-11-06T21:42:00Z"
weight = 1124
keywords = [ "mergcap" ]
aliases = [ "/questions/1124" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [How do I merge about 50 pcap files into one pcap?](/questions/1124/how-do-i-merge-about-50-pcap-files-into-one-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1124-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I used the Mergcap command and it does not seem to take *.pcap as the input for multiple files. Is that a Mergcap limitation?</p></div><div id="question-tags" class="tags-container tags">mergcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '10, 12:24</strong></p><img src="https://secure.gravatar.com/avatar/a47fc273546fcb5e2ce0cc7c3877369c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jambomj&#39;s gravatar image" /><p>jambomj<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jambomj has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Nov '10, 16:49</p></div></div><div id="comments-container-1124" class="comments-container"></div><div id="comment-tools-1124" class="comment-tools"></div><div class="clear"></div><div id="comment-1124-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="1125"></span>

<div id="answer-container-1125" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1125-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Does this thread help you? <a href="http://seclists.org/wireshark/2010/Feb/414">merging many files using mergecap</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '10, 14:22</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-1125" class="comments-container"></div><div id="comment-tools-1125" class="comment-tools"></div><div class="clear"></div><div id="comment-1125-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1127"></span>

<div id="answer-container-1127" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1127-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>After I posted my question I found a post which uses a batch as follows:</p><p>In the folder were all your pcap files are create a batch file called combine.bat run the batch from the command line so you know if it is working or not.</p><p>The batch file:</p><p>combine.bat:</p><p>setlocal enabledelayedexpansion</p><p>set myfiles=</p><p>for %%f in (*.pcap) do set myfiles=!myfiles! %%f</p><p>Cmd /V:on /c "c:Program FilesWiresharkmergecap.exe" -w temp.pcap %myfiles%</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '10, 14:45</strong></p><img src="https://secure.gravatar.com/avatar/a47fc273546fcb5e2ce0cc7c3877369c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jambomj&#39;s gravatar image" /><p>jambomj<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jambomj has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Nov '10, 14:47</p></div></div><div id="comments-container-1127" class="comments-container"><span id="2571"></span><div id="comment-2571" class="comment"><div id="post-2571-score" class="comment-score"></div><div class="comment-text"><p>That may not work in all cases if the number of files is very large. See bug 1118: https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=1118</p></div><div id="comment-2571-info" class="comment-info"><span class="comment-age">(25 Feb '11, 19:34)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-1127" class="comment-tools"></div><div class="clear"></div><div id="comment-1127-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1126"></span>

<div id="answer-container-1126" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1126-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think mergecap does not work with wildcards like *.pcap. You'll have to supply all filenames to it one by one, like this: "mergecap -w out.pcap infile1.pcap infile2.pcap infile3.pcap..." At least that's what I do when I have to merge multiple files, and I usually also use -a for concatenation.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '10, 14:30</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-1126" class="comments-container"></div><div id="comment-tools-1126" class="comment-tools"></div><div class="clear"></div><div id="comment-1126-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7258"></span>

<div id="answer-container-7258" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7258-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Pcapjoiner can do that for you...googe it</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Nov '11, 21:42</strong></p><img src="https://secure.gravatar.com/avatar/2fc18d78aabb7f5860b0e87c8a015ae6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ron33&#39;s gravatar image" /><p>Ron33<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ron33 has no accepted answers">0%</span></p></div></div><div id="comments-container-7258" class="comments-container"></div><div id="comment-tools-7258" class="comment-tools"></div><div class="clear"></div><div id="comment-7258-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

