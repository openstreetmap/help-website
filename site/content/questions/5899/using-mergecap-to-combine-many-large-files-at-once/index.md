+++
type = "question"
title = "using Mergecap to combine many large files at once"
description = '''Using the command &quot;Mergecap&quot; is great when you only have a handful of files (say less than 10) but i have an instance where I am generating lots of large files in Tshark (sizes = 200m @) from a single site and want to look at them in one continuous file instead of a file set. I also want to look at ...'''
date = "2011-08-26T21:27:00Z"
lastmod = "2011-08-27T15:13:00Z"
weight = 5899
keywords = [ "mergecap" ]
aliases = [ "/questions/5899" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [using Mergecap to combine many large files at once](/questions/5899/using-mergecap-to-combine-many-large-files-at-once)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5899-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5899-score" class="post-score" title="current number of votes">0</div><span id="post-5899-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Using the command "Mergecap" is great when you only have a handful of files (say less than 10) but i have an instance where I am generating lots of large files in Tshark (sizes = 200m @) from a single site and want to look at them in one continuous file instead of a file set. I also want to look at them in Pilot on occasion and when using Mergecap, I have to hand type each file in the string that I want to merge. A day's worth is often 140 files and 31G or more. Is there a way to take all the files in a given folder and merge them into a "superfile" all at once instead of that long string? The final file would get pretty big but Pilot is good up to 6 or so Gigs. Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mergecap" rel="tag" title="see questions tagged &#39;mergecap&#39;">mergecap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Aug '11, 21:27</strong></p><img src="https://secure.gravatar.com/avatar/f797bdc41d990dca073837114e048b1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EricKnaus&#39;s gravatar image" /><p><span>EricKnaus</span><br />
<span class="score" title="46 reputation points">46</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EricKnaus has no accepted answers">0%</span></p></div></div><div id="comments-container-5899" class="comments-container"></div><div id="comment-tools-5899" class="comment-tools"></div><div class="clear"></div><div id="comment-5899-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5901"></span>

<div id="answer-container-5901" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5901-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5901-score" class="post-score" title="current number of votes">2</div><span id="post-5901-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Here are some examples:<br />
$ mergecap *.cap -w test1.pcap<br />
$ mergecap *.pcap -w test2.pcap<br />
$ mergecap *.*cap -w test3.pcap</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '11, 01:28</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p><span>joke</span><br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Aug '11, 01:32</strong> </span></p></div></div><div id="comments-container-5901" class="comments-container"><span id="5904"></span><div id="comment-5904" class="comment"><div id="post-5904-score" class="comment-score"></div><div class="comment-text"><p>Thanks - those worked great!<br />
An interesting caveat though is that while I am able to open 1G and greater files that were merged using Mergecap in WS1.7, I am unable to open the same file in Pilot. It returns a "link layer" error. Would this be an issue in the way WS merges multiple large files or something going on in Pilot. Here's another. When I used the merge within in the WS GUI, Pilot WAS able to read that. Strange</p></div><div id="comment-5904-info" class="comment-info"><span class="comment-age">(27 Aug '11, 13:16)</span> <span class="comment-user userinfo">EricKnaus</span></div></div><span id="5905"></span><div id="comment-5905" class="comment"><div id="post-5905-score" class="comment-score">2</div><div class="comment-text"><p>That's because in WS1.7 the default file format has been changed to pcap-ng and pilot does not read pcap-ng files. Unfortunately there is no switch in the CLI utilities to save as pcap in WS1.7. You can either build your own version where you use the configure script to default back to pcap or you can use the CLI utilities of 1.6.1</p><p>(there needs to be a switch to save as pcap, but it is not developed yet)</p></div><div id="comment-5905-info" class="comment-info"><span class="comment-age">(27 Aug '11, 15:13)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-5901" class="comment-tools"></div><div class="clear"></div><div id="comment-5901-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

