+++
type = "question"
title = "Use plaintext file for a capturing filter"
description = '''Hi, Is it possible to use a plaintext file with ip-ranges (CIDR-Notation) in it to exclude specific ip-ranges from the capturing process? If so, how can i do that? Thanks in advance Steve'''
date = "2012-04-28T07:49:00Z"
lastmod = "2012-05-02T13:05:00Z"
weight = 10499
keywords = [ "cidr", "ip-ranges", "exclusion", "file" ]
aliases = [ "/questions/10499" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Use plaintext file for a capturing filter](/questions/10499/use-plaintext-file-for-a-capturing-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10499-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10499-score" class="post-score" title="current number of votes">0</div><span id="post-10499-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Is it possible to use a plaintext file with ip-ranges (CIDR-Notation) in it to exclude specific ip-ranges from the capturing process? If so, how can i do that?</p><p>Thanks in advance</p><p>Steve</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-cidr" rel="tag" title="see questions tagged &#39;cidr&#39;">cidr</span> <span class="post-tag tag-link-ip-ranges" rel="tag" title="see questions tagged &#39;ip-ranges&#39;">ip-ranges</span> <span class="post-tag tag-link-exclusion" rel="tag" title="see questions tagged &#39;exclusion&#39;">exclusion</span> <span class="post-tag tag-link-file" rel="tag" title="see questions tagged &#39;file&#39;">file</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Apr '12, 07:49</strong></p><img src="https://secure.gravatar.com/avatar/317bb5d05e5f6f6cba2d3f96858f50b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LA_FORGE&#39;s gravatar image" /><p><span>LA_FORGE</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LA_FORGE has no accepted answers">0%</span></p></div></div><div id="comments-container-10499" class="comments-container"></div><div id="comment-tools-10499" class="comment-tools"></div><div class="clear"></div><div id="comment-10499-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="10537"></span>

<div id="answer-container-10537" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10537-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10537-score" class="post-score" title="current number of votes">1</div><span id="post-10537-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>at least on unix you can do it this way:</p><p><span class="__cf_email__" data-cfemail="daa8b5b5ae9aa9afa8bca9aebbaeb3b5b4">[email protected]</span>:/var/tmp# cat excluded-networks<br />
10.1.1.0/24<br />
10.1.2.0/24<br />
192.168.0.0/16<br />
</p><p>Then run this command:</p><p><span class="__cf_email__" data-cfemail="57253838231724222531242336233e3839">[email protected]</span>:/var/tmp# tshark -n host 1.2.3.4 and `perl -pe 'BEGIN {print " ( ip"}; END {print ") "}; $_ =~ s/n//; $_ = " and not net $_ "' &lt; /var/tmp/excluded-networks`</p><p>Replace the first part of the filter - here 'host 1.2.3.4' with whatever you like.</p><p>WARNING: If the number of networks gets large (more than 10!), this does NOT scale, as the resulting capture filter will be ways to complex for fast networks!!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '12, 14:25</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Apr '12, 14:26</strong> </span></p></div></div><div id="comments-container-10537" class="comments-container"><span id="10548"></span><div id="comment-10548" class="comment"><div id="post-10548-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much!!</p></div><div id="comment-10548-info" class="comment-info"><span class="comment-age">(01 May '12, 08:36)</span> <span class="comment-user userinfo">LA_FORGE</span></div></div><span id="10549"></span><div id="comment-10549" class="comment"><div id="post-10549-score" class="comment-score"></div><div class="comment-text"><p><span>@LA_FORGE</span> I've converted your "answer" into a comment. Please see the <a href="http://ask.wireshark.org/faq/">FAQ</a> to see how this Q&amp;A site works.</p></div><div id="comment-10549-info" class="comment-info"><span class="comment-age">(01 May '12, 09:45)</span> <span class="comment-user userinfo">multipleinte...</span></div></div><span id="10551"></span><div id="comment-10551" class="comment"><div id="post-10551-score" class="comment-score"></div><div class="comment-text"><p>I'm glad that I was able to help...</p></div><div id="comment-10551-info" class="comment-info"><span class="comment-age">(01 May '12, 11:53)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="10552"></span><div id="comment-10552" class="comment"><div id="post-10552-score" class="comment-score"></div><div class="comment-text"><p><span>@Kurt</span> how many ranges are possible on slow networks? The CPU power shouldn't be the problem, i've a 80.000 MIPS machine here</p></div><div id="comment-10552-info" class="comment-info"><span class="comment-age">(01 May '12, 14:00)</span> <span class="comment-user userinfo">LA_FORGE</span></div></div><span id="10554"></span><div id="comment-10554" class="comment"><div id="post-10554-score" class="comment-score"></div><div class="comment-text"><p>Well, that's really hard to say. It depends on so many parameters. Just out of thin air, I would say around 20-30 (NOT tested!).</p><p>Besides the CPU, the max length of the CLI parameters (of the shell) could be a problem too. Maybe there is a limit in tshark regading the length off a capture filter (check the code).</p><p>BTW: What are you looking for? Maybe there is a better way to achieve that goal.</p></div><div id="comment-10554-info" class="comment-info"><span class="comment-age">(01 May '12, 14:38)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="10612"></span><div id="comment-10612" class="comment not_top_scorer"><div id="post-10612-score" class="comment-score"></div><div class="comment-text"><p>I want to exclude many ranges (blacklist) from the capturing process. Since the age of 18 i've been blind and i'm depending on a screenreader software to use the computer. But i don't want to refrain of wireshark/tshark, only the flood of information is the problem for me.</p></div><div id="comment-10612-info" class="comment-info"><span class="comment-age">(02 May '12, 13:05)</span> <span class="comment-user userinfo">LA_FORGE</span></div></div></div><div id="comment-tools-10537" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-10537-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10530"></span>

<div id="answer-container-10530" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10530-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10530-score" class="post-score" title="current number of votes">0</div><span id="post-10530-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Not directly.</p><p>You could however, do some scripting to specify as a command line arg a capture filter (or display filter) to wireshark or tshark or a capture filter to dumpcap.</p><p>See the wireshark/tshark/dumpcap help and man pages.</p><p>Feel free to submit an enhancement request (or patch implementing the feature) at <a href="http://bugs.wireshark.org">bugs.wireshark.org</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '12, 10:50</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Apr '12, 10:52</strong> </span></p></div></div><div id="comments-container-10530" class="comments-container"></div><div id="comment-tools-10530" class="comment-tools"></div><div class="clear"></div><div id="comment-10530-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

