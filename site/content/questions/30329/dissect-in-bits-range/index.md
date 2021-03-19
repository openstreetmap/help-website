+++
type = "question"
title = "dissect in bits range"
description = '''Hi, It seems the normal way of dissecting a packet only goes down to byte level. What if I have a value that is, say, 10 bits long (with no padding to make it into two bytes), is there a way I can add a tree item for it and highlight the corresponding bits? Thank you so much, yxi'''
date = "2014-03-02T09:27:00Z"
lastmod = "2014-03-03T18:19:00Z"
weight = 30329
keywords = [ "lua", "bit" ]
aliases = [ "/questions/30329" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [dissect in bits range](/questions/30329/dissect-in-bits-range)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30329-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30329-score" class="post-score" title="current number of votes">0</div><span id="post-30329-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>It seems the normal way of dissecting a packet only goes down to byte level.</p><p>What if I have a value that is, say, 10 bits long (with no padding to make it into two bytes), is there a way I can add a tree item for it and highlight the corresponding bits?</p><p>Thank you so much,</p><p>yxi</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-bit" rel="tag" title="see questions tagged &#39;bit&#39;">bit</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Mar '14, 09:27</strong></p><img src="https://secure.gravatar.com/avatar/b18cada3e3589f311e24f5ffbd1737bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YXI&#39;s gravatar image" /><p><span>YXI</span><br />
<span class="score" title="21 reputation points">21</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YXI has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> retagged <strong>02 Mar '14, 20:53</strong> </span></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span></p></div></div><div id="comments-container-30329" class="comments-container"></div><div id="comment-tools-30329" class="comment-tools"></div><div class="clear"></div><div id="comment-30329-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="30332"></span>

<div id="answer-container-30332" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30332-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30332-score" class="post-score" title="current number of votes">1</div><span id="post-30332-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It depends on how you mean that. Do you mean your protocol literally has a field that is 10 bits long and all subsequent fields/values are offset by those extra 2 bits from then on for the rest of the protocol's packet? Or do you just mean you've got a field that is 10 bits long, and the other 6 bits are used-for/part-of some unrelated field? If the latter case, that's what the bitmask is for (see <code>header_field_info</code> in proto.h). For an example of it being used, look in <code>epan/packet-vlan.c</code>, where the vlan_id is only 12 bits wide (but ultimately inside an even vlan tag size).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Mar '14, 11:22</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-30332" class="comments-container"><span id="30333"></span><div id="comment-30333" class="comment"><div id="post-30333-score" class="comment-score"></div><div class="comment-text"><p>If your protocol truly is bitoriented, take a look at proto_add_bits_item().</p></div><div id="comment-30333-info" class="comment-info"><span class="comment-age">(02 Mar '14, 12:14)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="30334"></span><div id="comment-30334" class="comment"><div id="post-30334-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>Thanks for the answers. Both situations are possible, in my case.<br />
I forgot to mention that I have to use Lua script, instead of C.<br />
Ideally, when a value is stored in bytes, when it is clicked, corresponding bytes will light up. When another value is stored in bits, when clicked, the display pane will switch to bit view and high light corresponding bits. I don't know if that's possible.<br />
</p></div><div id="comment-30334-info" class="comment-info"><span class="comment-age">(02 Mar '14, 20:04)</span> <span class="comment-user userinfo">YXI</span></div></div></div><div id="comment-tools-30332" class="comment-tools"></div><div class="clear"></div><div id="comment-30332-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30335"></span>

<div id="answer-container-30335" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30335-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30335-score" class="post-score" title="current number of votes">0</div><span id="post-30335-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can change the display pane to view bits - right-click in the Packet Bytes pane (usually the window pane shown on the bottom) and select "Bits View" instead of the default "Hex View". But it won't highlight the specific bit(s) of a field as far as I know - it still highlights the whole byte(s) those bits are in.</p><p>Even if <code>proto_tree_add_bits_item()</code> is used, it appears to highlight the whole byte(s). For example the IP header flags (reserved, don't fragment, more fragments) are added using that function and I can't discern any visual difference from just using a bitmask. (there probably is a difference, I just don't know what it is)</p><p>But anyway, I don't believe Lua has an exposed function for <code>proto_tree_add_bits_item()</code>, but you can use bitmasks. The <a href="http://wiki.wireshark.org/Lua/Examples?action=AttachFile&amp;do=get&amp;target=dissector.lua">dissector.lua</a> script that you can download from the top of the wiki <a href="http://wiki.wireshark.org/Lua/Examples">Lua examples</a> page uses bitmasks quite a bit. (hmmm, there's a pun there)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Mar '14, 20:50</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span> </br></br></p></div></div><div id="comments-container-30335" class="comments-container"><span id="30375"></span><div id="comment-30375" class="comment"><div id="post-30375-score" class="comment-score"></div><div class="comment-text"><p>Thanks Hadriel. At this point I will stop trying to highlight exact bits that don't occupy a whole byte. It is probably, like you said, impossible. I can always state the bits range in a tree item if I have to. Not as nice as highlighting, but that's what I can do. Thanks so much again, YXI</p></div><div id="comment-30375-info" class="comment-info"><span class="comment-age">(03 Mar '14, 18:19)</span> <span class="comment-user userinfo">YXI</span></div></div></div><div id="comment-tools-30335" class="comment-tools"></div><div class="clear"></div><div id="comment-30335-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

