+++
type = "question"
title = "No packets from other devices are captured."
description = '''Hi, I am new to Wireshark and I am using the &#x27;Stable 2.0.4 release&#x27; on a mac. When I capture It only captures traffic from my IP address and no traffic is appearing from mobile or other devices on my wireless network. I have been researching and maybe I need a &#x27;monitor mode&#x27; but I am yet to find it....'''
date = "2016-06-27T09:22:00Z"
lastmod = "2016-06-27T16:35:00Z"
weight = 53678
keywords = [ "packets" ]
aliases = [ "/questions/53678" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [No packets from other devices are captured.](/questions/53678/no-packets-from-other-devices-are-captured)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53678-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53678-score" class="post-score" title="current number of votes">0</div><span id="post-53678-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am new to Wireshark and I am using the 'Stable 2.0.4 release' on a mac. When I capture It only captures traffic from my IP address and no traffic is appearing from mobile or other devices on my wireless network. I have been researching and maybe I need a 'monitor mode' but I am yet to find it. Also a en0 when in the 'Options' and 'manage interfaces' but it's not there??? Thanks.<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jun '16, 09:22</strong></p><img src="https://secure.gravatar.com/avatar/d61b3938d5a1345901ab338df78e6caa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YellowNine&#39;s gravatar image" /><p><span>YellowNine</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YellowNine has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-53678" class="comments-container"></div><div id="comment-tools-53678" class="comment-tools"></div><div class="clear"></div><div id="comment-53678-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53679"></span>

<div id="answer-container-53679" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53679-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53679-score" class="post-score" title="current number of votes">0</div><span id="post-53679-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Some pointers for you:</p><p><a href="https://ask.wireshark.org/questions/53655/interface-stopped-showing-up-on-my-mac-osx-system">https://ask.wireshark.org/questions/53655/interface-stopped-showing-up-on-my-mac-osx-system</a><br />
<a href="https://ask.wireshark.org/questions/52077/cant-capture-5ghz-traffic-on-os-x">https://ask.wireshark.org/questions/52077/cant-capture-5ghz-traffic-on-os-x</a></p><p>I think link one addresses your concern about managing interfaces, and link two will help you prepare the interface for sniffing on a specific channel that you choose. The GTK version of Wireshark has an option to set monitor mode when you select capture --&gt; options.</p><p>In the QT version, there is a small window under options:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2016-06-27_at_7.33.22_PM.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '16, 16:35</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p><span>Bob Jones</span><br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Jun '16, 01:02</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-53679" class="comments-container"></div><div id="comment-tools-53679" class="comment-tools"></div><div class="clear"></div><div id="comment-53679-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

