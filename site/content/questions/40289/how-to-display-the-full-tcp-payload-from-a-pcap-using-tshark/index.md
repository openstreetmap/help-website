+++
type = "question"
title = "How to display the full TCP payload from a pcap using tshark?"
description = '''I have tried the following tshark command and the matching is working fine tshark -R &quot;tcp contains SEK&quot; -2 -r 2015-03-04.pcap -T fields -e tcp  However, the output of the tcp field doesn&#x27;t include the full data payload. Instead it contains a friendly summary. Transmission Control Protocol, Src Port:...'''
date = "2015-03-05T07:38:00Z"
lastmod = "2015-03-06T05:11:00Z"
weight = 40289
keywords = [ "field", "tshark", "tcp", "payload" ]
aliases = [ "/questions/40289" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to display the full TCP payload from a pcap using tshark?](/questions/40289/how-to-display-the-full-tcp-payload-from-a-pcap-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40289-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40289-score" class="post-score" title="current number of votes">0</div><span id="post-40289-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I have tried the following tshark command and the matching is working fine</p><pre><code>tshark -R &quot;tcp contains SEK&quot; -2 -r 2015-03-04.pcap -T fields -e tcp</code></pre><p>However, the output of the <code>tcp</code> field doesn't include the full data payload. Instead it contains a friendly summary.</p><pre><code>Transmission Control Protocol, Src Port: 18083 (18083), Dst Port: 53649 (53649), Seq: 1, Ack: 1, Len: 205</code></pre><p>I've done a bunch of Googling and have found similar questions, but the fields they indicate to use don't exist or are empty. I've tried <code>tcp.data</code>, <code>data.data</code>, <code>text</code>, <code>tcp.segment_data</code> and some others.</p><p>broset's answer to <a href="https://ask.wireshark.org/questions/14078/decapsulation-of-data">this question</a> came close in that it appears to get me the undecoded payload.<br />
</p><p>How do I instruct tshark to output the full decoded TCP payload without any ethernet, IP or TCP headers? Ideally I could do this without disabling the protocol dissector in Wireshark.</p><p>Thanks much, Rob</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-field" rel="tag" title="see questions tagged &#39;field&#39;">field</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-payload" rel="tag" title="see questions tagged &#39;payload&#39;">payload</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Mar '15, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/0af0895267b2e7e4fbee7bf27ecfaff7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rosensama&#39;s gravatar image" /><p><span>rosensama</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rosensama has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Mar '15, 07:55</strong> </span></p></div></div><div id="comments-container-40289" class="comments-container"><span id="40323"></span><div id="comment-40323" class="comment"><div id="post-40323-score" class="comment-score"></div><div class="comment-text"><p>What I think I want is my protocol dissector to include a .DecodedMessage field.</p></div><div id="comment-40323-info" class="comment-info"><span class="comment-age">(06 Mar '15, 05:11)</span> <span class="comment-user userinfo">rosensama</span></div></div></div><div id="comment-tools-40289" class="comment-tools"></div><div class="clear"></div><div id="comment-40289-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40311"></span>

<div id="answer-container-40311" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40311-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40311-score" class="post-score" title="current number of votes">0</div><span id="post-40311-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can do it in two steps.</p><blockquote><p>tshark -R "tcp contains SEK" -2 -r 2015-03-04.pcap -T fields -e tcp.stream</p></blockquote><p>Take the stream numbers from the output and run the following command:</p><p>ASCII:</p><blockquote><p>tshark -nr 2015-03-04.pcap -q -z follow,tcp,ascii,xxxxx<br />
</p></blockquote><p>Hex:</p><blockquote><p>tshark -nr 2015-03-04.pcap -q -z follow,tcp,hex,xxxxx<br />
</p></blockquote><p>Please replace xxxxx with the tcp stream number.</p><p>Obviously you can automate the whole process with a script.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '15, 16:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-40311" class="comments-container"><span id="40321"></span><div id="comment-40321" class="comment"><div id="post-40321-score" class="comment-score"></div><div class="comment-text"><p>Thanks. This does work in spirit as the second step does return the ASCII decoded payload. Unfortunately, I have long lived streams and while I can find the handful of packets I'm interested in the in first step, but then the second step returns far more packets (100,000's) than I'm interested in.</p></div><div id="comment-40321-info" class="comment-info"><span class="comment-age">(06 Mar '15, 05:00)</span> <span class="comment-user userinfo">rosensama</span></div></div></div><div id="comment-tools-40311" class="comment-tools"></div><div class="clear"></div><div id="comment-40311-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

