+++
type = "question"
title = "Search for a string that span over two data packets"
description = '''Was searching for a string that span over two TCP data packets, it doesn&#x27;t find it.  My Wireshark is 1.10.6. Thanks. '''
date = "2015-12-28T07:06:00Z"
lastmod = "2015-12-28T18:38:00Z"
weight = 48735
keywords = [ "wireshark" ]
aliases = [ "/questions/48735" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Search for a string that span over two data packets](/questions/48735/search-for-a-string-that-span-over-two-data-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48735-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48735-score" class="post-score" title="current number of votes">0</div><span id="post-48735-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Was searching for a string that span over two TCP data packets, it doesn't find it. <img src="https://osqa-ask.wireshark.org/upfiles/2a.png" alt="alt text" /></p><p>My Wireshark is 1.10.6. Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Dec '15, 07:06</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p><span>pktUser1001</span><br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></img></div></div><div id="comments-container-48735" class="comments-container"><span id="48741"></span><div id="comment-48741" class="comment"><div id="post-48741-score" class="comment-score"></div><div class="comment-text"><p>Do you have an example trace for us?</p></div><div id="comment-48741-info" class="comment-info"><span class="comment-age">(28 Dec '15, 12:45)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="48742"></span><div id="comment-48742" class="comment"><div id="post-48742-score" class="comment-score"></div><div class="comment-text"><p>Thanks <span>@christian_r</span>, here is an example pcap: <a href="https://www.dropbox.com/s/5gbpbea0rzxr3c2/http1.pcap?dl=0">https://www.dropbox.com/s/5gbpbea0rzxr3c2/http1.pcap?dl=0</a></p></div><div id="comment-48742-info" class="comment-info"><span class="comment-age">(28 Dec '15, 13:08)</span> <span class="comment-user userinfo">pktUser1001</span></div></div></div><div id="comment-tools-48735" class="comment-tools"></div><div class="clear"></div><div id="comment-48735-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="48744"></span>

<div id="answer-container-48744" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48744-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48744-score" class="post-score" title="current number of votes">0</div><span id="post-48744-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pktUser1001 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>So in this case you have to enable reassembling of the <code>TCP segments</code> AND the reassemling of the <code>HTTP bodies and headers</code>. You can activate it by right clicking the HTTP header in the packet detail and activate the reassembly features as it is shown in the first screenshot.</p><p>After that you can use the search dialog shown at the question. Than it should show you the string in the reassembled byte view. As you can see in the second screenshot.</p><p><strong>Screenshot 1:</strong> <img src="https://osqa-ask.wireshark.org/upfiles/HTTPReassembly1a_JEAPHDR.png" alt="alt text" /></p><p><br />
<strong>Screenshot 2:</strong> <img src="https://osqa-ask.wireshark.org/upfiles/HTTPreassembly2a.png" alt="alt text" /><br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Dec '15, 16:00</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span> </br></br></p></img></div></div><div id="comments-container-48744" class="comments-container"><span id="48745"></span><div id="comment-48745" class="comment"><div id="post-48745-score" class="comment-score"></div><div class="comment-text"><p>Thanks <span>@Christian_R</span>, the key is to select the radio button "Packet details". I used "Packet bytes" which didn't work in this case. Wonder if there are reference on exactly what is "Packet details", does it mean the reassembled TCP data?</p></div><div id="comment-48745-info" class="comment-info"><span class="comment-age">(28 Dec '15, 18:38)</span> <span class="comment-user userinfo">pktUser1001</span></div></div></div><div id="comment-tools-48744" class="comment-tools"></div><div class="clear"></div><div id="comment-48744-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="48736"></span>

<div id="answer-container-48736" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48736-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48736-score" class="post-score" title="current number of votes">0</div><span id="post-48736-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Do you know tcp ip address? If yes then right click on any packet in same sequence -&gt; Follow TCP Stream. In opened new window you can find a string if it exist in particular dump.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Dec '15, 08:31</strong></p><img src="https://secure.gravatar.com/avatar/ae9a73c94923328e3fdaf4998174c35e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vladimir%20R%C3%B5kovanov&#39;s gravatar image" /><p><span>Vladimir Rõk...</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vladimir Rõkovanov has no accepted answers">0%</span></p></img></div></div><div id="comments-container-48736" class="comments-container"><span id="48738"></span><div id="comment-48738" class="comment"><div id="post-48738-score" class="comment-score"></div><div class="comment-text"><p>Thanks <span>@vladimir</span>-rokovanov. Unfortunately I don't know IP address. Even in the case of knowing the session, finding the occurrence of follow TCP stream will not tell me what packets have these string. Any ideas?</p></div><div id="comment-48738-info" class="comment-info"><span class="comment-age">(28 Dec '15, 09:24)</span> <span class="comment-user userinfo">pktUser1001</span></div></div><span id="48739"></span><div id="comment-48739" class="comment"><div id="post-48739-score" class="comment-score"></div><div class="comment-text"><p>You can try search one part of the string and then follow this tcp stream.</p></div><div id="comment-48739-info" class="comment-info"><span class="comment-age">(28 Dec '15, 10:34)</span> <span class="comment-user userinfo">Vladimir Rõk...</span></div></div><span id="48740"></span><div id="comment-48740" class="comment"><div id="post-48740-score" class="comment-score"></div><div class="comment-text"><p>That could be a workaround, albeit tedious when the string is long. Thanks for the idea. Hope there is a clean method.</p></div><div id="comment-48740-info" class="comment-info"><span class="comment-age">(28 Dec '15, 11:56)</span> <span class="comment-user userinfo">pktUser1001</span></div></div></div><div id="comment-tools-48736" class="comment-tools"></div><div class="clear"></div><div id="comment-48736-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

