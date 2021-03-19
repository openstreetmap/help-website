+++
type = "question"
title = "Verifying IP&#x27;s"
description = '''Hi, I am not very familiar with Wireshark so I apologize if this is too basic of a question. I have searched the forums for hints on how to accomplish what I am about to ask but was unsuccessful in finding any clues. I want to verify the IP&#x27;s seen by Wireshark. Basically I want to turn wireshark on ...'''
date = "2011-12-19T15:30:00Z"
lastmod = "2011-12-19T16:19:00Z"
weight = 8051
keywords = [ "filter", "ip", "address" ]
aliases = [ "/questions/8051" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Verifying IP's](/questions/8051/verifying-ips)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8051-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8051-score" class="post-score" title="current number of votes">0</div><span id="post-8051-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am not very familiar with Wireshark so I apologize if this is too basic of a question. I have searched the forums for hints on how to accomplish what I am about to ask but was unsuccessful in finding any clues.</p><p>I want to verify the IP's seen by Wireshark. Basically I want to turn wireshark on for a while and have it gather a listing of all the IP's seen. No need for payload data at all. Currently I don't dare leave wireshark on for too long due to the amount of data it will consume. Is there a way to configure Wireshark to capture only this information so that I could leave it on for a while longer? As I said I just want to verify that the ip information corresponds to what we expect to see on a particular monitoring port.</p><p>This seems like a very basic utilization of Wireshark and maybe someone could suggest a tool better suited to this task on a windows 7 or XP machine.</p><p>Thanks for any hints on how to accomplish this.</p><p>Sammi<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Dec '11, 15:30</strong></p><img src="https://secure.gravatar.com/avatar/803b187fa9d3d2f8d8ac4540181e8bcc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SamHnery&#39;s gravatar image" /><p><span>SamHnery</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SamHnery has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-8051" class="comments-container"></div><div id="comment-tools-8051" class="comment-tools"></div><div class="clear"></div><div id="comment-8051-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8053"></span>

<div id="answer-container-8053" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8053-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8053-score" class="post-score" title="current number of votes">1</div><span id="post-8053-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you don't care about anything but the IP addresses, then to help cut down on the amount of data Wireshark captures, you can try setting the <a href="http://wiki.wireshark.org/SnapLen?highlight=%28snaplen%29">snaplen</a> to only capture what you need. For example, assuming you are capturing on an Ethernet interface and assuming no vlan tagging, tunneling, etc., you might try a snaplen of 34 to limit the bytes you capture to only the Ethernet and IP headers.</p><p>You may also want to try experimenting with the command-line tools such as <a href="http://www.wireshark.org/docs/man-pages/dumpcap.html">dumpcap</a> and/or <a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark</a> along with some other shell commands such as sort, uniq, etc to accomplish what you need.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Dec '11, 16:19</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-8053" class="comments-container"></div><div id="comment-tools-8053" class="comment-tools"></div><div class="clear"></div><div id="comment-8053-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

