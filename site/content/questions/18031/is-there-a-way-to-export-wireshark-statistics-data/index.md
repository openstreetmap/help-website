+++
type = "question"
title = "Is there a way to export wireshark statistics data"
description = '''Background: My requirements are to analyze network traffic from pcap files and present data in a graphical format for quick consumption. Wireshark is the most common choice that is recommended by many to analyze data from pcap files, but its graphical capabilities are limited What I would eventually...'''
date = "2013-01-29T04:36:00Z"
lastmod = "2013-03-01T13:36:00Z"
weight = 18031
keywords = [ "statistics", "export" ]
aliases = [ "/questions/18031" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a way to export wireshark statistics data](/questions/18031/is-there-a-way-to-export-wireshark-statistics-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18031-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18031-score" class="post-score" title="current number of votes">0</div><span id="post-18031-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Background:</p><p>My requirements are to analyze network traffic from pcap files and present data in a graphical format for quick consumption. Wireshark is the most common choice that is recommended by many to analyze data from pcap files, but its graphical capabilities are limited</p><p>What I would eventually want would be to extract data from pcap files in a understandable structure and then run statistical analysis on it depending on the requirements of my users.</p><p>When using wireshark, I found that it already provides a nice set of statistical analysis which I can make use of right away. But I have not found any menu option in wireshark to export these into some format of csv or txt.</p><p>I am able to export the entire packet/pcap file data as a txt file, and I could reconstruct the same statistics based on that. But since wireshark already has this in-built feature, I do not want re-invent it.</p><p>Does anyone of you know a way to achieve this?</p><p>Environment: Windows 7, C# 4.0 desktop client, VS2010</p><p>[Update]</p><p>I am interested in statistics like list of conversations, protocol hierarchy, summary</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '13, 04:36</strong></p><img src="https://secure.gravatar.com/avatar/c3d72e185d602198ef4fd9c59524e57c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="summerboy&#39;s gravatar image" /><p><span>summerboy</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="summerboy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Jan '13, 05:51</strong> </span></p></div></div><div id="comments-container-18031" class="comments-container"></div><div id="comment-tools-18031" class="comment-tools"></div><div class="clear"></div><div id="comment-18031-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18033"></span>

<div id="answer-container-18033" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18033-score" class="post-score" title="current number of votes">1</div><span id="post-18033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have you looked at the statistics offered by tshark (the command line version of Wireshark)? You haven't specified which statistics you require, so look at the <a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark man page</a>, especially the -z options.</p><p><strong>Edit:</strong></p><p>You have specified stats of list of conversations, protocol hierarchy, summary. Options for these would be:</p><ul><li>Conversations - use <code>-z conv,type</code> where type is the type of conversation, e.g. 'ip'.</li><li>Protocol Hierarchy - use <code>-z io,phs</code></li><li>Summary - I think you'll have to use capinfos (found next to the wireshark executable)</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '13, 04:58</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Jan '13, 07:35</strong> </span></p></div></div><div id="comments-container-18033" class="comments-container"><span id="19070"></span><div id="comment-19070" class="comment"><div id="post-19070-score" class="comment-score"></div><div class="comment-text"><p>Hello. Is there a way to get a CSV file with the output of tshark's -z conv,ip similar to the one I get in Wireshark-&gt;Statistics-&gt;Conversations-&gt;IP-&gt;Copy? Thank you!</p></div><div id="comment-19070-info" class="comment-info"><span class="comment-age">(01 Mar '13, 13:36)</span> <span class="comment-user userinfo">hugosp</span></div></div></div><div id="comment-tools-18033" class="comment-tools"></div><div class="clear"></div><div id="comment-18033-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

