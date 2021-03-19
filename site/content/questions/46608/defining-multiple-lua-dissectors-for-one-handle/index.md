+++
type = "question"
title = "Defining multiple LUA dissectors for one handle"
description = '''I&#x27;m having a packet type that contains one of two different versions of a certain protocol. One dump only consists of packets of one type. So I&#x27;ve defined two different protocol dissectors in lua. Initialization is done by the following code. gatt_table = DissectorTable.get(&quot;btatt.handle&quot;) gatt_tabl...'''
date = "2015-10-16T04:32:00Z"
lastmod = "2015-11-07T05:16:00Z"
weight = 46608
keywords = [ "lua", "dissector", "plugin" ]
aliases = [ "/questions/46608" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Defining multiple LUA dissectors for one handle](/questions/46608/defining-multiple-lua-dissectors-for-one-handle)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46608-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46608-score" class="post-score" title="current number of votes">0</div><span id="post-46608-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm having a packet type that contains one of two different versions of a certain protocol. One dump only consists of packets of one type. So I've defined two different protocol dissectors in lua. Initialization is done by the following code.</p><pre><code>gatt_table = DissectorTable.get(&quot;btatt.handle&quot;)
gatt_table:add(0x1234, myprotov1)</code></pre><p>The second one is added similarly in it's own lua file.</p><pre><code>gatt_table = DissectorTable.get(&quot;btatt.handle&quot;)
gatt_table:add(0x1234, myprotov2)</code></pre><p>My idea was to select which version to use by enabling only the used protocol via the GUI. Because each dump only consists of one version.</p><p>If I disable the first one everything works fine. But if I disable the second one the first one is not used but the default dissector kicks in.</p><p>So I guess the initialization stuff for both dissectors is run at startup and the second one overwrites the first.</p><p>So my question basically is: Is there a "best practice" how you could have two dissectors with the identical DissectorTable Entry and choose between them? (Deciding dynamically based on payload is currently not an option). Currently I have to replace the file in the plugin folder and restart Wireshark which is a pretty poor user experience.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Oct '15, 04:32</strong></p><img src="https://secure.gravatar.com/avatar/357eeb7795f5c0d1910f22757ef2109f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="heine&#39;s gravatar image" /><p><span>heine</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="heine has no accepted answers">0%</span></p></div></div><div id="comments-container-46608" class="comments-container"></div><div id="comment-tools-46608" class="comment-tools"></div><div class="clear"></div><div id="comment-46608-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47357"></span>

<div id="answer-container-47357" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47357-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47357-score" class="post-score" title="current number of votes">0</div><span id="post-47357-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, you should add your dissectors to "UUID" table, so you do not need touch "handle" table. Handle table is useful only for DecodeAs, so no dissector should assign any value of them, because those values may changed anytime. Also you should use DecodeAs instead of disabling/enabling your dissectors. You can decode payload as by handle or/and UUID. The best practise is capture BLE with Primary (and secondary) Service Discovery, so Wireshark know what UUID is assign to handle. This will solve your problem with different attributes assigned to the same handle.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '15, 05:16</strong></p><img src="https://secure.gravatar.com/avatar/6eabf35b1168a8242bb2d69db18a8a7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Micha%C5%82%20%C5%81ab%C4%99dzki&#39;s gravatar image" /><p><span>Michał Łabędzki</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michał Łabędzki has one accepted answer">8%</span></p></div></div><div id="comments-container-47357" class="comments-container"></div><div id="comment-tools-47357" class="comment-tools"></div><div class="clear"></div><div id="comment-47357-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

