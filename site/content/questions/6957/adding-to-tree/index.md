+++
type = "question"
title = "Adding to tree"
description = '''I am trying to build a dissector, and what I would like to do is extract pieces of data, perform some data manipulation (ie, logic, concatenating two separate sets of data together). After working on it some myself and looking at the documentation, it seems to me that the only way to add anything to...'''
date = "2011-10-18T09:32:00Z"
lastmod = "2011-10-18T23:13:00Z"
weight = 6957
keywords = [ "dissector", "tree", "proto_tree_add" ]
aliases = [ "/questions/6957" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Adding to tree](/questions/6957/adding-to-tree)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6957-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6957-score" class="post-score" title="current number of votes">0</div><span id="post-6957-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to build a dissector, and what I would like to do is extract pieces of data, perform some data manipulation (ie, logic, concatenating two separate sets of data together). After working on it some myself and looking at the documentation, it seems to me that the only way to add anything to a tree is the "proto_tree_add_item(tree, id, tvb, start, length, encoding)". Is there a different function I can use for my purposes? Or is it better for me to build this dissector in Lua (which from my understanding, will allow the functionality that I need)? I am new to building dissectors, so any help would be appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-tree" rel="tag" title="see questions tagged &#39;tree&#39;">tree</span> <span class="post-tag tag-link-proto_tree_add" rel="tag" title="see questions tagged &#39;proto_tree_add&#39;">proto_tree_add</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Oct '11, 09:32</strong></p><img src="https://secure.gravatar.com/avatar/dbf25b6d957ba19e5ce2ecf7589b2803?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JMalanga&#39;s gravatar image" /><p><span>JMalanga</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JMalanga has no accepted answers">0%</span></p></div></div><div id="comments-container-6957" class="comments-container"></div><div id="comment-tools-6957" class="comment-tools"></div><div class="clear"></div><div id="comment-6957-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="6959"></span>

<div id="answer-container-6959" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6959-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6959-score" class="post-score" title="current number of votes">1</div><span id="post-6959-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Check out <a href="http://anonsvn.wireshark.org/wireshark/trunk/doc/README.developer">doc/README.developer</a>. There is a multitude of proto_tree_add functions.</p><p>And you should read the rest too....</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '11, 09:56</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-6959" class="comments-container"></div><div id="comment-tools-6959" class="comment-tools"></div><div class="clear"></div><div id="comment-6959-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6961"></span>

<div id="answer-container-6961" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6961-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6961-score" class="post-score" title="current number of votes">0</div><span id="post-6961-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Any of the <code>proto_tree_add_*</code> functions can be used to add data to the tree, not just <code>proto_tree_add_item</code>. To "extract pieces of data" and then work with them, you can use the <code>tvb_get_*</code> functions (see <code>epan/tvbuff.h</code>).</p><p>For example, if you have a little-endian protocol with a two-byte field you want to examine, you could use <code>tvb_get_letohs(tvb, offset)</code>.</p><p>The Lua interface, while powerful, typically lags behind the C interface feature-wise for a long time. Where possible, you should prefer to write production-level dissectors in C, anyway, so that you can leverage the full featureset that Wireshark offers.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '11, 10:03</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Oct '11, 10:04</strong> </span></p></div></div><div id="comments-container-6961" class="comments-container"><span id="6975"></span><div id="comment-6975" class="comment"><div id="post-6975-score" class="comment-score"></div><div class="comment-text"><blockquote><p>The Lua interface, while powerful, typically lags behind the C interface feature-wise for a long time.</p></blockquote><p>That's true...the Lua API doesn't expose that much from C (but nobody has asked for it). The Lua API gets updated with a new feature mostly upon request. Someone has to see a need for it, or else it stays exactly where it is (and rightly so).</p></div><div id="comment-6975-info" class="comment-info"><span class="comment-age">(18 Oct '11, 15:25)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="6976"></span><div id="comment-6976" class="comment"><div id="post-6976-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Where possible, you should prefer to write production-level dissectors in C, anyway, so that you can leverage the full featureset that Wireshark offers</p></blockquote><p>IMHO, it really depends on your requirements. If the Lua API provides everything you need (and you don't need the full feature set from C), then choose Lua. Sometimes, the path of least resistance is best. On the other hand, Lua might pose a language barrier for you (or maybe you know it already...it's similar to Python), in which case, it might be easier for you to go with C.</p></div><div id="comment-6976-info" class="comment-info"><span class="comment-age">(18 Oct '11, 15:25)</span> <span class="comment-user userinfo">helloworld</span></div></div></div><div id="comment-tools-6961" class="comment-tools"></div><div class="clear"></div><div id="comment-6961-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6982"></span>

<div id="answer-container-6982" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6982-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6982-score" class="post-score" title="current number of votes">0</div><span id="post-6982-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hope this helps Requirement : Get some packet bytes and manipulate them and add to tree to view in pane 2 Suggestion : use proto_tree_add_*(_tree, hf_type,tvb,OFFSET,size, var); "var" is what you actually display in pane ...offset will help in highlighting the corresponding bytes in pane3</p><p>based upon your requirement proto_tree_add_text() will suit you most as you can use printf like arguments</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '11, 23:13</strong></p><img src="https://secure.gravatar.com/avatar/264adc05b644c1ab2d670b4773a12392?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flashkicker&#39;s gravatar image" /><p><span>flashkicker</span><br />
<span class="score" title="109 reputation points">109</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flashkicker has 5 accepted answers">41%</span></p></div></div><div id="comments-container-6982" class="comments-container"></div><div id="comment-tools-6982" class="comment-tools"></div><div class="clear"></div><div id="comment-6982-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

