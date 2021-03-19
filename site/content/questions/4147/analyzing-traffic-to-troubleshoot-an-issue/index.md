+++
type = "question"
title = "Analyzing Traffic to troubleshoot an issue"
description = '''I am helping out a school NetAdmin with an unusual problem they are having I believe may be network related. It appears that 7-8 desktops have issues opening up files on a share located on the school&#x27;s server during the mornings. The issue only affects these desktops - no one else on the subnet expe...'''
date = "2011-05-19T13:05:00Z"
lastmod = "2011-05-24T06:21:00Z"
weight = 4147
keywords = [ "files", "slow", "share", "network", "hangs" ]
aliases = [ "/questions/4147" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Analyzing Traffic to troubleshoot an issue](/questions/4147/analyzing-traffic-to-troubleshoot-an-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4147-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am helping out a school NetAdmin with an unusual problem they are having I believe may be network related. It appears that 7-8 desktops have issues opening up files on a share located on the school's server during the mornings. The issue only affects these desktops - no one else on the subnet experiences those issues at that time, and the issue clears up later in the day.</p><p>When someone tries to open up a file, it appears that Windows just hangs for an inordinate amount of time. Sometimes, the file will eventually open, but other times the desktop needs to be rebooted to unfreeze it. The switch to which these desktops connect as well as the fiber media convertor that connects the switch to the main switch that the server and the other desktops on the subnet connect to have both been replaced as part of the troubleshooting.</p><p>I am hoping we can garner some clues as to what is going on by using Wireshark on one of the problem desktops and the server, but I am unfamiliar with interpreting the output. Would it be possible to upload our two capture files here for someone more savvy to take a look at and point us in the right direction?</p></div><div id="question-tags" class="tags-container tags">files slow share network hangs</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 May '11, 13:05</strong></p><img src="https://secure.gravatar.com/avatar/01f57458360ddbfbb945cbd6ad3a0ed2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JBergJr&#39;s gravatar image" /><p>JBergJr<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JBergJr has no accepted answers">0%</span></p></div></div><div id="comments-container-4147" class="comments-container"></div><div id="comment-tools-4147" class="comment-tools"></div><div class="clear"></div><div id="comment-4147-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4158"></span>

<div id="answer-container-4158" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4158-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is no way to upload a file to this site directly, at least not that I'm aware of, but the answers to these other questions might help provide you with some alternative methods you could use:</p><ul><li><a href="http://ask.wireshark.org/questions/1221/standard-way-people-should-attach-capture-files-to-questions-in-this-forum">http://ask.wireshark.org/questions/1221/standard-way-people-should-attach-capture-files-to-questions-in-this-forum</a></li><li><a href="http://ask.wireshark.org/questions/281/attach-a-capture-file">http://ask.wireshark.org/questions/281/attach-a-capture-file</a></li></ul><p>If you find a way to post your file somewhere, then it's possible someone might take a look at it and give you some feedback about it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '11, 19:06</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-4158" class="comments-container"><span id="5463"></span><div id="comment-5463" class="comment"><div id="post-5463-score" class="comment-score"></div><div class="comment-text"><p>Not exactly the same context. I do need help in interpreting traces. A trojan (I think) in my machine is sending my IP somewhere. I reset and eventually I get an email (I know is spoof/phish) and don't know how to interpret. The outgoing message may have my IP encrypted, etc. and I don't even know where to begin.</p><p>I have read [b]cmaynard[/b]'s message and I do have a place to put the traces, just still have a question regarding the extension ".pcap" because it is not there [this is after reading that Wireshark keeps up to my close to 8GB memory and then crashes, I have reported this and found a workaround to limit files to +/- 100MB. I do suspect I captured the culprit because after changing my IP address, the following emails do have the new one.</p></div><div id="comment-5463-info" class="comment-info"><span class="comment-age">(03 Aug '11, 17:36)</span> LaoziSailor</div></div></div><div id="comment-tools-4158" class="comment-tools"></div><div class="clear"></div><div id="comment-4158-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4192"></span>

<div id="answer-container-4192" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4192-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks for the information. I will take a look at those files and test the program some more. Naturally, the problem has gone away for a few days, but it has done this in the past, so we are waiting until the next flare up.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 May '11, 06:21</strong></p><img src="https://secure.gravatar.com/avatar/01f57458360ddbfbb945cbd6ad3a0ed2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JBergJr&#39;s gravatar image" /><p>JBergJr<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JBergJr has no accepted answers">0%</span></p></div></div><div id="comments-container-4192" class="comments-container"><span id="4193"></span><div id="comment-4193" class="comment"><div id="post-4193-score" class="comment-score"></div><div class="comment-text"><p>Just make sure there is no confidential information included. If the files you are transfering contains sensitive data you should be aware that it can be reconstructed from the capture without much trouble (if not encrypted). In that case you should use test files that are noncritical.</p></div><div id="comment-4193-info" class="comment-info"><span class="comment-age">(24 May '11, 06:34)</span> Jasper ♦♦</div></div></div><div id="comment-tools-4192" class="comment-tools"></div><div class="clear"></div><div id="comment-4192-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

