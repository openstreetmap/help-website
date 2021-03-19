+++
type = "question"
title = "ver 2.0.5 host file location so that I can save manually"
description = '''I would like to manually save the host file info generated via version 2.0.5 so that I can reinstall when a new version of Wireshark becomes available. I used the Help and found the entry that indicated where the host file was supposed to be, however it was not there. When I put an earlier version i...'''
date = "2016-09-05T04:35:00Z"
lastmod = "2016-09-05T05:24:00Z"
weight = 55331
keywords = [ "hosts" ]
aliases = [ "/questions/55331" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ver 2.0.5 host file location so that I can save manually](/questions/55331/ver-205-host-file-location-so-that-i-can-save-manually)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55331-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to manually save the host file info generated via version 2.0.5 so that I can reinstall when a new version of Wireshark becomes available. I used the Help and found the entry that indicated where the host file was supposed to be, however it was not there. When I put an earlier version it was not used.</p><p>BobMiers</p></div><div id="question-tags" class="tags-container tags">hosts</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Sep '16, 04:35</strong></p><img src="https://secure.gravatar.com/avatar/339fb7653a7fe42fd859f58cbb9d431e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bobmiers&#39;s gravatar image" /><p>bobmiers<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bobmiers has no accepted answers">0%</span></p></div></div><div id="comments-container-55331" class="comments-container"></div><div id="comment-tools-55331" class="comment-tools"></div><div class="clear"></div><div id="comment-55331-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55332"></span>

<div id="answer-container-55332" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55332-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark never writes to the hosts file, only reads from it. In my tests, using a build from master, the hosts file is successfully read from both the user and global locations.</p><p>What OS are you using and what are the exact paths for the hosts file are you using?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Sep '16, 05:24</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-55332" class="comments-container"><span id="55334"></span><div id="comment-55334" class="comment"><div id="post-55334-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the quick response. I am using Win8.1 as the OS. What I have done in the past was put a hosts file in the USER/AppDat/roaming/wireshark folder. When I installed ver 2.0.5 it didn't seem to read from the file, even after a reboot.</p><p>I then noticed under the View&gt;Name Resolution tab there was a selection that permitted me to name an IP address. I renamed a bunch of my local fixed addresses using that function. Even after rebooting and starting a new scan, the Name Resolutions that I had entered seemed to be retained. After, without any success, searching for a modified file that might contain the hosts type of info I posted the question.</p><p>After reading your message, I edited the USER/AppDat/roaming/wireshark/hosts file to change one of the entries to a ASDFGHJKUIO name and saved the file, and restarted WireShark. This time it did read the file and I saw the ASDFGHJKUIO name appearing.</p><p>So it looks like I wasted your time.<br />
</p><p>Thanks a bunch. BobMiers<br />
</p></div><div id="comment-55334-info" class="comment-info"><span class="comment-age">(05 Sep '16, 10:15)</span> bobmiers</div></div><span id="55335"></span><div id="comment-55335" class="comment"><div id="post-55335-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-55335-info" class="comment-info"><span class="comment-age">(05 Sep '16, 10:57)</span> Jaap ♦</div></div><span id="55336"></span><div id="comment-55336" class="comment"><div id="post-55336-score" class="comment-score"></div><div class="comment-text"><p>As you may know there are multiple options to setup name resolution. The ones you probably know are DNS information and the hosts file. But now manually entered name resolution is also saved, in the pcap-ng file, which has special extensions for that. So the changed file you were looking for is actually the capture file.</p></div><div id="comment-55336-info" class="comment-info"><span class="comment-age">(05 Sep '16, 10:59)</span> Jaap ♦</div></div></div><div id="comment-tools-55332" class="comment-tools"></div><div class="clear"></div><div id="comment-55332-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

