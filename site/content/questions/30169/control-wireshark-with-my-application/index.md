+++
type = "question"
title = "Control wireshark with my application"
description = '''i am new in wireshark and lua script. I did some research and found that &quot;Wireshark contains a LUA language interpreter. LUA scripts that execute on this interpreter can control Wireshark&quot;. I want to make an application to control wireshark. When i give command &quot;start capture&quot; in my application it s...'''
date = "2014-02-25T00:05:00Z"
lastmod = "2014-02-25T08:41:00Z"
weight = 30169
keywords = [ "lua", "luainterface", "batch", "wireshark" ]
aliases = [ "/questions/30169" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Control wireshark with my application](/questions/30169/control-wireshark-with-my-application)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30169-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30169-score" class="post-score" title="current number of votes">0</div><span id="post-30169-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i am new in wireshark and lua script. I did some research and found that "Wireshark contains a LUA language interpreter. LUA scripts that execute on this interpreter can control Wireshark". I want to make an application to control wireshark. When i give command "start capture" in my application it should start capturing and same goes with filtering protocol. Is it possible to do that? if possible, can you give some example how can i do it?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-luainterface" rel="tag" title="see questions tagged &#39;luainterface&#39;">luainterface</span> <span class="post-tag tag-link-batch" rel="tag" title="see questions tagged &#39;batch&#39;">batch</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Feb '14, 00:05</strong></p><img src="https://secure.gravatar.com/avatar/a717f574f006b4977952372192a67e7f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amrit&#39;s gravatar image" /><p><span>Amrit</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amrit has no accepted answers">0%</span></p></div></div><div id="comments-container-30169" class="comments-container"></div><div id="comment-tools-30169" class="comment-tools"></div><div class="clear"></div><div id="comment-30169-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="30179"></span>

<div id="answer-container-30179" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30179-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30179-score" class="post-score" title="current number of votes">1</div><span id="post-30179-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Amrit: I'm not sure how you mean that question. You said "I want to make an application to control wireshark. When i give command "start capture" in my application it should start capturing and same goes with filtering protocol." You don't need Wireshark to capture and filter - you can use dumpcap instead, for example.</p><p>Lua is used for writing scripts inside Wireshark and tshark, to affect wireshark/tshark's behavior, but Lua doesn't "drive" the wireshark application - instead, wireshark invokes Lua when certain things happen. Think of it more like a plugin language inside wireshark/tshark than a shell script outside of wireshark/tshark. Lua can control wireshark/tshark in many ways, but not to start/stop capturing as far as I know. That could be added, but I don't understand any use-case for such a thing. Can you explain further what you want to do?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Feb '14, 07:21</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-30179" class="comments-container"></div><div id="comment-tools-30179" class="comment-tools"></div><div class="clear"></div><div id="comment-30179-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30172"></span>

<div id="answer-container-30172" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30172-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30172-score" class="post-score" title="current number of votes">0</div><span id="post-30172-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For my self personally, a colleague and I are hoping to release a light-weight open source tool that provides a top-down view on network data. It has already been written, tested and used in anger by others at the company where we work. It analyses pcap data then provides statistics on a list of IP conversations between hosts, allowing you to drill down into details about the TCP Connections for each conversation. Then from TCP Connections it can drill down into the individual packet data where it currently hooks into a prototype-dev version of Wireshark (by changing the filters on the GUI). It also provides the ability to script your own data classifications to help identify specific network conditions quickly. Our aim is to release it to the open source community within the next few weeks/months.</p><p>In my opinion I would rather connect to a Wireshark remote control API than use a bespoke version or re-create the wheel.</p><p>I think a "GUI remote control" would only need to support "Change GUI Filter" and "Remove GUI Filter" although it has a lot more potential too. I have implemented these controls in our prototype-dev version or Wireshark.</p><p>Any help you can offer would be appreciated.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Feb '14, 00:42</strong></p><img src="https://secure.gravatar.com/avatar/c03f8825d72ddaaecb18f8a6762c4207?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cusabio1&#39;s gravatar image" /><p><span>cusabio1</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cusabio1 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Feb '14, 01:39</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-30172" class="comments-container"><span id="30180"></span><div id="comment-30180" class="comment"><div id="post-30180-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Any help you can offer would be appreciated.</p></blockquote><p>help regarding what?</p><p>BTW: as you mentioned 'open source', is your code available somewhere?</p></div><div id="comment-30180-info" class="comment-info"><span class="comment-age">(25 Feb '14, 07:38)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-30172" class="comment-tools"></div><div class="clear"></div><div id="comment-30172-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30182"></span>

<div id="answer-container-30182" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30182-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30182-score" class="post-score" title="current number of votes">0</div><span id="post-30182-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>When i give command "start capture" in my application it should start capturing and same goes with filtering protocol.</p></blockquote><p>just start Wireshark with the appropriate commandline options in your application. See <a href="http://www.wireshark.org/docs/man-pages/wireshark.html">Wireshark man page</a>.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Feb '14, 08:41</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-30182" class="comments-container"></div><div id="comment-tools-30182" class="comment-tools"></div><div class="clear"></div><div id="comment-30182-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

