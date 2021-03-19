+++
type = "question"
title = "Dumpcap - Odd file size"
description = '''I am running dumpcap via the command sudo dumpcap -i 2 filesize:200000 -b files:2500 -B 1024 -w /media/root/CORE/capture/capture.pcapng  and noticed that despite downloading a 400MB~ file, on a repeater network (meaning the actual noise generated would be 800MB~) that my .pcapng was a mere 200MB! Is...'''
date = "2017-10-17T16:47:00Z"
lastmod = "2017-10-17T19:55:00Z"
weight = 63985
keywords = [ "editcap", "dumpcap", "monitor" ]
aliases = [ "/questions/63985" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Dumpcap - Odd file size](/questions/63985/dumpcap-odd-file-size)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63985-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63985-score" class="post-score" title="current number of votes">0</div><span id="post-63985-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am running dumpcap via the command</p><pre><code>sudo dumpcap -i 2 filesize:200000 -b files:2500 -B 1024 -w /media/root/CORE/capture/capture.pcapng</code></pre><p>and noticed that despite downloading a 400MB~ file, on a repeater network (meaning the actual noise generated would be 800MB~) that my .pcapng was a mere 200MB!</p><p>Is this normal, compression or something else? Or am I missing an excessive amount of packets? Thanks!</p><p>note: its possible -B may need to be increased?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-editcap" rel="tag" title="see questions tagged &#39;editcap&#39;">editcap</span> <span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span> <span class="post-tag tag-link-monitor" rel="tag" title="see questions tagged &#39;monitor&#39;">monitor</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Oct '17, 16:47</strong></p><img src="https://secure.gravatar.com/avatar/efcb279bb8d15ec2008e888616469d1f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cevestas&#39;s gravatar image" /><p><span>Cevestas</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cevestas has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Oct '17, 16:49</strong> </span></p></div></div><div id="comments-container-63985" class="comments-container"></div><div id="comment-tools-63985" class="comment-tools"></div><div class="clear"></div><div id="comment-63985-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63986"></span>

<div id="answer-container-63986" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63986-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63986-score" class="post-score" title="current number of votes">0</div><span id="post-63986-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Cevestas has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The syntax of your command is incorrect. Did you mean to write the following instead?</p><pre><code>sudo dumpcap -i 2 -b filesize:200000 -b files:2500 -B 1024 -w /media/root/CORE/capture/capture.pcapng</code></pre><p>The <code>-b filesize:200000</code> option will limit each file in the ring buffer to 200000 kB (or 200 MB). Refer to the <a href="https://www.wireshark.org/docs/man-pages/dumpcap.html"><code>dumpcap</code> man page</a> for more information. While it's possible there were dropped packets, the rest of the captured packets are almost certainly just written to the other files that were part of your ring buffer. Check your <code>/media/root/CORE/capture/</code> directory for the other files.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '17, 19:31</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-63986" class="comments-container"><span id="63988"></span><div id="comment-63988" class="comment"><div id="post-63988-score" class="comment-score"></div><div class="comment-text"><p>There are no other files in that directory (though have I have tested the ring buffer is working, I believe the file was just under 200MB when I killed the capture)</p><p>It seems that you're implying that if 1G was transferred (and all packets captured), then the .pcapng would 1G~?</p><p>Thank you! It's very nice to have a helpful forum like this.</p></div><div id="comment-63988-info" class="comment-info"><span class="comment-age">(17 Oct '17, 19:47)</span> <span class="comment-user userinfo">Cevestas</span></div></div><span id="63989"></span><div id="comment-63989" class="comment"><div id="post-63989-score" class="comment-score"></div><div class="comment-text"><p>You wrote, <code>filesize:200000</code> but you missed the preceding <code>-b</code>; it should be <code>-b filesize:200000</code> as I wrote. The result of using this option is that it will limit each file to 200MB and then close that file and start a new one, so no file will be bigger than 200MB.</p><p>If 1GB of data was transferred over the interface specified, then I'd expect you to have at least 5 files, each 200MB in size. If that's not the case, then you either dropped a ton of packets or the data was transferred on a different interface than you were capturing or ... <em>something else</em> TBD.</p></div><div id="comment-63989-info" class="comment-info"><span class="comment-age">(17 Oct '17, 19:55)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-63986" class="comment-tools"></div><div class="clear"></div><div id="comment-63986-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

