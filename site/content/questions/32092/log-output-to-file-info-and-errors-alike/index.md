+++
type = "question"
title = "Log output to file, info and errors alike"
description = '''Hi all,  I&#x27;m using tshark to record all traffic in my office during a day, for use in a research project.  I have a cron job mon-fri at 8 in the morning, that runs a shell script with the following:  tshark -i eth2 -i eth3 -w traces/$(date +%Y-%m-%d_%H-%M-%S)_benign.pcap -a duration:36000  I would l...'''
date = "2014-04-23T03:04:00Z"
lastmod = "2014-04-23T05:17:00Z"
weight = 32092
keywords = [ "tshark", "log" ]
aliases = [ "/questions/32092" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Log output to file, info and errors alike](/questions/32092/log-output-to-file-info-and-errors-alike)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32092-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32092-score" class="post-score" title="current number of votes">0</div><span id="post-32092-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I'm using tshark to record all traffic in my office during a day, for use in a research project. I have a cron job mon-fri at 8 in the morning, that runs a shell script with the following:</p><pre><code>tshark -i eth2 -i eth3 -w traces/$(date +%Y-%m-%d_%H-%M-%S)_benign.pcap -a duration:36000</code></pre><p>I would like to have access to the information printed by tshark, when executing, eg. drop count:</p><pre><code>[email protected]:~$ tshark -i eth2 -i eth3 -w traces/$(date +%Y-%m-%d_%H-%M-%S)_benign.pcap -a duration:36000
Capturing on &#39;eth2&#39; and &#39;eth3&#39;
185 ^C
1 packet dropped

1 packet dropped</code></pre><p>I was hoping to have a switch to specify a log file, however I'm unable to find such. Does such exist?</p><p>appending " &gt; tmp.log" doesn't catch the output..</p><p>Any suggestions as to how I can get a log?</p><p>Thanks in advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-log" rel="tag" title="see questions tagged &#39;log&#39;">log</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '14, 03:04</strong></p><img src="https://secure.gravatar.com/avatar/2face3431d8e964f0e598701da4ebced?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kidmose&#39;s gravatar image" /><p><span>kidmose</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kidmose has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Apr '14, 03:05</strong> </span></p></div></div><div id="comments-container-32092" class="comments-container"><span id="32095"></span><div id="comment-32095" class="comment"><div id="post-32095-score" class="comment-score">1</div><div class="comment-text"><p>Note that neither tshark nor Wireshark are recommended for continuous traffic capture, instead use dumpcap.</p><p>See <span>@Jasper</span>'s blog entry for more info: <a href="http://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/">http://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/</a></p></div><div id="comment-32095-info" class="comment-info"><span class="comment-age">(23 Apr '14, 05:17)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-32092" class="comment-tools"></div><div class="clear"></div><div id="comment-32092-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32093"></span>

<div id="answer-container-32093" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32093-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32093-score" class="post-score" title="current number of votes">2</div><span id="post-32093-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kidmose has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi kidmose,</p><p>if you would search on internet regarding redirection of i/o you would find a lot of info.</p><p>here are some useful links:</p><p><a href="http://www.tldp.org/LDP/abs/html/io-redirection.html">tldp</a></p><p><a href="http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-3.html">Bashk</a></p><p>or try this:</p><p><code>hostname:~ edmond$ tshark -i en0 -w yourfile.pcap -a duration:20 &gt; log 2&gt;&amp;1 hostname:~ edmond$ cat log Capturing on 'Ethernet' 441 packets captured hostname:~ edmond$ </code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '14, 03:16</strong></p><img src="https://secure.gravatar.com/avatar/57dca282828fcb7b6086c0a77af93ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Edmond&#39;s gravatar image" /><p><span>Edmond</span><br />
<span class="score" title="181 reputation points">181</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Edmond has 2 accepted answers">33%</span></p></div></div><div id="comments-container-32093" class="comments-container"></div><div id="comment-tools-32093" class="comment-tools"></div><div class="clear"></div><div id="comment-32093-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

