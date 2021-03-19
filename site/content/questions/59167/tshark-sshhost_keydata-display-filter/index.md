+++
type = "question"
title = "tshark ssh.host_key.data display filter"
description = '''I am trying to capture traffic between two CentOS vms that are using ssh key-based authentication. I looked up display filters on https://www.wireshark.org/docs/dfref/s/ssh.html and found the ssh.host_key.data filter, but I cannot make it work for tshark. Is there a way I can make this possible? Tha...'''
date = "2017-01-30T19:00:00Z"
lastmod = "2017-02-02T01:50:00Z"
weight = 59167
keywords = [ "display", "tshark", "display-filter", "ssh" ]
aliases = [ "/questions/59167" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark ssh.host\_key.data display filter](/questions/59167/tshark-sshhost_keydata-display-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59167-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59167-score" class="post-score" title="current number of votes">0</div><span id="post-59167-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to capture traffic between two CentOS vms that are using ssh key-based authentication. I looked up display filters on <a href="https://www.wireshark.org/docs/dfref/s/ssh.html">https://www.wireshark.org/docs/dfref/s/ssh.html</a> and found the ssh.host_key.data filter, but I cannot make it work for tshark. Is there a way I can make this possible? Thanks, Scott</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span> <span class="post-tag tag-link-ssh" rel="tag" title="see questions tagged &#39;ssh&#39;">ssh</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jan '17, 19:00</strong></p><img src="https://secure.gravatar.com/avatar/54ad0b2a8448a7314fb8fb95c8a83edb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scottctaylor12&#39;s gravatar image" /><p><span>scottctaylor12</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scottctaylor12 has no accepted answers">0%</span></p></div></div><div id="comments-container-59167" class="comments-container"></div><div id="comment-tools-59167" class="comment-tools"></div><div class="clear"></div><div id="comment-59167-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59239"></span>

<div id="answer-container-59239" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59239-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59239-score" class="post-score" title="current number of votes">0</div><span id="post-59239-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>ssh.host_key.data is only used (in Wireshark 2.2.X) when the Host-Key is not of type "ssh-rsa". So it depends on the host key of your SSH server.</p><p>Furthermore this part has been refactored in the current Development Version (2.3.X s. <a href="https://www.wireshark.org/download/automated/)">https://www.wireshark.org/download/automated/)</a> to catch other key types too.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Feb '17, 01:50</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p><span>Uli</span><br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div></div><div id="comments-container-59239" class="comments-container"></div><div id="comment-tools-59239" class="comment-tools"></div><div class="clear"></div><div id="comment-59239-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

