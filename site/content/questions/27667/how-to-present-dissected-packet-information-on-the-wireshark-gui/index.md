+++
type = "question"
title = "How to present dissected packet information on the Wireshark GUI?"
description = '''I would like to write a dissector to capture and parse a particular protocol, and update information on the Wireshark main window display; e.g., Source, Destination, and Info columns, and expand information in the Packet Details pane. How do I present the dissected packet information on the Wireshar...'''
date = "2013-12-02T10:03:00Z"
lastmod = "2013-12-02T14:04:00Z"
weight = 27667
keywords = [ "gui", "dissector" ]
aliases = [ "/questions/27667" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to present dissected packet information on the Wireshark GUI?](/questions/27667/how-to-present-dissected-packet-information-on-the-wireshark-gui)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27667-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27667-score" class="post-score" title="current number of votes">0</div><span id="post-27667-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to write a dissector to capture and parse a particular protocol, and update information on the Wireshark main window display; e.g., Source, Destination, and Info columns, and expand information in the Packet Details pane. How do I present the dissected packet information on the Wireshark GUI?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gui" rel="tag" title="see questions tagged &#39;gui&#39;">gui</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '13, 10:03</strong></p><img src="https://secure.gravatar.com/avatar/5616ea3bb0508befa40fd66a768acc65?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tinker&#39;s gravatar image" /><p><span>Tinker</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tinker has one accepted answer">100%</span></p></div></div><div id="comments-container-27667" class="comments-container"></div><div id="comment-tools-27667" class="comment-tools"></div><div class="clear"></div><div id="comment-27667-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27675"></span>

<div id="answer-container-27675" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27675-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27675-score" class="post-score" title="current number of votes">1</div><span id="post-27675-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Tinker has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use the <code>proto_tree_add_item</code> (and other <code>proto_tree_add_*</code> functions from epan/packet.h) to add items to the dissection tree, and <code>col_set_str</code> (and other column functions from epan/col_utils.h) to change the column data.<br />
The m2m dissector (plugins/m2m) is pretty easy to follow, but as a very simple example, see the below code (I assume here that you have your dissector basically set up; see doc/README.developer for more on that):</p><pre><code>void dissect_my_protocol(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree)
{
    col_set_str(pinfo-&gt;cinfo, COL_PROTOCOL, &quot;My Protocol&quot;);           /* Set the Protocol column text */
    col_append_str(pinfo-&gt;cinfo, COL_INFO, &quot; Some new information&quot;).  /* Append to the Info column */
    proto_tree_add_item(tree, hf_MyItem, tvb, 0, -1, ENC_BIG_ENDIAN); /* Add an item to the tree */
}</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '13, 14:00</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span> </br></p></div></div><div id="comments-container-27675" class="comments-container"><span id="27676"></span><div id="comment-27676" class="comment"><div id="post-27676-score" class="comment-score"></div><div class="comment-text"><p>Thanks. This is what I suspected, but had difficulty in confirming it. Much appreciated.</p></div><div id="comment-27676-info" class="comment-info"><span class="comment-age">(02 Dec '13, 14:04)</span> <span class="comment-user userinfo">Tinker</span></div></div></div><div id="comment-tools-27675" class="comment-tools"></div><div class="clear"></div><div id="comment-27675-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27674"></span>

<div id="answer-container-27674" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27674-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27674-score" class="post-score" title="current number of votes">1</div><span id="post-27674-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I would like to write a dissector to capture and parse a particular protocol,</p></blockquote><p>See, for example, the README.dissector file in the doc directory of the Wireshark source.</p><blockquote><p>and update information on the Wireshark main window display; e.g., Source, Destination, and Info columns, and expand information in the Packet Details pane.</p></blockquote><p>Wireshark takes the column values set by your dissector and uses them to set the columns, and takes the protocol tree built by your dissector and displays it in the Packet Details pane. You do not do any GUI work yourself in the dissector; that's all done for you by the Wireshark GUI code.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '13, 13:52</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-27674" class="comments-container"></div><div id="comment-tools-27674" class="comment-tools"></div><div class="clear"></div><div id="comment-27674-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

