+++
type = "question"
title = "How to detect TOR usage with Wireshark?"
description = '''I use TOR inside a Virtual Machine. I run Wireshark on my Host. I want to detect TOR usage (for learning/studying) with Wireshark but don&#x27;t know how. I&#x27;ve tried this: https://ask.wireshark.org/questions/13590/tor-detection but tshark output doesn&#x27;t show any cert names. Are there any other ways to ac...'''
date = "2014-11-29T02:56:00Z"
lastmod = "2014-12-04T07:51:00Z"
weight = 38234
keywords = [ "monitor" ]
aliases = [ "/questions/38234" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to detect TOR usage with Wireshark?](/questions/38234/how-to-detect-tor-usage-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38234-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38234-score" class="post-score" title="current number of votes">0</div><span id="post-38234-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I use TOR inside a Virtual Machine. I run Wireshark on my Host. I want to detect TOR usage (for learning/studying) with Wireshark but don't know how. I've tried this:</p><p><a href="https://ask.wireshark.org/questions/13590/tor-detection">https://ask.wireshark.org/questions/13590/tor-detection</a></p><p>but tshark output doesn't show any cert names. Are there any other ways to accomplish this task?</p><p><strong>Edit: reply to Kurt Knochner</strong></p><p>This is what I did:</p><pre><code>sudo wireshark</code></pre><p>Then I choose wan0 interface and basically start live capturing. I use Tor on my Virtual Machine and after decent amount of time I save the log to file.pcapng</p><p>Next according to your method I do:</p><pre><code>tshark -r file.pcapng -T fields -R &quot;ssl.handshake.certificate&quot; -e x509af.utcTime -e x509s</code></pre><p>Output:</p><pre><code>tshark: -R without -2 is deprecated. For single-pass filtering use -Y.
$</code></pre><p>And that's it, no certificates found. I also converted file.pcapng to file.pcap and ran the command again without luck. What am I doing wrong?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-monitor" rel="tag" title="see questions tagged &#39;monitor&#39;">monitor</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Nov '14, 02:56</strong></p><img src="https://secure.gravatar.com/avatar/ff212c191b452e1ed49f5f5cc1a29a1f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="student1111&#39;s gravatar image" /><p><span>student1111</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="student1111 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Dec '14, 07:50</strong> </span></p></div></div><div id="comments-container-38234" class="comments-container"></div><div id="comment-tools-38234" class="comment-tools"></div><div class="clear"></div><div id="comment-38234-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38265"></span>

<div id="answer-container-38265" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38265-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38265-score" class="post-score" title="current number of votes">0</div><span id="post-38265-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>but tshark output doesn't show any cert names. Are there any other ways to accomplish this task?</p></blockquote><p>apparently it does work in my example, as shown in my answer to the question you mentioned.</p><p>So, you either did not capture SSL/TLS handshake traffic or there is a problem with the way you ran tshark. As you neither provided the tshark command nor the capture file, it's kind of hard/impossible to help you!</p><p>Please add the information I mentioned (tshark command, pcap file).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Dec '14, 17:00</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-38265" class="comments-container"><span id="38331"></span><div id="comment-38331" class="comment"><div id="post-38331-score" class="comment-score"></div><div class="comment-text"><p>Question updated with details you asked for</p></div><div id="comment-38331-info" class="comment-info"><span class="comment-age">(04 Dec '14, 07:51)</span> <span class="comment-user userinfo">student1111</span></div></div></div><div id="comment-tools-38265" class="comment-tools"></div><div class="clear"></div><div id="comment-38265-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

