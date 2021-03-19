+++
type = "question"
title = "Convert libpcap to pdml"
description = '''Hi all, I am attempting to automate some capturing and conversion tasks using JAVA. I want to capture in files with size of 1024kB using the option -b filesize:1024 I also want these raw data converted to PDML/XML. I use: tshark -r infile &amp;gt; outfile -T pdml; This works fine using command prompt/co...'''
date = "2011-03-25T02:12:00Z"
lastmod = "2011-03-25T03:23:00Z"
weight = 3107
keywords = [ "convert", "pdml", "libpcap" ]
aliases = [ "/questions/3107" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Convert libpcap to pdml](/questions/3107/convert-libpcap-to-pdml)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3107-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I am attempting to automate some capturing and conversion tasks using JAVA.</p><p>I want to capture in files with size of 1024kB using the option -b filesize:1024</p><p>I also want these raw data converted to PDML/XML. I use: tshark -r <em>infile</em> &gt; <em>outfile</em> -T pdml; This works fine using command prompt/console, but in JAVA this '&gt;' to redirect stdout, seems to behave badly or not at all:</p><p>Runtime.getRuntime().exec("C:\Program Files\Wireshark\tshark -T pdml -r C:\test16 &gt;C:\test105");</p><p>The next line however works fine: Runtime.getRuntime().exec("C:\Program Files\Wireshark\tshark -r C:\test16 -w C:\test105"); So reading and writing files seems no problem.</p><p>Any suggestions to do this conversion task? Probably another program is more suitable? I saw the function of text2pcap but in fact I need this but then the other way round.</p><p>Thanks for your responses!</p></div><div id="question-tags" class="tags-container tags">convert pdml libpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Mar '11, 02:12</strong></p><img src="https://secure.gravatar.com/avatar/c7dbfca49db84cd170ae0e881badabce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="oty&#39;s gravatar image" /><p>oty<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="oty has no accepted answers">0%</span></p></div></div><div id="comments-container-3107" class="comments-container"></div><div id="comment-tools-3107" class="comment-tools"></div><div class="clear"></div><div id="comment-3107-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3108"></span>

<div id="answer-container-3108" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3108-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's because the "&gt;" is handled by the command shell and not by tshark. The function Runtime.getRuntime().exec() probably just passes all arguments to the executable and not run a shell underneath. I think the best way to solve this is by having a "glue" batch file that does the redirection for you:</p><pre><code>Runtime.getRuntime().exec(&quot;C:\convert.bat C:\test16 C:\test105&quot;);</code></pre><p>Where convert.bat should look something like:</p><pre><code>@echo off
C:\Program Files\Wireshark\tshark -T pdml -r %1 &gt; %2</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '11, 02:46</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-3108" class="comments-container"></div><div id="comment-tools-3108" class="comment-tools"></div><div class="clear"></div><div id="comment-3108-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3109"></span>

<div id="answer-container-3109" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3109-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks a lot, SYNbit!</p><p>You were right, there was no shell underneath but thanks to the batch file there is one now! :-]</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '11, 03:23</strong></p><img src="https://secure.gravatar.com/avatar/c7dbfca49db84cd170ae0e881badabce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="oty&#39;s gravatar image" /><p>oty<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="oty has no accepted answers">0%</span></p></div></div><div id="comments-container-3109" class="comments-container"></div><div id="comment-tools-3109" class="comment-tools"></div><div class="clear"></div><div id="comment-3109-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

