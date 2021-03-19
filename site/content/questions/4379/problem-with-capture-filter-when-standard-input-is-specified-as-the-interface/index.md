+++
type = "question"
title = "Problem with capture filter when standard input is specified as the interface."
description = '''Hi All, I am trying to do SSH tunnelling from remote machine and redirect that message to dumpcap which is running on local machine, as shown below. ssh root@172.19.52.133 &quot;/upapps/ptc/cbtcpa/bin/dumpcap -i eth0 -w -&quot; | /upapps/ptc/cbtcpa/bin/dumpcap -i - -f &quot;port not 22&quot; -a duration:60 -b duration:...'''
date = "2011-06-04T20:46:00Z"
lastmod = "2011-06-05T00:33:00Z"
weight = 4379
keywords = [ "capture-filter" ]
aliases = [ "/questions/4379" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Problem with capture filter when standard input is specified as the interface.](/questions/4379/problem-with-capture-filter-when-standard-input-is-specified-as-the-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4379-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I am trying to do SSH tunnelling from remote machine and redirect that message to dumpcap which is running on local machine, as shown below.</p><p>ssh [email protected] "/upapps/ptc/cbtcpa/bin/dumpcap -i eth0 -w -" | /upapps/ptc/cbtcpa/bin/dumpcap -i - -f "port not 22" -a duration:60 -b duration:60 -w test.pcap</p><p>But i am facing problem in the capture filter "-f "port not 22"", when i capture from the standard input. It is not filtering the desired packets. The file contains all the packets.</p><p>Does the capture filter not work with the above syntax, that is when capturing packets with interface specified as "-" standard input.</p><p>So, request your help to solve this.</p><p>Thanks in advance. Kiran Kumar G</p></div><div id="question-tags" class="tags-container tags">capture-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jun '11, 20:46</strong></p><img src="https://secure.gravatar.com/avatar/ae4b5aebc9d00c273018cc64d3ac583a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kiran%20Kumar%20G&#39;s gravatar image" /><p>Kiran Kumar G<br />
<span class="score" title="21 reputation points">21</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kiran Kumar G has no accepted answers">0%</span></p></div></div><div id="comments-container-4379" class="comments-container"></div><div id="comment-tools-4379" class="comment-tools"></div><div class="clear"></div><div id="comment-4379-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4380"></span>

<div id="answer-container-4380" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4380-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>IIRC capture filters in dumpcap don't work when reading from a file or a pipe. But even if it did, you want to filter on the capturing host, not on saving host. And the syntax is "not port 22" instead of "port not 22".</p><p>So you would want to use something like:</p><pre><code>ssh [email protected] &quot;/upapps/ptc/cbtcpa/bin/dumpcap -i eth0 -f &quot;not port 22&quot; -w -&quot; |\
    /upapps/ptc/cbtcpa/bin/dumpcap -i - -b duration:60 -w test.pcap</code></pre><p>Please note that combining -a and -b options might give you unexpected results. You have to use either the -a options or the -b options.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jun '11, 00:33</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4380" class="comments-container"><span id="4431"></span><div id="comment-4431" class="comment"><div id="post-4431-score" class="comment-score"></div><div class="comment-text"><p>Hi SYNbit,</p><pre><code>Thanks for your answer.

Actually there is a requirement to use tcpdump on the remote machine to capture the data and send over SSH tunnel to the local dumpcap to store packets on the remote machine. As given below.

ssh [email protected] &quot;tcpdump -i eth0 (not port 22 and tcp port 80) -w -&quot; | /upapps/ptc/cbtcpa/bin/dumpcap -i - -f &quot;port not 22&quot; -a duration:60 -b duration:60 -w test.pcap</code></pre><p>But i am facing issue with this, which is, if there are no packets captured for the above given capture command with the capture filter criteria then there will be no packets (file) dumped on the local machine. This is not the case with dumpcap, it will start dumping the packets into the file even if there are no packets captured.</p><pre><code>I want the file to be created on the local machine even if there are no packets captured. Is there a way through tcpdump to achieve this.

I am using -a and -b option because, -a specifies the total duration of the capture and -b is the resolution time for which the dumpcap should create the file. Ex: for 2 minutes capture, if -b is with 60 seconds then 2 files will be created.

Request your help on this.</code></pre><ul><li>Thanks and Regards, Kiran Kumar G</li></ul></div><div id="comment-4431-info" class="comment-info"><span class="comment-age">(07 Jun '11, 06:58)</span> Kiran Kumar G</div></div><span id="4439"></span><div id="comment-4439" class="comment"><div id="post-4439-score" class="comment-score"></div><div class="comment-text"><p>Sorry there is a mistake in the sentence, plese find below the correct sentence.</p><p>Actually there is a requirement to use tcpdump on the remote machine to capture the data and send over SSH tunnel to the local dumpcap to store packets on the local machine. As given below.</p></div><div id="comment-4439-info" class="comment-info"><span class="comment-age">(07 Jun '11, 10:41)</span> Kiran Kumar G</div></div></div><div id="comment-tools-4380" class="comment-tools"></div><div class="clear"></div><div id="comment-4380-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

