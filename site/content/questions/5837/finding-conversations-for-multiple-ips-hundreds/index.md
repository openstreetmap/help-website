+++
type = "question"
title = "Finding conversations for multiple ips (hundreds)"
description = '''Is there a way in tshark to look conversations from a large list of ips? I have a list of ips in a text file. There are usually 100+ ips in the file. I can do some command line scripting to make this work, but I was wondering if I could use a file as input to the filter. So ideally it would look som...'''
date = "2011-08-24T06:25:00Z"
lastmod = "2011-08-25T09:20:00Z"
weight = 5837
keywords = [ "filter", "ips", "multiple" ]
aliases = [ "/questions/5837" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Finding conversations for multiple ips (hundreds)](/questions/5837/finding-conversations-for-multiple-ips-hundreds)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5837-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5837-score" class="post-score" title="current number of votes">0</div><span id="post-5837-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way in tshark to look conversations from a large list of ips? I have a list of ips in a text file. There are usually 100+ ips in the file. I can do some command line scripting to make this work, but I was wondering if I could use a file as input to the filter.</p><p>So ideally it would look something like this: tshark -qnr mydump.pcap -z conv,ip,ip.addr==&lt;myipfile.txt&gt;</p><p>And get all conversations involving the ips in my file.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-ips" rel="tag" title="see questions tagged &#39;ips&#39;">ips</span> <span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Aug '11, 06:25</strong></p><img src="https://secure.gravatar.com/avatar/2027cc56dd6f4a890e14108d3864677c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DeBuG&#39;s gravatar image" /><p><span>DeBuG</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DeBuG has no accepted answers">0%</span></p></div></div><div id="comments-container-5837" class="comments-container"></div><div id="comment-tools-5837" class="comment-tools"></div><div class="clear"></div><div id="comment-5837-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5871"></span>

<div id="answer-container-5871" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5871-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5871-score" class="post-score" title="current number of votes">0</div><span id="post-5871-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Re: ... but I was wondering if I could use a file as input to the filter.</p><p>The short answer: not without some command line scripting. :)</p><p>Would it work (and be simpler) to just generate the conversation list without a filter and then use <code>grep -Ff myipfile.txt ...</code> (or something similar) to get the list of conversations for just the desired IPs ?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Aug '11, 09:20</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Aug '11, 09:21</strong> </span></p></div></div><div id="comments-container-5871" class="comments-container"></div><div id="comment-tools-5871" class="comment-tools"></div><div class="clear"></div><div id="comment-5871-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

