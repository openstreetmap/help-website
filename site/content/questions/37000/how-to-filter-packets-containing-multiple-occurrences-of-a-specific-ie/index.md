+++
type = "question"
title = "How to filter packets containing multiple occurrences of a specific IE?"
description = '''Background: Some IE may appear more than once in a packet, like &quot;Source IP&quot; in below pict:   Another example is Host name &quot;dns.resp.name&quot; in below DNS response (with red underline):  Question: Can we filter such message, with some generic expression like &quot;#(ip.src)&amp;gt;1&quot; or &quot;#(dns.resp.name)&amp;gt;1? T...'''
date = "2014-10-13T01:47:00Z"
lastmod = "2014-10-21T18:53:00Z"
weight = 37000
keywords = [ "filtering", "display-filter" ]
aliases = [ "/questions/37000" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to filter packets containing multiple occurrences of a specific IE?](/questions/37000/how-to-filter-packets-containing-multiple-occurrences-of-a-specific-ie)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37000-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37000-score" class="post-score" title="current number of votes">0</div><span id="post-37000-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><h1 id="background">Background:</h1><p>Some IE may appear more than once in a packet, like "Source IP" in below pict: <img src="https://osqa-ask.wireshark.org/upfiles/packet_IEs.png" alt="IE &quot;Source IP&quot; appears 2 times due to msg encapsulation" /></p><p>Another example is Host name "dns.resp.name" in below DNS response (with red underline): <img src="https://osqa-ask.wireshark.org/upfiles/packet_IEs-2.png" alt="Host names appears 2 times in DNS response" /></p><h1 id="question-can-we-filter-such-message-with-some-generic-expression-like-ip.src1-or-dns.resp.name1">Question: Can we filter such message, with some generic expression like "#(ip.src)&gt;1" or "#(dns.resp.name)&gt;1?</h1><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filtering" rel="tag" title="see questions tagged &#39;filtering&#39;">filtering</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Oct '14, 01:47</strong></p><img src="https://secure.gravatar.com/avatar/1076e6e05527f71ac739a860e91182e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Weller&#39;s gravatar image" /><p><span>Weller</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Weller has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Oct '14, 02:27</strong> </span></p></div></div><div id="comments-container-37000" class="comments-container"><span id="37002"></span><div id="comment-37002" class="comment"><div id="post-37002-score" class="comment-score"></div><div class="comment-text"><p>So you're not interested in finding specific IPs, but just packets that have more than one IP layer?</p></div><div id="comment-37002-info" class="comment-info"><span class="comment-age">(13 Oct '14, 01:57)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="37003"></span><div id="comment-37003" class="comment"><div id="post-37003-score" class="comment-score"></div><div class="comment-text"><p>That's right in this example. And the repeating IE could be something else, too, like alternative IPs in one DNS responses message. Then is it possible to filter DNS response with 2 or more IPs from the ones with only 1 IP?</p></div><div id="comment-37003-info" class="comment-info"><span class="comment-age">(13 Oct '14, 02:04)</span> <span class="comment-user userinfo">Weller</span></div></div><span id="37004"></span><div id="comment-37004" class="comment"><div id="post-37004-score" class="comment-score"></div><div class="comment-text"><p>I don't think this is possible - I would try to filter on things like the GPRS tunneling layer, because if that layer is present you'll know there are multiple layers.</p></div><div id="comment-37004-info" class="comment-info"><span class="comment-age">(13 Oct '14, 02:11)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-37000" class="comment-tools"></div><div class="clear"></div><div id="comment-37000-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37183"></span>

<div id="answer-container-37183" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37183-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37183-score" class="post-score" title="current number of votes">1</div><span id="post-37183-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Weller has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>(Just to put an Answer on this question):</p><p>This isn't possible today. It's something the Wireshark developers have been talking about for a while, although usually in the context of "how can I filter for only the encapsulated IP address (while ignoring the outer IP address)." But if we ever get that working it would likely solve your problem/question too.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '14, 03:41</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></img></div></div><div id="comments-container-37183" class="comments-container"><span id="37185"></span><div id="comment-37185" class="comment"><div id="post-37185-score" class="comment-score"></div><div class="comment-text"><p>Is IE an abbreviation of "Inner Encapsulation" or similar?</p></div><div id="comment-37185-info" class="comment-info"><span class="comment-age">(20 Oct '14, 03:45)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="37186"></span><div id="comment-37186" class="comment"><div id="post-37186-score" class="comment-score"></div><div class="comment-text"><p>To me IE means "Information Element" but I don't know if that was the intended use here.</p></div><div id="comment-37186-info" class="comment-info"><span class="comment-age">(20 Oct '14, 04:51)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="37192"></span><div id="comment-37192" class="comment"><div id="post-37192-score" class="comment-score"></div><div class="comment-text"><p>I have no idea, to me IE means a browser I'm occasionally forced to use due to regressive servers.</p></div><div id="comment-37192-info" class="comment-info"><span class="comment-age">(20 Oct '14, 05:10)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="37258"></span><div id="comment-37258" class="comment"><div id="post-37258-score" class="comment-score"></div><div class="comment-text"><p>Thank JeffMorriss for the answer and explanations! And yes, "IE" means "Information Element" here (Sorry for the confusion).</p></div><div id="comment-37258-info" class="comment-info"><span class="comment-age">(21 Oct '14, 18:42)</span> <span class="comment-user userinfo">Weller</span></div></div><span id="37259"></span><div id="comment-37259" class="comment"><div id="post-37259-score" class="comment-score"></div><div class="comment-text"><p>So it seems to be some function possibly in future implementation. Let me try some workaround for the moment then. Thank you, Jeff!</p></div><div id="comment-37259-info" class="comment-info"><span class="comment-age">(21 Oct '14, 18:53)</span> <span class="comment-user userinfo">Weller</span></div></div></div><div id="comment-tools-37183" class="comment-tools"></div><div class="clear"></div><div id="comment-37183-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

