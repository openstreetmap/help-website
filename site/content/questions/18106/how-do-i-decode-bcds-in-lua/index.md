+++
type = "question"
title = "How do I decode BCDs in Lua?"
description = '''In my Lua dissector, I have to decode BCDs. I see no readily available tools for this in Wireshark Lua. Can someone explain how I can do this? For example, a BCD of 0x12345678 is sent on the wire as 0x21436587. I have to dissect it and show it as 12345678.'''
date = "2013-01-30T08:24:00Z"
lastmod = "2013-02-04T22:59:00Z"
weight = 18106
keywords = [ "bcd", "lua" ]
aliases = [ "/questions/18106" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How do I decode BCDs in Lua?](/questions/18106/how-do-i-decode-bcds-in-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18106-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18106-score" class="post-score" title="current number of votes">0</div><span id="post-18106-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In my Lua dissector, I have to decode BCDs. I see no readily available tools for this in Wireshark Lua. Can someone explain how I can do this?</p><p>For example, a BCD of <code>0x12345678</code> is sent on the wire as <code>0x21436587</code>. I have to dissect it and show it as <code>12345678</code>.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bcd" rel="tag" title="see questions tagged &#39;bcd&#39;">bcd</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jan '13, 08:24</strong></p><img src="https://secure.gravatar.com/avatar/ceb9fa89fe77c08ded53b2ccf693aeaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aruna%20Sirigere&#39;s gravatar image" /><p><span>Aruna Sirigere</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aruna Sirigere has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Feb '13, 10:21</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-18106" class="comments-container"></div><div id="comment-tools-18106" class="comment-tools"></div><div class="clear"></div><div id="comment-18106-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18256"></span>

<div id="answer-container-18256" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18256-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18256-score" class="post-score" title="current number of votes">3</div><span id="post-18256-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Aruna Sirigere has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It depends on how you have the BCD sequence of bytes in Lua. For example do you literally have a Lua string of "21436587"? If so, then simply doing this will work:</p><pre><code>-- assuming myString = &quot;21436587&quot;
local fixed = myString:gsub(&quot;(.)(.)&quot;, &quot;%2%1&quot;)</code></pre><p>That's just a shorthand for:</p><pre><code>local fixed = string.gsub(myString, &quot;(.)(.)&quot;, &quot;%2%1&quot;)</code></pre><p>But if the BCD is in the packet and your Lua script only has a Tvb object, for example from a dissector function being called, then one way is to turn it into a Lua string of hex ascii, since BCD is just nibble-reversed hex representation. I could be wrong, but I don't think Wireshark's API provides a quick accessor to Tvb to just get a hex ascii representation, so you have to go through ByteRange to get it. So for example, do this:</p><pre><code>-- assuming &#39;buf&#39; is the Tvb object passed into dissector
local tvb = buf(offset,length)  -- gets a TvbRange from your packet, starting at offset, for length bytes
local range = tvb:bytes()  -- converts TvbRange to ByteRange
local hexStr =  tostring(range)  -- turns ByteRange into hex representation string, e.g, &quot;21:43:65:87&quot;
local fixed = hexStr:gsub(&quot;(.)(.):?&quot;, &quot;%2%1&quot;)  -- reverses the nibbles and removes the colons</code></pre><p>That's the really long/verbose way, which can be shortened to something like this:</p><pre><code>local fixed = tostring(buf(offset,length):bytes()):gsub(&quot;(.)(.):?&quot;, &quot;%2%1&quot;)</code></pre><p>Where 'offset' and 'length' are whatever numbers they need to be. Note I haven't tried the above snippets, but something like that should work.</p><p>Update: actually it looks like tostring metamethod of TvbRange gets the hex string, and without colons, so this should work:</p><pre><code>local fixed = tostring(buf(offset,length)):gsub(&quot;(.)(.)&quot;, &quot;%2%1&quot;)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Feb '13, 08:27</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Feb '13, 09:27</strong> </span></p></div></div><div id="comments-container-18256" class="comments-container"><span id="18306"></span><div id="comment-18306" class="comment"><div id="post-18306-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot Hadriel. Below code made the trick.. it did exactly what I was looking for.</p><p>local fixed = tostring(buf(offset,length)):gsub("(.)(.)", "%2%1")</p></div><div id="comment-18306-info" class="comment-info"><span class="comment-age">(04 Feb '13, 22:59)</span> <span class="comment-user userinfo">Aruna Sirigere</span></div></div></div><div id="comment-tools-18256" class="comment-tools"></div><div class="clear"></div><div id="comment-18256-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18138"></span>

<div id="answer-container-18138" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18138-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18138-score" class="post-score" title="current number of votes">0</div><span id="post-18138-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm no LUA expert but either you have to fetch byte by byte and do the conversion or add something similar to tvb_bcd_dig_to_ep_str() to the LUA methods in wslua_tvb.c I suppose.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '13, 14:47</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-18138" class="comments-container"><span id="18155"></span><div id="comment-18155" class="comment"><div id="post-18155-score" class="comment-score"></div><div class="comment-text"><p>Hello Anders,</p><p>Thanks for your response. I am not using C program. I am using LUA script and I just want to use readily available functions to do it.</p><p>If no ready functions available, at least if some one can give the lua script using some logic.</p><p>Thanks in Advance.</p></div><div id="comment-18155-info" class="comment-info"><span class="comment-age">(31 Jan '13, 01:45)</span> <span class="comment-user userinfo">Aruna Sirigere</span></div></div></div><div id="comment-tools-18138" class="comment-tools"></div><div class="clear"></div><div id="comment-18138-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

