+++
type = "question"
title = "Can&#x27;t apply/use &quot;obscure&quot; protocol decoder (DirectPlay)"
description = '''I&#x27;m trying to debug the DirectPlay protocol used by some old DirectX games (https://wiki.wireshark.org/DPlay). Neither my own capture, nor the example capture on the link above, is identified as anything other than generic UDP by Wireshark. I&#x27;ve checked that the DPLAY protocol is enabled (Analyze -&amp;...'''
date = "2016-08-21T10:04:00Z"
lastmod = "2016-08-21T12:04:00Z"
weight = 55027
keywords = [ "directplay", "dplay", "decoder" ]
aliases = [ "/questions/55027" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can't apply/use "obscure" protocol decoder (DirectPlay)](/questions/55027/cant-applyuse-obscure-protocol-decoder-directplay)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55027-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55027-score" class="post-score" title="current number of votes">0</div><span id="post-55027-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to debug the DirectPlay protocol used by some old DirectX games (<a href="https://wiki.wireshark.org/DPlay).">https://wiki.wireshark.org/DPlay).</a></p><p>Neither my own capture, nor the example capture on the link above, is identified as anything other than generic UDP by Wireshark.</p><p>I've checked that the DPLAY protocol is enabled (Analyze -&gt; Enabled Protocols).</p><p>When trying to bypass the heuristic protocol detection and manually choose the DPLAY decoder ("Decode As..."), I cannot even find DPLAY in the list of available decoders.</p><p>I've tried all this in Wireshark 1.12 as well as 2.0.4; same results.</p><p>Had a brief look at packet-dplay.c in the Wireshark source, but I'm not very skilled at C++ nor am I familiar with Wireshark's internals at all, so that didn't give me any clues, unfortunately.</p><p>What could be the reason for not being able to "Decode As" DPLAY?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-directplay" rel="tag" title="see questions tagged &#39;directplay&#39;">directplay</span> <span class="post-tag tag-link-dplay" rel="tag" title="see questions tagged &#39;dplay&#39;">dplay</span> <span class="post-tag tag-link-decoder" rel="tag" title="see questions tagged &#39;decoder&#39;">decoder</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Aug '16, 10:04</strong></p><img src="https://secure.gravatar.com/avatar/785123f99b62993072c4c6c0988131b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sheancell&#39;s gravatar image" /><p><span>Sheancell</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sheancell has no accepted answers">0%</span></p></div></div><div id="comments-container-55027" class="comments-container"></div><div id="comment-tools-55027" class="comment-tools"></div><div class="clear"></div><div id="comment-55027-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55029"></span>

<div id="answer-container-55029" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55029-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55029-score" class="post-score" title="current number of votes">0</div><span id="post-55029-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Probably the heuristics fail to classify these packets as DPlay. This is the relevant code, where <code>tvb</code> contains the packet data and is called for every packet. Either it calls the dissection functions and returns <code>TRUE</code> or returns <code>FALSE</code>. You can read the packet data and deduce how the heuristics fail.</p><pre><code>1123 static gboolean heur_dissect_dplay(tvbuff_t tvb, packet_info pinfo, proto_tree tree, void data U)
1124 {
1125     guint32 dplay_id, token;
1126 
1127     if(tvb_captured_length(tvb) &lt; 25)
1128         return FALSE;
1129 
1130     / The string play = 0x706c6179 /
1131     dplay_id = tvb_get_letohl(tvb, 20);
1132     if( dplay_id == 0x706c6179) {
1133         dissect_dplay(tvb, pinfo, tree);
1134         return TRUE;
1135     }
1136 
1137 
1138     / There is a player to player message that does not contain &quot;play&quot; /
1139     token = tvb_get_letohl(tvb, 0);
1140     token = (token &amp; 0xfff00000) &gt;&gt; 20;
1141     if (token == 0xfab || token == 0xbab || token == 0xcab) {
1142       / Check the s_addr_in structure /
1143       if (tvb_get_letohs(tvb, 4) == WINSOCK_AF_INET) {
1144         int offset;
1145         for (offset = 12; offset &lt;= 20; offset++)
1146           if (tvb_get_guint8(tvb, offset) != 0)
1147             return FALSE;
1148 
1149         dissect_dplay_player_msg(tvb, pinfo, tree);
1150         return TRUE;
1151       }
1152     }
1153 
1154     return FALSE;
1155 }</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Aug '16, 12:04</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-55029" class="comments-container"></div><div id="comment-tools-55029" class="comment-tools"></div><div class="clear"></div><div id="comment-55029-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

