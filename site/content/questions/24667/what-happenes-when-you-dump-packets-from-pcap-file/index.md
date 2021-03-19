+++
type = "question"
title = "What happenes when you dump packets from .pcap file ?"
description = '''i have .pcap file having total 3471 packets , after doing mpeg-ts dump (listener in lua script) it have 5033 packets.. in my output.pcap file can anyone explain this please ?'''
date = "2013-09-13T22:31:00Z"
lastmod = "2013-09-15T12:31:00Z"
weight = 24667
keywords = [ "dump" ]
aliases = [ "/questions/24667" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What happenes when you dump packets from .pcap file ?](/questions/24667/what-happenes-when-you-dump-packets-from-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24667-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24667-score" class="post-score" title="current number of votes">0</div><span id="post-24667-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i have .pcap file having total <strong>3471 packets</strong> , after doing <strong>mpeg-ts dump</strong> (listener in lua script) it have <strong>5033 packets..</strong> in my output.pcap file can anyone explain this please ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dump" rel="tag" title="see questions tagged &#39;dump&#39;">dump</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Sep '13, 22:31</strong></p><img src="https://secure.gravatar.com/avatar/e48354c5d3611f0840dc4f3f0acc2641?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pvv&#39;s gravatar image" /><p><span>pvv</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pvv has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Sep '13, 02:33</strong> </span></p></div></div><div id="comments-container-24667" class="comments-container"><span id="24669"></span><div id="comment-24669" class="comment"><div id="post-24669-score" class="comment-score"></div><div class="comment-text"><p>Sorry, but you need to explain in more detail what you did. This sounds like some kind of packet replay and capture szenario. What setup was used, and how did you capture?</p></div><div id="comment-24669-info" class="comment-info"><span class="comment-age">(14 Sep '13, 02:30)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="24686"></span><div id="comment-24686" class="comment"><div id="post-24686-score" class="comment-score"></div><div class="comment-text"><p>Thank you mr. jasper for replying</p><p>i am sorry for posting this simple silly question</p><p>actually in original file there were 719 MP2T packets,each 1358 bytes</p><p>and in output file each packet is of 188 bytes (1358/188 =7 ) that means 719 * 7 = 5033 packets</p></div><div id="comment-24686-info" class="comment-info"><span class="comment-age">(14 Sep '13, 10:44)</span> <span class="comment-user userinfo">pvv</span></div></div></div><div id="comment-tools-24667" class="comment-tools"></div><div class="clear"></div><div id="comment-24667-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24670"></span>

<div id="answer-container-24670" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24670-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24670-score" class="post-score" title="current number of votes">0</div><span id="post-24670-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Enter the file where the mpeg stream should be saved.<br />
</p></blockquote><p>according to the <a href="http://wiki.wireshark.org/mpeg_dump.lua?action=AttachFile&amp;do=view&amp;target=mpeg_packets_dump.lua">Lua code</a>:</p><blockquote><p>Enter the file where the <strong>mpeg stream</strong> should be saved.</p></blockquote><p>So, it's the binary MPEG stream, contained in the frames.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '13, 04:18</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Sep '13, 04:18</strong> </span></p></div></div><div id="comments-container-24670" class="comments-container"><span id="24685"></span><div id="comment-24685" class="comment"><div id="post-24685-score" class="comment-score"></div><div class="comment-text"><p>Oh Thank you So much Mr kurt knochner for replying</p><p>i am sorry for posting this simple silly question</p><p>actually in original file there were 719 MP2T packets,each 1358 bytes</p><p>and in output file each packet is of 188 bytes (1358/188 =7 ) that means 719 * 7 = 5033 packets</p></div><div id="comment-24685-info" class="comment-info"><span class="comment-age">(14 Sep '13, 10:42)</span> <span class="comment-user userinfo">pvv</span></div></div><span id="24720"></span><div id="comment-24720" class="comment"><div id="post-24720-score" class="comment-score"></div><div class="comment-text"><p>I would need to have access to your capture file to be able to analyze what's going on. Is it possible to post the capture file somewhere (google drive, dropbox, etc.)?</p></div><div id="comment-24720-info" class="comment-info"><span class="comment-age">(15 Sep '13, 12:31)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-24670" class="comment-tools"></div><div class="clear"></div><div id="comment-24670-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

