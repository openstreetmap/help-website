+++
type = "question"
title = "In a Profinet network sometimes the dataexchange messages are shown in the wrong order."
description = '''In a Profinet data exchange there is cyclecounter field. If you substract the previous cyclecounter from the current cyclecounter and you multiply it with 31.25 micro seconds you will get the cycletime of an IO-device. We have seen that there is a chance that the data exchange message are shown in w...'''
date = "2015-11-23T10:40:00Z"
lastmod = "2015-11-24T10:07:00Z"
weight = 47876
keywords = [ "pnio" ]
aliases = [ "/questions/47876" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [In a Profinet network sometimes the dataexchange messages are shown in the wrong order.](/questions/47876/in-a-profinet-network-sometimes-the-dataexchange-messages-are-shown-in-the-wrong-order)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47876-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47876-score" class="post-score" title="current number of votes">0</div><span id="post-47876-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In a Profinet data exchange there is cyclecounter field. If you substract the previous cyclecounter from the current cyclecounter and you multiply it with 31.25 micro seconds you will get the cycletime of an IO-device. We have seen that there is a chance that the data exchange message are shown in wireshark in de wrong order. If you look at the cyclecounters of the Profinet data exchange messages it 100% sure that messages are shown in de wrong order. A profinet data exchange has a Vlan pdiority of 6.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pnio" rel="tag" title="see questions tagged &#39;pnio&#39;">pnio</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Nov '15, 10:40</strong></p><img src="https://secure.gravatar.com/avatar/db610391310e46836abe17d89ecf1730?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="edwarddumay&#39;s gravatar image" /><p><span>edwarddumay</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="edwarddumay has no accepted answers">0%</span></p></div></div><div id="comments-container-47876" class="comments-container"></div><div id="comment-tools-47876" class="comment-tools"></div><div class="clear"></div><div id="comment-47876-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47880"></span>

<div id="answer-container-47880" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47880-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47880-score" class="post-score" title="current number of votes">2</div><span id="post-47880-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Shown in the wrong order or captured in the wrong order? Wireshark simply shows that frames as collected in the capture file. How this is done depends on how the capture files is created.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '15, 11:23</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-47880" class="comments-container"><span id="47886"></span><div id="comment-47886" class="comment"><div id="post-47886-score" class="comment-score"></div><div class="comment-text"><p>The messages between the PLC and the switch are mirrored to the mirrorport of that switch. The IO-device is connected to another port of the switch. Wireshark captures the messages from the mirrorport of the switch</p></div><div id="comment-47886-info" class="comment-info"><span class="comment-age">(23 Nov '15, 12:16)</span> <span class="comment-user userinfo">edwarddumay</span></div></div><span id="47909"></span><div id="comment-47909" class="comment"><div id="post-47909-score" class="comment-score"></div><div class="comment-text"><p>So, does the mirror port guarantee message order?</p></div><div id="comment-47909-info" class="comment-info"><span class="comment-age">(24 Nov '15, 01:40)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="47932"></span><div id="comment-47932" class="comment"><div id="post-47932-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jaap. Normaly the mirrorport keeps the messages in the right order. I have to ask the manufactuer of the switch if they can guarantee the message order on the mirrorport.</p></div><div id="comment-47932-info" class="comment-info"><span class="comment-age">(24 Nov '15, 10:07)</span> <span class="comment-user userinfo">edwarddumay</span></div></div></div><div id="comment-tools-47880" class="comment-tools"></div><div class="clear"></div><div id="comment-47880-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

