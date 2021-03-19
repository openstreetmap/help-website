+++
type = "question"
title = "Constructing protocol tree in a Lua dissector only when needed?"
description = '''I have just written a Lua heuristic dissector (attached to the UDP protocol) which does two things: - updating the Protocol Column - parsing large xml files in order to construct the protocol tree of items to be displayed I have noticed (and also read on this forum) that the dissector is called seve...'''
date = "2015-02-20T12:13:00Z"
lastmod = "2015-06-27T17:51:00Z"
weight = 39991
keywords = [ "performance", "dissector", "call", "lua", "slow" ]
aliases = [ "/questions/39991" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Constructing protocol tree in a Lua dissector only when needed?](/questions/39991/constructing-protocol-tree-in-a-lua-dissector-only-when-needed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39991-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39991-score" class="post-score" title="current number of votes">0</div><span id="post-39991-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have just written a Lua heuristic dissector (attached to the UDP protocol) which does two things: - updating the Protocol Column - parsing large xml files in order to construct the protocol tree of items to be displayed</p><p>I have noticed (and also read on this forum) that the dissector is called several times when loading, displaying and then selecting a packet. As a result, I am facing significant performance issues. I know the dissector could be rewritten in C to be faster but first I would like to know if the following is possible:</p><p>When the dissector is invoked by Wireshark, is it possible to know under which circumstances it is called i.e. clicking on a packet or scrolling the packet list, or just loading the pcap file.</p><p>The reason I am asking is that the tree only needs to be constructing when the user actually selects a packet. Otherwise, during the initial loading of the file by Wireshark for instance, the only thing that needs to happen is changing the name in the Protocol column which would be very quick.</p><p>Is this possible in any way? Or any other alternatives?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-call" rel="tag" title="see questions tagged &#39;call&#39;">call</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Feb '15, 12:13</strong></p><img src="https://secure.gravatar.com/avatar/258615514217bb9b718d4738b80328c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxvirrozeito&#39;s gravatar image" /><p><span>maxvirrozeito</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxvirrozeito has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Feb '15, 14:53</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-39991" class="comments-container"></div><div id="comment-tools-39991" class="comment-tools"></div><div class="clear"></div><div id="comment-39991-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="39993"></span>

<div id="answer-container-39993" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39993-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39993-score" class="post-score" title="current number of votes">0</div><span id="post-39993-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The tree only needs to be constructed when the dissector is told to construct a tree; for C dissectors, that's indicated by the tree argument being non-null.</p><p><span>@Hadriel</span>, is there a way to check for that in a Lua dissector?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Feb '15, 14:52</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-39993" class="comments-container"><span id="40019"></span><div id="comment-40019" class="comment"><div id="post-40019-score" class="comment-score"></div><div class="comment-text"><p>I checked the tree argument passed to my Lua dissector and it is never null. So the behaviour is not quite the same as in the C implementation.</p><p>As a temporary work-around, I have added a check on pinfo.visited in my Lua dissector which allows to avoid building the tree for the very first pass that Wireshark does on all packets. But there are still too many cases where the tree is built for no purpose, like the second pass for building the packet pane list, scrolling etc.</p><p>I do hope there is a way equivalent to your C-implementation description!</p></div><div id="comment-40019-info" class="comment-info"><span class="comment-age">(23 Feb '15, 03:34)</span> <span class="comment-user userinfo">maxvirrozeito</span></div></div><span id="40221"></span><div id="comment-40221" class="comment"><div id="post-40221-score" class="comment-score"></div><div class="comment-text"><p>For better performance, I decided to port the dissector to C.</p><p>For a five packet capture, I get: 1/ first dissector pass when Wireshark loads the file: tree = NULL (5 times) 2/ second pass (when Wireshark builds the View List?): tree != NULL (5 times) 3/ one extra pass for the selected packet: tree != NULL (1 time for the selected packet only)</p><p>Step 1 and 3 are as expected but why is the tree not NULL for step 2? The tree does not need to be built at that stage yet.</p></div><div id="comment-40221-info" class="comment-info"><span class="comment-age">(03 Mar '15, 09:39)</span> <span class="comment-user userinfo">maxvirrozeito</span></div></div><span id="43613"></span><div id="comment-43613" class="comment"><div id="post-43613-score" class="comment-score"></div><div class="comment-text"><p>Did you have a display or read filter set at the time? If so, the tree is not null in step 1 because the filter needs the fields to be parsed in order to figure out what matches the filter so it knows which packets to put in the view list.</p></div><div id="comment-43613-info" class="comment-info"><span class="comment-age">(27 Jun '15, 17:46)</span> <span class="comment-user userinfo">Hadriel</span></div></div></div><div id="comment-tools-39993" class="comment-tools"></div><div class="clear"></div><div id="comment-39993-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42814"></span>

<div id="answer-container-42814" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42814-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42814-score" class="post-score" title="current number of votes">0</div><span id="post-42814-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>So after playing with the example <a href="https://wiki.wireshark.org/Lua/Examples#dialogs_and_TextWindows">here</a> I found that the real dissection happens only after a call to local fields = { all_field_infos() }, everything above this function is called when Wireshark loads my PCAP file and the whole dissection happens when a tree is to be constructed.<br />
Can anybody explains this behavior?<br />
The function is not documented and the example gives a hint how Wireshark won't make a full dissection at the beginning, but why this function? At the end, we can use this (ugly) solution to improve the load time of the PCAP file</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '15, 12:39</strong></p><img src="https://secure.gravatar.com/avatar/6a8427ead4bf3634030701b9ba9940af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amine%20Ahd&#39;s gravatar image" /><p><span>Amine Ahd</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amine Ahd has one accepted answer">33%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Jun '15, 12:40</strong> </span></p></div></div><div id="comments-container-42814" class="comments-container"><span id="43614"></span><div id="comment-43614" class="comment"><div id="post-43614-score" class="comment-score"></div><div class="comment-text"><p>It's documented in the Lua API docs, on <a href="https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Field.html#global_functions_Field">this page</a>.</p><p>The example script uses that function to show what fields there are - it's not a function one would normally use when writing a dissector for a protocol; and the example itself doesn't do any real dissection, it's more of a helper type example to help explain things.</p></div><div id="comment-43614-info" class="comment-info"><span class="comment-age">(27 Jun '15, 17:51)</span> <span class="comment-user userinfo">Hadriel</span></div></div></div><div id="comment-tools-42814" class="comment-tools"></div><div class="clear"></div><div id="comment-42814-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

