+++
type = "question"
title = "How can we bypass the network interface card detection in Interface list in wireshark source code"
description = '''Hi,  I want to bypass the interface list in Capture option in wireshark gui,where can i do that in wireshark source code 1.12.6 release.ie i didn&#x27;t keep any ethernet cable to my pc even i uninstalled the network adapter and i tried to open wireshark Capture and then by clicking on Interfaces.. icon ...'''
date = "2015-07-08T22:29:00Z"
lastmod = "2015-07-17T02:25:00Z"
weight = 43996
keywords = [ "152" ]
aliases = [ "/questions/43996" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can we bypass the network interface card detection in Interface list in wireshark source code](/questions/43996/how-can-we-bypass-the-network-interface-card-detection-in-interface-list-in-wireshark-source-code)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43996-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43996-score" class="post-score" title="current number of votes">0</div><span id="post-43996-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I want to bypass the interface list in Capture option in wireshark gui,where can i do that in wireshark source code 1.12.6 release.ie i didn't keep any ethernet cable to my pc even i uninstalled the network adapter and i tried to open wireshark Capture and then by clicking on Interfaces.. icon i am getting "There are no interfaces on which a capture can be done" message is popping.where i can bypass this thing so that i can start capturing and see my own packet which was already hardcoded in winpcap driver(which was working fine even though ethernet cable is not connected).</p><p>Thanks, Karun.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-152" rel="tag" title="see questions tagged &#39;152&#39;">152</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jul '15, 22:29</strong></p><img src="https://secure.gravatar.com/avatar/50c4b78862c6ca806916c3a71498cdf3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="karun256&#39;s gravatar image" /><p><span>karun256</span><br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="karun256 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Jul '15, 06:36</strong> </span></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-43996" class="comments-container"><span id="44226"></span><div id="comment-44226" class="comment"><div id="post-44226-score" class="comment-score"></div><div class="comment-text"><p>Hello All, Can any one tell me the functions in wireshark 1.12.6 source code which will detect out network interface card and capture packets.</p><p>Thanks, Karun.</p></div><div id="comment-44226-info" class="comment-info"><span class="comment-age">(16 Jul '15, 21:51)</span> <span class="comment-user userinfo">karun256</span></div></div></div><div id="comment-tools-43996" class="comment-tools"></div><div class="clear"></div><div id="comment-43996-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44232"></span>

<div id="answer-container-44232" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44232-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44232-score" class="post-score" title="current number of votes">0</div><span id="post-44232-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Simply grep for that string in the source. For current dev master I came up with:</p><pre><code>capture_opts.c(475): cmdarg_err(&quot;There are no interfaces on which a capture can be done&quot;);
dumpcap.c(1540): cmdarg_err(&quot;There are no interfaces on which a capture can be done&quot;);
dumpcap.c(1577): cmdarg_err(&quot;There are no interfaces on which a capture can be done&quot;);
dumpcap.c(4904): cmdarg_err(&quot;There are no interfaces on which a capture can be done&quot;);
tshark.c(1428): cmdarg_err(&quot;There are no interfaces on which a capture can be done&quot;);
wireshark-qt.cpp(636): cmdarg_err(&quot;There are no interfaces on which a capture can be done&quot;);
ui\gtk\capture_if_dlg.c(637): simple_error_message_box(&quot;There are no interfaces on which a capture can be done.&quot;);
ui\gtk\main.c(2355): cmdarg_err(&quot;There are no interfaces on which a capture can be done&quot;);</code></pre><p>but 1.12.6 is likely to be a little different in the number of places. Basically the code calls <code>capture_interface_list()</code> and if that returns NULL without an error then the error message is displayed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '15, 02:25</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-44232" class="comments-container"></div><div id="comment-tools-44232" class="comment-tools"></div><div class="clear"></div><div id="comment-44232-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

