+++
type = "question"
title = "Monitor packet losses using Wireshark"
description = '''I&#x27;m using Wireshark to monitor network traffinc to test a new software installed on a router. The router itself lets other networks (4g, mobile devices through usb etc) connect to it and enhance the speed on that router. What I&#x27;m trying to do is to disconnect the connected devices and discover if th...'''
date = "2014-06-10T00:54:00Z"
lastmod = "2014-06-10T03:41:00Z"
weight = 33605
keywords = [ "wifi", "router", "ethernet", "packetloss" ]
aliases = [ "/questions/33605" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Monitor packet losses using Wireshark](/questions/33605/monitor-packet-losses-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33605-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33605-score" class="post-score" title="current number of votes">0</div><span id="post-33605-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using Wireshark to monitor network traffinc to test a new software installed on a router. The router itself lets other networks (4g, mobile devices through usb etc) connect to it and enhance the speed on that router.</p><p>What I'm trying to do is to disconnect the connected devices and discover if there are any packet losses while doing this. I know I can simply use a filter stating "tcp.analysis.lost_segment" to track down lost packets, but how can I eventually isolate the specific device that causes the packet loss? Or even know if the reason was because of a disconnected device when there is a loss?</p><p>Also, what is the most stable method to test this with? To download a big file? To stream a video? Etc etc</p><p>All input is greatly appreciated</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span> <span class="post-tag tag-link-router" rel="tag" title="see questions tagged &#39;router&#39;">router</span> <span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span> <span class="post-tag tag-link-packetloss" rel="tag" title="see questions tagged &#39;packetloss&#39;">packetloss</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jun '14, 00:54</strong></p><img src="https://secure.gravatar.com/avatar/1642e91b7f969069bc432fff4e2197aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vegard&#39;s gravatar image" /><p><span>Vegard</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vegard has no accepted answers">0%</span></p></div></div><div id="comments-container-33605" class="comments-container"><span id="33611"></span><div id="comment-33611" class="comment"><div id="post-33611-score" class="comment-score"></div><div class="comment-text"><blockquote><p>What I'm <strong>trying to do is to disconnect the connected devices</strong> and discover <strong>if there are any packet losses</strong> while doing this.</p></blockquote><p>without being able to predict the future, I can predict that <strong>there will be packet loss</strong> if you do that.</p><p>BTW: You told us nothing about the following things, which makes it hard/impossible to give any good answer!!</p><ul><li>how are the devices connected to the router? wlan/wifi, ethernet, 4G?</li><li>what kind of devices are these?</li><li>how do you plan to 'disconnect' the devices?</li><li>do you expect to get no packet loss at all?</li><li>what exactly is the router doing, while it is 'enhancing the speed'?</li><li>what kind of router / router software is this?</li><li><strong>there will be packet loss</strong>, so what kind of insight do you hope to get by looking at the 'line' (air, etherhnet, etc.) while you disconnect the devices?</li></ul></div><div id="comment-33611-info" class="comment-info"><span class="comment-age">(10 Jun '14, 03:41)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-33605" class="comment-tools"></div><div class="clear"></div><div id="comment-33605-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

