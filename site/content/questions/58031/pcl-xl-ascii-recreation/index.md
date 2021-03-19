+++
type = "question"
title = "PCL XL ASCII Recreation"
description = '''Hello, I am using wireshark to capture print packets as I am trying to troubleshoot a clients copier. I am relatively new to wireshark and would like to know if there is a way to recreate a print from the capture. The client is having half printed documents and I would like to capture and reprint th...'''
date = "2016-12-12T13:50:00Z"
lastmod = "2016-12-13T14:08:00Z"
weight = 58031
keywords = [ "print", "ascii", "wireshark" ]
aliases = [ "/questions/58031" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [PCL XL ASCII Recreation](/questions/58031/pcl-xl-ascii-recreation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58031-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am using wireshark to capture print packets as I am trying to troubleshoot a clients copier. I am relatively new to wireshark and would like to know if there is a way to recreate a print from the capture. The client is having half printed documents and I would like to capture and reprint the documents to see if the problem resides on the network or the printer. Thanks in advance for anyone who has an answer!</p></div><div id="question-tags" class="tags-container tags">print ascii wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Dec '16, 13:50</strong></p><img src="https://secure.gravatar.com/avatar/7a03ae15ee8ba753ee63ed99a94fcc89?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Corb&#39;s gravatar image" /><p>Corb<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Corb has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Dec '16, 14:02</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-58031" class="comments-container"></div><div id="comment-tools-58031" class="comment-tools"></div><div class="clear"></div><div id="comment-58031-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="58032"></span>

<div id="answer-container-58032" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58032-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately, we don't have a dissector for PCL XL, so, while Wireshark will dissect the print packets up to the payload, it won't dissect the payload itself - and even if it did, that wouldn't show you what the actual printed page would look like, any more than a dump of PostScript sent to a printer would directly show you what the actual printed page would look like.</p><p>Depending on the print protocol being used, Wireshark <em>might</em> let you save the raw PCL XL to a file. If you were to do that, you <em>might</em> be able to find a program that would convert it to a PDF; <a href="http://pclhelp.com/tag/pcl-xl/">this PCL support site</a> might offer some help there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Dec '16, 14:02</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-58032" class="comments-container"></div><div id="comment-tools-58032" class="comment-tools"></div><div class="clear"></div><div id="comment-58032-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="58054"></span>

<div id="answer-container-58054" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58054-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, I came across this RICOH's document: <a href="http://rfg-esource.ricoh-usa.com/oracle/groups/public/documents/communication/rfg042515.pdf">Extracting a Print Capture From a Network Packet Capture Using Wireshark White Paper</a></p><p>If the link does not work Google for the document name..</p><p>I have used this document few days ago to export the PCL print data to a file. Later I was able to print the file on printer using lpr DOS command from my Windows 7.<br />
hope it helps</p><p>Bob</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Dec '16, 14:08</strong></p><img src="https://secure.gravatar.com/avatar/4fd61c766c3399bb02b9b6813dff660b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cz50344&#39;s gravatar image" /><p>cz50344<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cz50344 has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Dec '16, 15:14</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-58054" class="comments-container"></div><div id="comment-tools-58054" class="comment-tools"></div><div class="clear"></div><div id="comment-58054-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

