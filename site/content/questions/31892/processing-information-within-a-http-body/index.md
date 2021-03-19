+++
type = "question"
title = "Processing information within a http body"
description = '''I am sending messages over http and would like to process the message information before displaying it in wireshark. Is is possible to write a plugin that can manipulate data contained within an http body before displaying it? I have been looking through the developers guide, specifically chapter 9,...'''
date = "2014-04-16T08:39:00Z"
lastmod = "2014-04-16T10:11:00Z"
weight = 31892
keywords = [ "http" ]
aliases = [ "/questions/31892" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Processing information within a http body](/questions/31892/processing-information-within-a-http-body)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31892-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31892-score" class="post-score" title="current number of votes">0</div><span id="post-31892-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am sending messages over http and would like to process the message information before displaying it in wireshark.</p><p>Is is possible to write a plugin that can manipulate data contained within an http body before displaying it? I have been looking through the developers guide, specifically chapter 9, and the examples there show how to create a dissector for a protocol which I don't believe is what I am trying to accomplish. If there is a way to preprocess the information for display where can I find an example of how to do that?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '14, 08:39</strong></p><img src="https://secure.gravatar.com/avatar/df8a5a3cf41de21fd790436554e4f138?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JME&#39;s gravatar image" /><p><span>JME</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JME has no accepted answers">0%</span></p></div></div><div id="comments-container-31892" class="comments-container"><span id="31894"></span><div id="comment-31894" class="comment"><div id="post-31894-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure what you are after but I think you can register a dissector for a specific content-type.</p></div><div id="comment-31894-info" class="comment-info"><span class="comment-age">(16 Apr '14, 08:45)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="31897"></span><div id="comment-31897" class="comment"><div id="post-31897-score" class="comment-score"></div><div class="comment-text"><p>What I am trying to get at is this. After a client sends an http request to the server, the server responds over http with a message that contains Apache Avro data. When I view the response in wireshark I would like to see the response as standard Json rather than Avro's binary file format. I have code that can take the Avro file and transform it to Json, and I would like to know how I can add that code to wireshark in order to make the server response human readable.</p></div><div id="comment-31897-info" class="comment-info"><span class="comment-age">(16 Apr '14, 09:49)</span> <span class="comment-user userinfo">JME</span></div></div><span id="31901"></span><div id="comment-31901" class="comment"><div id="post-31901-score" class="comment-score"></div><div class="comment-text"><p>What is the content type of that binary data? The first problem is to get only the http data you want. Then you can extract it from the tvb manipulate it put it in a new tvb and dissect that. Similar to deflating payload.</p></div><div id="comment-31901-info" class="comment-info"><span class="comment-age">(16 Apr '14, 10:11)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-31892" class="comment-tools"></div><div class="clear"></div><div id="comment-31892-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31899"></span>

<div id="answer-container-31899" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31899-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31899-score" class="post-score" title="current number of votes">1</div><span id="post-31899-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You're talking about a dissector. They take the information out of the packet in whatever format it's received, and dissect it into human readable chunks.</p><p>I'm not away of any parts of Wireshark that transform data in the particular manner you describe. You could write another tool that pre-processes captures so that the modified pcap file contains the converted Json protocol, but that's non-trivial as you have to manage all the underlying layers (e.g. Ethernet, tcp) that Wireshark handles for you.</p><p>You should be able to use your conversion code as a basis for a dissector though, as a dissector just takes the input buffer, parses it into the component parts and calls the Wireshark API to add the parsed info into the columns and tree display.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '14, 10:07</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-31899" class="comments-container"></div><div id="comment-tools-31899" class="comment-tools"></div><div class="clear"></div><div id="comment-31899-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

