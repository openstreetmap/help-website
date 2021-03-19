+++
type = "question"
title = "Confusing Lua reassembly documentation, how is this done in current 1.6.x/1.7.0 ?"
description = '''Hi, As I am using a Lua dissector to debug the implementation of a proprietary protocol, I am having trouble getting TCP reassembly to work. End user stuff such as allowing reassembly seems OK, but currently my dissector still sees each TCP segment/packet as a new stream, giving wrong results for da...'''
date = "2012-02-15T04:54:00Z"
lastmod = "2012-02-15T04:54:00Z"
weight = 9018
keywords = [ "lua", "luainterface", "dissector", "reassembly" ]
aliases = [ "/questions/9018" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Confusing Lua reassembly documentation, how is this done in current 1.6.x/1.7.0 ?](/questions/9018/confusing-lua-reassembly-documentation-how-is-this-done-in-current-16x170)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9018-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9018-score" class="post-score" title="current number of votes">4</div><span id="post-9018-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>As I am using a Lua dissector to debug the implementation of a proprietary protocol, I am having trouble getting TCP reassembly to work. End user stuff such as allowing reassembly seems OK, but currently my dissector still sees each TCP segment/packet as a new stream, giving wrong results for data crossing segment bounds.</p><p>The documentation I have been able to find is confusing and seems self-contradictory:</p><p>The current Wiki says to use pinfo OR signed return values, some other documents are more confusing.</p><p>Some other docs suggest figuring out how to install "Alien" for Lua (Alien's own documentation page just says to use some Lua-specific package manager which is presumably only available for standalone Lua) then figuring out how to specify a Lua prototype for a C API which takes two callback pointers amongst its args.</p><p>It is unclear how to access the reassembled data once called with enough bytes.</p><p>My own experiments have come up short, resulting in bad reassembly.</p><p>Where can I get clarity on how to write a reassembled TCP dissector in Lua?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-luainterface" rel="tag" title="see questions tagged &#39;luainterface&#39;">luainterface</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-reassembly" rel="tag" title="see questions tagged &#39;reassembly&#39;">reassembly</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Feb '12, 04:54</strong></p><img src="https://secure.gravatar.com/avatar/804bddf43796045a3e6b9082369cc2a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jb_wisemo&#39;s gravatar image" /><p><span>jb_wisemo</span><br />
<span class="score" title="61 reputation points">61</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jb_wisemo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Feb '12, 06:59</strong> </span></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-9018" class="comments-container"></div><div id="comment-tools-9018" class="comment-tools"></div><div class="clear"></div><div id="comment-9018-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

