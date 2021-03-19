+++
type = "question"
title = "remove duplicate results"
description = '''Hello, I am trying to produce report of nmap scan to my uni with all open ports on target host. I just need to remove duplicates from my outcome. Can you please help? ip.addr==172.16.121.145 &amp;amp;&amp;amp; ip.addr==172.16.121.143 &amp;amp;&amp;amp; ip.proto == 6 and tcp.flags == 18 Best regards Marcin'''
date = "2014-05-02T10:52:00Z"
lastmod = "2014-05-02T11:46:00Z"
weight = 32430
keywords = [ "duplicate" ]
aliases = [ "/questions/32430" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [remove duplicate results](/questions/32430/remove-duplicate-results)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32430-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32430-score" class="post-score" title="current number of votes">0</div><span id="post-32430-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am trying to produce report of nmap scan to my uni with all open ports on target host. I just need to remove duplicates from my outcome. Can you please help?</p><p>ip.addr==172.16.121.145 &amp;&amp; ip.addr==172.16.121.143 &amp;&amp; ip.proto == 6 and tcp.flags == 18</p><p>Best regards Marcin</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-duplicate" rel="tag" title="see questions tagged &#39;duplicate&#39;">duplicate</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 May '14, 10:52</strong></p><img src="https://secure.gravatar.com/avatar/f72baa65697144ca66ac3f4280d03bc7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brayan6611&#39;s gravatar image" /><p><span>brayan6611</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brayan6611 has no accepted answers">0%</span></p></div></div><div id="comments-container-32430" class="comments-container"><span id="32437"></span><div id="comment-32437" class="comment"><div id="post-32437-score" class="comment-score"></div><div class="comment-text"><p>Some questions.</p><ul><li>what's wrong with the nmap report itself, meaning why do you want to complicate things while you already have a good solution ? ;-))</li><li>can you please define what <strong>duplicates</strong> are in that context?</li></ul><blockquote><p>I need to present this in Wireshark <strong>as a proof</strong>,</p></blockquote><p>As a <strong>proof</strong> for what exactly?</p><blockquote><p>is there a filter parameter to show only <strong>unique</strong> results</p></blockquote><p><strong>unique</strong> in term of what? Unique IP address, unique destination port?</p></div><div id="comment-32437-info" class="comment-info"><span class="comment-age">(02 May '14, 11:46)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-32430" class="comment-tools"></div><div class="clear"></div><div id="comment-32430-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32432"></span>

<div id="answer-container-32432" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32432-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32432-score" class="post-score" title="current number of votes">0</div><span id="post-32432-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I guess you're not talking about duplicate packets, but somehow duplicate results in your report list.</p><p>Easiest way around things like that is to export the packet list to CSV (see File menu, choose "Export Packet Dissections" -&gt; "as CSV file" and save the results to a file. Then deduplicate the text lines in that file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '14, 11:29</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-32432" class="comments-container"><span id="32434"></span><div id="comment-32434" class="comment"><div id="post-32434-score" class="comment-score"></div><div class="comment-text"><p>Thank you Jasper for quick response. I need to present this in Wireshark as a proof, there fore I don't want to edit. I don't know Wireshark well but is there a filter parameter to show only unique results?</p><p>Best regards Marcin</p></div><div id="comment-32434-info" class="comment-info"><span class="comment-age">(02 May '14, 11:33)</span> <span class="comment-user userinfo">brayan6611</span></div></div><span id="32435"></span><div id="comment-32435" class="comment"><div id="post-32435-score" class="comment-score"></div><div class="comment-text"><p>That depends on your current results. Is there anything in a duplicate that is different than the original? If so, you can use that difference to filter the duplicates out. It's kinda hard to give more advice without seeing what you're working with; the filter does not help because it is unclear what it was used on.</p></div><div id="comment-32435-info" class="comment-info"><span class="comment-age">(02 May '14, 11:35)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-32432" class="comment-tools"></div><div class="clear"></div><div id="comment-32432-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

