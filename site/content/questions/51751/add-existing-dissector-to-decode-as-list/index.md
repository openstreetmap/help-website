+++
type = "question"
title = "Add existing dissector to decode as list"
description = '''Hi, I want to add the dissector iwarp-mpa to the decode as list of tcp using lua script. iwarp-mpa is not a registered dissector, so I can&#x27;t just use  local dis = Dissector.get(&quot;iwarp_mpa&quot;) and add it to tcp dissector table. Is there any other way to add it to the decode as list of tcp using lua scr...'''
date = "2016-04-18T04:36:00Z"
lastmod = "2016-04-26T05:23:00Z"
weight = 51751
keywords = [ "decode_as", "lua" ]
aliases = [ "/questions/51751" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Add existing dissector to decode as list](/questions/51751/add-existing-dissector-to-decode-as-list)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51751-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51751-score" class="post-score" title="current number of votes">0</div><span id="post-51751-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I want to add the dissector iwarp-mpa to the decode as list of tcp using lua script. iwarp-mpa is not a registered dissector, so I can't just use local dis = Dissector.get("iwarp_mpa") and add it to tcp dissector table.</p><p>Is there any other way to add it to the decode as list of tcp using lua script?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode_as" rel="tag" title="see questions tagged &#39;decode_as&#39;">decode_as</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '16, 04:36</strong></p><img src="https://secure.gravatar.com/avatar/af2964dd60c02ab6d0af2bc29a54dc69?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="user1095&#39;s gravatar image" /><p><span>user1095</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="user1095 has no accepted answers">0%</span></p></div></div><div id="comments-container-51751" class="comments-container"><span id="51753"></span><div id="comment-51753" class="comment"><div id="post-51753-score" class="comment-score">1</div><div class="comment-text"><p>Sorry, I've missed that <code>iwarp_mpa</code> is an existing dissector. So use</p><pre><code>local t = Dissector.list()

for _,name in ipairs(t) do
    print(name)
end</code></pre><p>to find its actual name to be used in <code>Dissector.get</code> (and run tshark so that you could see the output).</p></div><div id="comment-51753-info" class="comment-info"><span class="comment-age">(18 Apr '16, 06:18)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-51751" class="comment-tools"></div><div class="clear"></div><div id="comment-51751-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51805"></span>

<div id="answer-container-51805" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51805-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51805-score" class="post-score" title="current number of votes">1</div><span id="post-51805-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="user1095 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The iwarp_mpa dissector isn't register by name so it's not going to show up in that list (I don't think). It's a heuristic dissector, though, so it should automatically be called--assuming it's over TCP and no other dissector claims the traffic.</p><p>Are you trying to do this because you've got iwarp-mpa over something other than TCP? I don't know if there's a way try calling a heuristic dissector from Lua but even if there was I don't think you could call a specific one.</p><p>Typically in this situation people open an <a href="https://bugs.wireshark.org">enhancement request</a> to have the dissector register itself by name.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '16, 14:07</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-51805" class="comments-container"><span id="51841"></span><div id="comment-51841" class="comment"><div id="post-51841-score" class="comment-score"></div><div class="comment-text"><p>Looks like <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12361">bug 12361</a> was opened.</p></div><div id="comment-51841-info" class="comment-info"><span class="comment-age">(21 Apr '16, 10:40)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="51842"></span><div id="comment-51842" class="comment"><div id="post-51842-score" class="comment-score"></div><div class="comment-text"><p>Oh, and please be sure to accept the answer (by clicking on the checkmark) so this question no longer shows up as being unanswered.</p></div><div id="comment-51842-info" class="comment-info"><span class="comment-age">(21 Apr '16, 10:47)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="51958"></span><div id="comment-51958" class="comment"><div id="post-51958-score" class="comment-score"></div><div class="comment-text"><p>I need it because the heuristic rule doesn't always work. I solved it be writting a dissector for mpa fpdu using lua. Thanks!</p></div><div id="comment-51958-info" class="comment-info"><span class="comment-age">(26 Apr '16, 05:23)</span> <span class="comment-user userinfo">user1095</span></div></div></div><div id="comment-tools-51805" class="comment-tools"></div><div class="clear"></div><div id="comment-51805-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

