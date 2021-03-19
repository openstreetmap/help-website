+++
type = "question"
title = "How to use Wireshark to analyze QoS"
description = '''How can I use Wireshark to analyze the data coming into the network and to determine where the network is not supporting the required QoS? Also, how can I use Wireshark to tell when the QoS I/O queue is full (and any other information about the queue)? How are packets assigned to that queue?'''
date = "2011-10-13T21:19:00Z"
lastmod = "2011-10-17T04:56:00Z"
weight = 6884
keywords = [ "qos", "analysis" ]
aliases = [ "/questions/6884" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to use Wireshark to analyze QoS](/questions/6884/how-to-use-wireshark-to-analyze-qos)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6884-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6884-score" class="post-score" title="current number of votes">0</div><span id="post-6884-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I use Wireshark to analyze the data coming into the network and to determine where the network is not supporting the required QoS? Also, how can I use Wireshark to tell when the QoS I/O queue is full (and any other information about the queue)? How are packets assigned to that queue?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-qos" rel="tag" title="see questions tagged &#39;qos&#39;">qos</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Oct '11, 21:19</strong></p><img src="https://secure.gravatar.com/avatar/53e0fbfa9e08dce2dca9d7288877bac6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iti&#39;s gravatar image" /><p><span>iti</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iti has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Oct '11, 11:13</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6884" class="comments-container"></div><div id="comment-tools-6884" class="comment-tools"></div><div class="clear"></div><div id="comment-6884-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="6917"></span>

<div id="answer-container-6917" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6917-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6917-score" class="post-score" title="current number of votes">2</div><span id="post-6917-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark can't actually give you a direct view into what is going on in a network device like a router or switch. (So you can't see internal entities like queues or buffers or routing tables). It can only capture traffic as it passes a particular point in monitoring. However from that viewpoint, you can obviously infer a lot. The easiest way to think of it is to imagine you a standing on a bridge above an expressway, just before the crest of a hill so you can't see what is happening further down the road. If a traffic accident occurs further ahead you won't know for sure, but you might see traffic slowing down as it goes past. Or you might see ambulances coming back in the opposite direction. All of these things are indicators to what might be going on.</p><p>Similarly with Wireshark you can see if packets are being slowed in the throughput rate (using the graphs or round trip times and the like) and you can also see things like DiffServ marks in packets, dropped packets (or at least ones that are missing), retries and so on.</p><p>But as Jaap has intimated to be able to correctly understand what you are seeing (in terms of observed behaviour) you need to gain some experience or at least some grounding in knowledge, as to how network devices, hosts (and even black boxes) respond the conditions in the network.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '11, 04:38</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p><span>martyvis</span><br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-6917" class="comments-container"></div><div id="comment-tools-6917" class="comment-tools"></div><div class="clear"></div><div id="comment-6917-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6885"></span>

<div id="answer-container-6885" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6885-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6885-score" class="post-score" title="current number of votes">0</div><span id="post-6885-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You'll need to look into some serious training here. Join <a href="http://www.wiresharktraining.com/">Wireshark University</a> to learn of network analysis. Get your <a href="http://www.cisco.com/web/learning/le3/le2/le0/le9/learning_certification_type_home.html">CCNA</a> / <a href="http://www.cisco.com/web/learning/le3/le2/le37/le10/learning_certification_type_home.html">CCNP</a> to get on your networking gear.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Oct '11, 23:34</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-6885" class="comments-container"><span id="6901"></span><div id="comment-6901" class="comment"><div id="post-6901-score" class="comment-score"></div><div class="comment-text"><p>Do Wireshark University provide job called WCNA after the exam?</p></div><div id="comment-6901-info" class="comment-info"><span class="comment-age">(14 Oct '11, 23:01)</span> <span class="comment-user userinfo">Terrestrial ...</span></div></div><span id="6907"></span><div id="comment-6907" class="comment"><div id="post-6907-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your suggestion....but I want to knw "how to do that instead of doing any training".</p></div><div id="comment-6907-info" class="comment-info"><span class="comment-age">(16 Oct '11, 05:45)</span> <span class="comment-user userinfo">iti</span></div></div><span id="6908"></span><div id="comment-6908" class="comment"><div id="post-6908-score" class="comment-score"></div><div class="comment-text"><p>Dive into free online resources. Like the <a href="http://www.wireshark.org/docs/wsug_html_chunked/">Wireshark Users Guide</a>, or any other resources listed on the <a href="http://www.wireshark.org/docs/">Learn Wireshark page</a>. Then there's the <a href="http://wiki.wireshark.org/NetworkTroubleshooting">Wiki</a>, with a <a href="http://wiki.wireshark.org/Presentations">presentation overview</a>. Furthermore there is the <a href="http://www.tcpipguide.com/free/index.htm">TCP/IP Guide</a>. Enough to keep you busy for a while.</p></div><div id="comment-6908-info" class="comment-info"><span class="comment-age">(16 Oct '11, 07:44)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-6885" class="comment-tools"></div><div class="clear"></div><div id="comment-6885-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6918"></span>

<div id="answer-container-6918" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6918-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6918-score" class="post-score" title="current number of votes">0</div><span id="post-6918-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks frds, I'll try.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '11, 04:56</strong></p><img src="https://secure.gravatar.com/avatar/53e0fbfa9e08dce2dca9d7288877bac6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iti&#39;s gravatar image" /><p><span>iti</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iti has no accepted answers">0%</span></p></div></div><div id="comments-container-6918" class="comments-container"></div><div id="comment-tools-6918" class="comment-tools"></div><div class="clear"></div><div id="comment-6918-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

