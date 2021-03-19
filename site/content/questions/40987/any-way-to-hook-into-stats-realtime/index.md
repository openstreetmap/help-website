+++
type = "question"
title = "Any way to hook into stats realtime?"
description = '''I&#x27;m wondering, if possible, what the best way would be to get a realtime stream of statistics info (eg endpoint info) from wireshark? Perhaps via LUA or ???'''
date = "2015-03-29T19:24:00Z"
lastmod = "2015-03-30T08:51:00Z"
weight = 40987
keywords = [ "lua", "endpoints" ]
aliases = [ "/questions/40987" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Any way to hook into stats realtime?](/questions/40987/any-way-to-hook-into-stats-realtime)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40987-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40987-score" class="post-score" title="current number of votes">0</div><span id="post-40987-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm wondering, if possible, what the best way would be to get a realtime stream of statistics info (eg endpoint info) from wireshark? Perhaps via LUA or ???</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-endpoints" rel="tag" title="see questions tagged &#39;endpoints&#39;">endpoints</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Mar '15, 19:24</strong></p><img src="https://secure.gravatar.com/avatar/4bfef988deec3431b3448ec28576a531?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="canadaDry&#39;s gravatar image" /><p><span>canadaDry</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="canadaDry has no accepted answers">0%</span></p></div></div><div id="comments-container-40987" class="comments-container"><span id="40992"></span><div id="comment-40992" class="comment"><div id="post-40992-score" class="comment-score"></div><div class="comment-text"><blockquote><p>realtime stream of statistics info</p></blockquote><p>can you please be more specific, maybe with an example?</p></div><div id="comment-40992-info" class="comment-info"><span class="comment-age">(30 Mar '15, 03:14)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="41014"></span><div id="comment-41014" class="comment"><div id="post-41014-score" class="comment-score"></div><div class="comment-text"><p>I'd like to let Wireshark do all the tabulation work for all the endpoint stats (eg. bytes rx/tx per endpoint) but somehow get at that data in realtime by my own program (eg. python+pandas if at all possible) to track and monitor activity to/from endpoints over time. With the goal of my program being able to analyze and detect abnormal traffic patterns based on historical data.</p><p>Being able to hook into wireshark's data would presumably save having to reinvent the wheel.</p><p>Does that make any sense?</p></div><div id="comment-41014-info" class="comment-info"><span class="comment-age">(30 Mar '15, 07:53)</span> <span class="comment-user userinfo">canadaDry</span></div></div></div><div id="comment-tools-40987" class="comment-tools"></div><div class="clear"></div><div id="comment-40987-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41015"></span>

<div id="answer-container-41015" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41015-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41015-score" class="post-score" title="current number of votes">0</div><span id="post-41015-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>to <strong>track and monitor activity to/from endpoints over time</strong>.</p></blockquote><p>In that case, Wireshark is the wrong tool for you. It is a network troubleshooting tool and it was not designed for real time and long term analysis.</p><p>See my answer to similar questions and the tips and links therein.</p><blockquote><p><a href="https://ask.wireshark.org/questions/26434/sound-alert">https://ask.wireshark.org/questions/26434/sound-alert</a><br />
<a href="https://ask.wireshark.org/questions/29902/running-wireshark-continuously">https://ask.wireshark.org/questions/29902/running-wireshark-continuously</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Mar '15, 07:58</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-41015" class="comments-container"><span id="41023"></span><div id="comment-41023" class="comment"><div id="post-41023-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your assistance and patience Kurt!</p><p>A related query then... would it be possible to use LUA (or ??) to grab a snapshot of the internal endpoint data that wireshark has accumulated? Does wireshark make it possible to access whatever internal array/table that is used for its statistics?</p></div><div id="comment-41023-info" class="comment-info"><span class="comment-age">(30 Mar '15, 08:31)</span> <span class="comment-user userinfo">canadaDry</span></div></div><span id="41024"></span><div id="comment-41024" class="comment"><div id="post-41024-score" class="comment-score"></div><div class="comment-text"><p>There is no exposed API (I believe no way at all) to trigger any statistics while Wireshark is running and there is no way to access the output of any statistics in memory (or similar). So that won't help you either for your realtime and longterm monitoring.</p><p>Furthermore, there is no "exposed" API to access the internal data structures in a way you would need it.</p><p>I know the dissector functionality of Wireshark is inviting (we've had quite a few of these discussions here), but I have to repeat myself: Wireshark is the wrong tool for such a scenario. If you run it for a long time (hours, days - depends on the amount of traffic) it will run into a out-of-memory problem, as Wireshark needs to keep track of some information and this will eventually eat up all available memory. As I said, it was not designed to work in that mode/way.</p><p>See:</p><blockquote><p><a href="https://ask.wireshark.org/questions/30379/how-to-reduce-memory-usage-in-very-long-time-capture-and-analyze">https://ask.wireshark.org/questions/30379/how-to-reduce-memory-usage-in-very-long-time-capture-and-analyze</a><br />
<a href="https://ask.wireshark.org/questions/25794/tshark-generate-core-dump">https://ask.wireshark.org/questions/25794/tshark-generate-core-dump</a></p></blockquote></div><div id="comment-41024-info" class="comment-info"><span class="comment-age">(30 Mar '15, 08:51)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-41015" class="comment-tools"></div><div class="clear"></div><div id="comment-41015-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

