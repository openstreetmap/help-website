+++
type = "question"
title = "ISUP/BICC filtering by field in a Lua script"
description = '''Hi. I&#x27;ve been writing a Lua script to filter ISUP/BICC packets containing certain fields. In pseudo-code: f = Field.new(f_name) ... local tap = Listener.new()  function tap.packet(pinfo, tvb)  ...  if f.field() ~= nil then  ...  where f_name is the Wireshark display filter expression for the given f...'''
date = "2016-04-12T01:55:00Z"
lastmod = "2016-04-12T07:52:00Z"
weight = 51581
keywords = [ "lua", "isup", "scripting", "display-filter" ]
aliases = [ "/questions/51581" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [ISUP/BICC filtering by field in a Lua script](/questions/51581/isupbicc-filtering-by-field-in-a-lua-script)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51581-score" class="post-score" title="current number of votes">0</div><span id="post-51581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi.</p><p>I've been writing a Lua script to filter ISUP/BICC packets containing certain fields. In pseudo-code:</p><pre><code>f = Field.new(f_name)
...
local tap = Listener.new()

function tap.packet(pinfo, tvb)
    ...
    if f.field() ~= nil then
        ...</code></pre><p>where f_name is the Wireshark display filter expression for the given field.</p><p>This approach generally works, but some of the fields in my list ("CONNECTED NUMBER", "ORIGINAL CALLED NUMBER", "REDIRECTION NUMBER") do not appear to be associated with a display filter.</p><p>Same goes for RANAP/BSSAP protocol ("RP-Originating Address", "RP-Destination Address", "Calling Party BCD number", "Called party BCD number").</p><p>What do you suggest to do?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-isup" rel="tag" title="see questions tagged &#39;isup&#39;">isup</span> <span class="post-tag tag-link-scripting" rel="tag" title="see questions tagged &#39;scripting&#39;">scripting</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Apr '16, 01:55</strong></p><img src="https://secure.gravatar.com/avatar/18f314b4cc2ed0507877b655a3610694?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="angian&#39;s gravatar image" /><p><span>angian</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="angian has no accepted answers">0%</span></p></div></div><div id="comments-container-51581" class="comments-container"></div><div id="comment-tools-51581" class="comment-tools"></div><div class="clear"></div><div id="comment-51581-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51598"></span>

<div id="answer-container-51598" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51598-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51598-score" class="post-score" title="current number of votes">1</div><span id="post-51598-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="angian has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looking at the <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-isup.c">ISUP dissector source code</a> it appears that while the dissector does decode the parameters you list it does not put the whole number in a single field; see for example the dissect_isup_connected_number_parameter() function. Compare that function to, say, dissect_isup_calling_party_number_parameter() which, at the end of the function, does a proto_tree_add_string() on the complete number (thus making the called digits a filterable field).</p><p>I'd suggest <a href="https://bugs.wireshark.org">opening a bug report</a> to have these fields added as actual fields; there was recently a lot of work done to avoid this problem (by getting rid of the proto_tree_add_text() function) but these ISUP parameters escaped notice presumably due to the use of a subtree with proto_tree_append_text().</p><p>I can't really comment on the RANAP/BSSAP part of the question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Apr '16, 06:32</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-51598" class="comments-container"><span id="51604"></span><div id="comment-51604" class="comment"><div id="post-51604-score" class="comment-score">1</div><div class="comment-text"><p>For completeness: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12334">bug 12334</a> was opened.</p></div><div id="comment-51604-info" class="comment-info"><span class="comment-age">(12 Apr '16, 07:52)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-51598" class="comment-tools"></div><div class="clear"></div><div id="comment-51598-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

