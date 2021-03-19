+++
type = "question"
title = "capture ring buffer problem"
description = '''Hi , i am using dumpcap to caputre but the way i have setup my script a new file should be made everytime it reaches maximum filesize and its not doing it . can you please help  i am using the following command ...  /usr/bin/dumpcap -i eth0 -g -s 65536 -w /data/int0/int0 -b files:10000 -b filesize:2...'''
date = "2012-08-22T11:13:00Z"
lastmod = "2012-08-24T05:00:00Z"
weight = 13822
keywords = [ "capture", "dumpcap", "ringbuffer", "wireshark" ]
aliases = [ "/questions/13822" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [capture ring buffer problem](/questions/13822/capture-ring-buffer-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13822-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi , i am using dumpcap to caputre but the way i have setup my script a new file should be made everytime it reaches maximum filesize and its not doing it . can you please help i am using the following command ...</p><p>/usr/bin/dumpcap -i eth0 -g -s 65536 -w /data/int0/int0 -b files:10000 -b filesize:24000 -b duration:600 -q &amp;</p><p>capture ring buffer option not working<br />
</p></div><div id="question-tags" class="tags-container tags">capture dumpcap ringbuffer wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Aug '12, 11:13</strong></p><img src="https://secure.gravatar.com/avatar/9b296b0c1a89a6d15e65215e5e6c69b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld0722&#39;s gravatar image" /><p>helloworld0722<br />
<span class="score" title="10 reputation points">10</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld0722 has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Aug '12, 19:37</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-13822" class="comments-container"><span id="13861"></span><div id="comment-13861" class="comment"><div id="post-13861-score" class="comment-score"></div><div class="comment-text"><p>what is your wireshark version?</p></div><div id="comment-13861-info" class="comment-info"><span class="comment-age">(24 Aug '12, 02:31)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-13822" class="comment-tools"></div><div class="clear"></div><div id="comment-13822-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13871"></span>

<div id="answer-container-13871" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13871-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>For limiting your capture to 2.4 GB the number of KB= 2516582.4, But dumpcap takes only decimal. Below is the command</p><p><strong>"dumpcap -i eth0 -a filesize:2516582 -w output.pcap"</strong></p><p>For example if i want to capture 10 KB from eth0 interface i will give it as</p><p><strong>"dumpcap -i eth0 -a filesize:10 -w test.cap"</strong></p><p>If i check the size of the size its has 77 bytes more.</p><p>[[email protected] harsha]# ll total 12 -rw-------. 1 root root <strong>10317</strong> Aug 24 17:14 test.cap</p><p>So same will be the case with your 2.4 GB file, ie.. the bytes will be rounded off by the packet length (packet will not be chopped).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '12, 05:00</strong></p><img src="https://secure.gravatar.com/avatar/0cf7e05b14ad6662ecde4c327bb2c39f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harsha&#39;s gravatar image" /><p>Harsha<br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harsha has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Aug '12, 05:03</p></div></div><div id="comments-container-13871" class="comments-container"><span id="13872"></span><div id="comment-13872" class="comment"><div id="post-13872-score" class="comment-score"></div><div class="comment-text"><p>the above is answer is for (link:<a href="http://ask.wireshark.org/questions/13850/how-to-capture-using-dumpcap)">http://ask.wireshark.org/questions/13850/how-to-capture-using-dumpcap)</a></p></div><div id="comment-13872-info" class="comment-info"><span class="comment-age">(24 Aug '12, 05:04)</span> Harsha</div></div><span id="13873"></span><div id="comment-13873" class="comment"><div id="post-13873-score" class="comment-score"></div><div class="comment-text"><p>It would be more helpful to provide an answer for this question, not another very similar one. This just confuses other users.</p><p>The command line provided in this question clearly has <code>-b filesize:24000</code> so the poster knows how to limit the capture file to some value, even if that isn't the 2.4GB as per the other question.</p><p>What they haven't told us is what does happen, "not working" isn't really sufficient to help much.</p><p>Using the trunk dumpcap (r44426) and a similar command line the ring buffers work for me.</p></div><div id="comment-13873-info" class="comment-info"><span class="comment-age">(24 Aug '12, 05:28)</span> grahamb ♦</div></div></div><div id="comment-tools-13871" class="comment-tools"></div><div class="clear"></div><div id="comment-13871-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

