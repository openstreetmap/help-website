+++
type = "question"
title = "How do you make tshark read a ring buffer created by dumpcap?"
description = '''Greetings. I wish to use tshark to monitor an network interface. I understand that in do so, tshark executes dumpcap and dumpcap creates a pcap file that tshark then reads. The only problem is that I have restricted file capacity. I also understand that both tshark and dumpcap can be instructed to u...'''
date = "2012-08-21T22:57:00Z"
lastmod = "2012-08-22T16:38:00Z"
weight = 13808
keywords = [ "buffer", "ring", "tshark", "dumpcap" ]
aliases = [ "/questions/13808" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How do you make tshark read a ring buffer created by dumpcap?](/questions/13808/how-do-you-make-tshark-read-a-ring-buffer-created-by-dumpcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13808-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13808-score" class="post-score" title="current number of votes">0</div><span id="post-13808-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Greetings. I wish to use tshark to monitor an network interface. I understand that in do so, tshark executes dumpcap and dumpcap creates a pcap file that tshark then reads. The only problem is that I have restricted file capacity. I also understand that both tshark and dumpcap can be instructed to use files in a ring buffer manner with the -b option. The question is, can tshark be configured to execute dumpcap so that it writes the pcap data into a ring buffer and then read data from the ring buffer? Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-buffer" rel="tag" title="see questions tagged &#39;buffer&#39;">buffer</span> <span class="post-tag tag-link-ring" rel="tag" title="see questions tagged &#39;ring&#39;">ring</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Aug '12, 22:57</strong></p><img src="https://secure.gravatar.com/avatar/f9b0ffba1457b5e66231e0524d7a3b8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="richy&#39;s gravatar image" /><p><span>richy</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="richy has no accepted answers">0%</span></p></div></div><div id="comments-container-13808" class="comments-container"></div><div id="comment-tools-13808" class="comment-tools"></div><div class="clear"></div><div id="comment-13808-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="13831"></span>

<div id="answer-container-13831" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13831-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13831-score" class="post-score" title="current number of votes">2</div><span id="post-13831-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="richy has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The pipe is used for messages from dumpcap to {Wireshark,TShark}; those messages normally say "I've added N more packets to the end of the current capture file". Wireshark and TShark read those messages and, in response to them, read in N packets from the current capture file and process them. There are also "I've switched to a new file" messages, used if not capturing to a single file.</p><p>Currently, TShark requires that packets be written to a file specified with <code>-w</code> if you're going to use the ring buffer options. (If you don't specify <code>-w</code>, it just writes to a temporary file, and that will keep getting bigger over time, which is what you <em>don't</em> want).</p><p>So you'd have to do something such as</p><pre><code>tshark -P -b filesize:{size} -b files:{count} -w /tmp/ringfiles -i eth0</code></pre><p>which will write to files in <code>/tmp</code> with names beginning with <code>ringfiles</code>; it will switch files when a file gets bigger than {size}, and will keep only {count} such files around. <code>-P</code> will cause it to read and dissect the packets as they arrive, which, in your <em>reply</em>, you indicated that you want (had you indicated that in your <em>question</em>, for example, indicating that you want TShark to read the ring buffer files <em>as it runs</em>, rather than writing to a file without printing packet dissections and then running TShark on the saved files after you've finished running a dump to the files, the original answer might have applied better to the problem you were trying to solve).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Aug '12, 16:38</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-13831" class="comments-container"></div><div id="comment-tools-13831" class="comment-tools"></div><div class="clear"></div><div id="comment-13831-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13809"></span>

<div id="answer-container-13809" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13809-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13809-score" class="post-score" title="current number of votes">0</div><span id="post-13809-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>tshark can capture into a ring buffer by using the -b option you already mentioned, if you use it with the files:NUM parameter. And of course you can read the resulting trace files with tshark, but only one by one. If you need to read more than one file at once you can try to merge them together into a larger file using mergecap, but you need to keep in mind that the file might become too large to be read without a crash if you merge too many files.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Aug '12, 00:01</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-13809" class="comments-container"><span id="13829"></span><div id="comment-13829" class="comment"><div id="post-13829-score" class="comment-score"></div><div class="comment-text"><p>thanks but the whole point of the exercise is to capture traffic and analyze it with tshark in real time. When I do this using the -i eth0 (for instance) option the file which written to by dumpcap (as executed by tshark) amd read by tshark just grows until it exhausts the available disk space. When looking at the /proc/PID/fd directories for each, I noticed that they share a pipe. Even though the tshark is reading the filesystem file created by dumpcap. I assume the pipe is some kind of interprocess control channel. And that leads me to believe that there must be a way for ring buffer style transfer of pcap data between dumpcap and tshark in real time. Anyone else have any ideas?</p></div><div id="comment-13829-info" class="comment-info"><span class="comment-age">(22 Aug '12, 15:00)</span> <span class="comment-user userinfo">richy</span></div></div></div><div id="comment-tools-13809" class="comment-tools"></div><div class="clear"></div><div id="comment-13809-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

