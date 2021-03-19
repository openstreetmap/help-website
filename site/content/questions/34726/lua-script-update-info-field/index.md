+++
type = "question"
title = "lua script update Info field"
description = '''I&#x27;ve got a LUA script which decodes an IPv6 extension header. I&#x27;d like to have my LUA script write information into the &quot;Info&quot; column in the top wireshark pane (the one where each row is a packet-- the Info colum is on the right). In my Lua script I&#x27;ve done &quot;pinfo.cols.info = &#x27;stuff&#x27;&quot; but it doesn&#x27;t...'''
date = "2014-07-17T05:28:00Z"
lastmod = "2014-07-17T07:31:00Z"
weight = 34726
keywords = [ "override", "lua", "expert-info", "script" ]
aliases = [ "/questions/34726" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [lua script update Info field](/questions/34726/lua-script-update-info-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34726-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34726-score" class="post-score" title="current number of votes">0</div><span id="post-34726-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've got a LUA script which decodes an IPv6 extension header. I'd like to have my LUA script write information into the "Info" column in the top wireshark pane (the one where each row is a packet-- the Info colum is on the right). In my Lua script I've done "pinfo.cols.info = 'stuff'" but it doesn't appear-- what's shown is information from the transport protocol.</p><p>So my question is how might one write information from a LUA script to the Info field-- and prevent the transport layer from overriding that information?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-override" rel="tag" title="see questions tagged &#39;override&#39;">override</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-expert-info" rel="tag" title="see questions tagged &#39;expert-info&#39;">expert-info</span> <span class="post-tag tag-link-script" rel="tag" title="see questions tagged &#39;script&#39;">script</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jul '14, 05:28</strong></p><img src="https://secure.gravatar.com/avatar/530568ff96b9380fc92e410053efc97c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="314&#39;s gravatar image" /><p><span>314</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="314 has no accepted answers">0%</span></p></div></div><div id="comments-container-34726" class="comments-container"></div><div id="comment-tools-34726" class="comment-tools"></div><div class="clear"></div><div id="comment-34726-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34727"></span>

<div id="answer-container-34727" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34727-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34727-score" class="post-score" title="current number of votes">0</div><span id="post-34727-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Instead of this:</p><pre><code>pinfo.cols.info = &#39;stuff&#39;</code></pre><p>...try this instead:</p><pre><code>pinfo.cols.info:set(&#39;stuff&#39;)
pinfo.cols.info:fence()</code></pre><p>Note you need to be running Wireshark 1.10.6 or greater (the <code>fence()</code> function was added in 1.10.6).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '14, 07:31</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-34727" class="comments-container"></div><div id="comment-tools-34727" class="comment-tools"></div><div class="clear"></div><div id="comment-34727-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

