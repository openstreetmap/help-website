+++
type = "question"
title = "Dissector for CAN protocol"
description = '''Hello i&#x27;ve got an application protocol over CAN called CANSU. I want to write a custom dissector for it.  i&#x27;m trying to handle all CAN packets like this: void proto_reg_handoff_cansu(void) {  static dissector_handle_t cansu_handle;  cansu_handle = new_create_dissector_handle(dissect_cansu, proto_can...'''
date = "2015-11-29T23:15:00Z"
lastmod = "2015-12-01T02:04:00Z"
weight = 48065
keywords = [ "can" ]
aliases = [ "/questions/48065" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dissector for CAN protocol](/questions/48065/dissector-for-can-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48065-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48065-score" class="post-score" title="current number of votes">0</div><span id="post-48065-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello i've got an application protocol over CAN called CANSU. I want to write a custom dissector for it.</p><p>i'm trying to handle all CAN packets like this:</p><pre><code>void proto_reg_handoff_cansu(void)
{
    static dissector_handle_t cansu_handle;
    cansu_handle = new_create_dissector_handle(dissect_cansu, proto_cansu);
    dissector_add_for_decode_as(&quot;can&quot;,cansu_handle);
}</code></pre><p>but after wireshark starting i've got message:</p><pre><code>OOPS: dissector table &quot;can&quot; doesn&#39;t exist    
Protocol being registered is &quot;CANSU Protocol&quot;</code></pre><p>How can i capture whole can protocol for analyzing and processing?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-can" rel="tag" title="see questions tagged &#39;can&#39;">can</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Nov '15, 23:15</strong></p><img src="https://secure.gravatar.com/avatar/4c60eaad3bf660591697eba323786208?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="qmor&#39;s gravatar image" /><p><span>qmor</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="qmor has no accepted answers">0%</span></p></div></div><div id="comments-container-48065" class="comments-container"></div><div id="comment-tools-48065" class="comment-tools"></div><div class="clear"></div><div id="comment-48065-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48066"></span>

<div id="answer-container-48066" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48066-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48066-score" class="post-score" title="current number of votes">0</div><span id="post-48066-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The socket CAN dissector has a table named "can.subdissector" that allows other dissectors to register for CAN subdissection, maybe that's what you need.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Nov '15, 23:25</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-48066" class="comments-container"><span id="48067"></span><div id="comment-48067" class="comment"><div id="post-48067-score" class="comment-score"></div><div class="comment-text"><p>have tried, but</p><p>OOPS: dissector table "can.subdissector" doesn't exist</p></div><div id="comment-48067-info" class="comment-info"><span class="comment-age">(29 Nov '15, 23:48)</span> <span class="comment-user userinfo">qmor</span></div></div><span id="48069"></span><div id="comment-48069" class="comment"><div id="post-48069-score" class="comment-score"></div><div class="comment-text"><p>What version are you building with?</p></div><div id="comment-48069-info" class="comment-info"><span class="comment-age">(30 Nov '15, 01:28)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="48071"></span><div id="comment-48071" class="comment"><div id="post-48071-score" class="comment-score"></div><div class="comment-text"><p>i guess 2.1.0</p></div><div id="comment-48071-info" class="comment-info"><span class="comment-age">(30 Nov '15, 01:57)</span> <span class="comment-user userinfo">qmor</span></div></div><span id="48073"></span><div id="comment-48073" class="comment"><div id="post-48073-score" class="comment-score"></div><div class="comment-text"><p>So apparently the master branch. The table does exist in my copy of master (updated 10 minutes ago) and is used by several other dissectors.</p><p>I just rebuilt the dissectors concerned, and running the build did not generate that error message.</p><p>What OS and build mechanism (CMake, autotools or nmake) are you building on?</p><p>Have you tried the equivalent of a make dist-clean?</p></div><div id="comment-48073-info" class="comment-info"><span class="comment-age">(30 Nov '15, 03:28)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="48093"></span><div id="comment-48093" class="comment"><div id="post-48093-score" class="comment-score"></div><div class="comment-text"><p>i've cloned git repository 4 days ago and used cmake to build project. I've see thea source code contains "can.subdissector" table. Is using of dissector_add_for_decode_as are correct?</p></div><div id="comment-48093-info" class="comment-info"><span class="comment-age">(30 Nov '15, 07:44)</span> <span class="comment-user userinfo">qmor</span></div></div><span id="48094"></span><div id="comment-48094" class="comment not_top_scorer"><div id="post-48094-score" class="comment-score"></div><div class="comment-text"><p>can.subdissector has been around since Mar 18.</p><p><code>dissector_add_for_decode_as</code> is used by the other can subdissectors.</p><p>Looking at your code fragment, you don't need to make <code>cansu_handle</code> static, but I don't think that's the cause of your problem.</p><p>Are you building your dissector as a plugin or a "built-in"?</p></div><div id="comment-48094-info" class="comment-info"><span class="comment-age">(30 Nov '15, 08:12)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="48117"></span><div id="comment-48117" class="comment not_top_scorer"><div id="post-48117-score" class="comment-score"></div><div class="comment-text"><p>I'm so sorry. I've used new wireshark source to build plugin and then just copied it to already installed older wireshark version. For now i've build full wireshark and installed it to /tmp directory. For now i've got another problem - "No interfaces found". I've copied dumpcap locally to /tmp/bin directory and give all right that it need.</p></div><div id="comment-48117-info" class="comment-info"><span class="comment-age">(30 Nov '15, 23:12)</span> <span class="comment-user userinfo">qmor</span></div></div><span id="48120"></span><div id="comment-48120" class="comment not_top_scorer"><div id="post-48120-score" class="comment-score"></div><div class="comment-text"><p>I think the can.subdissector table is only in 2.x, so the plugin won't work on 1.2.x or older. To support your dissector on 1.12.x you'll need to build that version, modifying packet-socketcan to add a preference to allow your dissector to be used, then distribute the 1.12.x build you've made.</p><p>For your other problem you'll need to create a separate question.</p></div><div id="comment-48120-info" class="comment-info"><span class="comment-age">(01 Dec '15, 02:04)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-48066" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-48066-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

