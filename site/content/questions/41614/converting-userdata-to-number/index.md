+++
type = "question"
title = "converting userdata to number"
description = '''length_octect=tvb_get_guint8(tvb,2)&amp;amp;0x3FF;(last ten bits offset value) ti = proto_tree_add_text(data_tree, tvb, offset, length_octect, &quot;data&quot;); I used the above function in c for the offset length.How to get the length_octect in lua script I tried something like this: local length_octect=(buffer...'''
date = "2015-04-20T23:22:00Z"
lastmod = "2015-04-21T05:03:00Z"
weight = 41614
keywords = [ "lua", "error" ]
aliases = [ "/questions/41614" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [converting userdata to number](/questions/41614/converting-userdata-to-number)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41614-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41614-score" class="post-score" title="current number of votes">0</div><span id="post-41614-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>length_octect=tvb_get_guint8(tvb,2)&amp;0x3FF;(last ten bits offset value)</p><p>ti = proto_tree_add_text(data_tree, tvb, offset, length_octect, "data");</p><p>I used the above function in c for the offset length.How to get the length_octect in lua script</p><p>I tried something like this:</p><p>local length_octect=(buffer((offset,2) or 0x3FF):unit()</p><p>data=subtree:add(F.data,buffer(offset,length_octect))</p><p>but it is giving error as: Lua Error: C:\Program Files\Wireshark1\myproto.lua:104: No such 'unit' function/method/field for object type 'TvbRange'</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Apr '15, 23:22</strong></p><img src="https://secure.gravatar.com/avatar/a2e29df6af5eb33f09d1ed5321ea6586?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lakshmi&#39;s gravatar image" /><p><span>lakshmi</span><br />
<span class="score" title="16 reputation points">16</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lakshmi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Apr '15, 23:31</strong> </span></p></div></div><div id="comments-container-41614" class="comments-container"></div><div id="comment-tools-41614" class="comment-tools"></div><div class="clear"></div><div id="comment-41614-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41615"></span>

<div id="answer-container-41615" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41615-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41615-score" class="post-score" title="current number of votes">0</div><span id="post-41615-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You've got typo in your function name. Try uint() not unit().</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '15, 23:44</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p><span>izopizo</span><br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span></p></div></div><div id="comments-container-41615" class="comments-container"><span id="41616"></span><div id="comment-41616" class="comment"><div id="post-41616-score" class="comment-score"></div><div class="comment-text"><p>yes, i changed that . Now iam getting the following error:</p><p>Expert Info (Warn/Malformed): Trying to fetch an unsigned integer with length 18</p></div><div id="comment-41616-info" class="comment-info"><span class="comment-age">(20 Apr '15, 23:51)</span> <span class="comment-user userinfo">lakshmi</span></div></div><span id="41619"></span><div id="comment-41619" class="comment"><div id="post-41619-score" class="comment-score"></div><div class="comment-text"><p>Expert Info (Warn/Malformed): Trying to fetch an unsigned integer with length 18</p><p>This warning I am getting for every length greater than 4.</p></div><div id="comment-41619-info" class="comment-info"><span class="comment-age">(21 Apr '15, 01:36)</span> <span class="comment-user userinfo">lakshmi</span></div></div><span id="41623"></span><div id="comment-41623" class="comment"><div id="post-41623-score" class="comment-score"></div><div class="comment-text"><p>This seems to be expected, pr the Lua reference manual found here: <a href="https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Tvb.html">https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Tvb.html</a></p><p>11.8.3.3. tvbrange:uint()</p><p>Get a Big Endian (network order) unsigned integer from a TvbRange. The range must be 1, 2, 3 or 4 octets long. Returns</p><p>The unsigned integer value.</p></div><div id="comment-41623-info" class="comment-info"><span class="comment-age">(21 Apr '15, 05:03)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-41615" class="comment-tools"></div><div class="clear"></div><div id="comment-41615-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

