+++
type = "question"
title = "Equivalent of LUA Field extractors in C"
description = '''Hi, i am currently trying to write a post dissector in c that ive already written in LUA. In LUA fields can be extracted by using field extractor methods, e.g. i can read the &quot;udp.port&quot;. Is there any equivalent to this in C?'''
date = "2016-01-15T00:26:00Z"
lastmod = "2016-01-15T04:22:00Z"
weight = 49244
keywords = [ "lua", "postdissector" ]
aliases = [ "/questions/49244" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Equivalent of LUA Field extractors in C](/questions/49244/equivalent-of-lua-field-extractors-in-c)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49244-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>i am currently trying to write a post dissector in c that ive already written in LUA. In LUA fields can be extracted by using field extractor methods, e.g. i can read the "udp.port". Is there any equivalent to this in C?</p></div><div id="question-tags" class="tags-container tags">lua postdissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jan '16, 00:26</strong></p><img src="https://secure.gravatar.com/avatar/ce595bcaea627c29ed0222d44eccb874?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wodka&#39;s gravatar image" /><p>Wodka<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wodka has no accepted answers">0%</span></p></div></div><div id="comments-container-49244" class="comments-container"></div><div id="comment-tools-49244" class="comment-tools"></div><div class="clear"></div><div id="comment-49244-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49251"></span>

<div id="answer-container-49251" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49251-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You just use the normal dissector functions for accessing the tvb. Info is in doc\README.dissector.</p><p>Post-dissectors are much the same as a normal dissector, except they get called for every frame after all other dissectors have had a go as required.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jan '16, 04:22</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-49251" class="comments-container"><span id="49252"></span><div id="comment-49252" class="comment"><div id="post-49252-score" class="comment-score"></div><div class="comment-text"><p>I dont want to acess a range in the tvb but get information another dissector has already figured out, e.g. An UDP-Dissector would have created the meta-data field "udp.port". I need to acess this information field (which is in C resembled by header_field_info type i think).</p></div><div id="comment-49252-info" class="comment-info"><span class="comment-age">(15 Jan '16, 04:50)</span> Wodka</div></div><span id="49253"></span><div id="comment-49253" class="comment"><div id="post-49253-score" class="comment-score"></div><div class="comment-text"><p>You get that via the packet_info structure passed to your dissectors pinfo parameter.</p><p>For the ports, use <code>pinfo-&gt;srcport</code> or <code>pinfo-&gt;dstport</code>.</p></div><div id="comment-49253-info" class="comment-info"><span class="comment-age">(15 Jan '16, 04:58)</span> grahamb ♦</div></div><span id="49254"></span><div id="comment-49254" class="comment"><div id="post-49254-score" class="comment-score"></div><div class="comment-text"><p>i dont need the port. that was just an example. I just want to know - generally spoken, how to access a header field, e.g. called "xxx.yyy".</p></div><div id="comment-49254-info" class="comment-info"><span class="comment-age">(15 Jan '16, 06:40)</span> Wodka</div></div><span id="49255"></span><div id="comment-49255" class="comment"><div id="post-49255-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure that you can in C. A dissector is normally limited to the tvb, the packet_info and proto_tree and any data structure passed from the caller, although post-dissectors don't get the data structure.</p><p>I guess there must be some method for Lua to extract that info, digging into the code a little, it appears that Lua uses a tap and then processes the packet tree in the tap to extract fields. I'm not aware of any general API to do that that is available to C dissectors, but there might be one.</p></div><div id="comment-49255-info" class="comment-info"><span class="comment-age">(15 Jan '16, 07:32)</span> grahamb ♦</div></div></div><div id="comment-tools-49251" class="comment-tools"></div><div class="clear"></div><div id="comment-49251-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

