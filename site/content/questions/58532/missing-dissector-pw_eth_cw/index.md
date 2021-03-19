+++
type = "question"
title = "missing dissector pw_eth_cw ?"
description = '''in wireshark version 1.x the following script works without problems: dis_eth_pw = Dissector.get(&quot;pw_eth_cw&quot;) local mpls_table = DissectorTable.get(&quot;mpls.label&quot;) for label=0,1048575 do  mpls_table:add(label,dis_eth_pw) end  how should we modify the call to Dissector.get(&quot;pw_eth_cw&quot;) in order to be a...'''
date = "2017-01-05T02:13:00Z"
lastmod = "2017-01-08T06:26:00Z"
weight = 58532
keywords = [ "lua", "dissector", "mpls" ]
aliases = [ "/questions/58532" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [missing dissector pw\_eth\_cw ?](/questions/58532/missing-dissector-pw_eth_cw)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58532-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>in wireshark version 1.x the following script works without problems:</p><pre><code>dis_eth_pw = Dissector.get(&quot;pw_eth_cw&quot;)
local mpls_table = DissectorTable.get(&quot;mpls.label&quot;)
for label=0,1048575 do
  mpls_table:add(label,dis_eth_pw)
end</code></pre><p>how should we modify the call to <code>Dissector.get("pw_eth_cw")</code> in order to be able to use it with wireshark 2.x ?</p><p><code>Lua: Error during loading: (Dissector_get: No such dissector)</code></p></div><div id="question-tags" class="tags-container tags">lua dissector mpls</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jan '17, 02:13</strong></p><img src="https://secure.gravatar.com/avatar/742ba5366f391cc1422562fa87e3665b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="x42&#39;s gravatar image" /><p>x42<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="x42 has no accepted answers">0%</span></p></div></div><div id="comments-container-58532" class="comments-container"></div><div id="comment-tools-58532" class="comment-tools"></div><div class="clear"></div><div id="comment-58532-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="58540"></span>

<div id="answer-container-58540" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58540-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think you have to try your luck with <code>pw_eth_heuristic</code> instead.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jan '17, 09:52</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-58540" class="comments-container"><span id="58542"></span><div id="comment-58542" class="comment"><div id="post-58542-score" class="comment-score"></div><div class="comment-text"><p><code>pw_eth_heuristic</code> does not help us in our case, sorry ...</p><p>the reason why we are forced to write own lua-scripts to begin with is that the heuristic for mpls is probably limited to the case of ipv4 frames and does not recognize all our embedded ipv6-frames correctly.</p><p>so currently we would be limited to use wireshark 1.x together with lua-scripts that explicitely use the <code>pw_eth_cw</code> and <code>pw_eth_nocw</code> dissectors ?</p><p>otherwise we would humbly ask you - the wireshark-gurus - to extend the heuristic to include cases where the mpls payload consists of ipv6-frames ...</p></div><div id="comment-58542-info" class="comment-info"><span class="comment-age">(05 Jan '17, 11:12)</span> x42</div></div><span id="58544"></span><div id="comment-58544" class="comment"><div id="post-58544-score" class="comment-score"></div><div class="comment-text"><p>x42, Open a bug with your pcap file</p></div><div id="comment-58544-info" class="comment-info"><span class="comment-age">(05 Jan '17, 12:27)</span> Alexis La Go...</div></div><span id="58549"></span><div id="comment-58549" class="comment"><div id="post-58549-score" class="comment-score"></div><div class="comment-text"><p>thanks ... bug has been reported <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13295">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13295</a></p></div><div id="comment-58549-info" class="comment-info"><span class="comment-age">(05 Jan '17, 14:51)</span> x42</div></div><span id="58554"></span><div id="comment-58554" class="comment"><div id="post-58554-score" class="comment-score"></div><div class="comment-text"><blockquote><p>to extend the heuristic to include cases where the mpls payload consists of ipv6-frames ...</p></blockquote><p>It already does take IPv6 into consideration, according to BCP 4928, RFC 4385 and RFC 4448. I'll go and have a look at the sample capture to see what it does do.</p></div><div id="comment-58554-info" class="comment-info"><span class="comment-age">(05 Jan '17, 23:39)</span> Jaap ♦</div></div><span id="58563"></span><div id="comment-58563" class="comment"><div id="post-58563-score" class="comment-score"></div><div class="comment-text"><p>you are absolutely right in this point :-)</p><p>please also note the following bug which shows another case of mpls misinterpretation: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13301">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13301</a></p><p>seemingly mpls heuristic is very tricky indeed ...</p></div><div id="comment-58563-info" class="comment-info"><span class="comment-age">(06 Jan '17, 08:48)</span> x42</div></div><span id="58570"></span><div id="comment-58570" class="comment not_top_scorer"><div id="post-58570-score" class="comment-score"></div><div class="comment-text"><p>sometime along the way lines like</p><pre><code>register_dissector(&quot;pw_eth_cw&quot;, ...);
register_dissector(&quot;pw_eth_nocw&quot;, ...);</code></pre><p>were removed from epan/dissectors/packet-pw-eth.c</p><p>any strong reasons for doing so ? maybe we could simply get them back again ?</p></div><div id="comment-58570-info" class="comment-info"><span class="comment-age">(06 Jan '17, 15:02)</span> x42</div></div><span id="58577"></span><div id="comment-58577" class="comment not_top_scorer"><div id="post-58577-score" class="comment-score"></div><div class="comment-text"><p>it would seem that the reason for removing many <code>register_dissector()</code> code-lines given in</p><p><a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commitdiff;h=7ca04728c35560530304e7f2266bc9f01e020267">https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commitdiff;h=7ca04728c35560530304e7f2266bc9f01e020267</a></p><p>namely:</p><pre><code>Just use Decode As directly.
Also replace &quot;registered&quot; dissectors which just the creation of a handle 
since the dissectors really don&#39;t need to be &quot;found&quot; outside of themselves.</code></pre><p>could be arguable.</p><p>the important and regrettable side-effect thereof is that we loose the ability to use these dissectors in user-defined lua-scripts and implement or experiment with different mpls-heuristics ?</p><p>i would therefore suggest, that all mpls-related <code>register_dissector()</code> calls should be inserted back into the source code again ...</p></div><div id="comment-58577-info" class="comment-info"><span class="comment-age">(07 Jan '17, 05:12)</span> x42</div></div><span id="58578"></span><div id="comment-58578" class="comment not_top_scorer"><div id="post-58578-score" class="comment-score"></div><div class="comment-text"><p>Can't look ut up at the moment but do we have a function find protocol by filter name? Or somthing similar.</p></div><div id="comment-58578-info" class="comment-info"><span class="comment-age">(07 Jan '17, 07:44)</span> Anders ♦</div></div><span id="58582"></span><div id="comment-58582" class="comment not_top_scorer"><div id="post-58582-score" class="comment-score"></div><div class="comment-text"><p>please also consider the following argument as to why the mpls-dissectors like e.g. "<code>pw_eth_cw</code>" or "<code>pw_eth_nocw</code>" etc. ought to be available and callable from lua:</p><p>the reason why mpls-heuristics in wireshark (or other sniffers) has fundamental problems decoding the mpls-payload correctly, come from the simple fact that - as you probably all know very well - the mpls-header does not caontain any "type-field" which would define what kind of "protocol-over-mpls" will follow in the payload.</p><p>"protocol" might be "ethernet" (pw with or without cw) but also "ipv4" or "ipv6" or maybe even something completely different like e.g. "fabricpath" ;-)</p><p>wireshark <em>could</em> attempt to analyze different length-fields, checksums or god knows which other parameters and fields from all potential "protocols" in order to perform a successful identification.</p><p>when, however, some of these length-fields, checksums etc are corrupt or errornous, then the poor heuristic would have no earthly possibility to determine which "protocol" is being transported over mpls ...</p><p>so probably the only practical solution to be able to perform a successful dissection of a "protocol" in the presence of corrupt and/or errournous protocol-fields would be to have the knowledge of the "protocol" <em>beforehand</em> - for instance throgh the gui-function 'decode as ...' or through a lua-script.</p><p>in cases, where the number of mpls-labels is large, it is surely more user-friendly to use a lua-script (or possibly other global mpls dissection-settings) instead of manually define a large number of 'decode as ...' rules.</p><p>this is the reason, why it might be a good idea to be able to access all different dissectors via lua in addition of having a strong heuristic ...<br />
</p></div><div id="comment-58582-info" class="comment-info"><span class="comment-age">(07 Jan '17, 12:40)</span> x42</div></div></div><div id="comment-tools-58540" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-58540-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="58594"></span>

<div id="answer-container-58594" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58594-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>thanks to michael mann and anders broman the missing mpls-dissectors (<code>pw_eth_cw</code>, <code>pw_eth_nocw</code>, etc.) have now been merged back into the wireshark source-code :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '17, 06:26</strong></p><img src="https://secure.gravatar.com/avatar/742ba5366f391cc1422562fa87e3665b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="x42&#39;s gravatar image" /><p>x42<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="x42 has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jan '17, 09:19</p></div></div><div id="comments-container-58594" class="comments-container"></div><div id="comment-tools-58594" class="comment-tools"></div><div class="clear"></div><div id="comment-58594-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

