+++
type = "question"
title = "Lua dissector for proprietary bus protocol"
description = '''Dear experts, I&#x27;m new to Wireshark and I wonder if it&#x27;s possible to perform the following task.  I want to write a Lua dissector for viewing captured data in Wireshark. The captured data (recorded with a terminal program) normally looks like this: A:55 0D 00 00 1F 50 0A D0 2F 80 00 00 A2 B:55 0D 00 ...'''
date = "2017-10-11T15:19:00Z"
lastmod = "2017-10-12T07:04:00Z"
weight = 63825
keywords = [ "lua", "dissector", "proprietary", "serial-port" ]
aliases = [ "/questions/63825" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Lua dissector for proprietary bus protocol](/questions/63825/lua-dissector-for-proprietary-bus-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63825-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63825-score" class="post-score" title="current number of votes">0</div><span id="post-63825-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear experts,</p><p>I'm new to Wireshark and I wonder if it's possible to perform the following task.<br />
<br />
I want to write a Lua dissector for viewing captured data in Wireshark.<br />
The captured data (recorded with a terminal program) normally looks like this:</p><pre><code>A:55 0D 00 00 1F 50 0A D0 2F 80 00 00 A2
B:55 0D 00 40 1F 50 DA 26 2F 80 00 00 A2
B:55 0B 40 00 1F 10 FD 5C 2F 81 00
B:55 0D 00 00 1F 4F EF 2B 2F 80 00 00 82</code></pre><p><br />
This means:<br />
a) The captured data are lines of hex strings starting with "A:" or "B:" indicating the sender.<br />
b) It's not a protocol embedded in TCP or something else for what I can find a lot of examples.<br />
<br />
If for a) the solution would be that it had to be binary data instead of text, it would be easy enough to convert the data.<br />
I have actually tried it with the data converted to binary, but I could not get anything working.<br />
<br />
b) In most of the examples I've found so far, an existing DissectorTable is used.<br />
What would I have to do, as there is not any similar table or protocol already implemented?<br />
<br />
I do have a good description about the meaning of every byte.<br />
But for the beginning it would suffice, if I just could read the data and display it, only using the <strong>length byte</strong>, which is the second hex byte in each line.<br />
I think that decoding and displaying the remaining data would be more easy to accomplish.<br />
<br />
I would have enough experience to write a program with C# that shows the meaning of the data.<br />
But from using Wireshark I expect a better usability and it's something I really would like to learn.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-proprietary" rel="tag" title="see questions tagged &#39;proprietary&#39;">proprietary</span> <span class="post-tag tag-link-serial-port" rel="tag" title="see questions tagged &#39;serial-port&#39;">serial-port</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '17, 15:19</strong></p><img src="https://secure.gravatar.com/avatar/4f7fa3a32f08259fb3e6879a43b4e1a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Danton&#39;s gravatar image" /><p><span>Danton</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Danton has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-63825" class="comments-container"></div><div id="comment-tools-63825" class="comment-tools"></div><div class="clear"></div><div id="comment-63825-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63844"></span>

<div id="answer-container-63844" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63844-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63844-score" class="post-score" title="current number of votes">0</div><span id="post-63844-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark can import hex dumps of protocol frames using <code>File -&gt; Import from Hex Dump</code> in graphical Wireshark or using <code>text2pcap</code> command line utility, except that you'll have to pre-process them to fit the expected format. Running <code>text2pcap</code> gives you hints about the format which are missing <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChIOImportSection.html">here</a> - note the information regarding direction information (A -&gt; I, B -&gt; O or vice versa) and maybe regarding timestamps if you can have them in the original data.</p><p>When deciding which dissector to use to analyse the next piece of frame data, Wireshark uses "dissector tables". These are mapping tables which translate some integer or text values found in lower protocol layers to links to dissectors. In some cases more complex methods are use but that is not relevant here. The root level of such mapping is the encapsulation type (Ethernet, 802.11 etc.) which cannot be found in the frame data itself but in its metadata stored in the capture file. In your case, I'd assume the best way to be to choose one of the USER1-USER15 encapsulations when importing the hex dump, and to register your Lua dissector for that encapsulation type using <code>Edit -&gt; Preferences -&gt; Protocols -&gt; DLT_USER -&gt; Edit</code> with your Lua dissector already registered. Or you can do the same in the initialization part of your code, see the answer of <a href="https://ask.wireshark.org/users/79/guy-harris">@Guy Harris</a> to <a href="https://ask.wireshark.org/questions/48710/registering-a-dissector-for-a-third-party-protocol">this question</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Oct '17, 07:04</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span> </br></br></p></div></div><div id="comments-container-63844" class="comments-container"></div><div id="comment-tools-63844" class="comment-tools"></div><div class="clear"></div><div id="comment-63844-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

