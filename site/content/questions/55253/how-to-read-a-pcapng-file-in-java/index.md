+++
type = "question"
title = "[closed] How to read a .pcapng file in Java"
description = '''Hi,  I am trying to read a .pcapng file in Java to perform dissection. Basically I want to read the hex values present in the packet. So I wanted to know if there is any way to do so. I saw some libraries for Java listed on wikipedia as mentioned in other questions but it is not working for me. Henc...'''
date = "2016-08-31T13:53:00Z"
lastmod = "2016-08-31T23:03:00Z"
weight = 55253
keywords = [ "pcapng", "java", "dissector", "wireshark" ]
aliases = [ "/questions/55253" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] How to read a .pcapng file in Java](/questions/55253/how-to-read-a-pcapng-file-in-java)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55253-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55253-score" class="post-score" title="current number of votes">0</div><span id="post-55253-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am trying to read a .pcapng file in Java to perform dissection. Basically I want to read the hex values present in the packet. So I wanted to know if there is any way to do so. I saw some libraries for Java listed on wikipedia as mentioned in other questions but it is not working for me. Hence please let me know if there is any way to do this.</p><p>Thanks, Shobhit Garg.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcapng" rel="tag" title="see questions tagged &#39;pcapng&#39;">pcapng</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Aug '16, 13:53</strong></p><img src="https://secure.gravatar.com/avatar/3aaad26a48e6f507d8f9137404269a46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shobhit_garg91&#39;s gravatar image" /><p><span>shobhit_garg91</span><br />
<span class="score" title="16 reputation points">16</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shobhit_garg91 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> closed <strong>31 Aug '16, 23:10</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-55253" class="comments-container"></div><div id="comment-tools-55253" class="comment-tools"></div><div class="clear"></div><div id="comment-55253-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by Jaap 31 Aug '16, 23:10

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55259"></span>

<div id="answer-container-55259" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55259-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55259-score" class="post-score" title="current number of votes">0</div><span id="post-55259-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How to read a .pcapng file in Java</p></blockquote><p>If you have a library for Java that is a wrapper for libpcap, rather than a library that has its own capture file reading code, and if you're running on a system with libpcap 1.1 or later - or, on Windows, if you have Npcap rather than WinPcap installed - the file should be able to read pcapng files where all interfaces have the same link-layer header type and snapshot length.</p><p>It looks as if <a href="http://jnetpcap.com">jNetPcap</a> is a libpcap wrapper - they say it contains "A Java wrapper for nearly all libpcap library native calls". <a href="https://github.com/kaitoy/pcap4j">Pcap4j</a> also appears to be a wrapper.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Aug '16, 20:34</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-55259" class="comments-container"><span id="55260"></span><div id="comment-55260" class="comment"><div id="post-55260-score" class="comment-score"></div><div class="comment-text"><p>Hi Guy, Thanks for your inputs. Actually my project involves taking a binary capture file and dissecting the first few layers of the packet. Since pcapng is a binary file in itself, I am just trying to read the file in java byte by byte and trying to dissect it. The issue that I am facing is that I am able to get the byte values but those are getting converted to integer (read decimal). Also the byte values that start with an alphabet (from a to f) are subtracted by 256 and then displayed, while the byte values that start with a number are just converted to binary and then displayed. Please let me know if anything can be done in this regards.</p></div><div id="comment-55260-info" class="comment-info"><span class="comment-age">(31 Aug '16, 20:54)</span> <span class="comment-user userinfo">shobhit_garg91</span></div></div><span id="55262"></span><div id="comment-55262" class="comment"><div id="post-55262-score" class="comment-score"></div><div class="comment-text"><p>That's a Java programming question and has nothing to do with Wireshark.</p></div><div id="comment-55262-info" class="comment-info"><span class="comment-age">(31 Aug '16, 23:03)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-55259" class="comment-tools"></div><div class="clear"></div><div id="comment-55259-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

