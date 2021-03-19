+++
type = "question"
title = "Automate wireshark capture"
description = '''Hi Experts, I am new to Wireshark. I want to capture all the network traffic on one of our Windows servers. I wrote the following command in terminal  c:&#92;Program Files&#92;Wireshark&amp;gt;tshark -i 1 -a duration:3600 -w c:&#92;WiresharkCapture&#92;test It works perfectly fine, except I have 2 questions:  I want to...'''
date = "2012-09-11T19:59:00Z"
lastmod = "2016-07-21T10:48:00Z"
weight = 14195
keywords = [ "capture", "automate", "wireshark" ]
aliases = [ "/questions/14195" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Automate wireshark capture](/questions/14195/automate-wireshark-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14195-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14195-score" class="post-score" title="current number of votes">1</div><span id="post-14195-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Experts,</p><p>I am new to Wireshark. I want to capture all the network traffic on one of our Windows servers. I wrote the following command in terminal</p><p>c:\Program Files\Wireshark&gt;tshark -i 1 -a duration:3600 -w c:\WiresharkCapture\test</p><p>It works perfectly fine, except I have 2 questions:</p><ol><li>I want to capture all the traffic between 6am-7am. Is there a way I can schedule the task to automatically execute this command between 6am-7am?</li><li>The file gets overwritten everytime I execute this command. Can I save the file in format of testDDMMYYYY, so that I can keep history?</li></ol><p>Thanks in advance..</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-automate" rel="tag" title="see questions tagged &#39;automate&#39;">automate</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Sep '12, 19:59</strong></p><img src="https://secure.gravatar.com/avatar/d1fe132380fe31fbf31bdc97d79e687d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ravi007&#39;s gravatar image" /><p><span>ravi007</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ravi007 has no accepted answers">0%</span></p></div></div><div id="comments-container-14195" class="comments-container"><span id="14196"></span><div id="comment-14196" class="comment"><div id="post-14196-score" class="comment-score"></div><div class="comment-text"><p>OK.. I figured out how to automate this process, but I still don't know, how to save files in DDMMYYYY format..</p><p>Can anyone please help?</p><p>Many Thanks...</p></div><div id="comment-14196-info" class="comment-info"><span class="comment-age">(11 Sep '12, 22:24)</span> <span class="comment-user userinfo">ravi007</span></div></div></div><div id="comment-tools-14195" class="comment-tools"></div><div class="clear"></div><div id="comment-14195-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="14197"></span>

<div id="answer-container-14197" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14197-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14197-score" class="post-score" title="current number of votes">5</div><span id="post-14197-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm assuming you're on Windows (based on the path C:\Program Files\Wireshark). This isn't really a Wireshark question, it's a Windows command line question. The following works for me on Windows Vista:</p><p>tshark -i 1 -a duration:3600 -w C:\WiresharkCapture\test%date:~7,2%%date:~4,2%%date%~10,4%.pcap</p><p>This command was executed on September 12, 2012 and the filename was "<em>test12092012.pcap</em>".</p><p>This syntax is dependent on your locale and exactly how the date is displayed on your system, so you might have to tinker with it a bit. If this doesn't work for you, Google on "windows date filename" and you'll get dozens of results showing various commands for including the date in a file name from the command prompt. On my computer, the output of the 'date' command is displayed as "Wed 09/12/2012".</p><p>You could also use Wireshark's ring buffer option, but stop after a single file with something like this:</p><p>tshark -i 1 -a duration:3600 -b duration:3600 -w C:\WiresharkCapture\test.pcap</p><p>A ring buffer normally writes multiple files, but by setting the autostop (-a) option duration to the same value as the ring buffer (-b) option duration, tshark will only write one file, which is what your command above does. (However, an hour can be a long time to capture on a busy network, so you might want to consider using a ring buffer option that writes multiple files over the one-hour period.)</p><p>This will include the date and time in the filename, but will not give you any control over how the name is formatted. I ended up with a file named <em>test_00001_20120912001856.pcap</em> when I executed the command at 00:18:56 on September 12th, 2012.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '12, 00:39</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-14197" class="comments-container"><span id="14223"></span><div id="comment-14223" class="comment"><div id="post-14223-score" class="comment-score"></div><div class="comment-text"><p>Hi Jim,</p><p>Thanks for the information.. That was really helpful.. I am using Windowns Server 2008 and the following command worked for me..</p><p>tshark -i 1 -a duration:3600 -w c:\WiresharkCapture\test%date:~4,2%%date:~7,2%%date:~10,4%.pcap</p><p>Its all good now..</p><p>Thanks again...</p></div><div id="comment-14223-info" class="comment-info"><span class="comment-age">(12 Sep '12, 17:53)</span> <span class="comment-user userinfo">ravi007</span></div></div><span id="54229"></span><div id="comment-54229" class="comment"><div id="post-54229-score" class="comment-score"></div><div class="comment-text"><p>Ravi007,</p><p>You said you were able to figure out how to automate this process. Can you provide that solution?</p><p>Thanks</p></div><div id="comment-54229-info" class="comment-info"><span class="comment-age">(21 Jul '16, 10:48)</span> <span class="comment-user userinfo">mand009</span></div></div></div><div id="comment-tools-14197" class="comment-tools"></div><div class="clear"></div><div id="comment-14197-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21955"></span>

<div id="answer-container-21955" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21955-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21955-score" class="post-score" title="current number of votes">0</div><span id="post-21955-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>hwo to capture all files captured? I do get only the last file which is being captured for exporting. I dont get all the files captured to export.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '13, 23:17</strong></p><img src="https://secure.gravatar.com/avatar/e70c48e299a7f1ce009a482cb758f218?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nikhil&#39;s gravatar image" /><p><span>nikhil</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nikhil has no accepted answers">0%</span></p></div></div><div id="comments-container-21955" class="comments-container"></div><div id="comment-tools-21955" class="comment-tools"></div><div class="clear"></div><div id="comment-21955-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

