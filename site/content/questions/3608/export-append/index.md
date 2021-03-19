+++
type = "question"
title = "export append"
description = '''I have to run a scan for an 8 hour duration. Is there a method in which I can setup the multiple file option to write/export them to a folder in sequential order without interuption to the scan? That is a continuous run and export without interupting the scan and killing the laptop?'''
date = "2011-04-19T06:43:00Z"
lastmod = "2011-04-19T07:58:00Z"
weight = 3608
keywords = [ "100mg" ]
aliases = [ "/questions/3608" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [export append](/questions/3608/export-append)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3608-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have to run a scan for an 8 hour duration. Is there a method in which I can setup the multiple file option to write/export them to a folder in sequential order without interuption to the scan? That is a continuous run and export without interupting the scan and killing the laptop?</p></div><div id="question-tags" class="tags-container tags">100mg</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '11, 06:43</strong></p><img src="https://secure.gravatar.com/avatar/bad4b5911b6ae1890e7127955c596939?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spongerob&#39;s gravatar image" /><p>spongerob<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="spongerob has no accepted answers">0%</span></p></div></div><div id="comments-container-3608" class="comments-container"></div><div id="comment-tools-3608" class="comment-tools"></div><div class="clear"></div><div id="comment-3608-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3610"></span>

<div id="answer-container-3610" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3610-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, that's what the multiple files option does, it captures for a long period of time, breaking up the captured data in smaller pieces. The way to do it is:</p><ul><li>Choose a filename, this will be the base filename wireshark will use for the individual pieces</li><li>select "Use Multiple Files"</li><li>select either "Next file every X MB" or "Next file every X minutes"</li><li>My advice is to use the MB option and choose a filesize of 32MB or so</li><li>If you are worried about disk space, you can limit the amount of files by either creating a "ringbuffer" (oldest files will be deleted when more files need to be created) or "Stop after" to stop the capture once the configured amount of files are created</li><li>Make sure you have "Update list of packets in real time" <strong>disabled</strong></li></ul><p>If you want to be absolutely sure your capture session will not run out of memory, you better use the command line command <a href="http://www.wireshark.org/docs/man-pages/dumpcap.html">dumpcap</a> (which is used by Wireshark under the hood anyways). I had dumpcap running for months with a ring buffer trying to capture a very rarely occurring problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '11, 07:58</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-3610" class="comments-container"><span id="3648"></span><div id="comment-3648" class="comment"><div id="post-3648-score" class="comment-score"></div><div class="comment-text"><p>Thanks much - do you know of any online courses/classes for wireshark?</p><p>I'd like to get the cert!</p></div><div id="comment-3648-info" class="comment-info"><span class="comment-age">(20 Apr '11, 11:41)</span> spongerob</div></div><span id="3674"></span><div id="comment-3674" class="comment"><div id="post-3674-score" class="comment-score"></div><div class="comment-text"><p>Have a look at <a href="http://www.wiresharkuniversity.com">www.wiresharkuniversity.com</a></p></div><div id="comment-3674-info" class="comment-info"><span class="comment-age">(21 Apr '11, 00:29)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-3610" class="comment-tools"></div><div class="clear"></div><div id="comment-3610-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

