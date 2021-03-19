+++
type = "question"
title = "How to filter data by Capture Filter"
description = '''Hi, I would like to know who login on application and I see that by fltering the port 1100 and I have this type of line : 192.168.101.xxx 192.168.101.10 TCP 55482 &amp;gt; mctp [PSH, ACK] Seq=1352 Ack=195886 Win=65656 Len=163 But there are too many lines with this filter I need to filter data for this s...'''
date = "2012-12-11T07:51:00Z"
lastmod = "2012-12-14T10:41:00Z"
weight = 16769
keywords = [ "filter", "capture" ]
aliases = [ "/questions/16769" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to filter data by Capture Filter](/questions/16769/how-to-filter-data-by-capture-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16769-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16769-score" class="post-score" title="current number of votes">0</div><span id="post-16769-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I would like to know who login on application and I see that by fltering the port 1100 and I have this type of line : 192.168.101.xxx 192.168.101.10 TCP 55482 &gt; mctp [PSH, ACK] Seq=1352 Ack=195886 Win=65656 Len=163 But there are too many lines with this filter I need to filter data for this string "LoginData" but not after, during the capture, to not have too much lines (270Mb for one hour, and I want to make statistics on one month).</p><p>Thx in advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Dec '12, 07:51</strong></p><img src="https://secure.gravatar.com/avatar/ef55146a212a7ddc4d0dd965278ed663?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pheslot&#39;s gravatar image" /><p><span>Pheslot</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pheslot has no accepted answers">0%</span></p></div></div><div id="comments-container-16769" class="comments-container"></div><div id="comment-tools-16769" class="comment-tools"></div><div class="clear"></div><div id="comment-16769-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="16772"></span>

<div id="answer-container-16772" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16772-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16772-score" class="post-score" title="current number of votes">2</div><span id="post-16772-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Capture filters are based on BPF and are executed in kernel space for speed. BPF is a sort of virtual machine with a limited instruction set. To optimize for speed and to make sure it is impossible to end up in an infinite loop, there is no way in BPF to search for a specific string in the whole packet. It can only look for strings at specific offsets.</p><p>So unless the string "LoginData" is always at the same offset in a packet, there is no way to do this with BPF.</p><p>However, if the string "LoginData" is always at the start of the packet, the following packet-filter might just be your friend :-)</p><pre><code>tcp[0:4]=0x4c6f6769 and tcp[4:4]=0x6e446174 and tcp[8:1]=0x61</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Dec '12, 10:28</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-16772" class="comments-container"><span id="16790"></span><div id="comment-16790" class="comment"><div id="post-16790-score" class="comment-score"></div><div class="comment-text"><p>Hi SYN-bit,</p><p>Thank you but I'm not very familiar with that, what I can tell you it is that the whole packet is like that :</p><p><img src="https://osqa-ask.wireshark.org/upfiles/cs.JPG" alt="alt text" /></p></div><div id="comment-16790-info" class="comment-info"><span class="comment-age">(12 Dec '12, 01:51)</span> <span class="comment-user userinfo">Pheslot</span></div></div><span id="16855"></span><div id="comment-16855" class="comment"><div id="post-16855-score" class="comment-score"></div><div class="comment-text"><p>In this frame, the string LoginData starts at offset 0x006a. Since the packet looks like binary data (and not html for instance), it might just be that the string LoginData always starts at this offset. The filter would then become:</p><pre><code>tcp[0x6a:4]=0x4c6f6769 and tcp[0x6e:4]=0x6e446174 and tcp[0x72:1]=0x61</code></pre></div><div id="comment-16855-info" class="comment-info"><span class="comment-age">(13 Dec '12, 15:28)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-16772" class="comment-tools"></div><div class="clear"></div><div id="comment-16772-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16905"></span>

<div id="answer-container-16905" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16905-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16905-score" class="post-score" title="current number of votes">0</div><span id="post-16905-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I suggest to check ngrep.</p><blockquote><p><code>http://ngrep.sourceforge.net/usage.html</code><br />
</p></blockquote><p>This tools allows to search for strings in IP packets and if it finds the string, it will dump the content of the packet.</p><p>It does work on Linux and it should work on Windows.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '12, 10:41</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Dec '12, 10:47</strong> </span></p></div></div><div id="comments-container-16905" class="comments-container"></div><div id="comment-tools-16905" class="comment-tools"></div><div class="clear"></div><div id="comment-16905-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

