+++
type = "question"
title = "Does Wireshark support Modbus/TCP?"
description = '''Can I use Wireshark as a sniffer on Modbus/TCP traffic? Can I use it for simulating either a Modbus/TCP client or a server?'''
date = "2012-03-14T19:54:00Z"
lastmod = "2012-03-14T22:23:00Z"
weight = 9547
keywords = [ "modbus" ]
aliases = [ "/questions/9547" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Does Wireshark support Modbus/TCP?](/questions/9547/does-wireshark-support-modbustcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9547-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9547-score" class="post-score" title="current number of votes">0</div><span id="post-9547-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can I use Wireshark as a sniffer on Modbus/TCP traffic? Can I use it for simulating either a Modbus/TCP client or a server?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-modbus" rel="tag" title="see questions tagged &#39;modbus&#39;">modbus</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Mar '12, 19:54</strong></p><img src="https://secure.gravatar.com/avatar/2e05ec0a7f69462ab456430c3cbbeccb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mshani&#39;s gravatar image" /><p><span>mshani</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mshani has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Mar '12, 22:23</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-9547" class="comments-container"></div><div id="comment-tools-9547" class="comment-tools"></div><div class="clear"></div><div id="comment-9547-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9550"></span>

<div id="answer-container-9550" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9550-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9550-score" class="post-score" title="current number of votes">2</div><span id="post-9550-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Can I use WireShark as a sniffer on Modbus/TCP traffic?</p></blockquote><p>Wireshark includes, at least in the top of the SVN trunk, a Modbus/TCP dissector:</p><pre><code>$ tshark -G protocols | egrep -i modbus
$ CIP Modbus Object CIPMB   cipmb
$ Modbus    Modbus  modbus
$ Modbus/TCP    Modbus/TCP  mbtcp</code></pre><p>and I think that was added before the 1.6 release, so 1.6.x, and possibly earlier releases, should have it, so you should be able to decode and analyzer Modbus/TCP traffic on any network on which Wireshark can capture traffic.</p><blockquote><p>Can I use it for simulating either a Modbus/TCP client or a server?</p></blockquote><p>No. Wireshark is a packet sniffer (network analyzer), not a network simulator.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Mar '12, 22:23</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-9550" class="comments-container"></div><div id="comment-tools-9550" class="comment-tools"></div><div class="clear"></div><div id="comment-9550-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

