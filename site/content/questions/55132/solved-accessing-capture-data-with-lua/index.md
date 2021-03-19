+++
type = "question"
title = "*Solved* Accessing capture data with Lua"
description = '''I have already made a Lua script that uses a Listener to listen for packets as they are captured, and then uses data from them. But I am at a loss in figuring out how to access packet data after the capture has already occurred. For example, I want to be able to have my packet data listed out (eithe...'''
date = "2016-08-26T13:01:00Z"
lastmod = "2016-08-26T17:29:00Z"
weight = 55132
keywords = [ "lua" ]
aliases = [ "/questions/55132" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\*Solved\* Accessing capture data with Lua](/questions/55132/solved-accessing-capture-data-with-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55132-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55132-score" class="post-score" title="current number of votes">0</div><span id="post-55132-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have already made a Lua script that uses a Listener to listen for packets as they are captured, and then uses data from them. But I am at a loss in figuring out how to access packet data after the capture has already occurred. For example, I want to be able to have my packet data listed out (either from a capture that just occurred, or from a capture file that I opened), click on my script in the menu, then select a packet by its packet number, and then have access to all of its fields as if I had captured the packet from a listener. Is there a way to do this from Lua?</p><p>Edit: I discovered a function called "retap_packets", described in the GUI page in the Lua API documentation, and from its description, it sounds like what I'm looking for, but after trying it, it doesn't seem to work.</p><p>Edit again: To whom it may concern, I was originally calling the retap_packets() function before the declaration of the listener.packet() function. Putting it after that declaration fixed the problem.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Aug '16, 13:01</strong></p><img src="https://secure.gravatar.com/avatar/79fd2c038d7db19e310fd09e8b7d8a4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jr0026&#39;s gravatar image" /><p><span>jr0026</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jr0026 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Aug '16, 14:31</strong> </span></p></div></div><div id="comments-container-55132" class="comments-container"><span id="55134"></span><div id="comment-55134" class="comment"><div id="post-55134-score" class="comment-score"></div><div class="comment-text"><p>The right way to answer your own question is to, well, answer your own question - put whatever you discovered into an answer, and add that answer to the question. That way, the question shows up as answered, and other people who want to do the same thing can find the answer more easily. (Think of a Q&amp;A site, like this site, as a "crowdsourced FAQ" rather than as a forum.)</p></div><div id="comment-55134-info" class="comment-info"><span class="comment-age">(26 Aug '16, 17:29)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-55132" class="comment-tools"></div><div class="clear"></div><div id="comment-55132-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

