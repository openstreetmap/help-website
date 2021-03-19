+++
type = "question"
title = "How to get a reference to an existing heuristic dissector in LUA (in order to wrap RTPS) ?"
description = '''Hello, We are trying to create a chained dissector in LUA (as described in Wireshark wiki page) but we are not able to get a reference to existing heuristic dissector ! :( For &quot;normal&quot; (= non-heuristic) dissector, it works fine. In our case, we try to wrap RTPS (Real-Time Publish-Subscribe) protocol...'''
date = "2017-06-07T07:11:00Z"
lastmod = "2017-06-14T13:47:00Z"
weight = 61824
keywords = [ "chained-dissector", "lua", "rtps" ]
aliases = [ "/questions/61824" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to get a reference to an existing heuristic dissector in LUA (in order to wrap RTPS) ?](/questions/61824/how-to-get-a-reference-to-an-existing-heuristic-dissector-in-lua-in-order-to-wrap-rtps)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61824-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61824-score" class="post-score" title="current number of votes">0</div><span id="post-61824-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>We are trying to create a chained dissector in LUA (as described in Wireshark wiki page) but we are not able to get a reference to existing heuristic dissector ! :( For "normal" (= non-heuristic) dissector, it works fine. In our case, we try to wrap RTPS (Real-Time Publish-Subscribe) protocol.</p><p>We looked at source code (in epan/dissectors/packet-rtps.c) and we think we are using expected name. Unfortunately, with Wireshark v2.2.7, we are not able to get UDP heuristic dissector table, nor RTPS dissector. It seems that DissectorTable.get() is only used for "normal" dissector (it triggers an error for heuristic "udp" but not for normal "udp.port"). And Dissector.get("rtps") fails too: no such dissector. But Dissector.get("rtitcp") works fine. We can notice that RTPS is not contained in Dissector.list().</p><p>Q1) what are we missing ?</p><p>Q2) is it a bug in Wireshark ?</p><p>Thanks for your help, Contrib</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-chained-dissector" rel="tag" title="see questions tagged &#39;chained-dissector&#39;">chained-dissector</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-rtps" rel="tag" title="see questions tagged &#39;rtps&#39;">rtps</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jun '17, 07:11</strong></p><img src="https://secure.gravatar.com/avatar/ccf0e5d065ba0cf447fb96b746fce7d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lua%20Hobbyist&#39;s gravatar image" /><p><span>Lua Hobbyist</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lua Hobbyist has no accepted answers">0%</span></p></div></div><div id="comments-container-61824" class="comments-container"></div><div id="comment-tools-61824" class="comment-tools"></div><div class="clear"></div><div id="comment-61824-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="61825"></span>

<div id="answer-container-61825" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61825-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61825-score" class="post-score" title="current number of votes">0</div><span id="post-61825-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The Wireshark Lua <a href="https://wiki.wireshark.org/Lua/Examples">Examples</a> wiki page provides a <a href="https://wiki.wireshark.org/Lua/Examples?action=AttachFile&amp;do=get&amp;target=dissector.lua">dissector.lua</a> file written by Hadriel Kaplan that illustrates how to register a heuristic Lua dissector with UDP, namely:</p><pre><code>Line 587: dns:register_heuristic(&quot;udp&quot;,heur_dissect_dns)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jun '17, 07:54</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-61825" class="comments-container"><span id="61847"></span><div id="comment-61847" class="comment"><div id="post-61847-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/402/cmaynard">@cmaynard</a> Thanks, but we already found this example.</p><p>You may have been confused by the title (and my "poor" english, sorry ^_^): here, <em>"reference"</em> stands for <strong>LUA (runtime) object</strong>, not for documentation pointer.</p><p>But as described in my previous post, we need to wrap (aka create a "chained dissector" for) an existing protocol (here: <strong>RTPS</strong>). In order to do so, we need to:</p><ol><li>get original dissector (=&gt; rtps)</li><li>create a new dissector (=&gt; rtpswrap)</li><li>in wrapper body, call original dissector and then add our custom stuff</li><li>register this "new" wrapper</li></ol><p>Unfortunately, our problem is the first step: based on LUA API, it seems there are 2 ways to get original dissector:</p><ul><li><strong>1st way:</strong> get a dissector table (thanks to: <code>DissectorTable.get()</code>) then get existing dissector thanks to <code>dtbl:get_dissector()</code></li><li><strong>2nd way:</strong> call directly <code>Dissector.get()</code></li></ul><p>It turns out that in our case, with RTPS protocol, <strong>both ways return an error</strong> ! :(</p><p>We checked that in Wireshark GUI menu: <code>View</code> -&gt; <code>Internals</code> -&gt; <code>Dissector Tables</code>, RTPS protocol is contained in <strong>UDP</strong>'s <code>Heuristic Table</code> (<strong>and nowhere else</strong>). Consequently, following 1st way, we would need to be able to get UDP heuristic dissector table in LUA script, but <code>DissectorTable.get("udp")</code> triggers an error. It seems that this function should only be used for "normal" dissector, one registered to a fix port for example (<strong>so not heuristic</strong>). We also checked that <code>"udp"</code> is present in <code>DissectorTable.heuristic_list()</code> but it should only be used with <code>Proto:register_heuristic()</code> and so we can not access to original RTPS dissector.</p><p>Following 2nd way, we tried to call <code>Dissector.get("rtps")</code> but here again, an error is triggered: <code>no such dissector</code>. We noticed that <code>"rtps"</code> is not present in <code>Dissector.list()</code> and it seems weird.</p><p>Then, we looked at source code: <a href="https://github.com/wireshark/wireshark/blob/wireshark-2.2.7/epan/dissectors/packet-rtps.c#L11544">wireshark-2.2.7/epan/dissectors/packet-rtps.c#L11544</a> and we noticed another protocol implemented alongside RTPS: <code>"rtitcp"</code>. It turns out that <code>"rtitcp"</code> is present in <code>Dissector.list()</code> and call to <code>Dissector.get("rtitcp")</code> works fine (no error contrary to <code>"rtps"</code>).</p><p>Consequently, it seems that <code>"rtps"</code> protocol implementation missed something compare to <code>"rtitcp"</code>. In order to be able to access to original dissector in LUA, we may need to register it to a fix (dummy) port ? or add a new function in LUA API in order to get a heuristic dissector ?</p><p>Or maybe there is a 3rd way to get existing dissector ?</p></div><div id="comment-61847-info" class="comment-info"><span class="comment-age">(07 Jun '17, 14:16)</span> <span class="comment-user userinfo">Lua Hobbyist</span></div></div></div><div id="comment-tools-61825" class="comment-tools"></div><div class="clear"></div><div id="comment-61825-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="61937"></span>

