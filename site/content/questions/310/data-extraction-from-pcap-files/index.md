+++
type = "question"
title = "Data extraction from pcap files"
description = '''I have machines on taps at critical visibility points in my network that run tshark as a service so that I have continuous packet capture (see tip#7 at http://www.wiresharktraining.com/tips-1-20.html). Whether for troubleshooting or forensics, I frequently need to extract packets from the resulting ...'''
date = "2010-09-24T05:59:00Z"
lastmod = "2010-09-24T06:09:00Z"
weight = 310
keywords = [ "editshark", "extract", "tshark" ]
aliases = [ "/questions/310" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Data extraction from pcap files](/questions/310/data-extraction-from-pcap-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-310-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-310-score" class="post-score" title="current number of votes">0</div><span id="post-310-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have machines on taps at critical visibility points in my network that run tshark as a service so that I have continuous packet capture (see tip#7 at http://www.wiresharktraining.com/tips-1-20.html). Whether for troubleshooting or forensics, I frequently need to extract packets from the resulting pcap files for a specific IP address. Rather than having to use the (more manually intensive) GUI interface to do so, how can I use tshark (or editshark?) to extract data from one pcap file into another pcap file for that IP address?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-editshark" rel="tag" title="see questions tagged &#39;editshark&#39;">editshark</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Sep '10, 05:59</strong></p><img src="https://secure.gravatar.com/avatar/0da36e4b0d13eb5ac57d5e691f869cb4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johnb_hslda_org&#39;s gravatar image" /><p><span>johnb_hslda_org</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johnb_hslda_org has no accepted answers">0%</span></p></div></div><div id="comments-container-310" class="comments-container"></div><div id="comment-tools-310" class="comment-tools"></div><div class="clear"></div><div id="comment-310-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="311"></span>

<div id="answer-container-311" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-311-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-311-score" class="post-score" title="current number of votes">2</div><span id="post-311-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Usually I would just run <em>tshark.exe -r &lt;infile&gt; -R "ip.addr==x.x.x.x" -w &lt;outfile&gt;</em>, where <em>x.x.x.x</em> is the IP address you want to carve out. If I have more than one pcap file to process I run a batch on them, and sometimes merge them together in the end using <em>mergecap -a</em>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Sep '10, 06:09</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-311" class="comments-container"></div><div id="comment-tools-311" class="comment-tools"></div><div class="clear"></div><div id="comment-311-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

