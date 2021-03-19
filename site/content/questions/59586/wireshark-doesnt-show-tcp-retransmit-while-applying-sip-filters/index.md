+++
type = "question"
title = "Wireshark doesn&#x27;t show TCP retransmit while applying SIP filters ?"
description = '''Hey guys I am troubleshooting a voice call and I applied a SIP CallID filter, the problem is that I don&#x27;t see the TCP retransmit anymore in my capture for that specific call ... I have a friend that has Wireshark 1.10.5 and it is working for him but I am on the newer version and it does not show the...'''
date = "2017-02-21T09:10:00Z"
lastmod = "2017-03-17T05:50:00Z"
weight = 59586
keywords = [ "filter" ]
aliases = [ "/questions/59586" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark doesn't show TCP retransmit while applying SIP filters ?](/questions/59586/wireshark-doesnt-show-tcp-retransmit-while-applying-sip-filters)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59586-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59586-score" class="post-score" title="current number of votes">1</div><span id="post-59586-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey guys</p><p>I am troubleshooting a voice call and I applied a SIP CallID filter, the problem is that I don't see the TCP retransmit anymore in my capture for that specific call ...</p><p>I have a friend that has Wireshark 1.10.5 and it is working for him but I am on the newer version and it does not show the TCP retransmit .</p><p>Anyone has any hint to give me? :)</p><p>Thanks</p><p>vPackets</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Feb '17, 09:10</strong></p><img src="https://secure.gravatar.com/avatar/ce2a5532bb18a30f9dbf7462ec9a27f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vPackets&#39;s gravatar image" /><p><span>vPackets</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vPackets has no accepted answers">0%</span></p></div></div><div id="comments-container-59586" class="comments-container"></div><div id="comment-tools-59586" class="comment-tools"></div><div class="clear"></div><div id="comment-59586-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59588"></span>

<div id="answer-container-59588" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59588-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59588-score" class="post-score" title="current number of votes">1</div><span id="post-59588-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>By default in recent versions of Wireshark the TCP dissector does not pass "error" packets (such as retransmissions) to upper layer dissectors. This is because these error packets tend to confuse the upper-layer protocol dissectors (because they see the same data more than once).</p><p>If you want the old functionality back you can disable the TCP preference <code>Do not call subdissectors for error packets</code>. But you may be better off simply adding something like <code>|| tcp.analysis.retransmission</code> to your filter.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Feb '17, 10:50</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-59588" class="comments-container"><span id="59595"></span><div id="comment-59595" class="comment"><div id="post-59595-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot.</p><p>The problem with || tcp.analysis.retransmission is that it will add ALL the TCP retransmit I had during that capture ... not the specific ones for my SIP.CallID .</p><p>Nic</p></div><div id="comment-59595-info" class="comment-info"><span class="comment-age">(21 Feb '17, 23:14)</span> <span class="comment-user userinfo">vPackets</span></div></div><span id="59602"></span><div id="comment-59602" class="comment"><div id="post-59602-score" class="comment-score"></div><div class="comment-text"><p>True enough.</p><p>On a side note if my answer answers your question please be sure to Accept the answer (by clicking on the checkmark next to it). This is a Q&amp;A site, not a forum--see the FAQ.</p></div><div id="comment-59602-info" class="comment-info"><span class="comment-age">(22 Feb '17, 05:24)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="59677"></span><div id="comment-59677" class="comment"><div id="post-59677-score" class="comment-score"></div><div class="comment-text"><p>So Is there a way to filter a call and the specific TCP retransmit I had for that call ?</p><p>I tried SIP Call ID AND TCP.analysis.retransmission but without any luck :(</p><p>Thanks to let me know</p><p>Nic</p></div><div id="comment-59677-info" class="comment-info"><span class="comment-age">(24 Feb '17, 22:34)</span> <span class="comment-user userinfo">vPackets</span></div></div><span id="59707"></span><div id="comment-59707" class="comment"><div id="post-59707-score" class="comment-score"></div><div class="comment-text"><p>I think for that you'll need to disable the <code>Do not call subdissectors for error packets</code> preference (and even that's not going to be perfect; if the retransmitted segment doesn't include the Call ID then it won't be caught). AFAIK that's about as good as it's going to get (unless you can filter on something else like the TCP stream number or something).</p></div><div id="comment-59707-info" class="comment-info"><span class="comment-age">(27 Feb '17, 05:59)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="60044"></span><div id="comment-60044" class="comment"><div id="post-60044-score" class="comment-score"></div><div class="comment-text"><p>Hey Jeff !</p><p>Looks like I got the same results using your advice :(</p><p>Do you think of something else or should I downgrade to Wireshark 1.x ?</p><p>Thanks !</p></div><div id="comment-60044-info" class="comment-info"><span class="comment-age">(13 Mar '17, 21:09)</span> <span class="comment-user userinfo">vPackets</span></div></div><span id="60151"></span><div id="comment-60151" class="comment not_top_scorer"><div id="post-60151-score" class="comment-score"></div><div class="comment-text"><p>Sorry, which advice (we talked about a couple different options)? The one that should get you back to the old behavior is disabling the <code>Do not call subdissectors for error packets</code> option. It would be interesting to know if the behavior isn't the same.</p><p>Are there non-SIP fields you can filter on once you have the call isolated (e.g., IP addresses and ports)?</p></div><div id="comment-60151-info" class="comment-info"><span class="comment-age">(17 Mar '17, 05:50)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-59588" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-59588-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

