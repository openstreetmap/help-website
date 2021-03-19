+++
type = "question"
title = "How do I let the user specify a port for a Wireshark Lua dissector?"
description = '''Hi, I am trying to create Lua dissectors for wireshark that work on different port numbers. The port numbers that they use are not fixed. Hence I wanted to create a pop up or some other kind of system in wireshark to specify the port numbers they would work on so that those port numbers could be use...'''
date = "2016-07-18T13:04:00Z"
lastmod = "2016-07-18T13:35:00Z"
weight = 54141
keywords = [ "filter", "lua", "dissector" ]
aliases = [ "/questions/54141" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How do I let the user specify a port for a Wireshark Lua dissector?](/questions/54141/how-do-i-let-the-user-specify-a-port-for-a-wireshark-lua-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54141-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am trying to create Lua dissectors for wireshark that work on different port numbers. The port numbers that they use are not fixed. Hence I wanted to create a pop up or some other kind of system in wireshark to specify the port numbers they would work on so that those port numbers could be used to dissect the packets. I essentially want to input the port number from the user either when the user opens up wireshark or when the user applies the filter. Thanks</p></div><div id="question-tags" class="tags-container tags">filter lua dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jul '16, 13:04</strong></p><img src="https://secure.gravatar.com/avatar/3aaad26a48e6f507d8f9137404269a46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shobhit_garg91&#39;s gravatar image" /><p>shobhit_garg91<br />
<span class="score" title="16 reputation points">16</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shobhit_garg91 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Jul '16, 12:58</p></div></div><div id="comments-container-54141" class="comments-container"></div><div id="comment-tools-54141" class="comment-tools"></div><div class="clear"></div><div id="comment-54141-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="54146"></span>

<div id="answer-container-54146" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54146-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are 2 basic ways to do it:</p><ol><li>Register your dissector for the port table you're interested in and allow users to specify which ports to decode as your protocol through the "Decode As" dialog. See the discussion on <a href="https://wiki.wireshark.org/Lua/Dissectors">the wiki</a> for details.</li><li>(or) <a href="https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Proto.html#lua_class_Pref">register a preference</a></li></ol><p>These days the former is preferred.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jul '16, 13:35</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-54146" class="comments-container"><span id="54198"></span><div id="comment-54198" class="comment"><div id="post-54198-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jeff for the answer. I am trying to register a preference. Specifically I want my dissector to appear in the Edit&gt;&gt; Preferences &gt;&gt; Protocols with a field where I could specify multiple port numbers like the one present for HTTP. Please let me know if there is any method to do so such that those port numbers could be used to specify the dissector about the packets.</p></div><div id="comment-54198-info" class="comment-info"><span class="comment-age">(20 Jul '16, 11:47)</span> shobhit_garg91</div></div><span id="54200"></span><div id="comment-54200" class="comment"><div id="post-54200-score" class="comment-score"></div><div class="comment-text"><p>Try reading <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=doc/README.dissector;h=17b3273336f48a3831eada7fbaeaefce5135babc;hb=HEAD#l2899">doc/README.dissector</a> for how to add preferences. There are plenty of dissectors to look at for working examples too.</p></div><div id="comment-54200-info" class="comment-info"><span class="comment-age">(20 Jul '16, 12:08)</span> cmaynard ♦♦</div></div><span id="54201"></span><div id="comment-54201" class="comment"><div id="post-54201-score" class="comment-score"></div><div class="comment-text"><p>Hi, Thanks. I have added a preference for my dissector and it is showing in the edit &gt;&gt; Preferences &gt;&gt; Protocols. I have added a range type of preference to the dissector to read in a range of port numbers. My question is how to use this preference to add these as port numbers for my dissector. Thanks</p></div><div id="comment-54201-info" class="comment-info"><span class="comment-age">(20 Jul '16, 12:18)</span> shobhit_garg91</div></div><span id="54202"></span><div id="comment-54202" class="comment"><div id="post-54202-score" class="comment-score"></div><div class="comment-text"><p>According to the documentation (linked from item 2 above) the preferences get added to the <code>Proto.prefs</code> table. Never tried it myself but hopefully that's a good starting point.</p></div><div id="comment-54202-info" class="comment-info"><span class="comment-age">(20 Jul '16, 12:35)</span> JeffMorriss ♦</div></div><span id="54204"></span><div id="comment-54204" class="comment"><div id="post-54204-score" class="comment-score"></div><div class="comment-text"><p>Hi, I have added the preference for my dissector, and in my dissector, I am trying to read the preference value and use it to add the corresponding port numbers specified in the preference. However when I am opening wireshark, I am getting the following error: "No preference has been registered yet". Please let me know if there is any way to overcome this issue and read the value in the pref to use it as a port number. According to the documentation the pref is returned in the form of a string. Thanks.</p></div><div id="comment-54204-info" class="comment-info"><span class="comment-age">(20 Jul '16, 12:49)</span> shobhit_garg91</div></div><span id="54205"></span><div id="comment-54205" class="comment not_top_scorer"><div id="post-54205-score" class="comment-score"></div><div class="comment-text"><p>If your dissector is written in Lua, you might try stating that in the question next time. If you're looking for help with Lua, I posted some useful Lua-related links in my answer to <a href="https://ask.wireshark.org/questions/53802/how-dissect-two-segments-of-one-protocol-in-the-same-packet-in-the-same-tcp-segment-lua">this</a> question, which should help you. In particular, the <code>fpm.lua</code> script uses preferences and should be of particular use to you.</p></div><div id="comment-54205-info" class="comment-info"><span class="comment-age">(20 Jul '16, 12:55)</span> cmaynard ♦♦</div></div><span id="54222"></span><div id="comment-54222" class="comment not_top_scorer"><div id="post-54222-score" class="comment-score"></div><div class="comment-text"><p>Thank you everyone. I was able to handle the port numbers dynamically by setting up the dissector preference and using the function prefs_changed().</p></div><div id="comment-54222-info" class="comment-info"><span class="comment-age">(21 Jul '16, 07:13)</span> shobhit_garg91</div></div></div><div id="comment-tools-54146" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-54146-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="54145"></span>

<div id="answer-container-54145" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54145-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's not the way to go about it. For instance this same dissector has to work from the command line in tshark, dissectors may be called multiple times, which makes user interaction a problem.</p><p>The solution is either using the method of 'Decode as...' or add a preference for a port range.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jul '16, 13:28</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-54145" class="comments-container"><span id="54199"></span><div id="comment-54199" class="comment"><div id="post-54199-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jaap. I am trying to register a preference. Specifically I want my dissector to appear in the Edit&gt;&gt; Preferences &gt;&gt; Protocols with a field where I could specify multiple port numbers like the one present for HTTP. Please let me know if there is any method to do so such that those port numbers could be used to specify the dissector about the packets.</p></div><div id="comment-54199-info" class="comment-info"><span class="comment-age">(20 Jul '16, 11:47)</span> shobhit_garg91</div></div></div><div id="comment-tools-54145" class="comment-tools"></div><div class="clear"></div><div id="comment-54145-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

