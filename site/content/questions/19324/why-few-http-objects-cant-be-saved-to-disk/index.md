+++
type = "question"
title = "why few HTTP objects can&#x27;t be saved to disk?"
description = '''I tried to capture objects from adobe.com website. Triggered wireshark and browsed for a minute, saved the capture. When I tried to export all the objects to the disk I got an error message saying &quot;some files could not be saved&quot; Got couple of questions here:  Reason for the error message. What kind ...'''
date = "2013-03-08T17:27:00Z"
lastmod = "2013-03-11T10:07:00Z"
weight = 19324
keywords = [ "objects" ]
aliases = [ "/questions/19324" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [why few HTTP objects can't be saved to disk?](/questions/19324/why-few-http-objects-cant-be-saved-to-disk)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19324-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I tried to capture objects from adobe.com website. Triggered wireshark and browsed for a minute, saved the capture. When I tried to export all the objects to the disk I got an error message saying "some files could not be saved"</p><p>Got couple of questions here:</p><ol><li>Reason for the error message.</li><li>What kind of objects Wireshark can't save to disk?</li><li>Why we are not able to save objects "on the fly" to the disk (at this juncture I need to save the pcapng and then retrieve the objects by opening the saved trace) Any particular reason for this behavior?</li></ol></div><div id="question-tags" class="tags-container tags">objects</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Mar '13, 17:27</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p>krishnayeddula<br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Mar '13, 10:47</p></div></div><div id="comments-container-19324" class="comments-container"></div><div id="comment-tools-19324" class="comment-tools"></div><div class="clear"></div><div id="comment-19324-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19355"></span>

<div id="answer-container-19355" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19355-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Reason for the error message.</p></blockquote><p>Usually (from what I have seen in the code) problems in writing the data to disk (object size, length of filename, etc.) Wirshark will/should show an error message in that case. However, the several error messages are not <strong>that</strong> clear.</p><blockquote><p>What kind of objects Wireshark can't save to disk?</p></blockquote><p>Every kind that shows up in the list of objects (save/export dialog). I guess it's a size problem.</p><blockquote><p>Why we are not able to save objects "on the fly" to the disk</p></blockquote><p>Because that is not implemented. Furthermore Wireshark needs the whole communication to rebuild the objects (files, images, etc.).</p><p>To solve your problem: Please check the available disk space before you save that objects. If there is enough disk space available and you still cannot save all objects, you might run into a Wireshark bug.</p><p>Please first post here:</p><ul><li>Your OS</li><li>Your OS version</li><li>Your Wireshark version (wireshark -v)</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '13, 10:07</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-19355" class="comments-container"><span id="19360"></span><div id="comment-19360" class="comment"><div id="post-19360-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply/</p><p>Here are the details of OS and Wireshark Version:</p><p>wireshark 1.8.4 (SVN Rev 46250 from /trunk-1.8) Running on 64-bit Windows 7 Service Pack 1, build 7601, with WinPcap version Built using Microsoft Visual C++ 10.0 build 40219</p><p>Now the disk space: Used space: 65.9 GB Free space: 129 GB</p></div><div id="comment-19360-info" class="comment-info"><span class="comment-age">(11 Mar '13, 11:45)</span> krishnayeddula</div></div></div><div id="comment-tools-19355" class="comment-tools"></div><div class="clear"></div><div id="comment-19355-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

