+++
type = "question"
title = "How to find the connection type of a network from Wireshark trace?"
description = '''I&#x27;m doing some analysis on a wireshark network trace. How to find the connection type of the underlying network? (eg: wireless) Is it possible to obtain this information from packet analysis? Thanks in advance. Lasith.'''
date = "2013-09-07T07:21:00Z"
lastmod = "2013-09-09T06:04:00Z"
weight = 24442
keywords = [ "lan", "packet", "wireshark" ]
aliases = [ "/questions/24442" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to find the connection type of a network from Wireshark trace?](/questions/24442/how-to-find-the-connection-type-of-a-network-from-wireshark-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24442-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24442-score" class="post-score" title="current number of votes">0</div><span id="post-24442-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm doing some analysis on a wireshark network trace. How to find the connection type of the underlying network? (eg: wireless)</p><p>Is it possible to obtain this information from packet analysis?</p><p>Thanks in advance.</p><p>Lasith.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lan" rel="tag" title="see questions tagged &#39;lan&#39;">lan</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Sep '13, 07:21</strong></p><img src="https://secure.gravatar.com/avatar/b45da046cc88ee70f4ce6da77b44c137?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lasith%20Eranda%20Haputhanthiri&#39;s gravatar image" /><p><span>Lasith Erand...</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lasith Eranda Haputhanthiri has no accepted answers">0%</span></p></div></div><div id="comments-container-24442" class="comments-container"></div><div id="comment-tools-24442" class="comment-tools"></div><div class="clear"></div><div id="comment-24442-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24443"></span>

<div id="answer-container-24443" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24443-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24443-score" class="post-score" title="current number of votes">0</div><span id="post-24443-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could take a look at the lowest layer you find in the trace - if there's a 802.11 radio layer it's most certainly wireless. If there's an Ethernet layer, it's (in most cases) Ethernet. If there's TokenRing, it's TokenRing.</p><p>But you can also take a look at the Summary option in the Statistics menu, and look at the "Encapsulation" that is mentioned.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '13, 07:41</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-24443" class="comments-container"><span id="24444"></span><div id="comment-24444" class="comment"><div id="post-24444-score" class="comment-score"></div><div class="comment-text"><p>From your comments I was able to find that packets are sent through Ethernet. But my network connection is a wireless one. How can I distinguish whether the network is wired or wireless?</p></div><div id="comment-24444-info" class="comment-info"><span class="comment-age">(07 Sep '13, 07:52)</span> <span class="comment-user userinfo">Lasith Erand...</span></div></div><span id="24445"></span><div id="comment-24445" class="comment"><div id="post-24445-score" class="comment-score"></div><div class="comment-text"><p>If you captured the frames on Windows and did not use the AirPCAP adapter you will only be able to capture from Ethernet layer up, and it will look like it was just an wired Ethernet trace. I'm not sure if there is any way to tell from that kind of trace that it was actually a wireless connection - maybe if you saved the file in PCAPng format you can tell from the interface name that is also mentioned in the Statistics, but that once again won't help on Windows (because it is using GUIDs that won't tell you much unless you have access to the PC the trace was captured on)</p></div><div id="comment-24445-info" class="comment-info"><span class="comment-age">(07 Sep '13, 08:10)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="24451"></span><div id="comment-24451" class="comment"><div id="post-24451-score" class="comment-score"></div><div class="comment-text"><blockquote><p>If you captured the frames on Windows and did not use the AirPCAP adapter you will only be able to capture from Ethernet layer up, and it will look like it was just an wired Ethernet trace.</p></blockquote><p>The same also applies on most UN*Xes if you're not capturing in monitor mode.</p></div><div id="comment-24451-info" class="comment-info"><span class="comment-age">(07 Sep '13, 13:35)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="24452"></span><div id="comment-24452" class="comment"><div id="post-24452-score" class="comment-score"></div><div class="comment-text"><p>So you'd either have to look for protocols used by Wi-Fi devices (e.g., by access points) or look for something such as packet loss patterns that are more likely on Wi-Fi than Ethernet. (I don't have any suggestions to make for either of those cases.)</p></div><div id="comment-24452-info" class="comment-info"><span class="comment-age">(07 Sep '13, 13:40)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="24476"></span><div id="comment-24476" class="comment"><div id="post-24476-score" class="comment-score"></div><div class="comment-text"><blockquote><p>From your comments I was able to find that packets are sent through Ethernet. But my network connection is a wireless one. How can I distinguish whether the network is wired or wireless?</p></blockquote><p>How did you capture the wifi traffic?</p><ul><li>Tools (Wireshark, etc.)</li><li>OS (brand, version)</li></ul></div><div id="comment-24476-info" class="comment-info"><span class="comment-age">(09 Sep '13, 06:04)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-24443" class="comment-tools"></div><div class="clear"></div><div id="comment-24443-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

