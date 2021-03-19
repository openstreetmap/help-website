+++
type = "question"
title = "stream number for udp"
description = '''i want to ask the wireshark developers if there is any plan to add the udp stream numbers like we have for tcp streams. and was there any specific reason to use stream numbers only for tcp ?'''
date = "2012-11-17T00:15:00Z"
lastmod = "2012-11-20T01:25:00Z"
weight = 15999
keywords = [ "tshark", "wireshark" ]
aliases = [ "/questions/15999" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [stream number for udp](/questions/15999/stream-number-for-udp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15999-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15999-score" class="post-score" title="current number of votes">0</div><span id="post-15999-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i want to ask the wireshark developers if there is any plan to add the udp stream numbers like we have for tcp streams. and was there any specific reason to use stream numbers only for tcp ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Nov '12, 00:15</strong></p><img src="https://secure.gravatar.com/avatar/ce14610470a60c9adcc5f03599f66608?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="viks&#39;s gravatar image" /><p><span>viks</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="viks has no accepted answers">0%</span></p></div></div><div id="comments-container-15999" class="comments-container"></div><div id="comment-tools-15999" class="comment-tools"></div><div class="clear"></div><div id="comment-15999-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16007"></span>

<div id="answer-container-16007" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16007-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16007-score" class="post-score" title="current number of votes">0</div><span id="post-16007-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Since TCP is a connection orientated protocol with a distinctive session start and end, it is possible to determine which session/stream a packet belongs to by looking at the TCP headers alone.</p><p>UDP is a connectionless protocol, which means every packet is basically on its own. Only the upper layer protocols can determine whether a packet belongs to a certain session.</p><p>One thing that could be done is link UDP packets into a stream if they are less than a (configurable) timeout apart. But that might give funny results for some protocols.</p><p>Any particular reason you need this functionality?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Nov '12, 05:01</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-16007" class="comments-container"><span id="16080"></span><div id="comment-16080" class="comment"><div id="post-16080-score" class="comment-score"></div><div class="comment-text"><p>i am not able to get you when you say that to link udp pkts into a stream we can choose a configurable timeout value. why at all we need to do that when we can link udp (or even tcp)packets into a stream based on the 5 tuple ? one reason is the equivalence between tcp &amp; udp where we will have a stream no for each tcp or udp flow as shown by wireshark. other is writing scripts using tshark using various filters where udp.stream can also serve purpose in several scenarios like tcp.stream.</p></div><div id="comment-16080-info" class="comment-info"><span class="comment-age">(19 Nov '12, 11:27)</span> <span class="comment-user userinfo">viks</span></div></div><span id="16088"></span><div id="comment-16088" class="comment"><div id="post-16088-score" class="comment-score"></div><div class="comment-text"><p>Maybe the answers at <a href="http://stackoverflow.com/questions/658654/streams-and-udp">Streams and UDP</a> will provide some additional clarity.</p></div><div id="comment-16088-info" class="comment-info"><span class="comment-age">(19 Nov '12, 14:15)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="16098"></span><div id="comment-16098" class="comment"><div id="post-16098-score" class="comment-score"></div><div class="comment-text"><p>Many UDP protocols use the same 5-tuple for different streams. With TCP, they are separated by the closure of the first stream (FIN/ACK, ACK,FIN/ACK,ACK) and the creation of a new stream (SYN,SYN/ACK,ACK).</p><p>In UDP there is no session boundary at the UDP layer, the only way to differentiate between two UDP streams with the same 5-tuple would be to use a timeout and assume that when two packets with the same 5-tuple have a time difference larger than the timeout, they would belong to two different streams. I think streams for UDP can better be defined at the higher layer protocols on top of UDP.</p></div><div id="comment-16098-info" class="comment-info"><span class="comment-age">(20 Nov '12, 01:25)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-16007" class="comment-tools"></div><div class="clear"></div><div id="comment-16007-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

