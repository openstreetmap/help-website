+++
type = "question"
title = "Dumpcap issue while splitting files by duration"
description = '''Hi there, I&#x27;ve an issue with dumpcap command. First of all i&#x27;m working in a Linux environment (on Raspbian, on a Raspberry Pi, exactly). I&#x27;ve a PHP frontend, which ask the user to type parameters, and then when he launch the capture (by clicking on a button), the following php code is executed : she...'''
date = "2014-04-24T06:03:00Z"
lastmod = "2014-04-29T01:02:00Z"
weight = 32145
keywords = [ "duration", "tshark", "dumpcap" ]
aliases = [ "/questions/32145" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dumpcap issue while splitting files by duration](/questions/32145/dumpcap-issue-while-splitting-files-by-duration)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32145-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32145-score" class="post-score" title="current number of votes">0</div><span id="post-32145-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there, I've an issue with dumpcap command. First of all i'm working in a Linux environment (on Raspbian, on a Raspberry Pi, exactly). I've a PHP frontend, which ask the user to type parameters, and then when he launch the capture (by clicking on a button), the following php code is executed :</p><p>shell_exec("sudo nohup dumpcap -P -f \"".$fport."\" -b duration:".$ftime." -i ".$finterface." -w /mnt/hdd/files_to_proceed/REC.pcap &gt; /dev/null &amp;");</p><p>My Raspberry Pi is well connected to the network, the capture correctly start and all the packets are captured and stored in correct files. That's a good point. My problem is, if i chose 5min duration for example, dumpcap will correctly split files every 5 minutes, until he magically stops splitting and store all the packets in the same .pcap file during more than 5 minutes. And, about a random time, he suddenly resplit files every 5 minutes correctly. After many tests, i figured out that :<br />
- This issue is independent of the amount of time chosen<br />
- It appears at and for a random time<br />
- Sometimes it doesn't show up and the whole capture is a success<br />
Finally, the tests were fulfill during whole nights (so for many hours), simply because this feature is supposed to work 24 hours a day for several months.</p><p>I don't know if you guys already had that issue, if it's due to dumpcap lib or not, but i really need help on this !</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-duration" rel="tag" title="see questions tagged &#39;duration&#39;">duration</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Apr '14, 06:03</strong></p><img src="https://secure.gravatar.com/avatar/5306239c7fb32a4073c264763e4911c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lecclem&#39;s gravatar image" /><p><span>Lecclem</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lecclem has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-32145" class="comments-container"></div><div id="comment-tools-32145" class="comment-tools"></div><div class="clear"></div><div id="comment-32145-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32146"></span>

<div id="answer-container-32146" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32146-score" class="post-score" title="current number of votes">1</div><span id="post-32146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds like a bug to me, and a tricky one since it can not always be reproduced.</p><p>Most people I know do not use the "-b duration" switch since can get you into trouble when the line has bursty traffic patterns. Which is why usually "-b filesize" is used instead, to keep the capture files consistent in size (e.g. to be able to load them). So if you need time based splitting it is quite possible that this problem did not occur to anyone else, or they just used the filesize based splitting as a workaround and didn't say anything :-)</p><p>You might want to head over to the <a href="http://bugs.wireshark.org">Bugtracker</a> to open a report.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Apr '14, 06:26</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span> </br></br></p></div></div><div id="comments-container-32146" class="comments-container"><span id="32155"></span><div id="comment-32155" class="comment"><div id="post-32155-score" class="comment-score"></div><div class="comment-text"><p>Actually I think there's already a similar <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5547">bug report</a> for this. It's quite old so a report that it's still a problem would be useful.</p></div><div id="comment-32155-info" class="comment-info"><span class="comment-age">(24 Apr '14, 11:55)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="32284"></span><div id="comment-32284" class="comment"><div id="post-32284-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your answers ! I am currently working on my own way to capture packets (including time filter) through libpcap library in C, i see no other way (besides use a filesize filter, which will be my ultimate last solution)... But i'm glad that bug was reported and i'll try to "up" that report ASAP.</p></div><div id="comment-32284-info" class="comment-info"><span class="comment-age">(29 Apr '14, 01:02)</span> <span class="comment-user userinfo">Lecclem</span></div></div></div><div id="comment-tools-32146" class="comment-tools"></div><div class="clear"></div><div id="comment-32146-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

