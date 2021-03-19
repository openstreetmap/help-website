+++
type = "question"
title = "Store Data to use after two packets LUA"
description = '''Hey, I made a Dissector using LUA and I want to use an information that was available two packets before , is there a way to store data with the number of the frame to use later. I heard that it is done using &quot;conversations&quot; but i never saw a working example so I can do the same, or is there some wa...'''
date = "2017-10-13T00:02:00Z"
lastmod = "2017-10-13T12:52:00Z"
weight = 63861
keywords = [ "lua", "conversations", "wireshark" ]
aliases = [ "/questions/63861" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Store Data to use after two packets LUA](/questions/63861/store-data-to-use-after-two-packets-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63861-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63861-score" class="post-score" title="current number of votes">0</div><span id="post-63861-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey,</p><p>I made a Dissector using LUA and I want to use an information that was available two packets before , is there a way to store data with the number of the frame to use later.</p><p>I heard that it is done using "conversations" but i never saw a working example so I can do the same, or is there some way other than storing data in a session , maybe a way to retrieve data in a previous packet.</p><p>Thanks alot</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-conversations" rel="tag" title="see questions tagged &#39;conversations&#39;">conversations</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Oct '17, 00:02</strong></p><img src="https://secure.gravatar.com/avatar/d4d86ff8a9a663eba8ebbbbb4241f9e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="webtuto&#39;s gravatar image" /><p><span>webtuto</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="webtuto has no accepted answers">0%</span></p></div></div><div id="comments-container-63861" class="comments-container"><span id="63874"></span><div id="comment-63874" class="comment"><div id="post-63874-score" class="comment-score"></div><div class="comment-text"><p>There are several questions dealing with this subject here. You can create Lua tables (arrays) indexed by <code>frame.number</code> field or by some other unique identifiers available in the packets of your interest. On top of the quite obvious requirement that these tables must not be local to the dissector function, you have to deal with the fact that a dissector is called several times for the same packet, and that only the very first pass is sequential.</p></div><div id="comment-63874-info" class="comment-info"><span class="comment-age">(13 Oct '17, 12:52)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-63861" class="comment-tools"></div><div class="clear"></div><div id="comment-63861-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

