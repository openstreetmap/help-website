+++
type = "question"
title = "What is &quot;Use External Network Name Resolver&quot; setting?"
description = '''I noticed a new setting on the Name Resolution menu of Wireshark 1.9.0 development versions called &quot;Use External Network Name Resolver.&quot; It was enabled by default. What is the purpose of this setting? On my system, enabling this setting seems to result in Wireshark making DNS PTR queries even when V...'''
date = "2012-07-09T19:53:00Z"
lastmod = "2012-07-10T08:06:00Z"
weight = 12542
keywords = [ "ptr", "dns" ]
aliases = [ "/questions/12542" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What is "Use External Network Name Resolver" setting?](/questions/12542/what-is-use-external-network-name-resolver-setting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12542-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12542-score" class="post-score" title="current number of votes">0</div><span id="post-12542-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I noticed a new setting on the Name Resolution menu of Wireshark 1.9.0 development versions called "Use External Network Name Resolver." It was enabled by default. What is the purpose of this setting? On my system, enabling this setting seems to result in Wireshark making DNS PTR queries even when View &gt; Name Resolution &gt; Enable for Network Layer is unchecked.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ptr" rel="tag" title="see questions tagged &#39;ptr&#39;">ptr</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '12, 19:53</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-12542" class="comments-container"></div><div id="comment-tools-12542" class="comment-tools"></div><div class="clear"></div><div id="comment-12542-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12543"></span>

<div id="answer-container-12543" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12543-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12543-score" class="post-score" title="current number of votes">0</div><span id="post-12543-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please see <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7380">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7380</a> in short make it possible to select if name resolution is to be made trough DNS lookups or not.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jul '12, 20:54</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-12543" class="comments-container"><span id="12544"></span><div id="comment-12544" class="comment"><div id="post-12544-score" class="comment-score"></div><div class="comment-text"><p>So, if I understand correctly:</p><p>View &gt; Name Resolution &gt; Enable for Network Layer should determine <em>IF</em> name resolution is done.</p><p>View &gt; Name Resolution &gt; Use External Name Resolver should determine <em>HOW</em> name resolution is done.</p><p>So no Layer 3 name lookups should be done if "Enable for Network Layer" is unchecked, regardless of whether "Use External Name Resolver" is checked or not?</p><p>Am I seeing a bug in this new feature? When I enable "Use External Name Resolver," I see reverse DNS lookups even though "Enable for Network Layer" is unchecked.</p></div><div id="comment-12544-info" class="comment-info"><span class="comment-age">(09 Jul '12, 21:15)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div><span id="12545"></span><div id="comment-12545" class="comment"><div id="post-12545-score" class="comment-score"></div><div class="comment-text"><p>Yes looks like it.</p></div><div id="comment-12545-info" class="comment-info"><span class="comment-age">(09 Jul '12, 21:16)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="12546"></span><div id="comment-12546" class="comment"><div id="post-12546-score" class="comment-score"></div><div class="comment-text"><p>Judging from the discussion on <a href="http://bugs.wireshark.org">bugs.wireshark.org</a>, this is still under active development. Should I file a bug report, or wait until the initial implementation settles down?</p></div><div id="comment-12546-info" class="comment-info"><span class="comment-age">(09 Jul '12, 21:24)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div><span id="12547"></span><div id="comment-12547" class="comment"><div id="post-12547-score" class="comment-score"></div><div class="comment-text"><p>"Should I file a bug report, or wait until the initial implementation settles down?"</p><p>The answer to that question is "no". :-) You should comment on the <em>existing</em> bug, as it's not closed yet.</p></div><div id="comment-12547-info" class="comment-info"><span class="comment-age">(09 Jul '12, 21:49)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="12561"></span><div id="comment-12561" class="comment"><div id="post-12561-score" class="comment-score"></div><div class="comment-text"><p>The new preference wasn't being followed when translating hostnames into IP addresses. That's fixed in r43647.</p></div><div id="comment-12561-info" class="comment-info"><span class="comment-age">(10 Jul '12, 08:06)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-12543" class="comment-tools"></div><div class="clear"></div><div id="comment-12543-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

