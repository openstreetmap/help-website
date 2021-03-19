+++
type = "question"
title = "GTP: ip.src displays only encapsulated IP address"
description = '''Hi, I have GTP encapsulated traffic. So one IP package contains 2 IP addresses:  The address of the IP package The address of the GTP encapsulated IP package   When I specify ip.src as display filter or as &quot;field&quot; in tshark I only get the address of the encapsulated ip traffic. Can anyone tell me ho...'''
date = "2010-09-17T04:34:00Z"
lastmod = "2010-09-17T11:01:00Z"
weight = 169
keywords = [ "gtp" ]
aliases = [ "/questions/169" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [GTP: ip.src displays only encapsulated IP address](/questions/169/gtp-ipsrc-displays-only-encapsulated-ip-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-169-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-169-score" class="post-score" title="current number of votes">0</div><span id="post-169-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have GTP encapsulated traffic. So one IP package contains 2 IP addresses:</p><ul><li>The address of the IP package</li><li>The address of the GTP encapsulated IP package</li></ul><p>When I specify ip.src as display filter or as "field" in tshark I only get the address of the encapsulated ip traffic.</p><p>Can anyone tell me how I can display the ip address of the original ip package ?</p><p>Thanks, Ralf</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gtp" rel="tag" title="see questions tagged &#39;gtp&#39;">gtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Sep '10, 04:34</strong></p><img src="https://secure.gravatar.com/avatar/bff893de5b8eb326b46d7480d3750cd4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bradfield&#39;s gravatar image" /><p><span>bradfield</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bradfield has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Sep '10, 04:37</strong> </span></p></div></div><div id="comments-container-169" class="comments-container"></div><div id="comment-tools-169" class="comment-tools"></div><div class="clear"></div><div id="comment-169-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="176"></span>

<div id="answer-container-176" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-176-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-176-score" class="post-score" title="current number of votes">1</div><span id="post-176-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In tshark you can use the option "-E occurrence=&lt;f|l|a&gt;", where "f" means the first occurrence of a field with multiple instances, "l" means last occurrence and "a" means all occurrences. If you select "a", then all occurrences are aggregated by a comma by default, but this can be changed by the "-E aggregator=&lt;char&gt;" option.</p><p>This functionality does not (yet) exist for Wireshark's custom columns.</p><p><em>Update 22 September:</em> I just submitted new code that will make it possible to select the occurrence in Wireshark too. In a few hours there will be an automated build at <a href="http://www.wireshark.org/download/automated/">http://www.wireshark.org/download/automated/</a></p><p>(make sure you pick a file with a number higher than 34186, otherwise the patch will not be in it)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '10, 05:31</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Sep '10, 14:01</strong> </span></p></div></div><div id="comments-container-176" class="comments-container"></div><div id="comment-tools-176" class="comment-tools"></div><div class="clear"></div><div id="comment-176-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="188"></span>

<div id="answer-container-188" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-188-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-188-score" class="post-score" title="current number of votes">0</div><span id="post-188-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yep. That solved my problem.</p><p>Thanks, Ralf</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '10, 10:51</strong></p><img src="https://secure.gravatar.com/avatar/bff893de5b8eb326b46d7480d3750cd4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bradfield&#39;s gravatar image" /><p><span>bradfield</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bradfield has no accepted answers">0%</span></p></div></div><div id="comments-container-188" class="comments-container"><span id="189"></span><div id="comment-189" class="comment"><div id="post-189-score" class="comment-score"></div><div class="comment-text"><p>This is a Q&amp;A site, which operates a little differently from traditional web forums. If you're posting a comment, please click on the "add new comment" button.</p><p>If @SYNbit answered your question, please click on the check mark in order to accept his answer. That way it will float to the top and he'll earn karma points.</p></div><div id="comment-189-info" class="comment-info"><span class="comment-age">(17 Sep '10, 11:00)</span> <span class="comment-user userinfo">Gerald Combs ♦♦</span></div></div><span id="190"></span><div id="comment-190" class="comment"><div id="post-190-score" class="comment-score"></div><div class="comment-text"><p>Hi Ralf, glad it solved your problem!</p><p>Would you be so kind to "accept" my answer by clicking on the checkmark? That way the question will not show up on the "unanswered" list anymore. It also helps people to find the correct answer to the question (although that is not really a problem in this case) :-)</p><p>Last thing, it's better to use "add new comment" for this kind of message instead of posting a new "answer".</p><p>Cheers, Sake</p></div><div id="comment-190-info" class="comment-info"><span class="comment-age">(17 Sep '10, 11:01)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-188" class="comment-tools"></div><div class="clear"></div><div id="comment-188-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

