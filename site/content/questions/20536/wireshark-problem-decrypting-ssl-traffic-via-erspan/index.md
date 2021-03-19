+++
type = "question"
title = "Wireshark - Problem Decrypting SSL Traffic via ERSPAN"
description = '''Hi experts,  I have a question regarding Wireshark ability to decrypt SSL traffic via ERSPAN. We have ERSPAN mirroring session from our web server A to another server B. Our software on server B seems to have problem decrypting some of the traffic being mirrored from server A. Packet captures were c...'''
date = "2013-04-17T17:21:00Z"
lastmod = "2013-04-18T17:28:00Z"
weight = 20536
keywords = [ "ssl", "wireshark", "erspan" ]
aliases = [ "/questions/20536" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark - Problem Decrypting SSL Traffic via ERSPAN](/questions/20536/wireshark-problem-decrypting-ssl-traffic-via-erspan)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20536-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20536-score" class="post-score" title="current number of votes">0</div><span id="post-20536-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi experts,</p><p>I have a question regarding Wireshark ability to decrypt SSL traffic via ERSPAN.</p><p>We have ERSPAN mirroring session from our web server A to another server B. Our software on server B seems to have problem decrypting some of the traffic being mirrored from server A. Packet captures were conducted on both servers to determine root cause.</p><p>On Server A, I can see a full handshake with Client Key Exchange frame, and the subsequent traffic is decrypted as HTTP.</p><p>However on server B, the Client Key Exchange frame (#2386) was marked as [TCP Previous segment not captured] and [TCP segment of a reassembled PDU], in turn, this wasn't showned as Client Key Exchange step and wireshark was not able to decrypt the application data. Additionally, this frame is also marked as [Reassembled PDU in frame 2389], so it seems that the traffic arrived later but it wasn't pieced together to form Client Key Exchange.</p><p>Could anyone suggest any ideas why Wireshark is not able to reconstruct a Client Key Exchange step on server B?</p><p>Does this highlight a problem with the network? Or is it a problem with wireshark not being able to reconstruct out of order SSL traffic via ERSPAN. I can provide more details if needed.</p><p>Also, I tried to linked in a few screenshots from dropbox for illustration but my post were marked as spam and could not be publicized.</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-erspan" rel="tag" title="see questions tagged &#39;erspan&#39;">erspan</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Apr '13, 17:21</strong></p><img src="https://secure.gravatar.com/avatar/7a9ec956724ee0b1b98585eeaa3a94db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="huandn&#39;s gravatar image" /><p><span>huandn</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="huandn has no accepted answers">0%</span></p></div></div><div id="comments-container-20536" class="comments-container"></div><div id="comment-tools-20536" class="comment-tools"></div><div class="clear"></div><div id="comment-20536-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20548"></span>

<div id="answer-container-20548" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20548-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20548-score" class="post-score" title="current number of votes">1</div><span id="post-20548-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>SSL decryption does not really like out-of-order packets in the SSL handshake. If you really need to decrypt the traffic, you might need to manually reorder the packets by using editcap. This would take the following steps:</p><ol><li>extract frame 2386: <code>editcap -r &lt;file&gt; frame2386.pcap 2386</code></li><li>save the remaining file : <code>editcap &lt;file&gt; otherframes.pcap 2386</code></li><li>adjust the timestamp of frame 2386: <code>editcap -d &lt;timediff&gt; frame2386.pcap frame2386-new.pcap</code></li><li>merge to a new file: <code>mergecap -w &lt;newfile&gt; otherframes.pcap frame2386-new.pcap</code></li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '13, 00:03</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-20548" class="comments-container"><span id="20605"></span><div id="comment-20605" class="comment"><div id="post-20605-score" class="comment-score"></div><div class="comment-text"><p>Thanks very much for your answer. It was spot on.</p><p>We have a sniffing probe that inspect packets continuously and de-crypt them for analysis. We would need traffic to be decrypted all the time and not just in this instance.</p><p>Do we need to resolve the network TCP out of order problem first? Or whether our software have to be able to reorder packets before trying to decrypt them.</p></div><div id="comment-20605-info" class="comment-info"><span class="comment-age">(18 Apr '13, 17:28)</span> <span class="comment-user userinfo">huandn</span></div></div></div><div id="comment-tools-20548" class="comment-tools"></div><div class="clear"></div><div id="comment-20548-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

