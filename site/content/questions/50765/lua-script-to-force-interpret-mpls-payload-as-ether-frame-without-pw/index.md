+++
type = "question"
title = "lua script to force interpret mpls payload as ether frame without PW"
description = '''Trying to have a lua script to interpret mpls payload as ether frame without control word. I have to match certain mpls label value. Is there any way to match all label values? Looks like dissectortable:add(pattern, dissector) doesn&#x27;t like regex in pattern Here is the script. local dis_eth = Dissect...'''
date = "2016-03-08T07:52:00Z"
lastmod = "2016-03-08T08:38:00Z"
weight = 50765
keywords = [ "lua", "mpls" ]
aliases = [ "/questions/50765" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [lua script to force interpret mpls payload as ether frame without PW](/questions/50765/lua-script-to-force-interpret-mpls-payload-as-ether-frame-without-pw)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50765-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Trying to have a lua script to interpret mpls payload as ether frame without control word.</p><p>I have to match certain mpls label value. Is there any way to match all label values? Looks like <code>dissectortable:add(pattern, dissector)</code> doesn't like regex in <code>pattern</code></p><p>Here is the script.</p><pre><code>local dis_eth = Dissector.get(&quot;eth&quot;)
local mpls_table = DissectorTable.get(&quot;mpls.label&quot;)
mpls_table:add(261,dis_eth)</code></pre></div><div id="question-tags" class="tags-container tags">lua mpls</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Mar '16, 07:52</strong></p><img src="https://secure.gravatar.com/avatar/b7590de43adb375f2d9c6ba1f98b72cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yacare&#39;s gravatar image" /><p>yacare<br />
<span class="score" title="21 reputation points">21</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yacare has no accepted answers">0%</span></p></div></div><div id="comments-container-50765" class="comments-container"></div><div id="comment-tools-50765" class="comment-tools"></div><div class="clear"></div><div id="comment-50765-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50766"></span>

<div id="answer-container-50766" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50766-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>It does not like a pattern because the "pattern" values in the DissectorTable are indices to it, so using a pattern would require a change of the lookup method from the current plain</p><pre><code>dissector_to_use = table[value_x]</code></pre><p>to a more complex (and thus much slower) procedure involving regex-based matching of the plain <code>value_x</code> against the list of all defined key values of an associative table where the key values would be the regexes.</p><p>Repeating my suggestion in the follow-up of <a href="https://ask.wireshark.org/questions/49875/how-to-make-wireshark-parse-ethernet-frame-over-mpls-as-no-cw/49881">my answer to your older question</a>, you may want to file a "nice to have" category bug at Wireshark bugzilla, asking for a generic mechanism allowing some kind of reserved index value (such as <code>other</code>) to be used to set a default dissector (using Decode as... or Lua DissectorTable:add) for a given DissectorTable, which could still be overridden by the individual ones (meaning that if nothing would be found in the table for the given value, the default dissector would be used).</p><p>You may also ask for the regex way, maybe there <em>is</em> a way to implement use of regex (or numeric ranges) which would not cause a big slowdown, I'm not that deep in programming.</p><p>In any case, it is a matter for bugzilla, not for Q&amp;A.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Mar '16, 08:38</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-50766" class="comments-container"><span id="50768"></span><div id="comment-50768" class="comment"><div id="post-50768-score" class="comment-score"></div><div class="comment-text"><p>Thanks Sindy. I am new to wireshark. Will check how to file a "nice to have" bug.</p><p>Trying to find an immediate way to solve my need as for now. Where can I find all the available DissectorTable for mpls? Trying to use something like DissectorTable.get("mpls.ttl"), but the DissectorTable doesn't exist.</p></div><div id="comment-50768-info" class="comment-info"><span class="comment-age">(08 Mar '16, 09:01)</span> yacare</div></div><span id="50770"></span><div id="comment-50770" class="comment"><div id="post-50770-score" class="comment-score"></div><div class="comment-text"><p>"All the available payload dissector tables for MPLS" are the single one which uses MPLS label as an index, as you can see when you click <code>Decode as...</code>. The dissector tables for choosing payload dissector per transport's field are hardcoded - normally, the most logical field is chosen, which is the label in case of MPLS. I. e. you cannot arbitrarily choose any field of the transport protocol and dynamically attach to it a dissector table. The reason is once again the processing speed, if done that way, each dissector would have to go field by field and check whether by chance a table isn't hooked to it.</p></div><div id="comment-50770-info" class="comment-info"><span class="comment-age">(08 Mar '16, 12:58)</span> sindy</div></div><span id="56552"></span><div id="comment-56552" class="comment"><div id="post-56552-score" class="comment-score"></div><div class="comment-text"><p>we were using a slight modification to this:</p><p><code>local dis_eth = Dissector.get("eth") local mpls_table = DissectorTable.get("mpls.label") for label=0,1048575 do   mpls_table:add(label,dis_eth) end</code></p><p>now, in the recent wireshark versions (cannot tell when it started) we receive the error</p><p><code>Lua: Error during loading: [string "path"]:1: bad argument #1 to 'get' (Dissector_get: No such dissector)</code></p><p>any hint or idea what we may do to make this working again ?</p></div><div id="comment-56552-info" class="comment-info"><span class="comment-age">(21 Oct '16, 02:26)</span> x42</div></div><span id="56553"></span><div id="comment-56553" class="comment"><div id="post-56553-score" class="comment-score"></div><div class="comment-text"><p>@x42, your post was not an Answer to the original Question, so I've converted it into a Comment.</p><p>The issue you are facing is related to a change of ethernet handling in 2.2.0. You can find all you need in answers to <a href="https://ask.wireshark.org/questions/56432/how-to-find-the-ethernet-dissector">this</a> and <a href="https://ask.wireshark.org/questions/56469/renaming-of-eth-dissector-to-eth_withoutfcs">this</a> Question.</p></div><div id="comment-56553-info" class="comment-info"><span class="comment-age">(21 Oct '16, 02:32)</span> sindy</div></div><span id="56555"></span><div id="comment-56555" class="comment"><div id="post-56555-score" class="comment-score"></div><div class="comment-text"><p>cool ... thanks a lot for your info :-)</p><p>so we have simply substituted "eth" in our script with "eth_withoutfcs" and are able to work again.</p><p>our script IS working for all mpls-labels ... well it's ugly, since we have a huge loop, but wireshark seem to be able to handle this very nicely ;-)</p><p>we are still facing a slight complication detemining whether we have a control-word (cw) present or not: mpls-traffic flowing through our core-routers contain a mix of frames with and without cw.</p><p>it is not a big problem since we are planning to turn on cw's on all traffic, yet we may post a detailed question about this in future ...</p></div><div id="comment-56555-info" class="comment-info"><span class="comment-age">(21 Oct '16, 02:53)</span> x42</div></div><span id="56556"></span><div id="comment-56556" class="comment not_top_scorer"><div id="post-56556-score" class="comment-score"></div><div class="comment-text"><blockquote><p>so we have simply substituted "eth" in our script with "eth_withoutfcs" and are able to work again.</p></blockquote><p>If you do not need that your Lua dissector is backward compatible, it is enough indeed.</p><blockquote><p>we may post a detailed question about this in future ...</p></blockquote><p>Before doing that, please have a look at <a href="https://ask.wireshark.org/questions/49875/how-to-make-wireshark-parse-ethernet-frame-over-mpls-as-no-cw">this Question</a>:</p></div><div id="comment-56556-info" class="comment-info"><span class="comment-age">(21 Oct '16, 03:00)</span> sindy</div></div><span id="56557"></span><div id="comment-56557" class="comment not_top_scorer"><div id="post-56557-score" class="comment-score"></div><div class="comment-text"><p>great ... thanks a lot again for your extremely quick and competent answers :-)</p></div><div id="comment-56557-info" class="comment-info"><span class="comment-age">(21 Oct '16, 03:03)</span> x42</div></div></div><div id="comment-tools-50766" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-50766-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

