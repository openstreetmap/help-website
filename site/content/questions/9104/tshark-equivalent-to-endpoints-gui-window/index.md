+++
type = "question"
title = "Tshark equivalent to endpoints Gui window"
description = '''I&#x27;m interested in finding out how to produce an endpoints graph via Tshark that is essentially equivalent to the IPv4 endpoints window with no filter? Joke, I&#x27;m specifically looking for something that isn&#x27;t conversation specific, but host specific like the Wireshark IPv4 endpoints window... I&#x27;ve alr...'''
date = "2012-02-17T11:46:00Z"
lastmod = "2012-02-22T11:11:00Z"
weight = 9104
keywords = [ "statistics", "tshark" ]
aliases = [ "/questions/9104" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark equivalent to endpoints Gui window](/questions/9104/tshark-equivalent-to-endpoints-gui-window)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9104-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9104-score" class="post-score" title="current number of votes">0</div><span id="post-9104-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm interested in finding out how to produce an endpoints graph via Tshark that is essentially equivalent to the IPv4 endpoints window with no filter?</p><p>Joke, I'm specifically looking for something that isn't conversation specific, but host specific like the Wireshark IPv4 endpoints window... I've already been down the conversations road and it is too finely grained; I just need summarizations for each IPv4 endpoint only.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Feb '12, 11:46</strong></p><img src="https://secure.gravatar.com/avatar/9aca123fda28fb44956edeebcd5e9221?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kipswederman&#39;s gravatar image" /><p><span>kipswederman</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kipswederman has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Feb '12, 12:34</strong> </span></p></div></div><div id="comments-container-9104" class="comments-container"><span id="9126"></span><div id="comment-9126" class="comment"><div id="post-9126-score" class="comment-score"></div><div class="comment-text"><p>I don't think there's anything directly equivalent, but it can be done with scripting. What OS are you using?</p></div><div id="comment-9126-info" class="comment-info"><span class="comment-age">(18 Feb '12, 07:03)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="9128"></span><div id="comment-9128" class="comment"><div id="post-9128-score" class="comment-score"></div><div class="comment-text"><p>You can use <a href="http://www.wireshark.org/docs/man-pages/tshark.html">TShark statistics</a> to get an overview of the conversations.<br />
$ tshark -r test.pcap -q -z conv,eth -z conv,ip -z conv,tcp<br />
Please take a look at <a href="http://ask.wireshark.org/questions/5111/how-can-i-tshark-a-folder-full-of-tracefiles-for-the-biggest-tcp-stream-in-each-trace?page=1#5225">this question</a> or other questions tagged with <a href="http://ask.wireshark.org/tags/statistics/">statistics</a>.</p></div><div id="comment-9128-info" class="comment-info"><span class="comment-age">(18 Feb '12, 08:11)</span> <span class="comment-user userinfo">joke</span></div></div><span id="9154"></span><div id="comment-9154" class="comment"><div id="post-9154-score" class="comment-score"></div><div class="comment-text"><p>You still haven't stated what OS you are using, as your requirement can be met with scripting. If you are using Windows, I can post a PowerShell script that should do what you want.</p></div><div id="comment-9154-info" class="comment-info"><span class="comment-age">(20 Feb '12, 14:39)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="9174"></span><div id="comment-9174" class="comment"><div id="post-9174-score" class="comment-score"></div><div class="comment-text"><p>Mr. Graham, while I appreciate your assistance, I've already scripted my way to a solution for this dataset. Unfortunately, the added overhead of the scripting process is too slow, so I'm looking for a native T-Shark solution here. I do thank your for being willing to help though!</p></div><div id="comment-9174-info" class="comment-info"><span class="comment-age">(22 Feb '12, 11:11)</span> <span class="comment-user userinfo">kipswederman</span></div></div></div><div id="comment-tools-9104" class="comment-tools"></div><div class="clear"></div><div id="comment-9104-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

