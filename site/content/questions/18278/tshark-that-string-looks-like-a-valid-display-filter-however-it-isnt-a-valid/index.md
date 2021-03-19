+++
type = "question"
title = "tshark: That string looks like a valid display filter; however, it isn&#x27;t a valid"
description = '''here is the command I tried to use: tshark -i eth1 -f diameter  And the output: tshark: Invalid capture filter: &quot;diameter&quot;! That string looks like a valid display filter; however, it isn&#x27;t a valid capture filter (syntax error). Note that display filters and capture filters don&#x27;t have the same syntax...'''
date = "2013-02-04T06:41:00Z"
lastmod = "2013-02-04T10:16:00Z"
weight = 18278
keywords = [ "capture-filter", "tshark" ]
aliases = [ "/questions/18278" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [tshark: That string looks like a valid display filter; however, it isn't a valid](/questions/18278/tshark-that-string-looks-like-a-valid-display-filter-however-it-isnt-a-valid)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18278-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>here is the command I tried to use:</p><pre><code>tshark -i eth1 -f diameter</code></pre><p>And the output:</p><pre><code>tshark: Invalid capture filter: &quot;diameter&quot;!
That string looks like a valid display filter; however, it isn&#39;t a valid capture filter (syntax error).
Note that display filters and capture filters don&#39;t have the same syntax, o you can&#39;t use most display filter expressions as capture filters.
See the User&#39;s Guide for a description of the capture filter syntax.</code></pre><p>That is the <a href="http://wiki.wireshark.org/CaptureFilters">user guide</a> I found. But I didnt get any useful info according to my issue. Please help.<br />
<strong>Edit:</strong> I would like to save only the diameter packets, but when I am using this command:</p><pre><code>tshark -i eth1 -R diameter -w /home/ttcn3/traces/</code></pre><p>I got this:</p><pre><code>tshark: Read filters aren&#39;t supported when capturing and saving the captured packets.</code></pre><p>So how can save only those packets which I would filter by protocol name?</p></div><div id="question-tags" class="tags-container tags">capture-filter tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Feb '13, 06:41</strong></p><img src="https://secure.gravatar.com/avatar/0c7332e9fdd92b1e99d905c07ab4bdc2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HiB&#39;s gravatar image" /><p>HiB<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HiB has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Feb '13, 06:57</p></div></div><div id="comments-container-18278" class="comments-container"><span id="18282"></span><div id="comment-18282" class="comment"><div id="post-18282-score" class="comment-score">2</div><div class="comment-text"><p>With reference to question about filtering live captures with tshark, see <a href="http://ask.wireshark.org/questions/18130/tcpdump-r-not-filtering-live-captures">this</a> question. Note in particular the answer by @JeffMorriss</p></div><div id="comment-18282-info" class="comment-info"><span class="comment-age">(04 Feb '13, 07:09)</span> grahamb ♦</div></div><span id="18284"></span><div id="comment-18284" class="comment"><div id="post-18284-score" class="comment-score"></div><div class="comment-text"><p>thanks, so this is a bug in tshark</p></div><div id="comment-18284-info" class="comment-info"><span class="comment-age">(04 Feb '13, 08:30)</span> HiB</div></div><span id="18285"></span><div id="comment-18285" class="comment"><div id="post-18285-score" class="comment-score"></div><div class="comment-text"><p>The <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=2234">"bug"</a> is more a consequence of how tshark works after the privilege separation work was done. As the comments on the bug show, some work is being done to improve the situation, but right now doing this doesn't work in release builds.</p></div><div id="comment-18285-info" class="comment-info"><span class="comment-age">(04 Feb '13, 08:53)</span> grahamb ♦</div></div></div><div id="comment-tools-18278" class="comment-tools"></div><div class="clear"></div><div id="comment-18278-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18288"></span>

<div id="answer-container-18288" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18288-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The following might work for you: <code>tshark -i eth1 -f "tcp port 3868"</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '13, 10:16</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-18288" class="comments-container"><span id="18289"></span><div id="comment-18289" class="comment"><div id="post-18289-score" class="comment-score"></div><div class="comment-text"><p>thanks, in this case, but in generally I would do with protocol filtering, not with port filtering</p></div><div id="comment-18289-info" class="comment-info"><span class="comment-age">(04 Feb '13, 10:23)</span> HiB</div></div><span id="18291"></span><div id="comment-18291" class="comment"><div id="post-18291-score" class="comment-score"></div><div class="comment-text"><p>You indicated that, <em>"I would like to save only the diameter packets"</em>. That implies that you are in need of an appropriate <strong>capture filter</strong> in order to accomplish this. Since you need a capture filter, you must follow <a href="http://www.manpagez.com/man/7/pcap-filter/">capture filter syntax</a>, and not <a href="http://www.wireshark.org/docs/dfref/d/diameter.html">Wireshark's display filter syntax for the diameter protocol</a>. See also the <a href="http://wiki.wireshark.org/DIAMETER">Wireshark diameter wiki page</a>.</p></div><div id="comment-18291-info" class="comment-info"><span class="comment-age">(04 Feb '13, 11:00)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-18288" class="comment-tools"></div><div class="clear"></div><div id="comment-18288-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18280"></span>

<div id="answer-container-18280" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18280-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The output you're seeing is a pretty good explanation of what's going wrong. Capture filters are used to limit the packets that are actually sniffed off the wire. You are probably looking for a Display Filter, which can be applied using the -R flag:</p><pre><code>tshark -i eth1 -R diameter</code></pre><p>I'm not familiar with the 'diameter' protocol, but I believe this will help you out.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '13, 06:51</strong></p><img src="https://secure.gravatar.com/avatar/365cfc3c62b61b2ed219b5d146e8ad3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zachad&#39;s gravatar image" /><p>zachad<br />
<span class="score" title="331 reputation points">331</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zachad has 3 accepted answers">21%</span></p></div></div><div id="comments-container-18280" class="comments-container"><span id="18281"></span><div id="comment-18281" class="comment"><div id="post-18281-score" class="comment-score"></div><div class="comment-text"><p>thanks, but then I need to edit my original question, since I know this -R switch</p></div><div id="comment-18281-info" class="comment-info"><span class="comment-age">(04 Feb '13, 06:53)</span> HiB</div></div></div><div id="comment-tools-18280" class="comment-tools"></div><div class="clear"></div><div id="comment-18280-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

