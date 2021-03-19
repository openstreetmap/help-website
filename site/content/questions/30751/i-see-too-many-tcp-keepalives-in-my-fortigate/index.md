+++
type = "question"
title = "I see too many Tcp keepalives in my fortigate"
description = '''Hi I believe I have a problem with my fortigate firewall, I&#x27;m receiving too many tcp keep alive. I already talk about this, with my ISP provider. What I told him to do, was to increase the ttl session. An it did improve. But I believe he change it again, and know I&#x27;m seen other problems and I didn&#x27;t...'''
date = "2014-03-12T20:04:00Z"
lastmod = "2014-03-16T15:31:00Z"
weight = 30751
keywords = [ "anacaro" ]
aliases = [ "/questions/30751" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [I see too many Tcp keepalives in my fortigate](/questions/30751/i-see-too-many-tcp-keepalives-in-my-fortigate)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30751-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30751-score" class="post-score" title="current number of votes">0</div><span id="post-30751-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I believe I have a problem with my fortigate firewall, I'm receiving too many tcp keep alive. I already talk about this, with my ISP provider. What I told him to do, was to increase the ttl session. An it did improve. But I believe he change it again, and know I'm seen other problems and I didn't have before. Like a lot Tcp out of order like 3 o 4 in a row, as well as TCP ACK Duplicates. What could be the problem??????????</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-anacaro" rel="tag" title="see questions tagged &#39;anacaro&#39;">anacaro</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Mar '14, 20:04</strong></p><img src="https://secure.gravatar.com/avatar/cde8e77e3e71294edfcbf3d1dd923afd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Caro&#39;s gravatar image" /><p><span>Caro</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Caro has no accepted answers">0%</span></p></div></div><div id="comments-container-30751" class="comments-container"></div><div id="comment-tools-30751" class="comment-tools"></div><div class="clear"></div><div id="comment-30751-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="30810"></span>

<div id="answer-container-30810" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30810-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30810-score" class="post-score" title="current number of votes">2</div><span id="post-30810-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Tcp_keepalive packets are sent when connections are idle. Their purpose is to generate traffic that would cause a firewall to see activity on the session, reset its inactivity timer and keep the 5-tuple in the connectino table. The interval between keepalive packets can be configured but should be less than 5 minutes which is a common default in FWs to drop idle connections.</p><p>When you see <strong>too many</strong> keep alive packets the reason is probably that you have <strong>too many</strong> idle TCP connections going through your firewall. I don't know why you consider this as a <strong>problem</strong> because the result is the end users will be happy to remain in the connection table instead of seeing ECONNRESET errors on the socket.</p><p>As you are posting this problem here to the wireshark QA I assume you have a trace showing this scenario. This will help you identify</p><ol><li>How many unique TCP connections you have</li><li>What the keep_alive intervals are</li><li>Whether a single IP address is misbehaving in sending keep-alives too often</li></ol><p>So you apply the filter <strong><code>tcp.analysis.keep_alive_ack or tcp.analysis.keep_alive</code></strong> to the trace file, open the Statistics -&gt; Conversations panel, navigate to the TCP tab and check the 'limit to display filter' box. <img src="https://osqa-ask.wireshark.org/upfiles/Selection_186.png" alt="alt text" /></p><hr /><p>I don't see what an ISP could do about this and don't know what you are referring to when told them to <strong><em>increase the ttl session</em></strong>. Can you explain more what you recommended them to do?</p><p>The TCP out of order and duplicate acks should not be a problem, IP packets happen to arrive out-of-order, as Roland mentioned, and TCP will take care of it. For as long as you don't see <strong>too many</strong> retransmissions this is nothing to be concerned about.</p><hr /><p>If you have questions on this <em>seperate</em> issue, please raise another <em>seperate</em> Question in order to not mixed up things here.<br />
</p><hr /></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '14, 05:24</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></img></div></div><div id="comments-container-30810" class="comments-container"><span id="30865"></span><div id="comment-30865" class="comment"><div id="post-30865-score" class="comment-score"></div><div class="comment-text"><p>Caro, you may want to mention what has cause you to look at detailed traffic analysis. Is there a user or application indicated issue you are trying to troubleshoot? As meEede has indicated keepalives serve a purpose and on are not necessary indicating a problem. Also out of order packets are quite normal if you have load-balanced links, either at your end or even as traffic travels through and away from your ISP</p></div><div id="comment-30865-info" class="comment-info"><span class="comment-age">(16 Mar '14, 15:31)</span> <span class="comment-user userinfo">martyvis</span></div></div></div><div id="comment-tools-30810" class="comment-tools"></div><div class="clear"></div><div id="comment-30810-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30800"></span>

<div id="answer-container-30800" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30800-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30800-score" class="post-score" title="current number of votes">0</div><span id="post-30800-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>One reason for the tcp out of order packets could be asymmetric routing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Mar '14, 06:54</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p><span>Roland</span><br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-30800" class="comments-container"></div><div id="comment-tools-30800" class="comment-tools"></div><div class="clear"></div><div id="comment-30800-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

