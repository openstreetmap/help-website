+++
type = "question"
title = "How to resolve HTTP delay issue with Wireshark"
description = '''Hi Guys We&#x27;ve been having complaints that PC&#x27;s from a sites are experiencing slowness in accessing a HTTP server at the central site, the central site users do not experience the problem. I set up wireshark to detect HTTP requests over 1sec in duration and it picked up quite a number of packets with...'''
date = "2016-11-08T09:15:00Z"
lastmod = "2016-11-08T11:43:00Z"
weight = 57175
keywords = [ "http", "wireshark" ]
aliases = [ "/questions/57175" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to resolve HTTP delay issue with Wireshark](/questions/57175/how-to-resolve-http-delay-issue-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57175-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57175-score" class="post-score" title="current number of votes">0</div><span id="post-57175-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Guys</p><p>We've been having complaints that PC's from a sites are experiencing slowness in accessing a HTTP server at the central site, the central site users do not experience the problem. I set up wireshark to detect HTTP requests over 1sec in duration and it picked up quite a number of packets with such a parameter with quite a few experieincing delays of over 10 Seconds, Armed with this info and considering that the local PC's are fine I need to know what will be the next step to resolve this issue(would I need to use wireshark in another capacity to help me further ??), WAN links seem fine they are not getting saturated etc.</p><p>I look forward in hearing from you all</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '16, 09:15</strong></p><img src="https://secure.gravatar.com/avatar/452b81f3fa8ad714abef1b154d43313d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="s1mwat&#39;s gravatar image" /><p><span>s1mwat</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="s1mwat has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Nov '16, 11:43</strong> </span></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span></p></div></div><div id="comments-container-57175" class="comments-container"><span id="57182"></span><div id="comment-57182" class="comment"><div id="post-57182-score" class="comment-score"></div><div class="comment-text"><p>Could you provide us a trace at public accessible place; like cloudshark or google drive. If you concerned about security, you can use tracewrangeler: <a href="http://www.tracewrangler.com">http://www.tracewrangler.com</a> for some anonymization tasks.</p></div><div id="comment-57182-info" class="comment-info"><span class="comment-age">(08 Nov '16, 11:43)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-57175" class="comment-tools"></div><div class="clear"></div><div id="comment-57175-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57180"></span>

<div id="answer-container-57180" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57180-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57180-score" class="post-score" title="current number of votes">1</div><span id="post-57180-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It sounds like your initial capture was taken from the central site. I would recommend you now move to the complaining customers location to see it from their perspective. If travel is an issue, hopefully you have someone on the remote end that can do a capture for you.</p><p>I have found it beneficial in these scenarios to have captures running at both sites (hint: time sync capture devices), then have the complaining user run through the tasks that generate the issue. You can then take the two pcaps from local/remote and do some comparative analysis to see where the issues are occurring. At the very least you can start to rule at the endpoints and make decisions on where in the network chain you should focus next.</p><p>Troubleshoot TCP first, since that is generally a good area to start and it seems like the HTTP services are fine for local clients, so that potentially rules out HTTP server issues.</p><p>~Happy hunting</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '16, 10:10</strong></p><img src="https://secure.gravatar.com/avatar/bfccba6dc51febee5ca1641be7df63ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BruteForce&#39;s gravatar image" /><p><span>BruteForce</span><br />
<span class="score" title="120 reputation points">120</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BruteForce has one accepted answer">9%</span></p></div></div><div id="comments-container-57180" class="comments-container"></div><div id="comment-tools-57180" class="comment-tools"></div><div class="clear"></div><div id="comment-57180-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

