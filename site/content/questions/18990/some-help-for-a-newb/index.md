+++
type = "question"
title = "Some help for a NewB"
description = '''I have a ESXi VM Host running a VM of CentOS and a Windows 7 VM. My question is multi tiered and I apologize in advance if these questions could be answered elsewhere, I&#x27;m kinda in a crunch. (New boss - new &quot;Important Project&quot; - sure u been there before) From the CentOS VM I need to run TShark and s...'''
date = "2013-02-28T12:10:00Z"
lastmod = "2013-03-01T06:24:00Z"
weight = 18990
keywords = [ "tshark", "linux" ]
aliases = [ "/questions/18990" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Some help for a NewB](/questions/18990/some-help-for-a-newb)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18990-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18990-score" class="post-score" title="current number of votes">0</div><span id="post-18990-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a ESXi VM Host running a VM of CentOS and a Windows 7 VM. My question is multi tiered and I apologize in advance if these questions could be answered elsewhere, I'm kinda in a crunch. (New boss - new "Important Project" - sure u been there before)</p><p>From the CentOS VM I need to run TShark and set a script to only make 400MB files and dump them to a folder which can then be read by my Win7 VM running Netwitness. In addition, the TShark has to maintain its process, meaning that if it stops it must auto restart immediately (can probably use some type of Cron job to do this - unless better method is suggested - my thought is a script that loops checking to see if Tshark is running and if not auto-restarts it, perhaps with watchdog). Once the "dump" folder reaches 50GB, TShark would then begin overwriting the oldest file. I have managed to create a folder on my Win7 VM called "Tshark" and have even managed to mount it to my CentOS VM at "/var/log/Tshark". I want Tshark to run as a background program and "never stop", always starting with startup of the machine (should it reboot). I also need the PCAPS it creates to be as verbose as possible in their captures.</p><p>Did I mention I'm a NEWB and my boss wants this yesterday? I have very limited experience with scripting, linux, etc. I'm an analyst... it's always just been set up when I get there... now I gotta do a Neo dump and hope I can fit the peices together to build it from the ground - LOL. Thanks in advance for the kindness and responsiveness of the group. I'm sure the experience here will understand and be kind.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '13, 12:10</strong></p><img src="https://secure.gravatar.com/avatar/6be2dd82e2d57afcab83a76f80e07d22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ERitz&#39;s gravatar image" /><p><span>ERitz</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ERitz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Feb '13, 12:19</strong> </span></p></div></div><div id="comments-container-18990" class="comments-container"></div><div id="comment-tools-18990" class="comment-tools"></div><div class="clear"></div><div id="comment-18990-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18992"></span>

<div id="answer-container-18992" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18992-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18992-score" class="post-score" title="current number of votes">0</div><span id="post-18992-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>From the CentOS VM I need to run TShark and set a script to only make 400MB files and dump them to a folder which can then be read by my Win7 VM running Netwitness.</p></blockquote><p>If you want to analyze the data with Netwitness, don't capture with tshark. Either use <strong>dumpcap</strong> or <strong>tcpdump</strong> (see below).</p><blockquote><p>In addition, the TShark has to maintain its process, meaning that if it stops it must auto restart immediately (can probably use some type of Cron job to do this - unless better method is suggested</p></blockquote><p>You could add the dumpcap/tcpdump command to <strong>/etc/inittab</strong> with a <strong>respawn</strong> option, if <strong>inittab</strong> is available on your system. Init will then handle the restart of the command if it dies.</p><p>Another option would be monit.</p><blockquote><p><code>http://mmonit.com/monit/</code><br />
</p></blockquote><p>Unfortunately you need some linux skills to make either method work :-(</p><blockquote><p>Once the "dump" folder reaches 50GB, TShark would then begin overwriting the oldest file.</p></blockquote><p>For this you need the ring buffer feature of dumpcap and/or tcpdump:</p><blockquote><p><code>dumpcap -q -ni eth0 -s0 -b filesize:400000 -b files:125 -w /var/log/Tshark/evidence.cap</code><br />
</p></blockquote><p>or<br />
</p><blockquote><p><code>tcpdump -ni eth0 -s0 -C 400 -W 125 -w /var/log/Tshark/evidence.cap</code><br />
</p></blockquote><p>These commands will write 400 MB files (125 files == 50 GByte). The oldest file will then be overwritten.</p><blockquote><p>I also need the PCAPS it creates to be as verbose as possible in their captures.</p></blockquote><p>With the command above you will capture raw data, so it will contain the whole payload of the frames. The 'verbosity' comes with the analysis in Wireshark and/or Netwitness ;-)</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Feb '13, 12:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Feb '13, 12:56</strong> </span></p></div></div><div id="comments-container-18992" class="comments-container"><span id="19029"></span><div id="comment-19029" class="comment"><div id="post-19029-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt. Thanks for the suggestion to use dumpcap/tcpdump; though I don't understand the "why" you prefer those two vs. Tshark? Not a challenge, just desire for greater understanding :). In the interim of waiting for an answer I did figure out the following command</p><blockquote>[<span class="__cf_email__" data-cfemail="8dffe2e2f9cde1e2eeece1e5e2fef9">[email protected]</span> ~]# tshark -w /var/log/Tshark/evidence -t ad -b filesize:409600 -b files:125</blockquote><p>Is this not recommended?</p></div><div id="comment-19029-info" class="comment-info"><span class="comment-age">(01 Mar '13, 06:00)</span> <span class="comment-user userinfo">ERitz</span></div></div><span id="19030"></span><div id="comment-19030" class="comment"><div id="post-19030-score" class="comment-score"></div><div class="comment-text"><p>tshark (and wireshark) build up state information about conversations over time so will run out of memory. dumpcap/tcpdump don't do that.</p></div><div id="comment-19030-info" class="comment-info"><span class="comment-age">(01 Mar '13, 06:24)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-18992" class="comment-tools"></div><div class="clear"></div><div id="comment-18992-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

