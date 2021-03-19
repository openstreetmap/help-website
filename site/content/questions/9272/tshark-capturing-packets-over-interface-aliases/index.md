+++
type = "question"
title = "tshark capturing packets over interface aliases"
description = '''Hello, I am running tshark version 1.4.3 &amp;amp; I am running linux 2.6-18 kernel. I have two ethernet ports eth0 &amp;amp; eth1 on the box. Assuming I create three IP aliases based on the interface &quot;eth0&quot; namely &quot;eth0:0&quot;, &quot;eth0:1&quot;, &quot;eth0:2&quot;. The IP address for the interfaces &amp;amp; aliases are as below: e...'''
date = "2012-02-28T11:24:00Z"
lastmod = "2012-02-28T11:24:00Z"
weight = 9272
keywords = [ "interface", "capture", "alias", "tshark", "ip" ]
aliases = [ "/questions/9272" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark capturing packets over interface aliases](/questions/9272/tshark-capturing-packets-over-interface-aliases)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9272-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9272-score" class="post-score" title="current number of votes">0</div><span id="post-9272-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am running tshark version 1.4.3 &amp; I am running linux 2.6-18 kernel. I have two ethernet ports eth0 &amp; eth1 on the box. Assuming I create three IP aliases based on the interface "eth0" namely "eth0:0", "eth0:1", "eth0:2". The IP address for the interfaces &amp; aliases are as below:</p><p>eth0 192.168.10.10/255.255.0.0 eth0:0 172.27.0.10/255.255.255.0 eth0:1 172.27.0.11/255.255.255.0</p><p>I am running a ping to eth0 from another host on the same subnet as eth0 &amp; when I run tshark as below:</p><p>tshark -i eth0:0</p><p>I see packets that terminate on eth0 - Is this the expected behaviour? I would like to filter all packets that are not destined to eth0:0, Is there anyway to do this other than using the tshark's IP address filter??</p><p>Thanks</p><p>/Ramesh</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-alias" rel="tag" title="see questions tagged &#39;alias&#39;">alias</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '12, 11:24</strong></p><img src="https://secure.gravatar.com/avatar/c2f093aae48ae803c3409e8eb2b2eb39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ramesh&#39;s gravatar image" /><p><span>Ramesh</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ramesh has no accepted answers">0%</span></p></div></div><div id="comments-container-9272" class="comments-container"></div><div id="comment-tools-9272" class="comment-tools"></div><div class="clear"></div><div id="comment-9272-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

