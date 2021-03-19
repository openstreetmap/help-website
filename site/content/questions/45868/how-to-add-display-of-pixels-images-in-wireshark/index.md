+++
type = "question"
title = "How to add display of pixels (images) in Wireshark"
description = '''I&#x27;m working on a VNC-like dissector, a subdissector of TCP. With a large volume of messages, it would be helpful to see the image associated with a FramebufferUpdate message when looking through a capture file. I believe this would help locate the appropriate messages when working on a problem. Esse...'''
date = "2015-09-15T18:54:00Z"
lastmod = "2015-09-16T09:21:00Z"
weight = 45868
keywords = [ "image", "dissector", "wireshark" ]
aliases = [ "/questions/45868" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to add display of pixels (images) in Wireshark](/questions/45868/how-to-add-display-of-pixels-images-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45868-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45868-score" class="post-score" title="current number of votes">0</div><span id="post-45868-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm working on a VNC-like dissector, a subdissector of TCP. With a large volume of messages, it would be helpful to see the image associated with a FramebufferUpdate message when looking through a capture file. I believe this would help locate the appropriate messages when working on a problem.</p><p>Essentially, I would like to have a third option "Image View" added to the packet bytes pane. For packets with image data, the data would be shown in the packet bytes pane as pixels (visible image). In a perfect world, the non-image data in the packets would continue to be displayed in hex/text.</p><p>I'm very new to Wireshark, but I guess this has been thought about. My question is really how would this fit into the Wireshark architecture.</p><p>Enlightenment needed...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-image" rel="tag" title="see questions tagged &#39;image&#39;">image</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Sep '15, 18:54</strong></p><img src="https://secure.gravatar.com/avatar/3c7618d31ed754f5a8acab1f1f1a32e3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chad%20Farmer&#39;s gravatar image" /><p><span>Chad Farmer</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chad Farmer has no accepted answers">0%</span></p></div></div><div id="comments-container-45868" class="comments-container"></div><div id="comment-tools-45868" class="comment-tools"></div><div class="clear"></div><div id="comment-45868-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45869"></span>

<div id="answer-container-45869" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45869-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45869-score" class="post-score" title="current number of votes">0</div><span id="post-45869-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>how would this fit into the Wireshark architecture</p></blockquote><p>With the current architecture, nowhere.</p><p>Dissectors <strong><em>CANNOT</em></strong> do any GUI stuff, such as displaying images as their code must function within the purely command-line TShark, so you won't be able to get it as a packet bytes pane; changing that would require a <em>change</em> to the Wireshark architecture to allow a dissector to specify bytes to be shown as an image (for example, a field type of <code>FT_IMAGE</code> with something specifying the image format, or <code>FT_IMAGE_</code> types for various image formats), and the widgets that display protocol trees in Wireshark would have to then show them as images - TShark would simply ignore them.</p><p>There's really no good way to <em>mix</em> the display of hex/text data and images in the <em>same</em> tab in the packet bytes pane; that doesn't really fit with the purpose of that display, and it wouldn't let people look at the raw bytes of the image. You'd probably want, instead, to have additional tabs in that pane, one per image, displaying an image <em>instead</em> of the hex bytes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Sep '15, 20:01</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-45869" class="comments-container"><span id="45883"></span><div id="comment-45883" class="comment"><div id="post-45883-score" class="comment-score"></div><div class="comment-text"><p>That was enlightening, thank you. <code>FT_IMAGE_type</code> feels right. The data would be displayed in hex by default for TShark and Wireshark, but Wireshark could have an option for an image display. A separate tab would avoid disturbing existing code that manages the packet bytes pane.</p><p>I do a fair amount of work at the command line, so I understand its value.</p><p>Regards...</p></div><div id="comment-45883-info" class="comment-info"><span class="comment-age">(16 Sep '15, 09:21)</span> <span class="comment-user userinfo">Chad Farmer</span></div></div></div><div id="comment-tools-45869" class="comment-tools"></div><div class="clear"></div><div id="comment-45869-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

