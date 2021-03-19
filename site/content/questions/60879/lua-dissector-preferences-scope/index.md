+++
type = "question"
title = "Lua dissector preferences scope?"
description = '''I&#x27;m writing a dissector in Lua and I have two functions besides my dissection functions in the script. Previously, within the dissection function I would be able to get the value of the prefs, and then use them as I see fit. However, since I have two other function, I want those prefs to be inputs t...'''
date = "2017-04-18T10:05:00Z"
lastmod = "2017-04-18T10:05:00Z"
weight = 60879
keywords = [ "lua", "dissector", "preferences", "scope" ]
aliases = [ "/questions/60879" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Lua dissector preferences scope?](/questions/60879/lua-dissector-preferences-scope)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60879-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm writing a dissector in Lua and I have two functions besides my dissection functions in the script. Previously, within the dissection function I would be able to get the value of the prefs, and then use them as I see fit.</p><p>However, since I have two other function, I want those prefs to be inputs to those functions. These functions run only once, outside of the dissection function. However, when I try to input the prefs into the functions Wireshark says that they are of nil value, I suspect the go out of scope.</p><p>My code is structured as follows:</p><pre><code>-- Protocol Initialization 
-- ProtoField Initialization
-- ProtoField Registration
-- Pref Definitions

function proto.dissector(tvbuf, pktinfo, root)
     -- dissection stuff
     A = proto.prefs.a
     B = proto.prefs.b
     -- dissection stuff
end

function fun1(A, B)
     -- function def
end
x, y, z = fun1(A, B) -- function call

function fun2(A, B)
     -- function def
end
i, j = fun2(A, B) -- function call</code></pre><p>I've tried putting the prefs before and after the dissection function with no luck. Is there anyway to take those prefs and use them in fun1 and fun2? The interesting thing is the returned values, like I and j, can be used in the dissection function no problem.</p></div><div id="question-tags" class="tags-container tags">lua dissector preferences scope</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '17, 10:05</strong></p><img src="https://secure.gravatar.com/avatar/00cd850e8d2944c2c7dcdc13baf50a81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Irfan%20Hossain&#39;s gravatar image" /><p>Irfan Hossain<br />
<span class="score" title="11 reputation points">11</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Irfan Hossain has no accepted answers">0%</span></p></div></div><div id="comments-container-60879" class="comments-container"></div><div id="comment-tools-60879" class="comment-tools"></div><div class="clear"></div><div id="comment-60879-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

