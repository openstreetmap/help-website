+++
type = "question"
title = "How does Wireshark reassemble TCP Segments"
description = '''I am dealing with a packet capture that has two TCP packets that are re-assembled TCP. How can wireshark associate the two packets together? I am talking about TCP re-assembly, not IP header fragment offset usage to identify reassembly. In fact the IP header ID&#x27;s are not even in sequence. I am curio...'''
date = "2012-09-14T15:06:00Z"
lastmod = "2014-09-16T05:23:00Z"
weight = 14280
keywords = [ "reassembly", "tcp" ]
aliases = [ "/questions/14280" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How does Wireshark reassemble TCP Segments](/questions/14280/how-does-wireshark-reassemble-tcp-segments)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14280-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14280-score" class="post-score" title="current number of votes">0</div><span id="post-14280-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I am dealing with a packet capture that has two TCP packets that are re-assembled TCP. How can wireshark associate the two packets together? I am talking about TCP re-assembly, <strong>not IP header</strong> fragment offset usage to identify reassembly. In fact the IP header ID's are not even in sequence. I am curious how Wireshark can associate the two packets correctly when there are no identifiable correlation between the two packets?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reassembly" rel="tag" title="see questions tagged &#39;reassembly&#39;">reassembly</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Sep '12, 15:06</strong></p><img src="https://secure.gravatar.com/avatar/f20d4c6238a54f0bcf89eb2c02334acd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Erik&#39;s gravatar image" /><p><span>Erik</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Erik has no accepted answers">0%</span></p></div></div><div id="comments-container-14280" class="comments-container"></div><div id="comment-tools-14280" class="comment-tools"></div><div class="clear"></div><div id="comment-14280-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="14287"></span>

<div id="answer-container-14287" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14287-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14287-score" class="post-score" title="current number of votes">2</div><span id="post-14287-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are two parts in reassembling higher layer PDU's that are transported over TCP.</p><p>First of all (as Jasper mentioned) TCP uses sequence numbers to be able to re-order packets if they arrive out-of-order and also to resend segments that might have been dropped.</p><p>Secondly, the higher layer protocol must know how much data it is expecting. This is necessary for the higher layer protocols as TCP is providing a stream of data, so the protocol needs to know how to split the stream into PDU's.</p><p>The wireshark dissectors that perform TCP reassembly also know where the bounderies between PDU's are and in that way mimic the protocol.</p><p>As an example, the HTTP protocol has a few ways of identifying when an object has been completely transmitted.</p><ul><li>The HTTP header is terminated by a "CR/LF CR/LF" sequence, so the HTTP dissector will tell the TCP dissector to collect more data until it has a "CR/LF CR/LF" in it's data (and so a full HTTP header PDU)</li><li>In HTTP/1.0 without "Connection: Keep-Alive", each object is simply sent as data until the server sends a FIN. Wireshark will do the same and the HTTP dissector will tell the TCP dissector to collect more data until it sees the FIN. It then has the full HTTP body PDU</li><li>When "Connection: Keep-Alive" is used, there is a "Content-Length: xxx" line in the HTTP header. The HTTP dissector will keep asking the TCP to collect more data until it has xxx bytes of data and it knows it has collected the whole HTTP body PDU.</li></ul><p>Other protocols work the same way. They know how much data they need to collect and they tell the TCP dissector to keep re-assembling the data until they see a full PDU.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '12, 23:44</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-14287" class="comments-container"></div><div id="comment-tools-14287" class="comment-tools"></div><div class="clear"></div><div id="comment-14287-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14281"></span>

<div id="answer-container-14281" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14281-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14281-score" class="post-score" title="current number of votes">0</div><span id="post-14281-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>simple (well, in theory :-)) TCP uses sequence numbers to be able to reassemble the packets in the correct order on the receiving side, and that's what Wireshark does, too. So yes, there is a correlation, it is the TCP sequence number you can see in the TCP header decodes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '12, 15:47</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-14281" class="comments-container"><span id="14283"></span><div id="comment-14283" class="comment"><div id="post-14283-score" class="comment-score"></div><div class="comment-text"><p>I do not believe it uses only that. As there are multiple packets that contain the same ack number, that do not form the entire reassembled packet. Wireshark obviously identified that they did not belong within the reassembled packet.</p></div><div id="comment-14283-info" class="comment-info"><span class="comment-age">(14 Sep '12, 16:09)</span> <span class="comment-user userinfo">Erik</span></div></div><span id="14293"></span><div id="comment-14293" class="comment"><div id="post-14293-score" class="comment-score"></div><div class="comment-text"><p>The ACK number is only used to signal what packets have been successfully received, and isn't used for reassembling incoming packet contents. Sequence numbers are incoming, ACK numbers are outgoing and are related to the other nodes' sequence numbering.</p></div><div id="comment-14293-info" class="comment-info"><span class="comment-age">(15 Sep '12, 03:49)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-14281" class="comment-tools"></div><div class="clear"></div><div id="comment-14281-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="36360"></span>

<div id="answer-container-36360" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36360-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36360-score" class="post-score" title="current number of votes">0</div><span id="post-36360-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>TCP sequence number is used for reassembling packets. There is also a Stream Index which helps in identifying that these packets are part of the same stream.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '14, 05:23</strong></p><img src="https://secure.gravatar.com/avatar/7953ad2cbdf8a2e2f07eddd90262db99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Qazi&#39;s gravatar image" /><p><span>Qazi</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Qazi has no accepted answers">0%</span></p></div></div><div id="comments-container-36360" class="comments-container"></div><div id="comment-tools-36360" class="comment-tools"></div><div class="clear"></div><div id="comment-36360-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

