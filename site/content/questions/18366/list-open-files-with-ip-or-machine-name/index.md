+++
type = "question"
title = "list open files with ip or machine name"
description = '''I would like to know if there is a way to list the open files in the network - if so can I also list the machine name with it'''
date = "2013-02-06T08:23:00Z"
lastmod = "2013-02-07T16:32:00Z"
weight = 18366
keywords = [ "files", "machine", "open", "name", "user" ]
aliases = [ "/questions/18366" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [list open files with ip or machine name](/questions/18366/list-open-files-with-ip-or-machine-name)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18366-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to know if there is a way to list the open files in the network - if so can I also list the machine name with it</p></div><div id="question-tags" class="tags-container tags">files machine open name user</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Feb '13, 08:23</strong></p><img src="https://secure.gravatar.com/avatar/ff9bf840ce8dd240565ba1631ab91696?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gmail&#39;s gravatar image" /><p>gmail<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gmail has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Feb '13, 09:10</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-18366" class="comments-container"><span id="18376"></span><div id="comment-18376" class="comment"><div id="post-18376-score" class="comment-score"></div><div class="comment-text"><p>Do you mean "list, on a client machine, what files it has open on various file servers" or "list, on a server machine, what client machines have what files open on it"? (Note that the machine on your desk could be a "server" if it's exporting NFS/SMB/AFP/etc. files.) In either case, Wireshark isn't the right tool, as grahamb notes.</p></div><div id="comment-18376-info" class="comment-info"><span class="comment-age">(06 Feb '13, 13:57)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-18366" class="comment-tools"></div><div class="clear"></div><div id="comment-18366-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18368"></span>

<div id="answer-container-18368" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18368-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Not with Wireshark. For certain network file system protocols Wireshark can display the commands to open files if they are present at the time and location of capture, but that probably isn't reflective of the current state of file use though-out the "network", particularly if the capturing machine is on a switched network and not on the actual network file servers.</p><p>I think you'll need to look elsewhere for a solution to your problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Feb '13, 09:16</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-18368" class="comments-container"><span id="18383"></span><div id="comment-18383" class="comment"><div id="post-18383-score" class="comment-score"></div><div class="comment-text"><p>thanks - what tool is out there that you guys know of that can check who has a particular file open in a share network drive. By who I mean the ip or machine name</p></div><div id="comment-18383-info" class="comment-info"><span class="comment-age">(06 Feb '13, 19:10)</span> gmail</div></div><span id="18386"></span><div id="comment-18386" class="comment"><div id="post-18386-score" class="comment-score">1</div><div class="comment-text"><p>It sounds, from your comment, as if the answer to my question above is "list, on a server machine, what client machines have what files open on it". If so, then there might be a program you can run on the server to report what clients have files open on it. What operating system is the server running, and what file protocol or protocols are being used (NFS, SMB, AFP, Netware, something else)?</p></div><div id="comment-18386-info" class="comment-info"><span class="comment-age">(06 Feb '13, 21:35)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-18368" class="comment-tools"></div><div class="clear"></div><div id="comment-18368-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18427"></span>

<div id="answer-container-18427" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18427-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please check my answer to the following question:</p><blockquote><p><code>http://ask.wireshark.org/questions/12113/save-the-smb-object-list</code><br />
</p></blockquote><p>It will not show any 'open files', as there is no way (I know of) to do that in Wireshark. It will however list the files that have been accessed on an SMB share. Beware that this may not work in every environment!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Feb '13, 16:32</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-18427" class="comments-container"></div><div id="comment-tools-18427" class="comment-tools"></div><div class="clear"></div><div id="comment-18427-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

