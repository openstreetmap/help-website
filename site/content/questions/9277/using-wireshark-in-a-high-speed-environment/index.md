+++
type = "question"
title = "Using Wireshark In A High Speed Environment"
description = '''I am trying to measure a high speed telemetry system. It is capable of producing &amp;gt; 1000 frames per second or 1000Hz. I am using wireshark to capture the UDP port where these frames are produced. I have had much trouble getting a reliable measurement. I was wondering if your team has tested wiresh...'''
date = "2012-02-29T06:58:00Z"
lastmod = "2012-03-02T06:28:00Z"
weight = 9277
keywords = [ "speed" ]
aliases = [ "/questions/9277" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Using Wireshark In A High Speed Environment](/questions/9277/using-wireshark-in-a-high-speed-environment)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9277-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9277-score" class="post-score" title="current number of votes">0</div><span id="post-9277-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to measure a high speed telemetry system. It is capable of producing &gt; 1000 frames per second or 1000Hz. I am using wireshark to capture the UDP port where these frames are produced. I have had much trouble getting a reliable measurement. I was wondering if your team has tested wireshark at these rates before? If so, can you tell me what rate wireshark can reliably measure?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-speed" rel="tag" title="see questions tagged &#39;speed&#39;">speed</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Feb '12, 06:58</strong></p><img src="https://secure.gravatar.com/avatar/159042c157f7ed4217a17458f0933ded?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ggray08&#39;s gravatar image" /><p><span>ggray08</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ggray08 has no accepted answers">0%</span></p></div></div><div id="comments-container-9277" class="comments-container"><span id="9282"></span><div id="comment-9282" class="comment"><div id="post-9282-score" class="comment-score"></div><div class="comment-text"><p>What are you trying to "reliably measure" ?</p><p>Also: Assuming full size frames: 1000 frames/sec * 1500 bytes/frame ==&gt; 12 Mbits/sec doesn't seem to me to be be excessively high.</p></div><div id="comment-9282-info" class="comment-info"><span class="comment-age">(29 Feb '12, 16:57)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="9291"></span><div id="comment-9291" class="comment"><div id="post-9291-score" class="comment-score"></div><div class="comment-text"><p>This is a 10017 Byte UDP frame @ 1000 Hz (80 Mbits/sec). My system is capable of doubling that number also. I was just wondering if Wireshark can actually keep up and capture each frame at these speeds.</p></div><div id="comment-9291-info" class="comment-info"><span class="comment-age">(01 Mar '12, 08:29)</span> <span class="comment-user userinfo">ggray08</span></div></div></div><div id="comment-tools-9277" class="comment-tools"></div><div class="clear"></div><div id="comment-9277-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9292"></span>

<div id="answer-container-9292" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9292-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9292-score" class="post-score" title="current number of votes">0</div><span id="post-9292-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>OK:</p><ol><li><p>Do some web searches using terms like: 'wireshark "high-speed" capture loss' to find some discussions.</p></li><li><p>At the very least do capturing separately from analysis. That is: if you are using Wireshark (or tshark) try using dumpcap (or tcpdump ? or ?? ) to do the capture. Wireshark can then be used to analyze the resulting file.</p></li></ol><p>dumpcap is the program which actually does the capturing. Wireshark uses dumpcap to do the capturing but is also doing dissection as the capture takes place.</p><ol><li><p>Other thoughts: Do you need the complete contents of each frame ? ISTR that restricting the "snapshot length" (maximum amount of data actually captured from each frame) may help. If nothing else there will be less data to write to disk.</p></li><li><p>Obviously YMMV depending upon the hardware, OS, capture program, etc, etc being used and thus, in general, it's difficult if not impossible to provide a simple answer to your question.</p></li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '12, 10:02</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-9292" class="comments-container"><span id="9309"></span><div id="comment-9309" class="comment"><div id="post-9309-score" class="comment-score"></div><div class="comment-text"><p>Thank you! I will try your comments. Appreciate your time.</p></div><div id="comment-9309-info" class="comment-info"><span class="comment-age">(02 Mar '12, 06:28)</span> <span class="comment-user userinfo">ggray08</span></div></div></div><div id="comment-tools-9292" class="comment-tools"></div><div class="clear"></div><div id="comment-9292-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

