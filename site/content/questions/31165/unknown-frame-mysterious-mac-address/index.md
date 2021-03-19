+++
type = "question"
title = "Unknown Frame - mysterious mac address"
description = '''We are having some strange activity on the network, with intermittent slowing down.  Wireshark scans produce multiple results from the same source: Ethernet II, Src: fe:80:00:00:00:00 (fe:80:00:00:00:00), Dst: 59:de:e6:c9:98:55 (59:de:e6:c9:98:55) Any initial thoughts?'''
date = "2014-03-26T02:59:00Z"
lastmod = "2014-03-26T10:44:00Z"
weight = 31165
keywords = [ "unknown", "frame" ]
aliases = [ "/questions/31165" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unknown Frame - mysterious mac address](/questions/31165/unknown-frame-mysterious-mac-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31165-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31165-score" class="post-score" title="current number of votes">0</div><span id="post-31165-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are having some strange activity on the network, with intermittent slowing down. Wireshark scans produce multiple results from the same source:</p><p>Ethernet II, Src: fe:80:00:00:00:00 (fe:80:00:00:00:00), Dst: 59:de:e6:c9:98:55 (59:de:e6:c9:98:55)</p><p>Any initial thoughts?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-unknown" rel="tag" title="see questions tagged &#39;unknown&#39;">unknown</span> <span class="post-tag tag-link-frame" rel="tag" title="see questions tagged &#39;frame&#39;">frame</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Mar '14, 02:59</strong></p><img src="https://secure.gravatar.com/avatar/384473fce26892c23ec2e215ad8fc8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bl33pcode&#39;s gravatar image" /><p><span>bl33pcode</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bl33pcode has no accepted answers">0%</span></p></div></div><div id="comments-container-31165" class="comments-container"></div><div id="comment-tools-31165" class="comment-tools"></div><div class="clear"></div><div id="comment-31165-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31184"></span>

<div id="answer-container-31184" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31184-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31184-score" class="post-score" title="current number of votes">0</div><span id="post-31184-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Neither of those addresses are well known addresses, so it could be</p><ul><li>some special config in your local network setup, you don't know of</li><li>a broken device (switch, NIC, etc.) that just sends bogus frames and hence the unknown MAC addresses</li><li>someone playing tricks with you, like a local use who is 'testing' hacker tools</li></ul><p>Please check the switch logs and <a href="http://en.wikipedia.org/wiki/CAM_Table">CAM table</a> of your switches to figure out the switch port where the sending device is attached to the switch. Wireshark won't be able to help you, unless you see some clear text messages in the frames that help to identify the sending device.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Mar '14, 09:02</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Mar '14, 09:03</strong> </span></p></div></div><div id="comments-container-31184" class="comments-container"><span id="31190"></span><div id="comment-31190" class="comment"><div id="post-31190-score" class="comment-score"></div><div class="comment-text"><p>Yeah, we can't identify the mac address atm.</p><p>will check the switches.</p></div><div id="comment-31190-info" class="comment-info"><span class="comment-age">(26 Mar '14, 09:24)</span> <span class="comment-user userinfo">bl33pcode</span></div></div><span id="31198"></span><div id="comment-31198" class="comment"><div id="post-31198-score" class="comment-score"></div><div class="comment-text"><p>Don't forget to look at the content (payload) of the frames!</p><p>Is it possible to post a sample on <a href="http://cloudshark.org">http://cloudshark.org</a> ?</p></div><div id="comment-31198-info" class="comment-info"><span class="comment-age">(26 Mar '14, 10:44)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-31184" class="comment-tools"></div><div class="clear"></div><div id="comment-31184-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

