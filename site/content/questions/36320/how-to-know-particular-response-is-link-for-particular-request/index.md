+++
type = "question"
title = "How to know particular Response is link for particular Request."
description = '''Hello, Please help me, actually i&#x27;ve a one &quot;Capture.pcap&quot; file and this file open in wireshark software but after open lots of rows are showing in the wireshark and i&#x27;m confuse how to get a response on particular request, or how to show the data like :-  eg. row by row  1. request row  2. response r...'''
date = "2014-09-15T03:03:00Z"
lastmod = "2014-09-15T22:27:00Z"
weight = 36320
keywords = [ "request", "response" ]
aliases = [ "/questions/36320" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to know particular Response is link for particular Request.](/questions/36320/how-to-know-particular-response-is-link-for-particular-request)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36320-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36320-score" class="post-score" title="current number of votes">0</div><span id="post-36320-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Please help me, actually i've a one "Capture.pcap" file and this file open in wireshark software but after open lots of rows are showing in the wireshark and i'm confuse how to get a response on particular request, or how to show the data like :- eg. row by row 1. request row 2. response row 3. request row 4. response row</p><p>if is it possible, so please help me.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span> <span class="post-tag tag-link-response" rel="tag" title="see questions tagged &#39;response&#39;">response</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Sep '14, 03:03</strong></p><img src="https://secure.gravatar.com/avatar/a9767e4a94528beda88e866b70dc61aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dugesh&#39;s gravatar image" /><p><span>dugesh</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dugesh has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Sep '14, 22:28</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-36320" class="comments-container"><span id="36323"></span><div id="comment-36323" class="comment"><div id="post-36323-score" class="comment-score"></div><div class="comment-text"><p>Based on your reference to "request" and "respone", I assume you are talking about HTTP on port 80 (as opposed to HTTPS, or a different port). It's not exactly clear what you are after, but try using the simple display filter "http". That should collapse all the rows down to only show you HTTP request/response packets. If you want to see the actual data in ASCII, you can right-click any packet of the TCP stream and select "Follow TCP Stream".</p></div><div id="comment-36323-info" class="comment-info"><span class="comment-age">(15 Sep '14, 06:13)</span> <span class="comment-user userinfo">smp</span></div></div><span id="36328"></span><div id="comment-36328" class="comment"><div id="post-36328-score" class="comment-score"></div><div class="comment-text"><p>Are you trying to study one particular protocol? Can you tell us a bit about the problem you are investigating?</p></div><div id="comment-36328-info" class="comment-info"><span class="comment-age">(15 Sep '14, 11:01)</span> <span class="comment-user userinfo">PaulOfford</span></div></div><span id="36349"></span><div id="comment-36349" class="comment"><div id="post-36349-score" class="comment-score"></div><div class="comment-text"><p>Again, what protocol is are the requests and responses? For <em>some</em> protocols, Wireshark will match requests and responses and, in the detailed discussion, and sometimes in the Info column in the packet summary, it will say something such as "this is a response to frame 3". If that's <em>not</em> happening, perhaps Wireshark needs to be enhanced to make it happen.</p></div><div id="comment-36349-info" class="comment-info"><span class="comment-age">(15 Sep '14, 22:27)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-36320" class="comment-tools"></div><div class="clear"></div><div id="comment-36320-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

