+++
type = "question"
title = "destination MAC address not present on packet capture"
description = '''This may be a very trivial question but I can&#x27;t figure it out by myself. Examining a packet trace of a ping from node1 to node2 I see that in the echo/reply packets the destination MAC is not present under &quot;Linux cooked capture&quot; section on Wireshark. The capture was obtained with tcpdump on Ubuntu. ...'''
date = "2011-09-09T16:00:00Z"
lastmod = "2011-09-12T08:33:00Z"
weight = 6237
keywords = [ "mac", "address" ]
aliases = [ "/questions/6237" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [destination MAC address not present on packet capture](/questions/6237/destination-mac-address-not-present-on-packet-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6237-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6237-score" class="post-score" title="current number of votes">0</div><span id="post-6237-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This may be a very trivial question but I can't figure it out by myself. Examining a packet trace of a ping from node1 to node2 I see that in the echo/reply packets the destination MAC is not present under "Linux cooked capture" section on Wireshark.</p><p>The capture was obtained with tcpdump on Ubuntu.</p><p>Why the destination MAC address is not there?, how node2 knows that the packets should be received by its network interface if the packet doesn't have a destination MAC address?. The ping works fine but I am struggling with the concept of source and destination MAC when I analyze the trace.</p><p>Any help is appreciated.</p><p>Juan.<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Sep '11, 16:00</strong></p><img src="https://secure.gravatar.com/avatar/9a5ee19d2e9f749023c26b14b1872e88?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Juan&#39;s gravatar image" /><p><span>Juan</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Juan has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-6237" class="comments-container"><span id="6241"></span><div id="comment-6241" class="comment"><div id="post-6241-score" class="comment-score">1</div><div class="comment-text"><p>On what network device did you capture this? If it's on the "any" device, then see SYNbit's comment; given the way the "any" device works, it captures in a mode where you can't get the destination address. If it's on a particular network device (such as, for example, eth0), if that device is an Ethernet or Wi-Fi device, you should get the source and destination addresses.</p></div><div id="comment-6241-info" class="comment-info"><span class="comment-age">(09 Sep '11, 22:59)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="6290"></span><div id="comment-6290" class="comment"><div id="post-6290-score" class="comment-score"></div><div class="comment-text"><p>In fact I was using "any" on tcpdump, after I limited the capture to a particular interface I can see the destination address. Thanks.</p></div><div id="comment-6290-info" class="comment-info"><span class="comment-age">(12 Sep '11, 08:33)</span> <span class="comment-user userinfo">Juan</span></div></div></div><div id="comment-tools-6237" class="comment-tools"></div><div class="clear"></div><div id="comment-6237-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6238"></span>

<div id="answer-container-6238" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6238-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6238-score" class="post-score" title="current number of votes">0</div><span id="post-6238-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Juan has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See <a href="http://wiki.wireshark.org/SLL">http://wiki.wireshark.org/SLL</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Sep '11, 16:32</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-6238" class="comments-container"><span id="6289"></span><div id="comment-6289" class="comment"><div id="post-6289-score" class="comment-score"></div><div class="comment-text"><p>Thanks, that explains my problem.</p></div><div id="comment-6289-info" class="comment-info"><span class="comment-age">(12 Sep '11, 08:32)</span> <span class="comment-user userinfo">Juan</span></div></div></div><div id="comment-tools-6238" class="comment-tools"></div><div class="clear"></div><div id="comment-6238-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

