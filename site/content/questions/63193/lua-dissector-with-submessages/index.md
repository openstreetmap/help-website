+++
type = "question"
title = "lua dissector with submessages"
description = '''I&#x27;ve previously created a dissectors where the message had a constant format. Now I have the following case: A message sent over UDP with some header. The data of the message is contained with many sub messages which contains headers and data. Now this sub messages can be in any order inside the ori...'''
date = "2017-07-27T22:19:00Z"
lastmod = "2017-07-28T01:28:00Z"
weight = 63193
keywords = [ "lua", "dissector" ]
aliases = [ "/questions/63193" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [lua dissector with submessages](/questions/63193/lua-dissector-with-submessages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63193-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've previously created a dissectors where the message had a constant format. Now I have the following case:</p><p>A message sent over UDP with some header. The data of the message is contained with many sub messages which contains headers and data. Now this sub messages can be in any order inside the original big message. for example:</p><pre><code>IP - UDP - big message header - sub message A - sub message B - sub message C    
IP - UDP - big message header - sub message C - sub message A - sub message B</code></pre><p>The common of this sub messages is that they can be identified by a header (which is in common format for all, except some message id).</p><p>The order of those sub messages is unknown, the length of each sub message is varying. The length of the the big message is varying, but can be evaluated from the big message header.</p><p>What is the best way to create a dissector for this? Any code example for this would be great.</p><p>Thank you!</p></div><div id="question-tags" class="tags-container tags">lua dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '17, 22:19</strong></p><img src="https://secure.gravatar.com/avatar/b02c5dfff2049bed61dbced93bf455d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BMWE&#39;s gravatar image" /><p>BMWE<br />
<span class="score" title="46 reputation points">46</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BMWE has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Jul '17, 01:40</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-63193" class="comments-container"></div><div id="comment-tools-63193" class="comment-tools"></div><div class="clear"></div><div id="comment-63193-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63201"></span>

<div id="answer-container-63201" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63201-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The way you put it, the structure of your protocol is similar to many others (e.g., ISUP or Q.931) where the "big message" is the protocol message and the "submessages" inside it are called "information elements", often in Type-Length-Value structure, although sometimes the length and even the type is implicit (i.e. some types have fixed lengths and some types have fixed positions in the big message).</p><p>Well-written dissectors of such protocols are future-proof in terms that they create their own dissector table indexed by "type", so if some information elements (submessages) are added in future, it is enough to write a dissector for that particular submessage and place a reference to it into the basic dissector's dissector table, while information element types for which no row exists in the dissector table are handled by the basic dissector. But it is questionnable whether such aproach makes any sense for a Lua dissector.</p><p>Other than that, it is just a boring routine of parsing the contents of the big message submessage by submessage, taking into account their length, and calling a corresponding function to handle each submessage (consulting the dissector table first if you want to implement the approach mentioned above). If the last byte of last submessage is not the last byte of payload of the big message, something went wrong and you should report a malformed message.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jul '17, 01:28</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-63201" class="comments-container"></div><div id="comment-tools-63201" class="comment-tools"></div><div class="clear"></div><div id="comment-63201-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

