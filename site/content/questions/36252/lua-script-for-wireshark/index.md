+++
type = "question"
title = "lua script for wireshark"
description = '''Hi , I am trying to write the lua script ( 5.2.3) for windows . extension lua script for wireshark . facing error in this line &quot;local f_proto = ProtoField.uint8(&quot;multi.protocol&quot;,&quot;Protocol&quot;,base.DEC,vs_protos)&quot;  attempt to index global &#x27;base&#x27; (a nil value) . How to fix this issue ..??  regards, Beno '''
date = "2014-09-11T22:16:00Z"
lastmod = "2014-09-12T07:33:00Z"
weight = 36252
keywords = [ "lua", "script" ]
aliases = [ "/questions/36252" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [lua script for wireshark](/questions/36252/lua-script-for-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36252-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi ,</p><p>I am trying to write the lua script ( 5.2.3) for windows . extension lua script for wireshark .</p><p>facing error in this line "local f_proto = ProtoField.uint8("multi.protocol","Protocol",base.DEC,vs_protos)"</p><p>attempt to index global 'base' (a nil value) . How to fix this issue ..??</p><p>regards, Beno</p></div><div id="question-tags" class="tags-container tags">lua script</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Sep '14, 22:16</strong></p><img src="https://secure.gravatar.com/avatar/e44b50ffde6eca01b7296816ee96296c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="benok&#39;s gravatar image" /><p>benok<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="benok has no accepted answers">0%</span></p></div></div><div id="comments-container-36252" class="comments-container"><span id="36265"></span><div id="comment-36265" class="comment"><div id="post-36265-score" class="comment-score"></div><div class="comment-text"><p>Which version of wireshark/tshark are you using ?</p><p>And how are you executing the script ?</p><p>I've tried this specific line in Evaluate Lua window Tools-&gt;Lua-&gt;Evaluate of my wireshark 1.12.0 and it worked that is it did not raise any errors.</p></div><div id="comment-36265-info" class="comment-info"><span class="comment-age">(12 Sep '14, 05:09)</span> izopizo</div></div><span id="36266"></span><div id="comment-36266" class="comment"><div id="post-36266-score" class="comment-score"></div><div class="comment-text"><p>hi izopizo ,</p><p>I am using wireshark 1.12.0 , executing via wireshark init.lua ( added dofile( "test.lua" ) , the content on the test.lua is local p_multi = Proto("multi","MultiProto");</p><p>local vs_protos = { [2] = "mtp2", [3] = "mtp3", [4] = "alcap", [5] = "h248", [6] = "ranap", [7] = "rnsap", [8] = "nbap" }</p><p>local f_proto = ProtoField.uint8("multi.protocol","Protocol",base.DEC,vs_protos)</p></div><div id="comment-36266-info" class="comment-info"><span class="comment-age">(12 Sep '14, 05:22)</span> benok</div></div></div><div id="comment-tools-36252" class="comment-tools"></div><div class="clear"></div><div id="comment-36252-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36268"></span>

<div id="answer-container-36268" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36268-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Where in <code>init.lua</code> did you put your "<code>dofile(test.lua)</code>" statement? I ask because the "<code>base</code>" table it's complaining about being a nil value is a Lua table defined in <code>init.lua</code> itself, at line 448 (or around there). So if you call "<code>dofile(test.lua)</code>" in <code>init.lua</code> <em>before</em> the <code>base</code> table is defined, you'll get that error.</p><p>The best thing to do would be to not call <code>dofile()</code> to load your <code>test.lua</code> file, but instead put <code>test.lua</code> in your personal plugins directory and Wireshark will automatically load it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '14, 07:33</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-36268" class="comments-container"></div><div id="comment-tools-36268" class="comment-tools"></div><div class="clear"></div><div id="comment-36268-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

