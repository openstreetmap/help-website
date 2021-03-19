+++
type = "question"
title = "Refresh open File in Wireshark"
description = '''Hello All,  I have the following problem that iam trying to work out with the help of Wireshark   I have log files that keep getting updated. Using text2pcap the files are being processed and viewed in the wireshark.  As the files keep getting updated dynamically I am required to process the log fil...'''
date = "2012-11-07T22:49:00Z"
lastmod = "2012-11-08T06:09:00Z"
weight = 15676
keywords = [ "rtp" ]
aliases = [ "/questions/15676" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Refresh open File in Wireshark](/questions/15676/refresh-open-file-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15676-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15676-score" class="post-score" title="current number of votes">0</div><span id="post-15676-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All, I have the following problem that iam trying to work out with the help of Wireshark</p><ol><li>I have log files that keep getting updated.</li><li>Using text2pcap the files are being processed and viewed in the wireshark.</li></ol><p>As the files keep getting updated dynamically I am required to process the log files every few minutes to view the latest messages. Can anybody suggest if there is any way Wireshark can refresh the opened file automatically whenever the contents change or if there is any workaround to achieve the same affect instead of manually refreshing using CTRL+R.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '12, 22:49</strong></p><img src="https://secure.gravatar.com/avatar/97e620804d00012d2cec1885d6422a13?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="manojdeoli&#39;s gravatar image" /><p><span>manojdeoli</span><br />
<span class="score" title="1 reputation points">1</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="manojdeoli has no accepted answers">0%</span></p></div></div><div id="comments-container-15676" class="comments-container"></div><div id="comment-tools-15676" class="comment-tools"></div><div class="clear"></div><div id="comment-15676-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="15689"></span>

<div id="answer-container-15689" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15689-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15689-score" class="post-score" title="current number of votes">0</div><span id="post-15689-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark can read from a (named) pipe. Your tool would create that named pipe and write updated data to it. That data must be in pcap file format. As soon as you write to the pipe, Wireshark will display the packets.</p><p>Please read more about pipes in the Wiki:</p><blockquote><p><code>http://wiki.wireshark.org/CaptureSetup/Pipes</code><br />
</p></blockquote><p>Please check also my answer to the following question:</p><blockquote><p><code>http://ask.wireshark.org/questions/13059/capturing-from-multiple-pipes</code><br />
</p></blockquote><p>Basically you would do the following (on Windows):</p><ol><li><p>Create a pipe (\.\pipe\livedata) within your application that reads the log.</p></li><li><p>Read the log file and convert the data into pcap format. You can use/modify the source code of text2pcap to do that. Unfortunately you cannot use text2pcap, as it cannot write to the pipe in a way that would work in your scenario (continuous updates).</p></li><li><p>Read from the named pipe in Wireshark</p></li></ol><blockquote><p><code>wireshark -i \\.\pipe\livedata -k</code><br />
</p></blockquote><p>The same works in Linux. Please google for: mkfifo</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '12, 00:59</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Nov '12, 02:08</strong> </span></p></div></div><div id="comments-container-15689" class="comments-container"></div><div id="comment-tools-15689" class="comment-tools"></div><div class="clear"></div><div id="comment-15689-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15715"></span>

<div id="answer-container-15715" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15715-score" class="post-score" title="current number of votes">0</div><span id="post-15715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Also see my answer to your <a href="http://ask.wireshark.org/questions/15674/wireshark-display-increasing-trace-file">other question</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '12, 06:09</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span> </br></br></p></div></div><div id="comments-container-15715" class="comments-container"></div><div id="comment-tools-15715" class="comment-tools"></div><div class="clear"></div><div id="comment-15715-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

