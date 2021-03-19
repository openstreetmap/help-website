+++
type = "question"
title = "tshark support for LUA post-dissector"
description = '''Does tshark support LUA post-dissectors? I&#x27;m having problems getting a post-dissector that works fine with Wireshark to work with tshark. Before I get heavily into debugging the problem I just want to be sure that there is no fundamental problem with using a post-dissector with tshark.'''
date = "2015-07-24T14:28:00Z"
lastmod = "2015-07-24T16:01:00Z"
weight = 44451
keywords = [ "lua" ]
aliases = [ "/questions/44451" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark support for LUA post-dissector](/questions/44451/tshark-support-for-lua-post-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44451-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Does tshark support LUA post-dissectors?</p><p>I'm having problems getting a post-dissector that works fine with Wireshark to work with tshark. Before I get heavily into debugging the problem I just want to be sure that there is no fundamental problem with using a post-dissector with tshark.</p></div><div id="question-tags" class="tags-container tags">lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jul '15, 14:28</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p>PaulOfford<br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-44451" class="comments-container"></div><div id="comment-tools-44451" class="comment-tools"></div><div class="clear"></div><div id="comment-44451-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44459"></span>

<div id="answer-container-44459" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44459-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yup.</p><p>If you can post your script, I can take a crack at finding the problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '15, 16:01</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-44459" class="comments-container"><span id="44496"></span><div id="comment-44496" class="comment"><div id="post-44496-score" class="comment-score"></div><div class="comment-text"><p>Hi Hadriel,</p><p>Thanks for the post. The script is a bit big (1500 lines) so I'll upload somewhere and add a link here but there may be a more fundamental problem.</p><p>I need to use the -2 option of tshark to force two scans, and this seems to cause problems. I'll make a separate post on this as this issue seems to have nothing to do with LUA.</p><p>Best regards...Paul</p></div><div id="comment-44496-info" class="comment-info"><span class="comment-age">(26 Jul '15, 08:34)</span> PaulOfford</div></div></div><div id="comment-tools-44459" class="comment-tools"></div><div class="clear"></div><div id="comment-44459-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

