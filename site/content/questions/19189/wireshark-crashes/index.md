+++
type = "question"
title = "wireshark crashes"
description = '''Hello, I am trying to perform FAST decoding in 32-bit wireshark on linux and the size of the pcap file is about 1.2MB (20,000 packets). I start decoding and I am able to decode part of the file but wireshark suddenly crashes and gets closed. As I used to be able to decode 100,000 packets and I am us...'''
date = "2013-03-05T14:37:00Z"
lastmod = "2013-03-06T14:20:00Z"
weight = 19189
keywords = [ "crash", "wireshak" ]
aliases = [ "/questions/19189" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark crashes](/questions/19189/wireshark-crashes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19189-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19189-score" class="post-score" title="current number of votes">0</div><span id="post-19189-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am trying to perform FAST decoding in 32-bit wireshark on linux and the size of the pcap file is about 1.2MB (20,000 packets). I start decoding and I am able to decode part of the file but wireshark suddenly crashes and gets closed. As I used to be able to decode 100,000 packets and I am using the same machine and wireshark version, I am wondering what might be problem. I would appreciate if anyone could help me.</p><p>Thanks, Farhad</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span> <span class="post-tag tag-link-wireshak" rel="tag" title="see questions tagged &#39;wireshak&#39;">wireshak</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Mar '13, 14:37</strong></p><img src="https://secure.gravatar.com/avatar/023ec4b0dfece2e93187a50ec2fee0d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fhaghigh&#39;s gravatar image" /><p><span>fhaghigh</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fhaghigh has no accepted answers">0%</span></p></div></div><div id="comments-container-19189" class="comments-container"></div><div id="comment-tools-19189" class="comment-tools"></div><div class="clear"></div><div id="comment-19189-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19190"></span>

<div id="answer-container-19190" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19190-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19190-score" class="post-score" title="current number of votes">0</div><span id="post-19190-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It sounds like some specific data in the pcap is causuing Wireshark to crash.</p><p>Can you file a bug report at bugs.wireshark.org and attach the capture file causing the crash ? (see below)</p><p>(If necessary, you can mark the bug as private so that only the Wireshark core developers will be able to examine the capture file).</p><p>Note: you may find it useful to "bisect" the file to find the frame(s) causing the error.</p><p>You can use the command line tool editcap (part of the Wireshark package) to do this.</p><p>See 'editcap -h"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '13, 15:19</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Mar '13, 15:20</strong> </span></p></div></div><div id="comments-container-19190" class="comments-container"><span id="19212"></span><div id="comment-19212" class="comment"><div id="post-19212-score" class="comment-score"></div><div class="comment-text"><p>Thanks for you answer. I will post in bugs.wireshark.org.</p></div><div id="comment-19212-info" class="comment-info"><span class="comment-age">(06 Mar '13, 06:20)</span> <span class="comment-user userinfo">fhaghigh</span></div></div></div><div id="comment-tools-19190" class="comment-tools"></div><div class="clear"></div><div id="comment-19190-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19191"></span>

<div id="answer-container-19191" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19191-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19191-score" class="post-score" title="current number of votes">0</div><span id="post-19191-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>as discussed in <a href="http://ask.wireshark.org/questions/18785/problem-with-dissecting-a-large-pcap-file-as-fast">your other FAST question</a>, that dissector is an 'external' plugin and not part of Wireshark. There could be a bug in that plugin which causes Wireshark to crash. It's best to contact the developers of that plugin and ask for help.</p><p>If you are able to post the capture file (google docs, dropbox, etc.), someone here may (or may not) be able to help you.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '13, 15:22</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Mar '13, 15:22</strong> </span></p></div></div><div id="comments-container-19191" class="comments-container"><span id="19213"></span><div id="comment-19213" class="comment"><div id="post-19213-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure if it's because of the plugin. Could it because of wireshark running out of memory? I run it on a server and my guess is that it runs out of memory when many processes are running.</p></div><div id="comment-19213-info" class="comment-info"><span class="comment-age">(06 Mar '13, 06:22)</span> <span class="comment-user userinfo">fhaghigh</span></div></div><span id="19214"></span><div id="comment-19214" class="comment"><div id="post-19214-score" class="comment-score"></div><div class="comment-text"><p>hard to say without access to the capture file.... As you say it works with 100.000 packets but it does <strong>not</strong> work with 20.000 packets, I don't believe it's a memory problem.</p></div><div id="comment-19214-info" class="comment-info"><span class="comment-age">(06 Mar '13, 06:32)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="19215"></span><div id="comment-19215" class="comment"><div id="post-19215-score" class="comment-score"></div><div class="comment-text"><p>I just asked and unfortunately I cannot share the capture file. The reason i was suspicious about the memory is that last time I decoded 100,000 packets I was the only user using the server.</p></div><div id="comment-19215-info" class="comment-info"><span class="comment-age">(06 Mar '13, 06:38)</span> <span class="comment-user userinfo">fhaghigh</span></div></div><span id="19221"></span><div id="comment-19221" class="comment"><div id="post-19221-score" class="comment-score"></div><div class="comment-text"><blockquote><p>unfortunately I cannot share the capture file.</p></blockquote><p>well, then I guess it will be hard to troubleshoot the issue externally.</p></div><div id="comment-19221-info" class="comment-info"><span class="comment-age">(06 Mar '13, 08:08)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="19247"></span><div id="comment-19247" class="comment"><div id="post-19247-score" class="comment-score"></div><div class="comment-text"><p>I found out the problem! there are packets inside the capture file that don't contain any stop bit, so the dissector crashes on them. It wasn't wireshark! Thanks for all the helps.</p></div><div id="comment-19247-info" class="comment-info"><span class="comment-age">(06 Mar '13, 14:20)</span> <span class="comment-user userinfo">fhaghigh</span></div></div></div><div id="comment-tools-19191" class="comment-tools"></div><div class="clear"></div><div id="comment-19191-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

