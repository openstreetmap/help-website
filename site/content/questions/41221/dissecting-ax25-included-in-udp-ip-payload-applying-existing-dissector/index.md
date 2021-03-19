+++
type = "question"
title = "Dissecting AX25 included in UDP-IP payload applying existing dissector."
description = '''Hello Wireshark gurus, I have several frames where the UDP payload carries frames of AX25 protocol (AX25 is normally a DataLink layer protocol, but here we are dealing with AX25 over UDP-IP). The fantastic Wireshark is already able to dissect AX25 as DataLink layer protocol (dissector well running)....'''
date = "2015-04-06T07:50:00Z"
lastmod = "2015-04-07T09:12:00Z"
weight = 41221
keywords = [ "ax25", "over", "udp-ip" ]
aliases = [ "/questions/41221" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Dissecting AX25 included in UDP-IP payload applying existing dissector.](/questions/41221/dissecting-ax25-included-in-udp-ip-payload-applying-existing-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41221-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41221-score" class="post-score" title="current number of votes">1</div><span id="post-41221-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Wireshark gurus,</p><p>I have several frames where the UDP payload carries frames of AX25 protocol (AX25 is normally a DataLink layer protocol, but here we are dealing with AX25 over UDP-IP). The fantastic Wireshark is already able to dissect AX25 as DataLink layer protocol (dissector well running). Is it possible to dissect “on demand” the payload of some UDP packets applying the AX25 dissector over the payload of the UDP-OP packets, without developing a specific “AX25 over UDP-IP” dissector ? Any help appreciated Thank-you Cheer Ugo</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ax25" rel="tag" title="see questions tagged &#39;ax25&#39;">ax25</span> <span class="post-tag tag-link-over" rel="tag" title="see questions tagged &#39;over&#39;">over</span> <span class="post-tag tag-link-udp-ip" rel="tag" title="see questions tagged &#39;udp-ip&#39;">udp-ip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Apr '15, 07:50</strong></p><img src="https://secure.gravatar.com/avatar/32be8fa793e7da72a235cb9c965d6a03?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ugo&#39;s gravatar image" /><p><span>Ugo</span><br />
<span class="score" title="17 reputation points">17</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ugo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Apr '15, 00:59</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-41221" class="comments-container"></div><div id="comment-tools-41221" class="comment-tools"></div><div class="clear"></div><div id="comment-41221-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="41224"></span>

<div id="answer-container-41224" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41224-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41224-score" class="post-score" title="current number of votes">0</div><span id="post-41224-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is it possible to dissect “on demand” the payload of some UDP packets applying the AX25 dissector over the payload of the UDP-OP packets</p></blockquote><p>That would require a change of the dissector code.</p><p>Actually, there was some work on the way for this, but the author did not release his work, or stopped working on it.</p><blockquote><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7529#c8">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7529#c8</a></p></blockquote><p>Cite:</p><pre><code>Having said that, axip (ax.25 over IP) appears to work anyway, but not
axudp (ax.25 over UDP) or axtcp (ax.25 over tcp).  These probably only
require code to identify the payload type and then call the ax25 dissector.</code></pre><p>You can try to contact the author of that statement and ask if he is willing to publish his code or to finish the work.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Apr '15, 09:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-41224" class="comments-container"><span id="41230"></span><div id="comment-41230" class="comment"><div id="post-41230-score" class="comment-score"></div><div class="comment-text"><p><span>@Ugo</span>: You rewarded 4 reputation points to me. I'm not sure if you wanted to do that, so I'm rewarding them back to you.</p><p>This site works by up-voting answers (thumbs up) and/or by accepting an answer (check mark). See FAQ.</p></div><div id="comment-41230-info" class="comment-info"><span class="comment-age">(06 Apr '15, 11:16)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-41224" class="comment-tools"></div><div class="clear"></div><div id="comment-41224-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41254"></span>

<div id="answer-container-41254" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41254-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41254-score" class="post-score" title="current number of votes">0</div><span id="post-41254-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To answer the above regarding ax25 over IP/UDP/TCP.</p><p>For AX.25 over IP there is a protocol identifier for the encapsulation. So that one is done.</p><p>For AX.25 over UDP/TCP the issue is that there are 65536 ports that could be used but only a few are and those vary with the site in question. So, with the assistance of Ugo (the original poster) I offer an solution based on LUA that will need to be tuned on a site by site basis for the ports in use.</p><pre><code>Snip ----------------------------------------------------------
-- ax25-udp.lua
--
-- LUA script to handle AX.25 over UDP
-- Copyright 2015 R.W. Stearn &lt;[email protected]&gt;
--
-- This program is free software; you can redistribute it and/or
-- modify it under the terms of the GNU General Public License
-- as published by the Free Software Foundation; either version 2
-- of the License, or (at your option) any later version.
--
-- This program is distributed in the hope that it will be useful,
-- but WITHOUT ANY WARRANTY; without even the implied warranty of
-- MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
-- GNU General Public License for more details.
--
-- You should have received a copy of the GNU General Public License
-- along with this program; if not, write to the Free Software
-- Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
--
--

-- load the udp.port table
udp_table = DissectorTable.get( &quot;udp.port&quot; )

-- get a handle to the AX.25 dissector
proto_ax25 = Dissector.get( &quot;ax25&quot; )

-- register AX.25 to handle udp port
udp_table:add( 10093, proto_ax25 )

-- register AX.25 to handle udp port
-- udp_table:add( 10094, proto_ax25 )
Snip ----------------------------------------------------------

and

Snip ----------------------------------------------------------
-- ax25-tcp.lua
--
-- LUA script to handle AX.25 over TCP
-- Copyright 2015 R.W. Stearn &lt;[email protected]&gt;
--
-- This program is free software; you can redistribute it and/or
-- modify it under the terms of the GNU General Public License
-- as published by the Free Software Foundation; either version 2
-- of the License, or (at your option) any later version.
--
-- This program is distributed in the hope that it will be useful,
-- but WITHOUT ANY WARRANTY; without even the implied warranty of
-- MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
-- GNU General Public License for more details.
--
-- You should have received a copy of the GNU General Public License
-- along with this program; if not, write to the Free Software
-- Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
--
--

-- load the tcp.port table
tcp_table = DissectorTable.get( &quot;tcp.port&quot; )

-- get a handle to the AX.25 dissector
proto_ax25 = Dissector.get( &quot;ax25&quot; )

-- register AX.25 to handle tcp port
tcp_table:add( 10093, proto_ax25 )

-- register AX.25 to handle tcp port
-- tcp_table:add( 35272, proto_ax25 )
Snip ----------------------------------------------------------

Snip ----------------------------------------------------------
-- init.lua
dofile(USER_DIR..&quot;ax25-udp.lua&quot;)
dofile(USER_DIR..&quot;ax25-tcp.lua&quot;)
Snip ----------------------------------------------------------

The 3 code segments above need to be copied into 3 separate file
  ax25-udp.lua
  ax25-tcp.lua
  init.lua

and placed in ${HOME}/.wireshark for user.

Regards
  Richard
    (Author of the AX.25 suite in Wireshark.)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Apr '15, 09:12</strong></p><img src="https://secure.gravatar.com/avatar/40209355db87738c52896bb7e5777c26?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rstearn&#39;s gravatar image" /><p><span>rstearn</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rstearn has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Apr '15, 09:18</strong> </span></p></div></div><div id="comments-container-41254" class="comments-container"></div><div id="comment-tools-41254" class="comment-tools"></div><div class="clear"></div><div id="comment-41254-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