<div id="answer-container-61937" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61937-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61937-score" class="post-score" title="current number of votes">0</div><span id="post-61937-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Replying to my own questions: it seems there are limitations in current Wireshark LUA API</p><ol><li>no way to get a dissector that has <strong>only</strong> been registered as "heuristic" (EXAMPLE: RTPS)</li><li>no way to replace an existing heuristic dissector in a dissector table by a wrapper implemented in LUA. There is a way to <strong><em>add</em></strong> a heuristic dissector, but what if original dissector is called first ? wrapper will never be called... <strong>So we would need to be able to overwrite objects in heuristic dissector table or to change order in this list.</strong></li></ol><p>Concerning RTPS, a workaround to first previous limitation is below: <strong><em>(/!\ need to patch source code + recompile)</em></strong></p><p><strong>wireshark-2.2.7_RTPS_registration_for_LUA_access.patch</strong></p><hr /><pre><code>--- wireshark-2.2.7_OLD/epan/dissectors/packet-rtps.c
+++ wireshark-2.2.7_NEW/epan/dissectors/packet-rtps.c
@@ -11534,10 +11534,15 @@
               &amp;enable_topic_info);
register_init_routine(rtps_init);

rtps_type_name_table = register_dissector_table(&quot;rtps.type_name&quot;, &quot;RTPS Type Name&quot;,
       proto_rtps, FT_STRING, BASE_NONE);
+
+  /* In order to get this dissector in LUA (aka &quot;chained-dissector&quot;) */
+  register_dissector(&quot;rtps_udp&quot;, dissect_rtps_udp, proto_rtps);
+  register_dissector(&quot;rtps_tcp&quot;, dissect_rtps_tcp, proto_rtps);
+  register_dissector(&quot;rtps_rtitcp&quot;, dissect_rtps_rtitcp, proto_rtps);
 }


 void proto_reg_handoff_rtps(void) {
   heur_dissector_add(&quot;rtitcp&quot;, dissect_rtps_rtitcp, &quot;RTPS over RTITCP&quot;, &quot;rtps_rtitcp&quot;, proto_rtps, HEURISTIC_ENABLE);</code></pre><hr /><p>Thanks to previous patch, we are able to get access to original RTPS dissector in LUA script thanks to <code>Dissector.get("rtps_udp")</code>.</p><p>There is still the second limitation: this time, a workaround is to use UDP dissector table and register the new wrapper to a specific UDP port.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '17, 14:54</strong></p><img src="https://secure.gravatar.com/avatar/ccf0e5d065ba0cf447fb96b746fce7d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lua%20Hobbyist&#39;s gravatar image" /><p><span>Lua Hobbyist</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lua Hobbyist has no accepted answers">0%</span></p></div></div><div id="comments-container-61937" class="comments-container"><span id="62034"></span><div id="comment-62034" class="comment"><div id="post-62034-score" class="comment-score"></div><div class="comment-text"><p>Previous patch has been submitted, see: <a href="https://code.wireshark.org/review/#/c/22137/">https://code.wireshark.org/review/#/c/22137/</a></p></div><div id="comment-62034-info" class="comment-info"><span class="comment-age">(14 Jun '17, 13:47)</span> <span class="comment-user userinfo">Lua Hobbyist</span></div></div></div><div id="comment-tools-61937" class="comment-tools"></div><div class="clear"></div><div id="comment-61937-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

