+++
type = "question"
title = "Mark packets with Lua"
description = '''Hi, I need to do a Lua script which has to highlight some issues in a very huge heap of packets. Does somebody knows if it is possible through the Lua API and how? I suspected the &quot;frameinfo.flags&quot; but the reference to wtap_preference_flags does not exist in init.lua. I know that this option exists ...'''
date = "2014-06-27T06:04:00Z"
lastmod = "2014-06-27T10:04:00Z"
weight = 34240
keywords = [ "lua", "packet", "mark" ]
aliases = [ "/questions/34240" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Mark packets with Lua](/questions/34240/mark-packets-with-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34240-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I need to do a Lua script which has to highlight some issues in a very huge heap of packets. Does somebody knows if it is possible through the Lua API and how?</p><p>I suspected the "frameinfo.flags" but the reference to wtap_preference_flags does not exist in init.lua. I know that this option exists because I can filter on packet marks using the filter "frame.marked".</p><p>Any help would be much appreciated. Thanks Alex</p></div><div id="question-tags" class="tags-container tags">lua packet mark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jun '14, 06:04</strong></p><img src="https://secure.gravatar.com/avatar/b7e0754a346a7e6d5f9c1214fb01fd25?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="format_c&#39;s gravatar image" /><p>format_c<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="format_c has no accepted answers">0%</span></p></div></div><div id="comments-container-34240" class="comments-container"></div><div id="comment-tools-34240" class="comment-tools"></div><div class="clear"></div><div id="comment-34240-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34246"></span>

<div id="answer-container-34246" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34246-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is no way currently to mark packets, as far as I know. It would need to be exposed in an enhancement, and would be done by being added to <code>Pinfo</code> object rather than <code>FrameInfo</code>. It's a good request - please submit a <a href="https://bugs.wireshark.org/bugzilla/">bugzilla</a> request for it.</p><p>The "<code>FrameInfo.flags</code>" are different, though similar - they represent info about the frame/packet in the capture file, not info about the frame in the GUI display window. There's an overlap of course, but it's not the same information. (internally they're different data structures)</p><p>If you don't see the "<code>wtap_presence_flags</code>" table in <strong>init.lua</strong>, then you're not running a new enough version of wireshark. It only appeared starting in 1.11.3, so now it's 1.12.0rc2. But as mentioned above, it won't solve the problem for you as it doesn't control frame marking in the GUI.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '14, 10:04</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-34246" class="comments-container"><span id="34247"></span><div id="comment-34247" class="comment"><div id="post-34247-score" class="comment-score"></div><div class="comment-text"><p>Could the OP add expert info to the packets using lua and then filter on that?</p></div><div id="comment-34247-info" class="comment-info"><span class="comment-age">(27 Jun '14, 11:18)</span> grahamb ♦</div></div><span id="34249"></span><div id="comment-34249" class="comment"><div id="post-34249-score" class="comment-score"></div><div class="comment-text"><p>Sure, or a Lua-created protocol field too.</p></div><div id="comment-34249-info" class="comment-info"><span class="comment-age">(27 Jun '14, 12:30)</span> Hadriel</div></div></div><div id="comment-tools-34246" class="comment-tools"></div><div class="clear"></div><div id="comment-34246-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

