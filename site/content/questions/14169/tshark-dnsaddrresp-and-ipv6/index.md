+++
type = "question"
title = "tshark, dns.addr.resp and IPv6"
description = '''Hello, I am attempting to use tshark to collect DNS answers. Below is the command I am using: tshark -e frame.time -e dns.resp.name -e dns.resp.addr -e dns.resp.ttl -e dns.resp.type -e dns.resp.rpimaryname -E separator=/t -T fields -nl -e eth1 -f &quot;port 53&quot; -R &quot;dns &amp;amp;&amp;amp; dns.count.answers != 0 &amp;...'''
date = "2012-09-10T10:17:00Z"
lastmod = "2012-09-10T17:46:00Z"
weight = 14169
keywords = [ "ipv6" ]
aliases = [ "/questions/14169" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [tshark, dns.addr.resp and IPv6](/questions/14169/tshark-dnsaddrresp-and-ipv6)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14169-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14169-score" class="post-score" title="current number of votes">0</div><span id="post-14169-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am attempting to use tshark to collect DNS answers. Below is the command I am using:</p><p>tshark -e frame.time -e dns.resp.name -e dns.resp.addr -e dns.resp.ttl -e dns.resp.type -e dns.resp.rpimaryname -E separator=/t -T fields -nl -e eth1 -f "port 53" -R "dns &amp;&amp; dns.count.answers != 0 &amp;&amp; dns.flags.response == 1"</p><p>This works fine for DNS responses that contain ipv4 addresses, but fails to return ipv6 addresses. Unfortunately after going through the documentation and possible filters, it doesn't appear as though ipv6 is supported. Am I doing something incorrectly here or is this simply not currently supported? If it isn't supported, does anyone have any ideas for a solution or alternative?</p><p>Thanks in advance for any help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ipv6" rel="tag" title="see questions tagged &#39;ipv6&#39;">ipv6</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Sep '12, 10:17</strong></p><img src="https://secure.gravatar.com/avatar/60956fdf143e42f8090bf38166286782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joebasey&#39;s gravatar image" /><p><span>joebasey</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joebasey has no accepted answers">0%</span></p></div></div><div id="comments-container-14169" class="comments-container"></div><div id="comment-tools-14169" class="comment-tools"></div><div class="clear"></div><div id="comment-14169-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14170"></span>

<div id="answer-container-14170" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14170-score" class="post-score" title="current number of votes">1</div><span id="post-14170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="joebasey has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>AAAA answers are not accessible through the dns.xxx fields. They are however accessible through the <code>text</code> field. Why? Good question ....</p><p>Unfortunately, the output of <code>text</code> breaks the "nice" structure, but at least you have something to work with ;-)</p><blockquote><p><code>tshark -e text -e "all your other options"</code></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '12, 10:42</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Sep '12, 17:46</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-14170" class="comments-container"><span id="14179"></span><div id="comment-14179" class="comment"><div id="post-14179-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>AAAA answers are not accessible through the dns.xxx fields. They are however accessible through the text field. Why? Good question ....</p></blockquote><p>...to which the answer is "because nobody's bothered giving them named fields". That's not a feature; <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7709">bug 7709</a> speaks of "[making fields] filterable", so perhaps that's one thing Alexis will be fixing.</p></div><div id="comment-14179-info" class="comment-info"><span class="comment-age">(10 Sep '12, 17:46)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-14170" class="comment-tools"></div><div class="clear"></div><div id="comment-14170-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

