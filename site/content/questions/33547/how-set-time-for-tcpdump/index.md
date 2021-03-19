+++
type = "question"
title = "how set time for tcpdump"
description = '''Hi I want to capture traffic with tcpdump and I want to have a script that get as input a time and start capturing traffic with tcpdump and after the time stop the capturing. can you help that how set for tcpdump or for a shellscript???'''
date = "2014-06-08T08:21:00Z"
lastmod = "2014-06-12T06:31:00Z"
weight = 33547
keywords = [ "set", "time" ]
aliases = [ "/questions/33547" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how set time for tcpdump](/questions/33547/how-set-time-for-tcpdump)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33547-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I want to capture traffic with tcpdump and I want to have a script that get as input a time and start capturing traffic with tcpdump and after the time stop the capturing.</p><p>can you help that how set for tcpdump or for a shellscript???</p></div><div id="question-tags" class="tags-container tags">set time</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '14, 08:21</strong></p><img src="https://secure.gravatar.com/avatar/deec7afda5035771868d6acfbc90d994?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mosa&#39;s gravatar image" /><p>mosa<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mosa has no accepted answers">0%</span></p></div></div><div id="comments-container-33547" class="comments-container"></div><div id="comment-tools-33547" class="comment-tools"></div><div class="clear"></div><div id="comment-33547-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33710"></span>

<div id="answer-container-33710" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33710-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You don't need any script, if the following simple method is good enough for you.</p><p>The first command will schedule tcpdump at 15:30, using the <a href="http://manpages.ubuntu.com/manpages/hardy/man1/at.1posix.html">command at</a> (should be available on any Unix like system).</p><blockquote><p>echo "/usr/sbin/tcpdump -ni eth0 -s0 -w /var/tmp/capture_eth0.pcap host 1.2.3.4 and port 80" | at 15:30<br />
</p></blockquote><p>The second command will schedule the 'end' of tcpdump, by simply killing all running tcpdump processes 5 minutes later (15:35).</p><blockquote><p>echo "killall tcpdump; killall tcpdump" | at 15:35</p></blockquote><p><strong>atq</strong> will show the jobs</p><blockquote><p>atq<br />
4 Thu Jun 12 15:35:00 2014 a surfer<br />
3 Thu Jun 12 15:30:00 2014 a surfer<br />
</p></blockquote><p>And <strong><code>at -c [jobid]</code></strong> will show the content of the jobs</p><blockquote><p>at -c 3 | tail -1<br />
tcpdump -ni eth0 -s0 -w /var/tmp/capture_eth0.pcap host 1.2.3.4 and port 80</p><p>at -c 4 | tail -1<br />
killall tcpdump; killall tcpdump</p></blockquote><p>If you need a solution for a more complex environment, you'll have to write a shell script that gets started with the <code>at</code> command (or by cron) and that kills only the tcpdump instance that was started by the script after some time (hint: SIGALRM). However, that's plain shell scripting and this is certainly the wrong place to ask for shell scripting tips ;-)</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '14, 06:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Jun '14, 06:47</p></div></div><div id="comments-container-33710" class="comments-container"></div><div id="comment-tools-33710" class="comment-tools"></div><div class="clear"></div><div id="comment-33710-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

