+++
type = "question"
title = "Compare and merge capture files"
description = '''I&#x27;m looking for a method or tool to compare and merge capture-files. I already googled a lot and found tools like pcapdiff and the buildin ws-compare-function, but none fits my needs. I want to do the same action (maybe sending an email) three times and everytime capture the internet-traffic. Afterw...'''
date = "2015-05-29T10:27:00Z"
lastmod = "2015-05-30T08:06:00Z"
weight = 42744
keywords = [ "filter", "pattern", "compare", "difference", "merge" ]
aliases = [ "/questions/42744" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Compare and merge capture files](/questions/42744/compare-and-merge-capture-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42744-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42744-score" class="post-score" title="current number of votes">0</div><span id="post-42744-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm looking for a method or tool to compare and merge capture-files. I already googled a lot and found tools like pcapdiff and the buildin ws-compare-function, but none fits my needs.</p><p>I want to do the same action (maybe sending an email) three times and everytime capture the internet-traffic. Afterwards I want to compare all three capture-files and filter out the packets which are captured everytime (cut off unique packets or packet-pattern), so i could cut out the traffic which has nothing to do with sending the email.</p><p>Is there any know tool which compares different pcap files and filter out packets which not fits the overall pattern of packets according to IP-Adresse and size ? It is not possible to compare those files by reference to time-stamps or payload. (payload encrypted)</p><p>I would be very happy if anyone knows this problem and got a solution.</p><p>Kind regards,</p><p>Alex</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-pattern" rel="tag" title="see questions tagged &#39;pattern&#39;">pattern</span> <span class="post-tag tag-link-compare" rel="tag" title="see questions tagged &#39;compare&#39;">compare</span> <span class="post-tag tag-link-difference" rel="tag" title="see questions tagged &#39;difference&#39;">difference</span> <span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 May '15, 10:27</strong></p><img src="https://secure.gravatar.com/avatar/582563271436bdeb3aada21543ecc652?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="z4ck&#39;s gravatar image" /><p><span>z4ck</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="z4ck has no accepted answers">0%</span></p></div></div><div id="comments-container-42744" class="comments-container"><span id="42761"></span><div id="comment-42761" class="comment"><div id="post-42761-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I would be very happy if anyone knows this problem and got a solution.</p></blockquote><p>well, you did not describe your problem, so it's hard to suggest a solution. What 'similarities' are you trying to find in <strong>3 totally different ( TCP streams</strong> (because the payload is encrypted)?</p></div><div id="comment-42761-info" class="comment-info"><span class="comment-age">(30 May '15, 08:06)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-42744" class="comment-tools"></div><div class="clear"></div><div id="comment-42744-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42745"></span>

<div id="answer-container-42745" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42745-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42745-score" class="post-score" title="current number of votes">0</div><span id="post-42745-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Most tools I have seen only compare capture files that have been captured at multiple locations at the same time (meaning, with at least some truly identical packets). I'm not even sure your approach of comparing different captures taken at different times is going to work - even things as simple as sending a mail may not be the same in each capture, e.g. when the MX record for the destination mailserver is doing some kind of round robin. In that case you'll get different destination IPs every time and can't compare anything.</p><p>Other than that I guess you're down to manual work - I don't think there is any tool that can do what you want. Maybe you can use the conversation statistics of Wireshark, export the table for each file you have (sorted the same way, of course), and then use a text diff tool to find out which lines are different.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 May '15, 10:57</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-42745" class="comments-container"><span id="42749"></span><div id="comment-42749" class="comment"><div id="post-42749-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper,</p><p>thanks for your fast answer.</p><p>Atm I guess I have to filter packets manually as you said. May I try export to txt and cut with awk or sed. Maybe afterwards I get a result to work with.</p><p>I don't really thought about the MX records and my other routing-changes.</p><p>May I could try to compare pcap-entries by reference to packet-size and progress.</p><p>In the end the merge-process is not the main thing, but it could be helpful to cut off some surrounding traffic.</p><p>Thanks</p></div><div id="comment-42749-info" class="comment-info"><span class="comment-age">(29 May '15, 11:36)</span> <span class="comment-user userinfo">z4ck</span></div></div></div><div id="comment-tools-42745" class="comment-tools"></div><div class="clear"></div><div id="comment-42745-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

