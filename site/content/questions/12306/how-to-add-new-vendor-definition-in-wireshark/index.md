+++
type = "question"
title = "How to add New vendor definition in wireshark?"
description = '''hi, can anyone tell me how to add new vendor-id &amp;amp; its attributes definition in wireshark? I have wireshark Version 1.6.5 (SVN Rev 40429 from /trunk-1.6) installed on my laptop with windows7 (64-bit edition).  I tried to add the vendor Id for Starent in dictionary.xml and also copied the starent....'''
date = "2012-06-29T03:04:00Z"
lastmod = "2012-06-29T13:37:00Z"
weight = 12306
keywords = [ "starent", "dictionary" ]
aliases = [ "/questions/12306" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to add New vendor definition in wireshark?](/questions/12306/how-to-add-new-vendor-definition-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12306-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12306-score" class="post-score" title="current number of votes">0</div><span id="post-12306-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi, can anyone tell me how to add new vendor-id &amp; its attributes definition in wireshark?</p><p>I have wireshark Version 1.6.5 (SVN Rev 40429 from /trunk-1.6) installed on my laptop with windows7 (64-bit edition).</p><p>I tried to add the vendor Id for Starent in dictionary.xml and also copied the starent.xml under the diameter folder in Program Files&gt;&gt;wireshark; but it seems either I have missed out somewhere or added wrong definition. I still get the following error when reading the pcap. "Unknown Vendor, if you know whose this is you can add it to dictionary.xml"</p><p>Your help is appreciated.</p><p>BR//Abhinav</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-starent" rel="tag" title="see questions tagged &#39;starent&#39;">starent</span> <span class="post-tag tag-link-dictionary" rel="tag" title="see questions tagged &#39;dictionary&#39;">dictionary</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jun '12, 03:04</strong></p><img src="https://secure.gravatar.com/avatar/ebea5e28ef7f9e151dd0b1b1b6986389?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Abhinav%20Singh&#39;s gravatar image" /><p><span>Abhinav Singh</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Abhinav Singh has no accepted answers">0%</span></p></div></div><div id="comments-container-12306" class="comments-container"></div><div id="comment-tools-12306" class="comment-tools"></div><div class="clear"></div><div id="comment-12306-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12336"></span>

<div id="answer-container-12336" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12336-score" class="post-score" title="current number of votes">0</div><span id="post-12336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It would help if you listed exactly the changes you made to dictionary.xml and also starent.xml. Actually, even better, submit them as a bug report so we could support into Wireshark.</p><p>If you added Starent as a subfile (starent.xml) then there are some things that have to be done in dictionary.xml; you do need to be sure you follow the same pattern as is done with the other sub-files. If in doubt, you could also just try adding the vendor and attributes in dictionary.xml directly.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '12, 13:37</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-12336" class="comments-container"></div><div id="comment-tools-12336" class="comment-tools"></div><div class="clear"></div><div id="comment-12336-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

