+++
type = "question"
title = "Decode TCP as HTTP"
description = '''I am using a mac via thunderbolt display port mirroring on the switch connected to my thunderbolt. For some reason on the 2.0.0 Developer version of wireshark, I will some times get HTTP (rarely) but most of the time I will only get TCP. I try to right click on the stream and click decode as, then c...'''
date = "2015-11-20T13:03:00Z"
lastmod = "2015-11-23T14:47:00Z"
weight = 47812
keywords = [ "decode_as_http", "decode_tcp" ]
aliases = [ "/questions/47812" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Decode TCP as HTTP](/questions/47812/decode-tcp-as-http)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47812-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using a mac via thunderbolt display port mirroring on the switch connected to my thunderbolt. For some reason on the 2.0.0 Developer version of wireshark, I will some times get HTTP (rarely) but most of the time I will only get TCP. I try to right click on the stream and click decode as, then choose http, and press okay. Neither when it loads or when I start wireshark again will it show the HTTP stream instead. In fact I don't get http from anything that I should be getting it from even. I would think that it's my switch set up, but I get http every now and then. Any help would be appreciated.</p><p>====EDITED==== I also noticed I keep getting this in the packet info [Dissector bug, protocol TCP: /Users/buildslave/Documents/wireshark-2.0/osx106x64/build/epan/dissectors/packet-tcp.c:1969: failed assertion "mptcpd != ((void *)0)"]</p></div><div id="question-tags" class="tags-container tags">decode_as_http decode_tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Nov '15, 13:03</strong></p><img src="https://secure.gravatar.com/avatar/98b66f05f2156cf806889fb0231ed3b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kristaphonie&#39;s gravatar image" /><p>Kristaphonie<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kristaphonie has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Nov '15, 14:43</p></div></div><div id="comments-container-47812" class="comments-container"></div><div id="comment-tools-47812" class="comment-tools"></div><div class="clear"></div><div id="comment-47812-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="47898"></span>

<div id="answer-container-47898" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47898-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The assert you a reporting was in 2.0.0 RC1 and was fixed in official release. It prevented any proper dissection of TCP traffic.</p><p>Please upgrade your Wireshark version to the official 2.0.0 final version. Hopefully it should fix your issue.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '15, 14:47</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-47898" class="comments-container"><span id="47936"></span><div id="comment-47936" class="comment"><div id="post-47936-score" class="comment-score"></div><div class="comment-text"><p>That was it. The version I was on was breaking it. I hadn't checked for a new version and I couldn't find a bug trail or anything on the specific issue when I looked, so thank you for helping me.</p></div><div id="comment-47936-info" class="comment-info"><span class="comment-age">(24 Nov '15, 12:10)</span> Kristaphonie</div></div></div><div id="comment-tools-47898" class="comment-tools"></div><div class="clear"></div><div id="comment-47898-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="47816"></span>

<div id="answer-container-47816" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47816-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The 'Decode As' setting is not saved be default, unless you click on the Save button. So your setting is not saved between Wireshark instances.</p><p>Instead of using 'Decode As' functionality, you might double check what are the TCP ports configured in Edit -&gt; Preferences -&gt; Protocols -&gt; HTTP -&gt; TCP ports and add the missing one.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '15, 14:24</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-47816" class="comments-container"><span id="47818"></span><div id="comment-47818" class="comment"><div id="post-47818-score" class="comment-score"></div><div class="comment-text"><p>@Pascal: I am afraid Kristaphonie may rather be complaining about 2.0.0 Dev not auto-detecting tcp towards port 80 as http automatically.</p><p>@Kristaphonie: may you clear the doubt and post an example of such capture?</p></div><div id="comment-47818-info" class="comment-info"><span class="comment-age">(20 Nov '15, 14:59)</span> sindy</div></div><span id="47820"></span><div id="comment-47820" class="comment"><div id="post-47820-score" class="comment-score"></div><div class="comment-text"><p>@sindy: 2.0.0 has port 80 in the list of ports for TCP and it's working perfectly fine for me.</p></div><div id="comment-47820-info" class="comment-info"><span class="comment-age">(20 Nov '15, 15:13)</span> Pascal Quantin</div></div><span id="47889"></span><div id="comment-47889" class="comment"><div id="post-47889-score" class="comment-score"></div><div class="comment-text"><p>@Pascal So my protocol preferences has 80,3128,3132,5985,8080,8088,11371,1900,2869,2710 as all the TCP ports it's currently looking for, which should be fine. I've also got all three checkboxes for HTTP reassembly checked as well.</p></div><div id="comment-47889-info" class="comment-info"><span class="comment-age">(23 Nov '15, 13:54)</span> Kristaphonie</div></div><span id="47896"></span><div id="comment-47896" class="comment"><div id="post-47896-score" class="comment-score"></div><div class="comment-text"><p>Could you please share a capture so as to see what the issue could be? You are so far the first one reporting this. Just to remove any doubt: when you talk about a 2.0.0 developer version, are you referring to Wireshark 2.0.0 officially released last week? Or are you using a nightly build prior to this official launch?</p></div><div id="comment-47896-info" class="comment-info"><span class="comment-age">(23 Nov '15, 14:41)</span> Pascal Quantin</div></div></div><div id="comment-tools-47816" class="comment-tools"></div><div class="clear"></div><div id="comment-47816-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

