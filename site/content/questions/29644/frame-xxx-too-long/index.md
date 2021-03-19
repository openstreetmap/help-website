+++
type = "question"
title = "Frame xxx too long"
description = '''Hi, I&#x27;m working on wireshark to sniff the channel on which there are associated some nodes to one coordinator (it&#x27;s a wireless sensors network). The tx power is set to 0dB, somentimes it appears an error saying &quot;the frame xxx is too long&quot; and there is the payload (sometimes negative, sometimes posit...'''
date = "2014-02-10T10:45:00Z"
lastmod = "2014-02-11T01:54:00Z"
weight = 29644
keywords = [ "frame", "payload" ]
aliases = [ "/questions/29644" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Frame xxx too long](/questions/29644/frame-xxx-too-long)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29644-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29644-score" class="post-score" title="current number of votes">0</div><span id="post-29644-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm working on wireshark to sniff the channel on which there are associated some nodes to one coordinator (it's a wireless sensors network). The tx power is set to 0dB, somentimes it appears an error saying "the frame xxx is too long" and there is the payload (sometimes negative, sometimes positive) into round brackts. I'm tx varying the size of the payload from 5 bytes to 50 bytes, with steps of 5 bytes but I do not know which could be the problem. Is there anyone that can help me? Thanks best regards Ivana</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-frame" rel="tag" title="see questions tagged &#39;frame&#39;">frame</span> <span class="post-tag tag-link-payload" rel="tag" title="see questions tagged &#39;payload&#39;">payload</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '14, 10:45</strong></p><img src="https://secure.gravatar.com/avatar/105c3ff4c22af3ec11e726327bd5d6c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ivana%20Ester%20Marra&#39;s gravatar image" /><p><span>Ivana Ester ...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ivana Ester Marra has no accepted answers">0%</span></p></div></div><div id="comments-container-29644" class="comments-container"><span id="29647"></span><div id="comment-29647" class="comment"><div id="post-29647-score" class="comment-score"></div><div class="comment-text"><p>Some questions:</p><ul><li>what is your OS and OS version of the Wireshark system?</li><li>what is your Wireshark version?</li><li>how do you capture the traffic (with Wireshark, or other tools)?</li><li>on which interface do you capture?</li><li>is it possible to post a sample capture file somewhere (google drive, dropbox, cloudshark.org)?</li></ul></div><div id="comment-29647-info" class="comment-info"><span class="comment-age">(10 Feb '14, 11:30)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="29667"></span><div id="comment-29667" class="comment"><div id="post-29667-score" class="comment-score"></div><div class="comment-text"><p>Hi, thanks for you reply. I'm using windows 7 and the versione of Wireshark is 1.10.5. I have a sniffer connected to the pc thanks to which is possible to sniff the channel through \.\pipe\wireshark. The problem occurs only in this case, before that I have programmed the same nodes with tx power -5dBm and everything is gone well. I attach the screenshot of the error/message as you can see. <a href="https://www.dropbox.com/s/mlk7g4tba8jo4xf/errore.jpg">https://www.dropbox.com/s/mlk7g4tba8jo4xf/errore.jpg</a></p><p>Thanks Ivana</p></div><div id="comment-29667-info" class="comment-info"><span class="comment-age">(11 Feb '14, 01:12)</span> <span class="comment-user userinfo">Ivana Ester ...</span></div></div><span id="29669"></span><div id="comment-29669" class="comment"><div id="post-29669-score" class="comment-score"></div><div class="comment-text"><p>Looks like the capture file is damaged. Did you transfer the file via FTP or is that error message shown while you do a live capture?</p></div><div id="comment-29669-info" class="comment-info"><span class="comment-age">(11 Feb '14, 01:21)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="29670"></span><div id="comment-29670" class="comment"><div id="post-29670-score" class="comment-score"></div><div class="comment-text"><p>No. How can it be possible? no problems just changing the power in the software. Could it be the interference on the channel? I don't think so, actually.</p></div><div id="comment-29670-info" class="comment-info"><span class="comment-age">(11 Feb '14, 01:23)</span> <span class="comment-user userinfo">Ivana Ester ...</span></div></div></div><div id="comment-tools-29644" class="comment-tools"></div><div class="clear"></div><div id="comment-29644-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29675"></span>

<div id="answer-container-29675" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29675-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29675-score" class="post-score" title="current number of votes">0</div><span id="post-29675-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The software that writes to the pipe could be buggy... If possible, let that software write a capture file directly, instead of writing to a pipe.</p><p>You can also try to use dumpcap to read from the pipe and write a capture file.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '14, 01:54</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Feb '14, 01:58</strong> </span></p></div></div><div id="comments-container-29675" class="comments-container"></div><div id="comment-tools-29675" class="comment-tools"></div><div class="clear"></div><div id="comment-29675-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

