+++
type = "question"
title = "File export as &quot;Plain Text File&quot; feature missing?"
description = '''I just installed Vewrsion 1.8.4 64 bit for Windows 7. It seems to be able to capture from the machine&#x27;s ethernet port, and save/load pcap files, but I can&#x27;t find the File Export to plain text file option anywhere. Has this feature been removed?'''
date = "2013-01-18T17:17:00Z"
lastmod = "2013-01-18T17:29:00Z"
weight = 17784
keywords = [ "export", "feature", "feature-request" ]
aliases = [ "/questions/17784" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [File export as "Plain Text File" feature missing?](/questions/17784/file-export-as-plain-text-file-feature-missing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17784-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I just installed Vewrsion 1.8.4 64 bit for Windows 7. It seems to be able to capture from the machine's ethernet port, and save/load pcap files, but I can't find the File Export to plain text file option anywhere.</p><p>Has this feature been removed?</p></div><div id="question-tags" class="tags-container tags">export feature feature-request</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jan '13, 17:17</strong></p><img src="https://secure.gravatar.com/avatar/4ab25fcdc5efc06ad32fb07eaa378c82?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gordwait&#39;s gravatar image" /><p>gordwait<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gordwait has no accepted answers">0%</span></p></div></div><div id="comments-container-17784" class="comments-container"></div><div id="comment-tools-17784" class="comment-tools"></div><div class="clear"></div><div id="comment-17784-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17785"></span>

<div id="answer-container-17785" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17785-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Has this feature been removed?</p></blockquote><p>No. It's been renamed, in the hopes that people will not mistakenly think that, having done an export as plain text, the resulting files can be read by Wireshark. What's being exported is the result of dissecting the packet, <em>NOT</em> raw packet data that Wireshark, or other packet analyzers, can directly read.</p><p>It's now File -&gt; Export Packet Dissections -&gt; as "Plain Text" file...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jan '13, 17:29</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-17785" class="comments-container"><span id="17817"></span><div id="comment-17817" class="comment"><div id="post-17817-score" class="comment-score"></div><div class="comment-text"><p>Ah, very effective :) I would have been one of "those people". I am looking for a simple ascii format to exchange ethernet frames between Wireshark and a VHDL simulation run. For some reason the simple hex import feature isn't working for me, but that need's it's own question here on the forum (coming soon)..</p></div><div id="comment-17817-info" class="comment-info"><span class="comment-age">(21 Jan '13, 10:38)</span> gordwait</div></div><span id="17818"></span><div id="comment-17818" class="comment"><div id="post-17818-score" class="comment-score"></div><div class="comment-text"><p>Note, the "built in" documentation for Wireshark still documents the old File Export process, (as do many stale web links) adding to the confusion..</p></div><div id="comment-17818-info" class="comment-info"><span class="comment-age">(21 Jan '13, 10:47)</span> gordwait</div></div></div><div id="comment-tools-17785" class="comment-tools"></div><div class="clear"></div><div id="comment-17785-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

