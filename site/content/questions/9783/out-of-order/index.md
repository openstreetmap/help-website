+++
type = "question"
title = "OUT-OF-ORDER"
description = '''13 0.000000 10.151.19.21 10.151.17.21 TCP 1518 [TCP Out-Of-Order] 59988 &amp;gt; vnetd [ACK] Seq=1 Ack=1 Win=65535 Len=1460  我怎么样才能解决这个问题？ how to solve this problem?'''
date = "2012-03-27T01:58:00Z"
lastmod = "2012-04-08T09:29:00Z"
weight = 9783
keywords = [ "out-of-order" ]
aliases = [ "/questions/9783" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [OUT-OF-ORDER](/questions/9783/out-of-order)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9783-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9783-score" class="post-score" title="current number of votes">0</div><span id="post-9783-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>13 0.000000 10.151.19.21 10.151.17.21 TCP 1518 [TCP Out-Of-Order] 59988 &gt; vnetd [ACK] Seq=1 Ack=1 Win=65535 Len=1460 <img src="http://img170.poco.cn/mypoco/myphoto/20120327/16/6470392820120327165255033.png" alt="alt text" /> 我怎么样才能解决这个问题？ how to solve this problem?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-out-of-order" rel="tag" title="see questions tagged &#39;out-of-order&#39;">out-of-order</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Mar '12, 01:58</strong></p><img src="https://secure.gravatar.com/avatar/098a04795ad589f49fd02b9c9e7ccab6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wtycc&#39;s gravatar image" /><p><span>wtycc</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wtycc has no accepted answers">0%</span></p></img></div></div><div id="comments-container-9783" class="comments-container"></div><div id="comment-tools-9783" class="comment-tools"></div><div class="clear"></div><div id="comment-9783-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9798"></span>

<div id="answer-container-9798" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9798-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9798-score" class="post-score" title="current number of votes">1</div><span id="post-9798-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your screenshot is showing a strange trace. First of all, you only seem to have captured one direction of the communication, from IP 10.151.19.21 to 10.151.17.21. So we don't know what the IP 10.151.17.21 sends back. But that is not the biggest problem.</p><p>In frame 5, the (relative) Sequence number starts at 1 and goes up by 1460 bytes, as expected. There's a packet loss before frame 8, where Sequence 4381 should have been - but we see 5841 instead. So one segment is missing, and Wireshark is correct about the "TCP Previous Segment Lost". So far it's all pretty normal.</p><p>The really strange thing happens in frame 11: suddenly the Sequence jumps (well, not a tiny jump, but more of a long range interstellar teleport) to 4294964377 (when it should have been a mere relative number of 10221). Something went really wrong here, and I doubt it's Wiresharks fault - more likely the packet got corrupted somehow, or the capture setup was faulty - especially since the following frame 12 has a correct sequence number of 11681 (10221 + 1460).</p><p>Anyway, after frame 11 Wireshark seems a bit confused because huge amounts of data seem to be missing, which is probably why you get all the "Out-Of-Order" messages. Since we don't know what the other side replied we cannot tell what happened after , but it looks like the communication is started again at Sequence 1 in frame 13. Another very funny thing happens in frame 15 - suddenly we see an ACK number that is the same as the bogus sequence number in frame 11.</p><p><strong>Final verdict:</strong> your capture process didn't work well, and it looks like your captured data was kind of garbled. Forget about the Wireshark expert messages like "Out-Of-Order" and try to capture with a better capture device - it's not worth putting thought into analyzing this mess. I bet you didn't capture this on a PC but probably locally on a Netscreen firewall. Problem is that it didn't even bother to either capture both directions, much less write proper timestamps (which is always 0 in your trace) or good sequence numbers.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '12, 15:02</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Mar '12, 15:05</strong> </span></p></div></div><div id="comments-container-9798" class="comments-container"><span id="9803"></span><div id="comment-9803" class="comment"><div id="post-9803-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your answer.The first week of my two servers traffic is 2T, the second week of traffic up to 8T, the third week of traffic up to 13T, always feel some unusual stuff in there, but still have not found what reason, I will work to try to use theWireshark to solve some things, but not progress.Anyway, Thank you for your selfless assistance.</p></div><div id="comment-9803-info" class="comment-info"><span class="comment-age">(27 Mar '12, 18:22)</span> <span class="comment-user userinfo">wtycc</span></div></div><span id="9806"></span><div id="comment-9806" class="comment"><div id="post-9806-score" class="comment-score">1</div><div class="comment-text"><p>13T? You mean 13 Terabyte of data between the servers in a week? What are you trying to solve? The screenshot you provided indicated that you're looking for some kind of connection trouble or slow performance. If you're really looking for what causes that much traffic you're better of using the statistics menu, for example the conversion statistics. It will tell you what IP has how many connections and the number of packets/bytes/bps. By looking at the port numbers you should be able to match it to applications on the server.</p></div><div id="comment-9806-info" class="comment-info"><span class="comment-age">(28 Mar '12, 03:08)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="9955"></span><div id="comment-9955" class="comment"><div id="post-9955-score" class="comment-score"></div><div class="comment-text"><p>I come from China, my English is too poor,Can you help me to analysis under my packet, I put it in my blog below <a href="http://www.wtycc.com/airsea/1921.zip">http://www.wtycc.com/airsea/1921.zip</a> Thank you very much and look forward to your reply. You are a good man .</p></div><div id="comment-9955-info" class="comment-info"><span class="comment-age">(05 Apr '12, 02:31)</span> <span class="comment-user userinfo">wtycc</span></div></div><span id="10013"></span><div id="comment-10013" class="comment"><div id="post-10013-score" class="comment-score"></div><div class="comment-text"><p>Sorry, I couldn't get a look sooner. Now having the trace file I see why your sequence numbers look crazy on your screenshot. The huge jump in frame 11 isn't that huge, it's just going backwards beyond the relative zero sequence (which can happen when Wireshark didn't see the three way handshake).</p><p>Without having spent too much time on the trace I can tell you this: the line you captured on is so busy that you had tons of drops (packets that were there but didn't get captured because the capture device was too slow). You'll need to find a better way to capture your data I'm afraid, because with a capture file like this you can't really tell what happened (or if anything bad happened at all). You can still do some statistics on a file like this, but it won't be 100% accurate.</p></div><div id="comment-10013-info" class="comment-info"><span class="comment-age">(08 Apr '12, 06:17)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-9798" class="comment-tools"></div><div class="clear"></div><div id="comment-9798-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10014"></span>

<div id="answer-container-10014" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10014-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10014-score" class="post-score" title="current number of votes">1</div><span id="post-10014-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This appears to be server backup traffic, and data flow in only one direction. TCP port 13724 is used by Veritas/Symantec.</p><p>In our network, we normally filter out port 13724 traffic, when we take traces. Unless we are dealing with backup issue, and we truncate packets to make it easier for wireshark to capture.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '12, 09:29</strong></p><img src="https://secure.gravatar.com/avatar/f24e48940d8b97fd56789ed422038a0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CKC&#39;s gravatar image" /><p><span>CKC</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CKC has no accepted answers">0%</span></p></div></div><div id="comments-container-10014" class="comments-container"></div><div id="comment-tools-10014" class="comment-tools"></div><div class="clear"></div><div id="comment-10014-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

