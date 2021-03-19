+++
type = "question"
title = "Decode as Modbus/TCP problem"
description = '''Hi, I am trying to analyze some Modbus/TCP traffic. I am using ports other than standard 502. When trying to use Decode As only about halp of packets are marked as Modbus even though I chose both directions in Decode As window. Also there is no possibility to add additional ports to Modbus in Edit-&amp;...'''
date = "2014-11-14T11:25:00Z"
lastmod = "2014-11-14T11:40:00Z"
weight = 37869
keywords = [ "modbus", "decode", "decode_as" ]
aliases = [ "/questions/37869" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decode as Modbus/TCP problem](/questions/37869/decode-as-modbustcp-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37869-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37869-score" class="post-score" title="current number of votes">0</div><span id="post-37869-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am trying to analyze some Modbus/TCP traffic. I am using ports other than standard 502. When trying to use Decode As only about halp of packets are marked as Modbus even though I chose both directions in Decode As window. Also there is no possibility to add additional ports to Modbus in Edit-&gt;Preferences-&gt;Protocols. Any help would be appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-modbus" rel="tag" title="see questions tagged &#39;modbus&#39;">modbus</span> <span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span> <span class="post-tag tag-link-decode_as" rel="tag" title="see questions tagged &#39;decode_as&#39;">decode_as</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '14, 11:25</strong></p><img src="https://secure.gravatar.com/avatar/3adf4eae18b311e9e62e4db158cfbf4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ciupol&#39;s gravatar image" /><p><span>ciupol</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ciupol has no accepted answers">0%</span></p></div></div><div id="comments-container-37869" class="comments-container"></div><div id="comment-tools-37869" class="comment-tools"></div><div class="clear"></div><div id="comment-37869-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37870"></span>

<div id="answer-container-37870" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37870-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37870-score" class="post-score" title="current number of votes">0</div><span id="post-37870-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Worst case you could modify the capture file and replace your port with the standard port... e.g using <a href="http://www.tracewrangler.com">TraceWrangler</a> with a Anonymization task where you disable every replacement setting except the TCP port replacement (or use bittwiste or tcprewrite). Maybe Wireshark will then decode everything as expected.</p><p>You could also open a bug report at <a href="http://bugs.wireshark.org">bugs.wireshark.org</a>, but it may take a while until the bug is fixed (if it is in fact a bug)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '14, 11:40</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-37870" class="comments-container"></div><div id="comment-tools-37870" class="comment-tools"></div><div class="clear"></div><div id="comment-37870-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

