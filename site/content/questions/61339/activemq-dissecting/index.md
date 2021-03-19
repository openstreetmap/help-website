+++
type = "question"
title = "ActiveMQ dissecting"
description = '''Hi All, The following tells me that Wireshark can dissect OpenWire at least since 2012: http://activemq.2283324.n4.nabble.com/Wireshark-packet-dissection-Openwire-td4631635.html , however I&#x27;m unable to get it to dissect my ActiveMQ trace for some reason when I choose &quot;Decode As... OpenWire&quot;: https:/...'''
date = "2017-05-10T08:23:00Z"
lastmod = "2017-05-11T12:15:00Z"
weight = 61339
keywords = [ "activemq" ]
aliases = [ "/questions/61339" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ActiveMQ dissecting](/questions/61339/activemq-dissecting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61339-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61339-score" class="post-score" title="current number of votes">0</div><span id="post-61339-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>The following tells me that Wireshark can dissect OpenWire at least since 2012: <a href="http://activemq.2283324.n4.nabble.com/Wireshark-packet-dissection-Openwire-td4631635.html">http://activemq.2283324.n4.nabble.com/Wireshark-packet-dissection-Openwire-td4631635.html</a></p><p>, however I'm unable to get it to dissect my ActiveMQ trace for some reason when I choose "Decode As... OpenWire": <a href="https://drive.google.com/open?id=0B31e47Ucqt4BOXJrSTEwMi1OdWc">https://drive.google.com/open?id=0B31e47Ucqt4BOXJrSTEwMi1OdWc</a></p><p>I also tried "Decode As... AMQP", still no luck. Packet bytes view of some packets in the trace suggests it's ActiveMQ (which I think is different from AMQP though).</p><p>Is there a way to get Wireshark to dissect my trace anyway?</p><p>Many thanks in advance,</p><p>Dmitriy</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-activemq" rel="tag" title="see questions tagged &#39;activemq&#39;">activemq</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 May '17, 08:23</strong></p><img src="https://secure.gravatar.com/avatar/4c43e04f0ef8eacb2a3173436cb432f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dmitriy&#39;s gravatar image" /><p><span>Dmitriy</span><br />
<span class="score" title="21 reputation points">21</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dmitriy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 May '17, 08:31</strong> </span></p></div></div><div id="comments-container-61339" class="comments-container"></div><div id="comment-tools-61339" class="comment-tools"></div><div class="clear"></div><div id="comment-61339-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61340"></span>

<div id="answer-container-61340" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61340-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61340-score" class="post-score" title="current number of votes">1</div><span id="post-61340-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The protocol in use is <a href="http://stomp.github.io/">STOMP</a>, for which Wireshark doesn't currently have a dissector.</p><p>As it's a text based protocol you can see the text lines in the "Data" part of the dissector tree, or see the conversation by right clicking a packet in the list and selecting Follow -&gt; TCP Stream.</p><p>If you want to see STOMP dissection added to Wireshark, please raise an enhancement request on the <a href="https://bugs.wireshark.org">Wireshark Bugzilla</a>, attaching your capture file to the request.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 May '17, 08:55</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-61340" class="comments-container"><span id="61341"></span><div id="comment-61341" class="comment"><div id="post-61341-score" class="comment-score"></div><div class="comment-text"><p>Thank you: trying to restore my access to Wireshark Bugzilla to raise it there as you advised.</p></div><div id="comment-61341-info" class="comment-info"><span class="comment-age">(10 May '17, 12:43)</span> <span class="comment-user userinfo">Dmitriy</span></div></div><span id="61355"></span><div id="comment-61355" class="comment"><div id="post-61355-score" class="comment-score"></div><div class="comment-text"><p>Done: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13695">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13695</a></p></div><div id="comment-61355-info" class="comment-info"><span class="comment-age">(11 May '17, 08:45)</span> <span class="comment-user userinfo">Dmitriy</span></div></div><span id="61358"></span><div id="comment-61358" class="comment"><div id="post-61358-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-61358-info" class="comment-info"><span class="comment-age">(11 May '17, 12:15)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-61340" class="comment-tools"></div><div class="clear"></div><div id="comment-61340-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

