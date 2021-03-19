+++
type = "question"
title = "Capture traffic from Riverbed steelhead"
description = '''We were trying to establish a connection from Oracle Client to Oracle Server through Riverbed Steelhead but not working when we use optimization, but it worked again when it come to Pass-Through mode. '''
date = "2015-09-23T08:14:00Z"
lastmod = "2015-09-24T15:27:00Z"
weight = 46077
keywords = [ "oracle", "rivedbed" ]
aliases = [ "/questions/46077" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture traffic from Riverbed steelhead](/questions/46077/capture-traffic-from-riverbed-steelhead)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46077-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46077-score" class="post-score" title="current number of votes">0</div><span id="post-46077-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We were trying to establish a connection from Oracle Client to Oracle Server through Riverbed Steelhead but not working when we use optimization, but it worked again when it come to Pass-Through mode.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture_O5dLGLD.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-oracle" rel="tag" title="see questions tagged &#39;oracle&#39;">oracle</span> <span class="post-tag tag-link-rivedbed" rel="tag" title="see questions tagged &#39;rivedbed&#39;">rivedbed</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Sep '15, 08:14</strong></p><img src="https://secure.gravatar.com/avatar/959a02c0a2a8c18f34b5f043501da0af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="monsterlazy&#39;s gravatar image" /><p><span>monsterlazy</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="monsterlazy has no accepted answers">0%</span></p></img></div></div><div id="comments-container-46077" class="comments-container"><span id="46080"></span><div id="comment-46080" class="comment"><div id="post-46080-score" class="comment-score"></div><div class="comment-text"><p>Could you share the tracefile? Or could you provide us a screenshot without relative sequence numbers?</p></div><div id="comment-46080-info" class="comment-info"><span class="comment-age">(23 Sep '15, 10:14)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="46081"></span><div id="comment-46081" class="comment"><div id="post-46081-score" class="comment-score"></div><div class="comment-text"><p>Hi, Christian_R Thank you for you attention. we would like share more information as below,</p><p>This is set pass-through :: <a href="https://www.cloudshark.org/captures/27b963dbe093">https://www.cloudshark.org/captures/27b963dbe093</a></p><p>This is set optimization :: <a href="https://www.cloudshark.org/captures/f09fee92db1b">https://www.cloudshark.org/captures/f09fee92db1b</a></p></div><div id="comment-46081-info" class="comment-info"><span class="comment-age">(23 Sep '15, 10:57)</span> <span class="comment-user userinfo">monsterlazy</span></div></div></div><div id="comment-tools-46077" class="comment-tools"></div><div class="clear"></div><div id="comment-46077-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46089"></span>

<div id="answer-container-46089" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46089-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46089-score" class="post-score" title="current number of votes">0</div><span id="post-46089-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don´t know exactly where the trace has been taken. But in the trace untaged and tagged frames can be seen.</p><p>In the Riverbed Optimize trace I can see the following behaviour: Frame #2 has been sent from Riverbed device to Cisco device. But with Frame #7 the Riverbed device talks directly with the F5 device.</p><p>This is different to the other trace.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Sep '15, 13:16</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div></div><div id="comments-container-46089" class="comments-container"><span id="46091"></span><div id="comment-46091" class="comment"><div id="post-46091-score" class="comment-score"></div><div class="comment-text"><p>Hi, Christian_R We would like to share Network Diagrams Server-&gt;F5-&gt;Riverbed-&gt;CiscoRouter&lt;---&gt;CiscoRouter&lt;-Riverbed&lt;-CiscoFirewall&lt;-F5&lt;-Server</p></div><div id="comment-46091-info" class="comment-info"><span class="comment-age">(23 Sep '15, 22:04)</span> <span class="comment-user userinfo">monsterlazy</span></div></div><span id="46129"></span><div id="comment-46129" class="comment"><div id="post-46129-score" class="comment-score"></div><div class="comment-text"><p>I think the Frame #6 didn´t make it to the other host. But why? If I where you I would analyze if the MAC addresses we see in the trace are really correct.<img src="https://osqa-ask.wireshark.org/upfiles/Unbenannt.JPG" alt="alt text" /></p></div><div id="comment-46129-info" class="comment-info"><span class="comment-age">(24 Sep '15, 15:27)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-46089" class="comment-tools"></div><div class="clear"></div><div id="comment-46089-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

