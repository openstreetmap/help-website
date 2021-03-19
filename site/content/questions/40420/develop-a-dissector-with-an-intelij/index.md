+++
type = "question"
title = "develop a dissector with an intelij?"
description = '''hi.. is there a way to develop a dissector for wireshark using an ide (including an auto complete on wireshark api ) '''
date = "2015-03-10T05:15:00Z"
lastmod = "2015-03-10T05:44:00Z"
weight = 40420
keywords = [ "lua", "ide", "dissector", "intelij" ]
aliases = [ "/questions/40420" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [develop a dissector with an intelij?](/questions/40420/develop-a-dissector-with-an-intelij)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40420-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi.. is there a way to develop a dissector for wireshark using an ide (including an auto complete on wireshark api )</p></div><div id="question-tags" class="tags-container tags">lua ide dissector intelij</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Mar '15, 05:15</strong></p><img src="https://secure.gravatar.com/avatar/c1ae031356d61509c1e12593563f937d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emaayan&#39;s gravatar image" /><p>emaayan<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emaayan has no accepted answers">0%</span></p></div></div><div id="comments-container-40420" class="comments-container"></div><div id="comment-tools-40420" class="comment-tools"></div><div class="clear"></div><div id="comment-40420-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40422"></span>

<div id="answer-container-40422" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40422-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Probably.</p><p>Whichever IDE you use will have to have some method for examining the Wireshark sources to create the auto-complete lists, and as most of the WS sources are for other dissectors which you generally aren't interested in (they're useful as examples but you won't generally be calling functions in them), not much of that will be helpful.</p><p>If you're brave, and like to live on the bleeding edge, building on the Windows platform can now use CMake to generate Visual Studio solution files and then edit away in the IDE. Even with that, I still work on the dissectors I maintain with a text editor as I've done for the last decade and a bit. Note that I use VS for the day job, so I'm not anti-IDE, I just don't find it useful for WS dev.</p><p>Dissector writing is mostly defining hf entries and a big switch statement to dissect the data and call <code>proto_tree_add_item()</code>, adding subtrees where it makes sense. There is also a a bit of boiler plate for registration, maybe some preferences handling, maybe some code for heuristics and maybe some code for reassembly and conversations, but nothing to get too excited about. README.dissector should cover it all and if it doesn't, let us know so we can update it (or even better submit a change).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Mar '15, 05:44</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-40422" class="comments-container"><span id="40424"></span><div id="comment-40424" class="comment"><div id="post-40424-score" class="comment-score"></div><div class="comment-text"><p>thanks, is was more looking for something that gives me docs and api descriptions, for example i would imagine the when i do a buf(pos, 1) it gives me an object not a byte value, which means i can't really compare it to a hex value and have to use tostring. this article gave me an excellent starting point <a href="https://delog.wordpress.com/2010/09/27/create-a-wireshark-dissector-in-lua/">https://delog.wordpress.com/2010/09/27/create-a-wireshark-dissector-in-lua/</a> the only i had problems with it was i didn't know how to call a previous dissector (because using mine suddenly eliminated the data field)</p></div><div id="comment-40424-info" class="comment-info"><span class="comment-age">(10 Mar '15, 06:44)</span> emaayan</div></div><span id="40425"></span><div id="comment-40425" class="comment"><div id="post-40425-score" class="comment-score"></div><div class="comment-text"><p>Lua is another matter (I didn't sport the tag when I answered), and the <a href="http://wiki.wireshark.org/Lua">Wireshark Lua</a> Wiki page is your starting point for info.</p><p>Hopefully someone else (@Hadriel ?) will chime in about any possible IDE's for use with Lua and the Wireshark Lua API.</p></div><div id="comment-40425-info" class="comment-info"><span class="comment-age">(10 Mar '15, 07:04)</span> grahamb ♦</div></div></div><div id="comment-tools-40422" class="comment-tools"></div><div class="clear"></div><div id="comment-40422-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

