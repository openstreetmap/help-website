+++
type = "question"
title = "Wireshark 1.7 display filtering on Multiple capture interfaces"
description = '''Now that we can capture on two or more interfaces concurrently with 1.7, is there a way to create a dislay filter only on one or the other within the capture file? Or in the case of, say 4 ethernet interfaces, filter on the first 2 and not the last 2. Application (in my case), you have the main corp...'''
date = "2011-08-07T21:35:00Z"
lastmod = "2011-08-07T21:35:00Z"
weight = 5565
keywords = [ "capture", "interfaces", "display-filter" ]
aliases = [ "/questions/5565" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 1.7 display filtering on Multiple capture interfaces](/questions/5565/wireshark-17-display-filtering-on-multiple-capture-interfaces)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5565-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5565-score" class="post-score" title="current number of votes">0</div><span id="post-5565-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Now that we can capture on two or more interfaces concurrently with 1.7, is there a way to create a dislay filter only on one or the other within the capture file? Or in the case of, say 4 ethernet interfaces, filter on the first 2 and not the last 2. Application (in my case), you have the main corp network and a separate segment for a test lab and yet another for the accounting dept. I can think of some roundabout ways of doing it but I was looking for something like <code>"!ip.int == eth0/1 &amp;&amp; !ip.int == eth0/3"</code>. Wishful thinking maybe but I can definitely see this coming up in the near future.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-interfaces" rel="tag" title="see questions tagged &#39;interfaces&#39;">interfaces</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Aug '11, 21:35</strong></p><img src="https://secure.gravatar.com/avatar/f797bdc41d990dca073837114e048b1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EricKnaus&#39;s gravatar image" /><p><span>EricKnaus</span><br />
<span class="score" title="46 reputation points">46</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EricKnaus has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Aug '11, 21:56</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-5565" class="comments-container"></div><div id="comment-tools-5565" class="comment-tools"></div><div class="clear"></div><div id="comment-5565-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

