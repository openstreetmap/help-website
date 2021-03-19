+++
type = "question"
title = "Register heuristic function for multiple heuristic list names in Lua"
description = '''I&#x27;m writing a custom Lua dissector for a protocol that can be sent over both TCP and UDP. According to the README.heuristic file, this can be done using the following code: / register as heuristic dissector for both TCP and UDP / heur_dissector_add(&quot;tcp&quot;, dissect_PROTOABBREV_heur_tcp, &quot;PROTOABBREV o...'''
date = "2016-07-19T08:20:00Z"
lastmod = "2020-02-14T07:37:00Z"
weight = 54158
keywords = [ "lua", "register_heuristic" ]
aliases = [ "/questions/54158" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Register heuristic function for multiple heuristic list names in Lua](/questions/54158/register-heuristic-function-for-multiple-heuristic-list-names-in-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54158-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm writing a custom Lua dissector for a protocol that can be sent over both TCP and UDP. According to the README.heuristic file, this can be done using the following code:</p><p>/ <em>register as heuristic dissector for both TCP and UDP</em> /</p><pre><code>heur_dissector_add(&quot;tcp&quot;, dissect_PROTOABBREV_heur_tcp, &quot;PROTOABBREV over TCP&quot;,
                   &quot;PROTOABBREV_tcp&quot;, proto_PROTOABBREV, HEURISTIC_ENABLE);
heur_dissector_add(&quot;udp&quot;, dissect_PROTOABBREV_heur_udp, &quot;PROTOABBREV over UDP&quot;,
                   &quot;PROTOABBREV_udp&quot;, proto_PROTOABBREV, HEURISTIC_ENABLE);</code></pre><p>I have successfully implemented this for our dissector written in C/C++. However, the Lua implementation of proto:register_heuristic(listname, func) only allows one heuristic function to be registered per protocol object even though I'm using two unique heuristic list names.<br />
</p><p>Calls to:</p><p>my_proto:register_heuristic("udp", my_heur_func)</p><p>my_proto:register_heuristic("tcp", my_heur_func)</p><p>Result in Wireshark displaying an error that my_proto already has a heuristic function registered. Inspecting the source, it appears the C code behind the Lua function checks against the proto name instead of the heuristic list name. Therefore, I can only register my heuristic function for a single heuristic list name.</p><p>Is this a Lua limitation or is there another way I can register my heuristic function with multiple heuristic list names? Short of another solution, it appears I may have to create two separate Lua dissectors. One for TCP and one for UDP.</p></div><div id="question-tags" class="tags-container tags">lua register_heuristic</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jul '16, 08:20</strong></p><img src="https://secure.gravatar.com/avatar/c8d9b99aa59ee95888e89a41b5e55453?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emucker&#39;s gravatar image" /><p>emucker<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emucker has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-54158" class="comments-container"><span id="54160"></span><div id="comment-54160" class="comment"><div id="post-54160-score" class="comment-score"></div><div class="comment-text"><p>Just a comment, not a answer: the workaround should be simpler in terms that you would create two functions (and, as each protocol can only have a single dissector function, also two protocol names), but one of the functions would be just a wrapper of the other one (i.e. it would call it with the same parameters it has received itself). But you may end up with two sets of display filter names (myproto_udp.xyz and myproto_tcp.xyz) if Lua is equally restrictive when registering the field names.</p><p>There is no limitation on how many protocols you register in a single .lua file.</p></div><div id="comment-54160-info" class="comment-info"><span class="comment-age">(19 Jul '16, 08:49)</span> sindy</div></div></div><div id="comment-tools-54158" class="comment-tools"></div><div class="clear"></div><div id="comment-54158-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64343"></span>

<div id="answer-container-64343" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64343-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>An old question to be sure, but I believe the answer is:</p><pre><code>my_proto:register_heuristic(my_proto, &quot;udp&quot;, my_heur_func)
my_proto:register_heuristic(my_proto, &quot;tcp&quot;, my_heur_func)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '20, 07:37</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Feb '20, 07:38</p></div></div><div id="comments-container-64343" class="comments-container"></div><div id="comment-tools-64343" class="comment-tools"></div><div class="clear"></div><div id="comment-64343-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

