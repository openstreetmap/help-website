+++
type = "question"
title = "update decryption table from Lua"
description = '''Is it possible to force Wireshark to reload the decryption table from within Lua code? Or other automatic means triggered by code/script. I&#x27;m writing a small script for debugging during development, in which I&#x27;ve gathered the required information in order to decrypt ISAKMP packets. The information i...'''
date = "2015-07-28T05:36:00Z"
lastmod = "2015-07-28T06:33:00Z"
weight = 44562
keywords = [ "lua", "ikev2", "isakmp", "decryption", "wireshark" ]
aliases = [ "/questions/44562" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [update decryption table from Lua](/questions/44562/update-decryption-table-from-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44562-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44562-score" class="post-score" title="current number of votes">0</div><span id="post-44562-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to force Wireshark to reload the decryption table from within Lua code? Or other automatic means triggered by code/script.</p><p>I'm writing a small script for debugging during development, in which I've gathered the required information in order to decrypt ISAKMP packets. The information is correct, and I currently copy/paste it straight into the table through the Wireshark GUI. As such, the next step would be to push it into the table from script/code and have Wireshark update it on the fly.</p><p>Preferably I would like to avoid having to save the capture and reopen it after editing the table and restarting Wireshark.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-ikev2" rel="tag" title="see questions tagged &#39;ikev2&#39;">ikev2</span> <span class="post-tag tag-link-isakmp" rel="tag" title="see questions tagged &#39;isakmp&#39;">isakmp</span> <span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jul '15, 05:36</strong></p><img src="https://secure.gravatar.com/avatar/626dc7d7cbd0b6462df0ed121c99bf73?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spoki0&#39;s gravatar image" /><p><span>spoki0</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="spoki0 has no accepted answers">0%</span></p></div></div><div id="comments-container-44562" class="comments-container"></div><div id="comment-tools-44562" class="comment-tools"></div><div class="clear"></div><div id="comment-44562-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44564"></span>

<div id="answer-container-44564" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44564-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44564-score" class="post-score" title="current number of votes">1</div><span id="post-44564-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="spoki0 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, Lua can't do that right now - but it's a good enhancement request. Please submit an enhancement bug on <a href="https://bugs.wireshark.org/bugzilla/">bugs.wireshark.org</a>.</p><p>In terms of other "scripts": you may be able to set the key info through the command-line, because ultimately they're all just preferences, which can be set by using the "<code>-o [prefname:value]</code>" command-line switch for both wireshark and tshark. So then you can write a shell script to do so for you, though of course this means restarting wireshark/tshark each time you change the keys.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jul '15, 06:33</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-44564" class="comments-container"></div><div id="comment-tools-44564" class="comment-tools"></div><div class="clear"></div><div id="comment-44564-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

