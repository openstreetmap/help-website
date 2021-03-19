+++
type = "question"
title = "Wireshark/dumpcap ip address frequency/occurrence? How to?"
description = '''Hi, all... I posted this in another forum, so if you&#x27;ve seen it please don&#x27;t gripe me out. My question will appear to present a dumbass-ness that I do not actually possess. In other words, I don&#x27;t know what I&#x27;m doing here or even how to ask about it, but I&#x27;m not completely clueless: I&#x27;m just new to ...'''
date = "2016-07-11T09:20:00Z"
lastmod = "2016-07-12T07:08:00Z"
weight = 53985
keywords = [ "frequency", "dumpcap", "analysis" ]
aliases = [ "/questions/53985" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark/dumpcap ip address frequency/occurrence? How to?](/questions/53985/wiresharkdumpcap-ip-address-frequencyoccurrence-how-to)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53985-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53985-score" class="post-score" title="current number of votes">0</div><span id="post-53985-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, all...</p><p>I posted this in another forum, so if you've seen it please don't gripe me out.</p><p>My question will appear to present a dumbass-ness that I do not actually possess. In other words, I don't know what I'm doing here or even how to ask about it, but I'm not completely clueless: I'm just new to this tool and the best way to analyze its output.</p><p>I'm working on a potential hacking case. I've already exploited 4 of their computers (drives), imaged them and used FTK and Paraben's P2C on them. What I'm trying to do now is see if there is any current activity happening on their network (either outbound or inbound).</p><p>I've got a script running that is capturing (via dumpcap, netstat, handles.exe and listdlls.exe) most of their network traffic and the running processes, et al.</p><p>I've got a few weeks of this data, which means mucho packets obviously. What I was hoping to find was a way to evaluate the frequency/periodicity of any particular IP address' appearance in the dumpcap/Wireshark captures. I need a starting place.</p><p>I've got scripts running on the data to do more Address Name Resolutions and I will use that to knock out obviously benign addresses. But on the ones I don't know or question, I need to figure some way of seeing when and how often any particular IP address is appearing in the captures.</p><p>And it wouldn't be just one. It would be any that I couldn't eliminate as benign.</p><p>I know there's an I/O graph on Wireshark for ALL traffic...it would be great to see something like that for SPECIFIC IP addresses.</p><p>Maybe there's a piece that is native in Wireshark itself that I haven't found, yet. Maybe there's an app or some other way to see this.</p><p>Any ideas? I'd sure appreciate the help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-frequency" rel="tag" title="see questions tagged &#39;frequency&#39;">frequency</span> <span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jul '16, 09:20</strong></p><img src="https://secure.gravatar.com/avatar/a49d8c2d2413907e0853c46527225c6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chasaway&#39;s gravatar image" /><p><span>chasaway</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chasaway has no accepted answers">0%</span></p></div></div><div id="comments-container-53985" class="comments-container"></div><div id="comment-tools-53985" class="comment-tools"></div><div class="clear"></div><div id="comment-53985-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54005"></span>

<div id="answer-container-54005" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54005-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54005-score" class="post-score" title="current number of votes">0</div><span id="post-54005-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://www.ntop.org/products/traffic-analysis/ntop/">ntopng</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jul '16, 07:08</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-54005" class="comments-container"></div><div id="comment-tools-54005" class="comment-tools"></div><div class="clear"></div><div id="comment-54005-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

