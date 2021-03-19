+++
type = "question"
title = "Dump raw packet &#x27;data&#x27; field only?"
description = '''Here&#x27;s the problem: I have some network traffic pcap files. I need the raw data layer packets from these files, which I can get (in one file) by right-clicking the &#x27;data&#x27; layer, and &#x27;Export selected packet bytes...&#x27;, but I then have to combine these raw files for all packets in the capture. I can pr...'''
date = "2012-10-30T09:19:00Z"
lastmod = "2015-06-18T06:40:00Z"
weight = 15374
keywords = [ "raw", "payload", "data", "tshark", "output" ]
aliases = [ "/questions/15374" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Dump raw packet 'data' field only?](/questions/15374/dump-raw-packet-data-field-only)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15374-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15374-score" class="post-score" title="current number of votes">0</div><span id="post-15374-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Here's the problem:</p><p>I have some network traffic pcap files. I need the raw data layer packets from these files, which I can get (in one file) by right-clicking the 'data' layer, and 'Export selected packet bytes...', but I then have to combine these raw files for all packets in the capture.</p><p>I can print just the data, in ASCII format, using tshark:</p><pre><code>tshark -r infile -T fields -e data</code></pre>But, when I try to do the same thing for the raw data:<pre><code>tshark -r infile -T fields -e data -w outfile.raw</code></pre>I'm not sure that outfile.raw is what I want. A file that I've converted manually can't be opened in Wireshark, as it can't understand the format. The one generated using the above command (outfile.raw) can be, so I'm assuming it's still outputting the headers.<p>Is there any way to either convert the hex/ascii back to raw packet data, or to output JUST the data payload in raw format?</p><p>I have many files to convert in this fashion, and being able to script the process would greatly speed things up...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-raw" rel="tag" title="see questions tagged &#39;raw&#39;">raw</span> <span class="post-tag tag-link-payload" rel="tag" title="see questions tagged &#39;payload&#39;">payload</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-output" rel="tag" title="see questions tagged &#39;output&#39;">output</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Oct '12, 09:19</strong></p><img src="https://secure.gravatar.com/avatar/79d7ee2589743eef43349a74a58bd291?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shearn89&#39;s gravatar image" /><p><span>shearn89</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shearn89 has one accepted answer">100%</span></p></div></div><div id="comments-container-15374" class="comments-container"><span id="15380"></span><div id="comment-15380" class="comment"><div id="post-15380-score" class="comment-score">1</div><div class="comment-text"><p>If you have the output of the raw data in ASCII, you can always convert that to a binary file with a script !??!</p><p>So, what are you going to do with the raw data what you can't do with the ASCII representation of that data?</p></div><div id="comment-15380-info" class="comment-info"><span class="comment-age">(30 Oct '12, 09:54)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="15409"></span><div id="comment-15409" class="comment"><div id="post-15409-score" class="comment-score"></div><div class="comment-text"><p>Ah, I hadn't thought of that! That might be a good simple solution to my problem. I need to netcat the data into a network socket that my program listens on, and it's expecting raw data, not ASCII...</p></div><div id="comment-15409-info" class="comment-info"><span class="comment-age">(31 Oct '12, 02:12)</span> <span class="comment-user userinfo">shearn89</span></div></div></div><div id="comment-tools-15374" class="comment-tools"></div><div class="clear"></div><div id="comment-15374-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="15413"></span>

<div id="answer-container-15413" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15413-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15413-score" class="post-score" title="current number of votes">2</div><span id="post-15413-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="shearn89 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To answer my question for future googlers: I used <span><span>@Kurt</span></span>'s suggestion, and converted the ascii to binary.</p><p>I had to remove the newlines that tshark adds in between the packets, so:</p><pre><code>tshark -r infile -T fields -e data | tr -d &#39;\n&#39; &gt; tempfile</code></pre><p>I then used the following short python script to convert from tempfile to binary: <code> import binascii import sys string = open(sys.argv[1],'r').read() sys.stdout.write(binascii.unhexlify(string)) # needs to be stdout.write to avoid trailing newline</code></p><p>You can then redirect the output of the python script to a file, and you get exactly what I need.</p><p>Also, it turns out this is equivalent to "follow tcp stream" in the Wireshark gui, and exporting the data as raw. EDIT: the reason 'follow tcp stream' wouldn't have worked in this situation is that I had two streams I needed in one file, in the order they were sent.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Oct '12, 03:15</strong></p><img src="https://secure.gravatar.com/avatar/79d7ee2589743eef43349a74a58bd291?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shearn89&#39;s gravatar image" /><p><span>shearn89</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shearn89 has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Jan '13, 15:08</strong> </span></p></div></div><div id="comments-container-15413" class="comments-container"><span id="43327"></span><div id="comment-43327" class="comment"><div id="post-43327-score" class="comment-score"></div><div class="comment-text"><p>Do any of you know how to do this using the Windows command line?</p></div><div id="comment-43327-info" class="comment-info"><span class="comment-age">(18 Jun '15, 06:40)</span> <span class="comment-user userinfo">dippy</span></div></div></div><div id="comment-tools-15413" class="comment-tools"></div><div class="clear"></div><div id="comment-15413-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15377"></span>

<div id="answer-container-15377" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15377-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15377-score" class="post-score" title="current number of votes">0</div><span id="post-15377-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think <strong>-w</strong> forces tshark to write the packets out again in pcap format, which you can easily verify by running the capinfos tool, e.g. "capinfos outfile.raw". It will tell you what File Type it is.</p><p>Maybe you can try to redirect the console output into a file by using the "&gt;" operator. I haven't tried it, but maybe something like this works (or gives you an idea):</p><pre><code>tshark -r infile -T fields -e data &gt;outfile.raw</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Oct '12, 09:39</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-15377" class="comments-container"><span id="15410"></span><div id="comment-15410" class="comment"><div id="post-15410-score" class="comment-score"></div><div class="comment-text"><p>That produces an ASCII file, which is what I'm trying to avoid. Cheers for the idea though!</p></div><div id="comment-15410-info" class="comment-info"><span class="comment-age">(31 Oct '12, 02:14)</span> <span class="comment-user userinfo">shearn89</span></div></div></div><div id="comment-tools-15377" class="comment-tools"></div><div class="clear"></div><div id="comment-15377-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

