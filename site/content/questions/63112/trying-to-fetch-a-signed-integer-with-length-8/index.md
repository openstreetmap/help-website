+++
type = "question"
title = "Trying to fetch a signed integer with length 8"
description = '''Hi,  I&#x27;m getting this warning on my decoded section of an item.  &quot;Expert Info (Warning/Malformed): Trying to fetch a signed integer with length 8&quot; As it is suggested I&#x27;m trying to add an item that is 8 bytes and i should use an unsigned int in order that the item is properly displayed. However I&#x27;m t...'''
date = "2017-07-26T01:37:00Z"
lastmod = "2017-07-26T22:59:00Z"
weight = 63112
keywords = [ "decimal", "unsigned", "display" ]
aliases = [ "/questions/63112" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Trying to fetch a signed integer with length 8](/questions/63112/trying-to-fetch-a-signed-integer-with-length-8)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63112-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63112-score" class="post-score" title="current number of votes">0</div><span id="post-63112-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm getting this warning on my decoded section of an item. "Expert Info (Warning/Malformed): Trying to fetch a signed integer with length 8"</p><p>As it is suggested I'm trying to add an item that is 8 bytes and i should use an unsigned int in order that the item is properly displayed. However I'm trying to use the proto_tree_add_uint64 but unsuccessfully.</p><p>This is my part of the code</p><pre><code>proto_item *count_id = proto_tree_add_item(count_tree_, hf_map_pdu_eth_count, tvb, offset, 1, ENC_BIG_ENDIAN);
proto_tree *val = proto_item_add_subtree(count_id, ett_map);
offset += 1;
**proto_tree_add_item(val, hf_map_pdu_c_value, tvb, offset, 8, ENC_BIG_ENDIAN);**
offset += 8;</code></pre><p>What is the approach when we want to display in DEC 8 bytes?</p><p>many thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decimal" rel="tag" title="see questions tagged &#39;decimal&#39;">decimal</span> <span class="post-tag tag-link-unsigned" rel="tag" title="see questions tagged &#39;unsigned&#39;">unsigned</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jul '17, 01:37</strong></p><img src="https://secure.gravatar.com/avatar/0cc0debf9f6cf8601913135a0d0ec76b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gerolima&#39;s gravatar image" /><p><span>gerolima</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gerolima has one accepted answer">50%</span></p></div></div><div id="comments-container-63112" class="comments-container"></div><div id="comment-tools-63112" class="comment-tools"></div><div class="clear"></div><div id="comment-63112-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63113"></span>

<div id="answer-container-63113" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63113-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63113-score" class="post-score" title="current number of votes">0</div><span id="post-63113-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please double check hf_map_pdu_c_value definition and ensure that it is defined as FT_UINT64 and not (let's say) FT_INT32.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '17, 02:23</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-63113" class="comments-container"><span id="63121"></span><div id="comment-63121" class="comment"><div id="post-63121-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>Yes it's 64.</p><p>&amp;hf_map_pdu_c_value, { "Counter value", "map.c_value", FT_UINT64, BASE_DEC, NULL, 0x0, NULL, HFILL }</p></div><div id="comment-63121-info" class="comment-info"><span class="comment-age">(26 Jul '17, 04:09)</span> <span class="comment-user userinfo">gerolima</span></div></div><span id="63125"></span><div id="comment-63125" class="comment"><div id="post-63125-score" class="comment-score"></div><div class="comment-text"><p>With such code, the error you are reporting cannot happen with the current development version. Are you building a plugin or an internal dissector? Which Wireshark version are you building with?</p></div><div id="comment-63125-info" class="comment-info"><span class="comment-age">(26 Jul '17, 04:27)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="63129"></span><div id="comment-63129" class="comment"><div id="post-63129-score" class="comment-score"></div><div class="comment-text"><p>No, I'm building a plugin. Sorry it's been a while since I started this project. I think it's 2.1.1 is there any way to verify the version to be sure?</p></div><div id="comment-63129-info" class="comment-info"><span class="comment-age">(26 Jul '17, 05:44)</span> <span class="comment-user userinfo">gerolima</span></div></div><span id="63138"></span><div id="comment-63138" class="comment"><div id="post-63138-score" class="comment-score"></div><div class="comment-text"><p>Except in some rare cases or if you just like living dangerously, you should really work with a stable release version, currently the latest stable release being 2.4.0.</p><p>You can check <code>configure.ac</code> for the version, for example:</p><pre><code>$ head -n 10 configure.ac
#
# Autoconf script for Wireshark
#

#
# Define variables for the components of the Wireshark version number.
#
m4_define([version_major], [2])
m4_define([version_minor], [4])
m4_define([version_micro], [0])</code></pre></div><div id="comment-63138-info" class="comment-info"><span class="comment-age">(26 Jul '17, 08:55)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="63144"></span><div id="comment-63144" class="comment"><div id="post-63144-score" class="comment-score"></div><div class="comment-text"><blockquote><p>FT_UINT64</p></blockquote><p>That's an <em>unsigned</em> 64-bit integer; if you want a <em>signed</em> 64-bit integer, you want <code>FT_INT64</code>.</p></div><div id="comment-63144-info" class="comment-info"><span class="comment-age">(26 Jul '17, 10:53)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="63149"></span><div id="comment-63149" class="comment not_top_scorer"><div id="post-63149-score" class="comment-score"></div><div class="comment-text"><p>So presumably you are building a plugin with a given version of Wireshark, and trying to run it with another version where the numerical value for FT_UINT64 corresponds to FT_INT8, FT_INT16 or FT_INT32. This is a very classic issue when building plugins. Wireshark API is not stable between major releases, so you need to recompile your plugin against the release you intend to use.</p></div><div id="comment-63149-info" class="comment-info"><span class="comment-age">(26 Jul '17, 11:15)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="63154"></span><div id="comment-63154" class="comment not_top_scorer"><div id="post-63154-score" class="comment-score"></div><div class="comment-text"><p>Just to clarify, I just checked the version:</p><p>Define variables for the components of the Wireshark version number.</p><p>m4_define([version_major], [2]) m4_define([version_minor], [3]) m4_define([version_micro], [0])</p><p>So, each time there is a new major release I need to git pull the changes and re-compile the project? To be honest, I'm a bit afraid to mess with my dev environment, it took me a lot of effort to reach a stable state :)</p></div><div id="comment-63154-info" class="comment-info"><span class="comment-age">(26 Jul '17, 22:51)</span> <span class="comment-user userinfo">gerolima</span></div></div><span id="63155"></span><div id="comment-63155" class="comment not_top_scorer"><div id="post-63155-score" class="comment-score"></div><div class="comment-text"><p>Using a plugin, you have no other choice. Note that 2.3.0 was a development snapshot, so API could change at anytime. Stable release always have an even minor version.</p></div><div id="comment-63155-info" class="comment-info"><span class="comment-age">(26 Jul '17, 22:59)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-63113" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-63113-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

