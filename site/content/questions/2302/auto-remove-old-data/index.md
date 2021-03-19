+++
type = "question"
title = "auto remove old data"
description = '''Is there a way to set wireshark to automatically delete capture data that is older than a given time? For example, I would like to have wireshark constantly running, but I don&#x27;t have unlimited storage space, so I would just like to see the data for the past 12 hours. I check my computer more than on...'''
date = "2011-02-13T08:39:00Z"
lastmod = "2011-02-14T06:56:00Z"
weight = 2302
keywords = [ "auto", "old", "remove", "data" ]
aliases = [ "/questions/2302" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [auto remove old data](/questions/2302/auto-remove-old-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2302-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2302-score" class="post-score" title="current number of votes">0</div><span id="post-2302-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to set wireshark to automatically delete capture data that is older than a given time?</p><p>For example, I would like to have wireshark constantly running, but I don't have unlimited storage space, so I would just like to see the data for the past 12 hours. I check my computer more than once every 12 hours, so if I see something strange happening, or if I want to see my packet history due to some recent event, I could do so and save the important parts if I wish.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-auto" rel="tag" title="see questions tagged &#39;auto&#39;">auto</span> <span class="post-tag tag-link-old" rel="tag" title="see questions tagged &#39;old&#39;">old</span> <span class="post-tag tag-link-remove" rel="tag" title="see questions tagged &#39;remove&#39;">remove</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Feb '11, 08:39</strong></p><img src="https://secure.gravatar.com/avatar/ecf73f7b5095f46d4d145d6d6851d552?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="1proof&#39;s gravatar image" /><p><span>1proof</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="1proof has no accepted answers">0%</span></p></div></div><div id="comments-container-2302" class="comments-container"></div><div id="comment-tools-2302" class="comment-tools"></div><div class="clear"></div><div id="comment-2302-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2308"></span>

<div id="answer-container-2308" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2308-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2308-score" class="post-score" title="current number of votes">4</div><span id="post-2308-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="1proof has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Or to give an example, you can make a ringbuffer with <strong>dumpcap</strong> as follows:</p><pre><code>dumpcap -i &lt;interface&gt; -w &lt;file.pcap&gt; -b files:48 -b duration:900</code></pre><p>This will create files of 900 seconds each, but after creating 48 files, it will remove the first one. Effectively it will keep 12 hours of data.</p><p>When you create new files based on time, you still might run out of diskspace if network traffic is unusually high. I always prefer something like the following:</p><pre><code>dumpcap -i &lt;interface&gt; -w &lt;file.pcap&gt; -b files:1024 -b filesize:16384</code></pre><p>Which will create files of 16MB and it will keep only the last 1024 of them, so you know the capture buffer will never grow beyond 16GB.</p><p>You can use <strong>capinfos</strong> to show which file contains which timeframe like so:</p><pre><code>capinfos -Taecu *.pcap</code></pre><p>If you need to combine data of multiple of these files, you can use <strong>mergecap</strong> to combine them:</p><pre><code>mergecap -w combined.pcap file1.pcap file2.pcap ... fileX.pcap</code></pre><p>This will combine file1 to fileX into the new file <code>'combined.pcap'</code>.</p><p>Last but not least, you can use <strong>editcap</strong> to get a certain time interval from the resulting tracefile with:</p><pre><code>editcap -A &quot;2011-02-13 20:00&quot; -B &quot;2011-02-13 21:00&quot; combined.pcap result.pcap</code></pre><p>Which will create a file <code>'result.pcap'</code> with only the packets from time range 20:00-21:00 on Feb 13th, 2011.</p><p>All used commands are included with Wireshark :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '11, 11:49</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-2308" class="comments-container"><span id="2316"></span><div id="comment-2316" class="comment"><div id="post-2316-score" class="comment-score"></div><div class="comment-text"><p>I think it's about time we get a new badge called "command line hero" for Sake :-)</p></div><div id="comment-2316-info" class="comment-info"><span class="comment-age">(13 Feb '11, 16:23)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="2321"></span><div id="comment-2321" class="comment"><div id="post-2321-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot for the reply! I'm new to wireshark, so I'm sure this was a very elementary problem for you.</p><p>I used dumpcap -i &lt;interface&gt; -w &lt;file.pcap&gt; -b files:1024 -b filesize:16384 as you said</p><p>So far its working well...</p><p>In case someone doesn't know, In windows you can get the proper name for &lt;interface&gt; by using dumpcap -D</p></div><div id="comment-2321-info" class="comment-info"><span class="comment-age">(14 Feb '11, 06:45)</span> <span class="comment-user userinfo">1proof</span></div></div><span id="2322"></span><div id="comment-2322" class="comment"><div id="post-2322-score" class="comment-score"></div><div class="comment-text"><p>I'm glad this works for you. If my answer did answer your question, you can click on the "checkmark" on the left of it (below the thumps-down) to accept the answer so the question will not appear in the "Unanswered" list anymore.</p><p>BTW I changed your "answer" to a "comment" to adhere to the Q&amp;A style of this website.</p></div><div id="comment-2322-info" class="comment-info"><span class="comment-age">(14 Feb '11, 06:56)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-2308" class="comment-tools"></div><div class="clear"></div><div id="comment-2308-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2306"></span>

<div id="answer-container-2306" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2306-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2306-score" class="post-score" title="current number of votes">0</div><span id="post-2306-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Look into using the ringbuffer options. And for long running capture, use dumpcap i.s.o. wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '11, 11:19</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-2306" class="comments-container"></div><div id="comment-tools-2306" class="comment-tools"></div><div class="clear"></div><div id="comment-2306-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

