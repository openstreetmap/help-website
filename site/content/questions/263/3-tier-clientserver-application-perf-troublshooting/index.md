+++
type = "question"
title = "3-tier Client/Server  application perf. troublshooting"
description = '''Hi, I have a C/S app starts from a shared folder on the file server then connects to the AD to authenticate, and finally connects to the DB server to pull up the data. During certain moments clients complain of slow access to the data at the different stages of the app! I want to use Wireshark to ca...'''
date = "2010-09-22T11:11:00Z"
lastmod = "2012-10-18T18:28:00Z"
weight = 263
keywords = [ "packets", "troubleshooting", "multi-tier", "correlation" ]
aliases = [ "/questions/263" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [3-tier Client/Server application perf. troublshooting](/questions/263/3-tier-clientserver-application-perf-troublshooting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-263-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-263-score" class="post-score" title="current number of votes">0</div><span id="post-263-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a C/S app starts from a shared folder on the file server then connects to the AD to authenticate, and finally connects to the DB server to pull up the data. During certain moments clients complain of slow access to the data at the different stages of the app! I want to use Wireshark to capture traffic at different segments of the access network and then correlate them in one file to be analyzed by Wireshark Analysis tool. Is this possible? does Wireshark has the capacity to do such a job?</p><p>Thank you indeed.</p><p>Ahmed Althagafi IT Consultant Washington DC.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-troubleshooting" rel="tag" title="see questions tagged &#39;troubleshooting&#39;">troubleshooting</span> <span class="post-tag tag-link-multi-tier" rel="tag" title="see questions tagged &#39;multi-tier&#39;">multi-tier</span> <span class="post-tag tag-link-correlation" rel="tag" title="see questions tagged &#39;correlation&#39;">correlation</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Sep '10, 11:11</strong></p><img src="https://secure.gravatar.com/avatar/1e2f1cab5f7659363ec665a02797dbb6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="althagafi&#39;s gravatar image" /><p><span>althagafi</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="althagafi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Sep '10, 01:57</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-263" class="comments-container"></div><div id="comment-tools-263" class="comment-tools"></div><div class="clear"></div><div id="comment-263-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="265"></span>

<div id="answer-container-265" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-265-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-265-score" class="post-score" title="current number of votes">3</div><span id="post-265-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark itself can not correlate the packets taken at different places, but you can use "editcap -t" to adjust the timestamps in a tracefile. If you know the delta between the same packet in two tracefiles, you can adjust one file and then use 'mergecap' to merge the files into one. You can repeat the process for other tiers until you have one big file. You can then use 'wireshark' to analyze that file, but you still have to correlate packets from each tier yourself.</p><p>You can use an icmp-echo/icmp-echo-reply pair to calculate the delta time between files. Or another good one to use is a SYN and SYN/ACK. I use both a request and a responce and calculate the mean to rule out the round-trip time between the systems.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '10, 11:31</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-265" class="comments-container"><span id="15029"></span><div id="comment-15029" class="comment"><div id="post-15029-score" class="comment-score"></div><div class="comment-text"><p>Is there any simpler method to do this ? or any tool through which we can accomplish this ?</p></div><div id="comment-15029-info" class="comment-info"><span class="comment-age">(16 Oct '12, 01:13)</span> <span class="comment-user userinfo">Akhtar</span></div></div><span id="15098"></span><div id="comment-15098" class="comment"><div id="post-15098-score" class="comment-score"></div><div class="comment-text"><p>Are you sure your app talks <em>directly</em> to the DB? There is no middleware in involved? Although Riverbed's Pilot and Opnet can do multi-tier analysis, I'm not convinced you need it. It's TCP after all and you're not trying to nail down where the packet loss is occurring. If there is no middleware involved, this is normal protocol analysis. As the DBA if he/she sees any table scans or locked tables. That may explain the periodic slowness. Again, I'm assuming you ruled out pkt loss as a culprit.</p></div><div id="comment-15098-info" class="comment-info"><span class="comment-age">(18 Oct '12, 18:28)</span> <span class="comment-user userinfo">hansangb</span></div></div></div><div id="comment-tools-265" class="comment-tools"></div><div class="clear"></div><div id="comment-265-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

