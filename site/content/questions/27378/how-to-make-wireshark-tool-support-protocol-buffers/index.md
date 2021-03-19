+++
type = "question"
title = "How to make Wireshark tool support Protocol Buffers?"
description = '''Hello Sir, How to make Wireshark tool support Protocol Buffers? How to add my protobuf decoder into wireshark tool &amp;gt;&amp;gt; Analyze menu &amp;gt;&amp;gt; “Enabled Protocls&quot; dialog?'''
date = "2013-11-26T01:34:00Z"
lastmod = "2014-11-25T10:18:00Z"
weight = 27378
keywords = [ "protocol", "buffers", "wireshark" ]
aliases = [ "/questions/27378" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to make Wireshark tool support Protocol Buffers?](/questions/27378/how-to-make-wireshark-tool-support-protocol-buffers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27378-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27378-score" class="post-score" title="current number of votes">0</div><span id="post-27378-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Sir, How to make Wireshark tool support Protocol Buffers? How to add my protobuf decoder into wireshark tool &gt;&gt; Analyze menu &gt;&gt; “Enabled Protocls" dialog?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span> <span class="post-tag tag-link-buffers" rel="tag" title="see questions tagged &#39;buffers&#39;">buffers</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '13, 01:34</strong></p><img src="https://secure.gravatar.com/avatar/b1efcd6a306ee67d1d674d36b10cbc64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MartinXie&#39;s gravatar image" /><p><span>MartinXie</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MartinXie has no accepted answers">0%</span></p></div></div><div id="comments-container-27378" class="comments-container"></div><div id="comment-tools-27378" class="comment-tools"></div><div class="clear"></div><div id="comment-27378-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27384"></span>

<div id="answer-container-27384" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27384-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27384-score" class="post-score" title="current number of votes">4</div><span id="post-27384-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From your many similar questions I assume you are talking about google protocol buffers. As thet project never aproched Wireshark or offered their code to us we have no knowledge of the dissector but in general if you have a plugin or a builtin dissector you nedd to complie it agains your verion of Wireshark or put the ready made plugin executable in the plugins directory (See help-Aabout-&gt;folders) Not thet a plugin is only garanteed to work with the version of Wireshark it was built against. Other than that you'd better ask the people who made the plugin.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '13, 01:54</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-27384" class="comments-container"><span id="27390"></span><div id="comment-27390" class="comment"><div id="post-27390-score" class="comment-score"></div><div class="comment-text"><p>Thank you Anders! Yes, I'm talking about google protocol buffers. How can I compile a plugin or built-in dissector against Wireshark1.10.3 please?</p></div><div id="comment-27390-info" class="comment-info"><span class="comment-age">(26 Nov '13, 02:13)</span> <span class="comment-user userinfo">MartinXie</span></div></div><span id="27411"></span><div id="comment-27411" class="comment"><div id="post-27411-score" class="comment-score"></div><div class="comment-text"><p><a href="http://www.wireshark.org/docs/wsdg_html_chunked/">http://www.wireshark.org/docs/wsdg_html_chunked/</a></p></div><div id="comment-27411-info" class="comment-info"><span class="comment-age">(26 Nov '13, 04:04)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-27384" class="comment-tools"></div><div class="clear"></div><div id="comment-27384-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38134"></span>

<div id="answer-container-38134" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38134-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38134-score" class="post-score" title="current number of votes">0</div><span id="post-38134-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Take a look at the <a href="https://code.google.com/p/protobuf-wireshark/">protobuf-wireshark</a> project. I've <a href="https://code.google.com/p/protobuf-wireshark/issues/detail?id=13">approached them about contributing it</a> to the upstream Wireshark project so everyone can benefit without jumping through hoops of compiling it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '14, 10:18</strong></p><img src="https://secure.gravatar.com/avatar/2d128be9e2e492517499a7dc00af1a42?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="leif81&#39;s gravatar image" /><p><span>leif81</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="leif81 has no accepted answers">0%</span></p></div></div><div id="comments-container-38134" class="comments-container"></div><div id="comment-tools-38134" class="comment-tools"></div><div class="clear"></div><div id="comment-38134-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

